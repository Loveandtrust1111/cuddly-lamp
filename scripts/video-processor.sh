#!/bin/bash

# Video Processor Script
# This script helps process and optimize videos for web use

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
RESOLUTION="1280x720"
BITRATE="2M"
OUTPUT_DIR=""
EXTRACT_THUMBNAIL=0
VERBOSE=0

# Function to print usage
usage() {
    cat << EOF
Usage: $0 [OPTIONS] <input_video>

Options:
    -r, --resolution <WxH>      Output resolution (default: 1280x720)
    -b, --bitrate <rate>        Video bitrate (default: 2M)
    -o, --output <directory>    Output directory (default: same as input)
    -t, --thumbnail             Extract thumbnail from video
    -v, --verbose               Verbose output
    -h, --help                  Display this help message

Examples:
    # Convert video to 720p
    $0 video.mov

    # Convert with custom resolution and bitrate
    $0 -r 1920x1080 -b 5M video.avi

    # Extract thumbnail and convert
    $0 -t video.mp4

    # Process and save to different location
    $0 -o ./processed video.mov

Dependencies:
    This script requires FFmpeg. Install with:
    - Ubuntu/Debian: sudo apt-get install ffmpeg
    - macOS: brew install ffmpeg
    - Windows: Download from https://ffmpeg.org/

EOF
    exit 1
}

# Function to check if FFmpeg is installed
check_dependencies() {
    if ! command -v ffmpeg &> /dev/null; then
        echo -e "${RED}Error: FFmpeg is not installed.${NC}"
        echo "Please install FFmpeg:"
        echo "  Ubuntu/Debian: sudo apt-get install ffmpeg"
        echo "  macOS: brew install ffmpeg"
        exit 1
    fi
}

# Function to extract thumbnail from video
extract_thumbnail() {
    local input="$1"
    local output="$2"
    local filename=$(basename "$input")
    local name="${filename%.*}"
    local thumbnail="$output/${name}-thumbnail.jpg"
    
    echo "Extracting thumbnail..."
    
    # Extract frame at 1 second (ss before -i for better performance)
    ffmpeg -ss 00:00:01 -i "$input" -vframes 1 -q:v 2 "$thumbnail" -y &>/dev/null || {
        echo -e "${RED}Failed to extract thumbnail${NC}"
        return 1
    }
    
    echo -e "${GREEN}✓${NC} Thumbnail saved: ${name}-thumbnail.jpg"
}

# Function to process a video
process_video() {
    local input="$1"
    local output_dir="$2"
    local filename=$(basename "$input")
    local name="${filename%.*}"
    local output="$output_dir/${name}.mp4"
    
    if [ "$VERBOSE" -eq 1 ]; then
        echo "Processing: $filename"
    fi
    
    # Get original size
    local original_size=$(stat -f%z "$input" 2>/dev/null || stat -c%s "$input" 2>/dev/null)
    
    # Process the video
    echo "Converting video..."
    local vf_string="scale=$RESOLUTION:force_original_aspect_ratio=decrease,pad=$RESOLUTION:(ow-iw)/2:(oh-ih)/2"
    
    if [ "$VERBOSE" -eq 1 ]; then
        ffmpeg -i "$input" \
            -vf "$vf_string" \
            -c:v libx264 \
            -preset medium \
            -b:v "$BITRATE" \
            -c:a aac \
            -b:a 128k \
            -movflags +faststart \
            "$output" -y
    else
        ffmpeg -i "$input" \
            -vf "$vf_string" \
            -c:v libx264 \
            -preset medium \
            -b:v "$BITRATE" \
            -c:a aac \
            -b:a 128k \
            -movflags +faststart \
            "$output" -y &>/dev/null || {
                echo -e "${RED}Failed to process video${NC}"
                return 1
            }
    fi
    
    # Get new size and calculate savings
    local new_size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output" 2>/dev/null)
    local savings=$((100 - (new_size * 100 / original_size)))
    
    echo -e "${GREEN}✓${NC} ${name}.mp4"
    if [ "$VERBOSE" -eq 1 ]; then
        echo "  Original: $(numfmt --to=iec-i --suffix=B $original_size 2>/dev/null || echo "${original_size}B")"
        echo "  Processed: $(numfmt --to=iec-i --suffix=B $new_size 2>/dev/null || echo "${new_size}B")"
        echo "  Saved: ${savings}%"
    fi
    
    # Extract thumbnail if requested
    if [ "$EXTRACT_THUMBNAIL" -eq 1 ]; then
        extract_thumbnail "$output" "$output_dir"
    fi
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -r|--resolution)
            RESOLUTION="$2"
            shift 2
            ;;
        -b|--bitrate)
            BITRATE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -t|--thumbnail)
            EXTRACT_THUMBNAIL=1
            shift
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
    echo -e "${RED}Error: No input video specified${NC}"
    usage
fi

# Check if input file exists
if [ ! -f "$INPUT" ]; then
    echo -e "${RED}Error: '$INPUT' does not exist${NC}"
    exit 1
fi

# Check dependencies
check_dependencies

# Set output directory
if [ -z "$OUTPUT_DIR" ]; then
    OUTPUT_DIR=$(dirname "$INPUT")
fi
mkdir -p "$OUTPUT_DIR"

echo "Video Processor"
echo "==============="
echo "Resolution: $RESOLUTION"
echo "Bitrate: $BITRATE"
echo ""

# Process the video
process_video "$INPUT" "$OUTPUT_DIR"

echo ""
echo -e "${GREEN}Done!${NC}"
