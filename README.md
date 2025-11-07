# cuddly-lamp

A simple, elegant project template for quick repository setup and transfer, with comprehensive support for images, pictures, and videos.

## Overview

This repository provides a clean starting point for new projects with proper documentation and structure, including powerful tools and guides for working with media assets.

## Features

- Clean repository structure
- Well-documented codebase
- **Complete image and video handling support**
- **Automated optimization scripts for media assets**
- **Comprehensive media management guides**
- Easy to fork and customize
- Ready for collaboration

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Loveandtrust1111/cuddly-lamp.git
   cd cuddly-lamp
   ```

2. Start building your project!

## Working with Images and Videos

This repository includes powerful tools and comprehensive documentation for handling images, pictures, and videos:

### Quick Start

```bash
# Optimize images
./scripts/image-optimizer.sh image.jpg

# Process videos
./scripts/video-processor.sh video.mp4
```

### Documentation

- **[Quick Start Guide](IMAGE_VIDEO_QUICKSTART.md)** - Get started quickly with common tasks
- **[Complete Media Guide](MEDIA_GUIDE.md)** - Comprehensive documentation on images and videos
- **[Assets Directory](assets/README.md)** - Organized structure for your media files

### Features

- 🖼️ **Image Optimization**: Automated scripts to resize and compress images
- 🎥 **Video Processing**: Tools to convert and optimize videos for web
- 📁 **Organized Structure**: Pre-configured directory layout for media assets
- 📚 **Comprehensive Guides**: Detailed documentation with examples
- 🛠️ **Command-line Tools**: Easy-to-use scripts for batch processing

### Example Usage

```bash
# Optimize all images in a directory
./scripts/image-optimizer.sh -q 85 -w 1920 ./assets/images/

# Convert video to web-optimized MP4
./scripts/video-processor.sh -r 1280x720 -t video.mov

# Get help on any script
./scripts/image-optimizer.sh --help
./scripts/video-processor.sh --help
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in this repository.
