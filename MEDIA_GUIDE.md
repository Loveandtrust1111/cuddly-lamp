# Media Guide: Images, Pictures, and Videos

This guide provides comprehensive help for working with images, pictures, and videos in your projects.

## Table of Contents

- [Image Handling](#image-handling)
- [Video Handling](#video-handling)
- [Best Practices](#best-practices)
- [Tools and Resources](#tools-and-resources)

## Image Handling

### Supported Image Formats

- **JPEG/JPG**: Best for photographs and complex images
- **PNG**: Best for graphics, logos, and images requiring transparency
- **GIF**: Best for simple animations
- **WebP**: Modern format with superior compression
- **SVG**: Best for vector graphics and icons

### Image Organization

Organize your images in a structured directory:

```
assets/
├── images/
│   ├── photos/          # Photographs
│   ├── graphics/        # Graphics and illustrations
│   ├── icons/           # Icon files
│   ├── thumbnails/      # Thumbnail versions
│   └── originals/       # Original high-res versions
```

### Image Optimization Tips

1. **Choose the Right Format**
   - Use JPEG for photos (quality 80-90%)
   - Use PNG for graphics with transparency
   - Use WebP for web images (better compression)
   - Use SVG for logos and icons

2. **Resize Images**
   - Don't use larger dimensions than needed
   - Common web sizes: 1920px, 1280px, 800px, 400px
   - Create responsive image sets for different devices

3. **Compress Images**
   - Use tools like ImageOptim, TinyPNG, or Squoosh
   - Target file sizes: < 100KB for thumbnails, < 500KB for full images

4. **Use Proper Naming Conventions**
   - Use descriptive names: `hero-image.jpg` not `img1.jpg`
   - Use lowercase and hyphens: `profile-photo-2024.jpg`
   - Include dimensions when relevant: `logo-200x200.png`

### Image Accessibility

- Always include `alt` text descriptions
- Use descriptive filenames
- Ensure sufficient contrast
- Provide text alternatives for complex images

## Video Handling

### Supported Video Formats

- **MP4 (H.264)**: Best compatibility across browsers
- **WebM (VP9)**: Excellent compression, good for web
- **MOV**: High quality, larger file sizes
- **AVI**: Legacy format, larger file sizes

### Video Organization

```
assets/
├── videos/
│   ├── tutorials/       # How-to videos
│   ├── demos/          # Product demonstrations
│   ├── clips/          # Short video clips
│   ├── originals/      # Original source files
│   └── thumbnails/     # Video thumbnail images
```

### Video Optimization Tips

1. **Choose Appropriate Resolution**
   - 1080p (1920x1080): High quality
   - 720p (1280x720): Good quality, smaller size
   - 480p (854x480): Mobile-friendly

2. **Optimize Encoding**
   - Use H.264 codec for MP4
   - Target bitrate: 5-10 Mbps for 1080p
   - Use variable bitrate (VBR) for better quality

3. **Keep File Sizes Manageable**
   - Aim for < 50MB for short clips
   - Consider streaming for longer videos
   - Use video hosting platforms (YouTube, Vimeo) for large files

4. **Create Thumbnails**
   - Extract a representative frame
   - Size: 1280x720 or 1920x1080
   - Format: JPEG or WebP

### Video Accessibility

- Provide captions and subtitles
- Include audio descriptions for visual content
- Offer transcript files
- Ensure video controls are keyboard accessible

## Best Practices

### Storage and Organization

1. **Use Version Control for Small Assets**
   - Keep small images (< 1MB) in repository
   - Use Git LFS for larger files
   - Store large videos externally

2. **Maintain Original Files**
   - Keep uncompressed originals separate
   - Document processing steps
   - Version your assets

3. **Create a Style Guide**
   - Define image dimensions
   - Set quality standards
   - Document naming conventions

### Performance

1. **Lazy Loading**
   - Load images only when needed
   - Improves initial page load time

2. **Progressive Loading**
   - Show low-quality placeholders first
   - Load high-quality versions progressively

3. **Responsive Images**
   - Serve different sizes for different devices
   - Use `srcset` and `sizes` attributes

4. **CDN Usage**
   - Serve media from Content Delivery Networks
   - Reduces latency and improves performance

### Security

1. **Validate File Uploads**
   - Check file types and extensions
   - Scan for malicious content
   - Limit file sizes

2. **Sanitize Filenames**
   - Remove special characters
   - Prevent directory traversal attacks

3. **Control Access**
   - Use proper permissions
   - Implement authentication where needed

## Tools and Resources

### Image Tools

**Editing:**
- [GIMP](https://www.gimp.org/) - Free, open-source image editor
- [Photopea](https://www.photopea.com/) - Online Photoshop alternative
- [Pixlr](https://pixlr.com/) - Online image editor

**Optimization:**
- [TinyPNG](https://tinypng.com/) - PNG and JPEG compression
- [Squoosh](https://squoosh.app/) - Google's image compression tool
- [ImageOptim](https://imageoptim.com/) - Mac image optimizer

**Conversion:**
- [CloudConvert](https://cloudconvert.com/) - Online file converter
- [Convertio](https://convertio.co/) - Image format converter

### Video Tools

**Editing:**
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) - Professional, free video editor
- [OpenShot](https://www.openshot.org/) - Free, open-source video editor
- [Shotcut](https://shotcut.org/) - Cross-platform video editor

**Compression:**
- [HandBrake](https://handbrake.fr/) - Open-source video transcoder
- [FFmpeg](https://ffmpeg.org/) - Command-line video processing

**Hosting:**
- [YouTube](https://www.youtube.com/) - Free video hosting
- [Vimeo](https://vimeo.com/) - Professional video hosting
- [Cloudinary](https://cloudinary.com/) - Media management platform

### Command-Line Tools

**ImageMagick** - Image manipulation
```bash
# Resize image
convert input.jpg -resize 800x600 output.jpg

# Convert format
convert input.png output.jpg

# Compress JPEG
convert input.jpg -quality 85 output.jpg
```

**FFmpeg** - Video processing
```bash
# Convert video format
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4

# Extract thumbnail
ffmpeg -i video.mp4 -ss 00:00:01 -vframes 1 thumbnail.jpg

# Resize video
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
```

## Quick Reference

### Image File Size Guidelines

| Use Case | Max Size | Format |
|----------|----------|--------|
| Favicon | 10KB | PNG/ICO |
| Icons | 50KB | PNG/SVG |
| Thumbnails | 100KB | JPEG/WebP |
| Content Images | 500KB | JPEG/WebP |
| Hero Images | 1MB | JPEG/WebP |

### Video File Size Guidelines

| Duration | Resolution | Target Size |
|----------|------------|-------------|
| < 30s | 720p | 10-20MB |
| 1-2 min | 720p | 20-50MB |
| < 30s | 1080p | 20-40MB |
| 1-2 min | 1080p | 50-100MB |

## Additional Resources

- [Web.dev Image Optimization](https://web.dev/fast/#optimize-your-images)
- [MDN Web Docs: Images in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)
- [MDN Web Docs: Video and Audio](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)
- [Google's Image Optimization Guide](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/image-optimization)

## Need More Help?

For specific questions or issues:
1. Check the documentation of your specific tools
2. Search for solutions on Stack Overflow
3. Open an issue in this repository
4. Consult the community for best practices

---

*Last updated: 2025-11-07*
