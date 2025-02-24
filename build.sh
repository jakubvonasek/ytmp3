#!/bin/bash

# Define app name
APP_NAME="YTMP3"
ICON_FILE="./icon.icns"
SCRIPT_FILE="script.py"
# Find FFmpeg dynamically
FFMPEG_PATH=$(which ffmpeg)

if [ -z "$FFMPEG_PATH" ]; then
    echo "⚠️  FFmpeg not found. Please install it or update the path in this script."
    exit 1
fi

echo "🛠️  Cleaning old builds..."
rm -rf build dist "$APP_NAME.spec"

# Ensure FFmpeg is bundled
if [ ! -f "$FFMPEG_PATH" ]; then
    echo "⚠️  FFmpeg not found at $FFMPEG_PATH. Please install it or update the path in this script."
    exit 1
fi

echo "🚀 Building $APP_NAME with bundled FFmpeg..."
pyinstaller --onedir --windowed --name "$APP_NAME" --icon="$ICON_FILE" --add-binary "$FFMPEG_PATH:." "$SCRIPT_FILE"

# Check if build was successful
if [ -d "dist/$APP_NAME.app" ]; then
    echo "✅ Build successful! Moving to Applications..."
    mv "dist/$APP_NAME.app" /Applications/
    echo "🎉 Done! You can now open $APP_NAME from Applications."
else
    echo "❌ Build failed! Check for errors."
fi
