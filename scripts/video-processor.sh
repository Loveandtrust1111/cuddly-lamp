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

# Process video
echo "Converting video..."

# Build FFmpeg command using array to avoid eval and command injection
FFMPEG_ARGS=(-i "$INPUT_FILE" -y)

# Add resolution scaling if specified
if [ -n "$RESOLUTION" ]; then
    FFMPEG_ARGS+=(-vf "scale=$RESOLUTION")
fi

# Add video codec and quality settings
FFMPEG_ARGS+=(-c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k)

# Add output file
FFMPEG_ARGS+=("$OUTPUT_FILE")

# Execute FFmpeg
ffmpeg "${FFMPEG_ARGS[@]}"

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
    
    # Get video duration in seconds
    DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$INPUT_FILE" 2>/dev/null)
    
    # Validate that DURATION is a valid number, use 1.0 as safe default if probe fails
    if ! [[ "$DURATION" =~ ^[0-9]+\.?[0-9]*$ ]] || [ -z "$DURATION" ]; then
        echo "  Warning: Could not determine video duration, using default timestamp"
        DURATION="1.0"
    fi
    
    # Calculate thumbnail timestamp (minimum of 10% of duration or 0.5 seconds)
    THUMB_TIME=$(awk -v d="$DURATION" 'BEGIN {
        ten_percent = d * 0.1;
        threshold = 0.5;
        t = (ten_percent < threshold) ? ten_percent : threshold;
        if (t < 0) t = 0;
        printf "%.2f", t
    }')
    
    # Extract frame at calculated timestamp
    # Capture exit code before filtering output
    FFMPEG_OUTPUT=$(ffmpeg -i "$INPUT_FILE" -ss "$THUMB_TIME" -vframes 1 -q:v 2 "$THUMBNAIL_FILE" -y 2>&1)
    FFMPEG_EXIT=$?
    
    # Show relevant errors if any (filter out verbose info)
    if [ $FFMPEG_EXIT -ne 0 ]; then
        echo "$FFMPEG_OUTPUT" | grep -i "error" | head -5
    fi
    
    # Check if thumbnail was created successfully
    if [ $FFMPEG_EXIT -eq 0 ] && [ -f "$THUMBNAIL_FILE" ]; then
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
