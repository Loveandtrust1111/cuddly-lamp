# Quick Start: Working with Images and Videos

This quick start guide helps you get up and running with image and video handling in your project.

## 🚀 Quick Setup

### 1. Install Dependencies

**For Images (ImageMagick):**
```bash
# Ubuntu/Debian
sudo apt-get install imagemagick

# macOS
brew install imagemagick

# Verify installation
convert --version
```

**For Videos (FFmpeg):**
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Verify installation
ffmpeg -version
```

## 📸 Working with Images

### Basic Image Optimization

```bash
# Optimize a single image
./scripts/image-optimizer.sh photo.jpg

# Optimize all images in a directory
./scripts/image-optimizer.sh ./assets/images/photos/

# Custom quality and size
./scripts/image-optimizer.sh -q 90 -w 1280 photo.jpg

# Save to different directory
./scripts/image-optimizer.sh -o ./optimized ./assets/images/
```

### Common Image Tasks

**Resize an image:**
```bash
convert input.jpg -resize 800x600 output.jpg
```

**Convert format:**
```bash
convert input.png output.jpg
```

**Compress JPEG:**
```bash
convert input.jpg -quality 85 output.jpg
```

**Create thumbnail:**
```bash
convert input.jpg -thumbnail 200x200 thumbnail.jpg
```

**Batch resize all images:**
```bash
for img in *.jpg; do convert "$img" -resize 1920x1080 "resized-$img"; done
```

## 🎥 Working with Videos

### Basic Video Processing

```bash
# Convert and optimize video
./scripts/video-processor.sh video.mov

# Convert with custom settings
./scripts/video-processor.sh -r 1920x1080 -b 5M video.avi

# Extract thumbnail
./scripts/video-processor.sh -t video.mp4

# Save to different directory
./scripts/video-processor.sh -o ./processed video.mov
```

### Common Video Tasks

**Convert to MP4:**
```bash
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4
```

**Resize video:**
```bash
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
```

**Extract thumbnail:**
```bash
ffmpeg -i video.mp4 -ss 00:00:01 -vframes 1 thumbnail.jpg
```

**Reduce file size:**
```bash
ffmpeg -i input.mp4 -b:v 1M -b:a 128k output.mp4
```

**Convert to WebM:**
```bash
ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 2M output.webm
```

## 📁 Directory Structure

Organize your media files:

```
your-project/
├── assets/
│   ├── images/
│   │   ├── photos/          # Photo content
│   │   ├── graphics/        # Graphics and designs
│   │   ├── icons/           # Icons
│   │   ├── thumbnails/      # Image thumbnails
│   │   └── originals/       # Original files (not in git)
│   └── videos/
│       ├── tutorials/       # Tutorial videos
│       ├── demos/          # Demo videos
│       ├── clips/          # Short clips
│       ├── originals/      # Original files (not in git)
│       └── thumbnails/     # Video thumbnails
└── scripts/
    ├── image-optimizer.sh  # Image optimization script
    └── video-processor.sh  # Video processing script
```

## 🎯 Common Use Cases

### Web Project Images

```bash
# Optimize all images for web
./scripts/image-optimizer.sh -q 85 -w 1920 ./assets/images/

# Create thumbnails
for img in assets/images/photos/*.jpg; do
  convert "$img" -thumbnail 300x300 "assets/images/thumbnails/$(basename "$img")"
done
```

### Video for Web

```bash
# Optimize for web streaming
./scripts/video-processor.sh -r 1280x720 -b 2M -t video.mov

# Create multiple resolutions
ffmpeg -i input.mp4 -vf scale=1920:1080 -b:v 5M 1080p.mp4
ffmpeg -i input.mp4 -vf scale=1280:720 -b:v 2.5M 720p.mp4
ffmpeg -i input.mp4 -vf scale=854:480 -b:v 1M 480p.mp4
```

### Batch Processing

```bash
# Optimize all JPEGs in current directory
for img in *.jpg; do
  ./scripts/image-optimizer.sh -q 85 "$img"
done

# Convert all MOV files to MP4
for video in *.mov; do
  ./scripts/video-processor.sh "$video"
done
```

## 💡 Tips & Tricks

### Image Tips

1. **Always keep originals**: Store unprocessed originals separately
2. **Use appropriate formats**: JPEG for photos, PNG for graphics, WebP for web
3. **Optimize for web**: Target < 500KB for images, < 100KB for thumbnails
4. **Use lazy loading**: Load images only when needed
5. **Add alt text**: Always include descriptive alt text for accessibility

### Video Tips

1. **Choose right codec**: H.264 (MP4) for compatibility, VP9 (WebM) for efficiency
2. **Optimize bitrate**: 1-2 Mbps for 720p, 3-5 Mbps for 1080p
3. **Add faststart flag**: Enables streaming before full download
4. **Create thumbnails**: Extract representative frames
5. **Consider hosting**: Use YouTube/Vimeo for large files

### Performance Tips

1. **Compress before uploading**: Reduce bandwidth and storage
2. **Use CDN**: Serve media from Content Delivery Networks
3. **Implement responsive images**: Serve appropriate sizes for devices
4. **Enable caching**: Set proper cache headers
5. **Monitor file sizes**: Keep images < 500KB, videos < 50MB

## 📚 Learn More

- [Complete Media Guide](MEDIA_GUIDE.md) - Comprehensive documentation
- [Assets README](assets/README.md) - Directory structure and guidelines
- [ImageMagick Documentation](https://imagemagick.org/script/command-line-options.php)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

## 🆘 Troubleshooting

**ImageMagick not found:**
```bash
# Check if installed
which convert

# Install if missing
# Ubuntu: sudo apt-get install imagemagick
# macOS: brew install imagemagick
```

**FFmpeg not found:**
```bash
# Check if installed
which ffmpeg

# Install if missing
# Ubuntu: sudo apt-get install ffmpeg
# macOS: brew install ffmpeg
```

**Permission denied on scripts:**
```bash
# Make scripts executable
chmod +x scripts/*.sh
```

**Out of memory errors:**
- Process fewer files at once
- Reduce output quality/resolution
- Use lower bitrate for videos

## 🤝 Need Help?

- Check the [full documentation](MEDIA_GUIDE.md)
- Open an issue in the repository
- Consult tool documentation (ImageMagick, FFmpeg)

---

*Ready to start? Run `./scripts/image-optimizer.sh -h` or `./scripts/video-processor.sh -h` for detailed help!*
