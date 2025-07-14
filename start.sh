#!/bin/bash

# Start script for live preview
# Makes it easy to start the preview server with a single command

echo "Annotated Bill Live Preview"
echo "=============================="
echo ""

# Check if markdown file is provided
if [ -z "$1" ]; then
    # No argument provided, look for common files
    if [ -f "bill.md" ]; then
        MD_FILE="bill.md"
    elif [ -f "document.md" ]; then
        MD_FILE="document.md"
    else
        # Find first .md file
        MD_FILE=$(find . -maxdepth 1 -name "*.md" -not -name "README.md" | head -n 1)
        
        if [ -z "$MD_FILE" ]; then
            echo "❌ No markdown file found!"
            echo ""
            echo "Usage: ./start.sh [markdown-file]"
            echo ""
            echo "Examples:"
            echo "  ./start.sh bill.md"
            echo "  ./start.sh my-document.md"
            echo ""
            echo "Or create a file named 'bill.md' and run ./start.sh"
            exit 1
        fi
    fi
else
    MD_FILE="$1"
fi

# Check if file exists
if [ ! -f "$MD_FILE" ]; then
    echo "❌ Error: File '$MD_FILE' not found!"
    exit 1
fi

# Check if Python scripts exist
if [ ! -f "md_to_annotated_html.py" ]; then
    echo "❌ Error: md_to_annotated_html.py not found!"
    echo "Make sure you have all the required files in your repository."
    exit 1
fi

if [ ! -f "live_preview.py" ]; then
    echo "❌ Error: live_preview.py not found!"
    echo "Make sure you have all the required files in your repository."
    exit 1
fi

# Determine output filename
HTML_FILE="${MD_FILE%.md}.html"

echo "📄 Input:  $MD_FILE"
echo "📄 Output: $HTML_FILE"
echo ""
echo "Starting live preview server..."
echo ""

# Make sure Python uses unbuffered output
export PYTHONUNBUFFERED=1

# Start the live preview server
python live_preview.py "$MD_FILE" "$HTML_FILE"