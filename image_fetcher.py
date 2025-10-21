import requests
import os
import hashlib
from urllib.parse import urlparse

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
HASH_DB_PATH = os.path.join("Fetched_Images", ".image_hashes")


def compute_hash(content: bytes) -> str:
    """Compute SHA-256 hash of file content."""
    return hashlib.sha256(content).hexdigest()


def load_hash_db():
    """Load existing hashes from file (if exists)."""
    if not os.path.exists(HASH_DB_PATH):
        return set()
    with open(HASH_DB_PATH, "r") as f:
        return set(line.strip() for line in f.readlines())


def save_hash(hash_value: str):
    """Append a new hash to DB file."""
    with open(HASH_DB_PATH, "a") as f:
        f.write(hash_value + "\n")


def fetch_image(url: str, existing_hashes: set):
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

        # Download after checks
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 3. Hash image before saving to detect duplicates
        file_hash = compute_hash(response.content)
        if file_hash in existing_hashes:
            print(f"⚠ {url} skipped - Duplicate image detected")
            return False

        # 4. Extract filename safely
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or f"image_{abs(hash(url))}.jpg"

        # Ensure proper extension
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
            filename += ".jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # 5. Validate size against actual bytes downloaded
        if len(response.content) > MAX_FILE_SIZE:
            print(f"✗ {url} rejected - Downloaded file too large")
            return False

        # Save file
        with open(filepath, 'wb') as f:
            f.write(response.content)

        # Save hash to DB
        save_hash(file_hash)
        existing_hashes.add(file_hash)

        print(f"✓ Successfully fetched (verified & unique): {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch {url}: {e}")
        return False


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user
    urls = input("Enter image URLs (separate by comma or space):\n").split()

    # Create directory if not exists
    os.makedirs("Fetched_Images", exist_ok=True)

    # Load existing hash DB
    existing_hashes = load_hash_db()

    print("\n--- Starting downloads ---\n")

    for url in urls:
        url = url.strip().rstrip(",")
        if url:
            fetch_image(url, existing_hashes)

    print("\n--- Task complete ---")
    print("Connection strengthened. Community enriched.\n")


if __name__ == "__main__":
    main()
