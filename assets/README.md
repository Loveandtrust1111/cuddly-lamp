# Assets Directory

This directory contains all media assets for the project including images and videos.

## Structure

```
assets/
├── images/
│   ├── photos/          # Photography and photo content
│   ├── graphics/        # Graphics, illustrations, and designs
│   ├── icons/           # Icon files and sprites
│   ├── thumbnails/      # Thumbnail versions of images
│   └── originals/       # Original, unprocessed high-resolution images
└── videos/
    ├── tutorials/       # Tutorial and educational videos
    ├── demos/          # Product demonstration videos
    ├── clips/          # Short video clips and snippets
    ├── originals/      # Original source video files
    └── thumbnails/     # Video thumbnail images
```

## Usage Guidelines

### Images

- Place original high-resolution images in `images/originals/`
- Store optimized web-ready images in the appropriate category folder
- Use the image optimizer script: `../scripts/image-optimizer.sh`
- Keep thumbnails in `images/thumbnails/`

### Videos

- Store original video source files in `videos/originals/`
- Place processed web-optimized videos in the appropriate category
- Use the video processor script: `../scripts/video-processor.sh`
- Save video thumbnails in `videos/thumbnails/`

## Best Practices

1. **Naming Convention**
   - Use descriptive, lowercase names with hyphens
   - Example: `hero-image-2024.jpg`, `product-demo-v2.mp4`

2. **File Sizes**
   - Images: Keep under 500KB for web use
   - Videos: Compress to appropriate sizes for streaming

3. **Format Selection**
   - Images: JPEG for photos, PNG for graphics, WebP for web
   - Videos: MP4 (H.264) for best compatibility

4. **Version Control**
   - Commit optimized images (< 1MB)
   - Use Git LFS for larger files
   - Store very large videos externally (e.g., YouTube, Vimeo)

## Scripts

Use the provided scripts in the `scripts/` directory to optimize your media:

```bash
# Optimize images
../scripts/image-optimizer.sh -q 85 -w 1920 image.jpg

# Process videos
../scripts/video-processor.sh -r 1280x720 -t video.mov
```

For detailed documentation, see [MEDIA_GUIDE.md](../MEDIA_GUIDE.md).
