# Ubuntu_Requests

An Ubuntu-inspired image fetcher application that demonstrates the use of HTTP requests to download and manage images from the web.

## Overview

This project is designed as a learning assignment to practice working with HTTP requests, file handling, and implementing an Ubuntu-themed aesthetic. The application fetches images from specified URLs and saves them locally while providing a clean, Ubuntu-inspired user interface.

## Features

- **Image Fetching**: Download images from URLs using HTTP requests
- **Ubuntu-Inspired Design**: Clean interface following Ubuntu design principles
- **Error Handling**: Robust error handling for network requests and file operations
- **Progress Tracking**: Visual feedback during image download operations
- **Local Storage**: Save downloaded images to local filesystem

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/G-alileo/Ubuntu_Requests.git
cd Ubuntu_Requests
```

## Usage

### Basic Usage

Run the main script to start the image fetcher:

```bash
python image_fetcher.py
```

## Error Handling

The application handles various error scenarios:

- **Invalid URLs**: Validates URL format before attempting download
- **Network Errors**: Handles connection timeouts and network failures
- **File System Errors**: Manages permission issues and disk space
- **Invalid Image Files**: Validates downloaded files are valid images

## Examples

- URLs to try out

```
https://images.pexels.com/photos/2014422/pexels-photo-2014422.jpeg
https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg
https://images.pexels.com/photos/34950/pexels-photo.jpg
https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg
https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg
https://images.pexels.com/photos/1439224/pexels-photo-1439224.jpeg
https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg
https://images.pexels.com/photos/248616/pexels-photo-248616.jpeg
https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg
https://images.pexels.com/photos/793226/pexels-photo-793226.jpeg

```


## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused

## Troubleshooting

### Common Issues

**Issue**: "Connection timeout error"
- **Solution**: Check your internet connection or increase timeout value

**Issue**: "Permission denied when saving file"
- **Solution**: Ensure you have write permissions in the output directory

**Issue**: "Invalid image format"
- **Solution**: Verify the URL points to a valid image file

## Roadmap

- [ ] Add support for authenticated requests
- [ ] Implement resume capability for large downloads
- [ ] Add image format conversion
- [ ] Create GUI version with Ubuntu theme
- [ ] Add support for bulk URL import from CSV
- [ ] Implement image metadata extraction

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Ubuntu design team for inspiration
- Pexels community for images
- Python requests library maintainers
- All contributors to this project

## Contact

**Author**: G-alileo

**Repository**: [https://github.com/G-alileo/Ubuntu_Requests](https://github.com/G-alileo/Ubuntu_Requests)

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/G-alileo/Ubuntu_Requests/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**Note**: This is an educational project created for learning purposes. Use responsibly and respect website terms of service when downloading images.