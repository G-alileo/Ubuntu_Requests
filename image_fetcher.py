import requests
import os
from urllib.parse import urlparse

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def fetch_image(url: str):
    try:
        head = requests.head(url, timeout=10)
        content_type = head.headers.get("Content-Type", "")

        # 1. Validate MIME type
        if not content_type.startswith("image/"):
            print(f"✗ {url} rejected - Not a valid image (MIME: {content_type})")
            return False

        # 2. Validate file size (if content-length present)
        content_length = head.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"✗ {url} rejected - File too large")
            return False

        # Download after initial checks
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 3. Extract filename safely
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:
            filename = "image_" + str(abs(hash(url))) + ".jpg"

        # Double-check extension against MIME
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
            filename += ".jpg"

        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, 'wb') as f:
            # 4. Validate size again from actual content length
            if len(response.content) > MAX_FILE_SIZE:
                print(f"✗ {url} rejected - Downloaded file too large")
                return False

            f.write(response.content)

        print(f"✓ Successfully fetched (verified safe): {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch {url}: {e}")
        return False

    
def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user
    urls = input("Enter image URLs (separate by comma or new line):\n").split()

    # Create directory if not exists
    os.makedirs("Fetched_Images", exist_ok=True)

    print("\n--- Starting downloads ---\n")

    for url in urls:
        url = url.strip().rstrip(",")  # clean trailing spaces/commas
        if url:
            fetch_image(url)

    print("\n--- Task complete ---")
    print("Connection strengthened. Community enriched.\n")

if __name__ == "__main__":
    main()
