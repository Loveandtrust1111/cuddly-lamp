#!/bin/bash

# Video Processor Script
# Converts videos to MP4 format with specified resolution and generates thumbnails

set -e

# Default values
RESOLUTION=""
GENERATE_THUMBNAIL=false
INPUT_FILE=""

# Display usage information
usage() {
    cat << EOF
Usage: $0 [OPTIONS] INPUT_VIDEO

Process and convert video files to MP4 format.

OPTIONS:
    -r RESOLUTION   Set output resolution (e.g., 1280x720, 1920x1080)
    -t              Generate thumbnail from video
    -h              Display this help message

EXAMPLES:
    $0 -r 1280x720 -t video.mov
    $0 -r 1920x1080 input.avi
    $0 -t video.mp4

REQUIREMENTS:
    - FFmpeg

EOF
    exit 1
}

# Parse command line arguments
while getopts "r:th" opt; do
    case $opt in
        r)
            RESOLUTION=$OPTARG
            if ! [[ "$RESOLUTION" =~ ^[0-9]+x[0-9]+$ ]]; then
                echo "Error: Resolution must be in format WIDTHxHEIGHT (e.g., 1280x720)"
                exit 1
            fi
            ;;
        t)
            GENERATE_THUMBNAIL=true
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

# Get input file
INPUT_FILE="$1"

if [ -z "$INPUT_FILE" ]; then
    echo "Error: Input video file is required"
    usage
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' does not exist"
    exit 1
fi

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: FFmpeg is not installed. Please install it first."
    echo "On Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "On macOS: brew install ffmpeg"
    exit 1
fi

echo "Video Processor"
echo "==============="
echo "Input file: $INPUT_FILE"
if [ -n "$RESOLUTION" ]; then
    echo "Resolution: $RESOLUTION"
fi
echo "Generate thumbnail: $GENERATE_THUMBNAIL"
echo ""

# Get input file information
BASENAME=$(basename "$INPUT_FILE")
FILENAME="${BASENAME%.*}"
DIRNAME=$(dirname "$INPUT_FILE")

# Generate output filename
OUTPUT_FILE="${DIRNAME}/${FILENAME}_processed.mp4"

# Build FFmpeg command
FFMPEG_CMD="ffmpeg -i \"$INPUT_FILE\" -y"

# Add resolution scaling if specified
if [ -n "$RESOLUTION" ]; then
    FFMPEG_CMD="$FFMPEG_CMD -vf scale=$RESOLUTION"
fi

# Add video codec and quality settings
FFMPEG_CMD="$FFMPEG_CMD -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k"

# Add output file
FFMPEG_CMD="$FFMPEG_CMD \"$OUTPUT_FILE\""

# Process video
echo "Converting video..."
eval $FFMPEG_CMD

if [ $? -eq 0 ]; then
    echo "✓ Video converted successfully: $OUTPUT_FILE"
else
    echo "✗ Error converting video"
    exit 1
fi

# Generate thumbnail if requested
if [ "$GENERATE_THUMBNAIL" = true ]; then
    THUMBNAIL_FILE="${DIRNAME}/${FILENAME}_thumb.jpg"
    echo ""
    echo "Generating thumbnail..."
    
    # Extract frame at 1 second or 10% of video duration, whichever is smaller
    ffmpeg -i "$INPUT_FILE" -ss 00:00:01 -vframes 1 -q:v 2 "$THUMBNAIL_FILE" -y 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "✓ Thumbnail generated: $THUMBNAIL_FILE"
    else
        echo "✗ Error generating thumbnail"
        exit 1
    fi
fi

echo ""
echo "Complete!"
echo "Output video: $OUTPUT_FILE"
if [ "$GENERATE_THUMBNAIL" = true ]; then
    echo "Thumbnail: $THUMBNAIL_FILE"
fi

# Display file sizes
echo ""
echo "File sizes:"
echo "  Input:  $(du -h "$INPUT_FILE" | cut -f1)"
echo "  Output: $(du -h "$OUTPUT_FILE" | cut -f1)"
if [ "$GENERATE_THUMBNAIL" = true ]; then
    echo "  Thumbnail: $(du -h "$THUMBNAIL_FILE" | cut -f1)"
fi
