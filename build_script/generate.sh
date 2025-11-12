#!/bin/bash

# Vegetarian Cookbook PWA Generator - Quick Run Script

echo "🌱 Vegetarian Cookbook PWA Generator"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Error: Python is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

# Use python3 if available, otherwise python
if command -v python3 &> /dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

echo "✓ Python found"

# Check if markdown is installed
echo "Checking dependencies..."
$PYTHON -c "import markdown" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  markdown package not found. Installing..."
    $PYTHON -m pip install markdown
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install markdown. Please run: pip install markdown"
        exit 1
    fi
fi

echo "✓ Dependencies OK"
echo ""

# Check if build folder exists
if [ ! -d "build" ]; then
    echo "⚠️  'build' folder not found. Creating it..."
    mkdir build
    echo "✓ Created 'build' folder"
    echo ""
    echo "📝 Next steps:"
    echo "  1. Add your recipe folders inside 'build/' (e.g., build/snacks/)"
    echo "  2. Add recipe files (.md or .html) to each folder"
    echo "  3. Run this script again"
    echo ""
    exit 0
fi

# Count recipe folders and files
folder_count=$(find build -maxdepth 1 -type d ! -path build -print | wc -l)
recipe_count=$(find build -type f \( -name "*.md" -o -name "*.html" \) -print | wc -l)

if [ $recipe_count -eq 0 ]; then
    echo "⚠️  No recipes found in 'build' folder"
    echo ""
    echo "📝 To add recipes:"
    echo "  1. Create category folders in 'build/' (e.g., build/snacks/)"
    echo "  2. Add recipe files (.md or .html) to each folder"
    echo "  3. Run this script again"
    echo ""
    exit 0
fi

echo "Found: $folder_count categories, $recipe_count recipes"
echo ""
echo "Starting generation..."
echo ""

# Run the generator
$PYTHON cookbook_generator.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Success!"
    echo ""
    echo "To test your cookbook:"
    echo "  cd deploy"
    echo "  python -m http.server 8000"
    echo "  Open: http://localhost:8000"
    echo ""
else
    echo ""
    echo "❌ Generation failed. Check the errors above."
    exit 1
fi
