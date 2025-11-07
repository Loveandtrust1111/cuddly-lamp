#!/bin/bash

# Image Optimizer Script
# Optimizes images by resizing and compressing them

set -e

# Default values
QUALITY=85
MAX_WIDTH=1920
TARGET_DIR=""

# Display usage information
usage() {
    cat << EOF
Usage: $0 [OPTIONS] TARGET_DIRECTORY

Optimize images in the specified directory by resizing and compressing them.

OPTIONS:
    -q QUALITY      Set JPEG quality (1-100, default: 85)
    -w WIDTH        Set maximum width in pixels (default: 1920)
    -h              Display this help message

EXAMPLES:
    $0 -q 85 -w 1920 ./assets/images/
    $0 -q 90 ./photos/

REQUIREMENTS:
    - ImageMagick (convert command)

EOF
    exit 1
}

# Parse command line arguments
while getopts "q:w:h" opt; do
    case $opt in
        q)
            QUALITY=$OPTARG
            if ! [[ "$QUALITY" =~ ^[0-9]+$ ]] || [ "$QUALITY" -lt 1 ] || [ "$QUALITY" -gt 100 ]; then
                echo "Error: Quality must be between 1 and 100"
                exit 1
            fi
            ;;
        w)
            MAX_WIDTH=$OPTARG
            if ! [[ "$MAX_WIDTH" =~ ^[0-9]+$ ]] || [ "$MAX_WIDTH" -lt 1 ]; then
                echo "Error: Width must be a positive number"
                exit 1
            fi
            ;;
        h)
            usage
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
    esac
done

# Shift past the options
shift $((OPTIND-1))

# Get target directory
TARGET_DIR="$1"

if [ -z "$TARGET_DIR" ]; then
    echo "Error: Target directory is required"
    usage
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' does not exist"
    exit 1
fi

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is not installed. Please install it first."
    echo "On Ubuntu/Debian: sudo apt-get install imagemagick"
    echo "On macOS: brew install imagemagick"
    exit 1
fi

echo "Image Optimizer"
echo "==============="
echo "Target directory: $TARGET_DIR"
echo "Quality: $QUALITY%"
echo "Max width: ${MAX_WIDTH}px"
echo ""

# Find and process images
PROCESSED=0
SKIPPED=0

# Process common image formats
for ext in jpg jpeg png gif bmp tiff; do
    while IFS= read -r -d '' file; do
        echo "Processing: $file"
        
        # Get image dimensions
        WIDTH=$(identify -format "%w" "$file" 2>/dev/null || echo "0")
        
        if [ "$WIDTH" -eq 0 ]; then
            echo "  Skipped: Could not read image"
            SKIPPED=$((SKIPPED + 1))
            continue
        fi
        
        # Create backup
        BACKUP="${file}.bak"
        cp "$file" "$BACKUP"
        
        # Resize and optimize
        if [ "$WIDTH" -gt "$MAX_WIDTH" ]; then
            convert "$file" -resize "${MAX_WIDTH}x>" -quality "$QUALITY" "$file"
            echo "  Resized and optimized (${WIDTH}px -> ${MAX_WIDTH}px, quality: ${QUALITY}%)"
        else
            convert "$file" -quality "$QUALITY" "$file"
            echo "  Optimized (quality: ${QUALITY}%)"
        fi
        
        # Remove backup after successful processing
        rm "$BACKUP"
        PROCESSED=$((PROCESSED + 1))
        
    done < <(find "$TARGET_DIR" -type f -iname "*.${ext}" -print0)
done

echo ""
echo "Complete!"
echo "Images processed: $PROCESSED"
echo "Images skipped: $SKIPPED"
