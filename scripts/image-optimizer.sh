#!/bin/bash

# Image Optimizer Script
# This script helps optimize images for web use

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
QUALITY=85
MAX_WIDTH=1920
OUTPUT_DIR=""
VERBOSE=0

# Function to print usage
usage() {
    cat << EOF
Usage: $0 [OPTIONS] <input_file_or_directory>

Options:
    -q, --quality <1-100>       JPEG quality (default: 85)
    -w, --width <pixels>        Maximum width (default: 1920)
    -o, --output <directory>    Output directory (default: same as input)
    -v, --verbose               Verbose output
    -h, --help                  Display this help message

Examples:
    # Optimize a single image
    $0 image.jpg

    # Optimize all images in a directory
    $0 ./images/

    # Set quality to 90 and max width to 1280px
    $0 -q 90 -w 1280 image.jpg

    # Process directory and save to different location
    $0 -o ./optimized ./images/

Dependencies:
    This script requires ImageMagick. Install with:
    - Ubuntu/Debian: sudo apt-get install imagemagick
    - macOS: brew install imagemagick
    - Windows: Download from https://imagemagick.org/

EOF
    exit 1
}

# Function to check if ImageMagick is installed
check_dependencies() {
    if ! command -v convert &> /dev/null; then
        echo -e "${RED}Error: ImageMagick is not installed.${NC}"
        echo "Please install ImageMagick:"
        echo "  Ubuntu/Debian: sudo apt-get install imagemagick"
        echo "  macOS: brew install imagemagick"
        exit 1
    fi
}

# Function to optimize a single image
optimize_image() {
    local input="$1"
    local output="$2"
    local filename=$(basename "$input")
    local extension="${filename##*.}"
    
    if [ "$VERBOSE" -eq 1 ]; then
        echo "Processing: $filename"
    fi
    
    # Check if file is an image (case-insensitive)
    extension_lower=$(echo "$extension" | tr '[:upper:]' '[:lower:]')
    if [[ ! "$extension_lower" =~ ^(jpg|jpeg|png|gif|webp)$ ]]; then
        echo -e "${YELLOW}Skipping non-image file: $filename${NC}"
        return
    fi
    
    # Get original size
    local original_size=$(stat -f%z "$input" 2>/dev/null || stat -c%s "$input" 2>/dev/null)
    
    # Optimize the image
    if [[ "$extension_lower" =~ ^(jpg|jpeg)$ ]]; then
        # JPEG optimization
        convert "$input" \
            -resize "${MAX_WIDTH}x${MAX_WIDTH}>" \
            -quality "$QUALITY" \
            -strip \
            "$output" 2>/dev/null || {
                echo -e "${RED}Failed to process: $filename${NC}"
                return
            }
    elif [[ "$extension_lower" =~ ^(png)$ ]]; then
        # PNG optimization
        convert "$input" \
            -resize "${MAX_WIDTH}x${MAX_WIDTH}>" \
            -strip \
            "$output" 2>/dev/null || {
                echo -e "${RED}Failed to process: $filename${NC}"
                return
            }
    else
        # Other formats
        convert "$input" \
            -resize "${MAX_WIDTH}x${MAX_WIDTH}>" \
            -strip \
            "$output" 2>/dev/null || {
                echo -e "${RED}Failed to process: $filename${NC}"
                return
            }
    fi
    
    # Get new size and calculate savings
    local new_size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null)
    local savings=$((100 - (new_size * 100 / original_size)))
    
    echo -e "${GREEN}✓${NC} $filename"
    if [ "$VERBOSE" -eq 1 ]; then
        echo "  Original: $(numfmt --to=iec-i --suffix=B $original_size 2>/dev/null || echo "${original_size}B")"
        echo "  Optimized: $(numfmt --to=iec-i --suffix=B $new_size 2>/dev/null || echo "${new_size}B")"
        echo "  Saved: ${savings}%"
    fi
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -q|--quality)
            QUALITY="$2"
            shift 2
            ;;
        -w|--width)
            MAX_WIDTH="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            INPUT="$1"
            shift
            ;;
    esac
done

# Check if input is provided
if [ -z "$INPUT" ]; then
    echo -e "${RED}Error: No input file or directory specified${NC}"
    usage
fi

# Check dependencies
check_dependencies

# Validate quality
if [ "$QUALITY" -lt 1 ] || [ "$QUALITY" -gt 100 ]; then
    echo -e "${RED}Error: Quality must be between 1 and 100${NC}"
    exit 1
fi

echo "Image Optimizer"
echo "==============="
echo "Quality: $QUALITY"
echo "Max Width: ${MAX_WIDTH}px"
echo ""

# Process input
if [ -f "$INPUT" ]; then
    # Single file
    if [ -z "$OUTPUT_DIR" ]; then
        OUTPUT_DIR=$(dirname "$INPUT")
    fi
    mkdir -p "$OUTPUT_DIR"
    
    filename=$(basename "$INPUT")
    output_path="$OUTPUT_DIR/$filename"
    
    optimize_image "$INPUT" "$output_path"
    
elif [ -d "$INPUT" ]; then
    # Directory
    if [ -z "$OUTPUT_DIR" ]; then
        OUTPUT_DIR="$INPUT"
    fi
    mkdir -p "$OUTPUT_DIR"
    
    # Find and process all images
    count=0
    while IFS= read -r -d '' file; do
        filename=$(basename "$file")
        output_path="$OUTPUT_DIR/$filename"
        optimize_image "$file" "$output_path"
        ((count++))
    done < <(find "$INPUT" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" \) -print0)
    
    echo ""
    echo -e "${GREEN}Processed $count images${NC}"
else
    echo -e "${RED}Error: '$INPUT' is not a valid file or directory${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Done!${NC}"
