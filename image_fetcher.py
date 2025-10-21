import requests
import os
from urllib.parse import urlparse

def fetch_image(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  
            filename = "image_" + str(abs(hash(url))) + ".jpg"  # generate fallback name

        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
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
