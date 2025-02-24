#!/bin/bash

APP_NAME="YTMP3"

echo "🗑️  Uninstalling $APP_NAME..."

# Remove the app from Applications
if [ -d "/Applications/$APP_NAME.app" ]; then
    echo "🗑️  Removing /Applications/$APP_NAME.app..."
    rm -rf "/Applications/$APP_NAME.app"
else
    echo "⚠️  $APP_NAME.app not found in Applications."
fi

# Remove build artifacts
echo "🗑️  Cleaning up build files..."
rm -rf build dist "$APP_NAME.spec"

# Ask user if they want to delete the project folder
read -p "❓ Do you also want to delete the project folder? (y/N): " DELETE_PROJECT
if [[ "$DELETE_PROJECT" =~ ^[Yy]$ ]]; then
    cd ..
    rm -rf "$(basename "$PWD")"
    echo "✅ Project folder deleted."
else
    echo "✅ Uninstallation complete, project folder kept."
fi

echo "🎉 Done! $APP_NAME has been removed." 