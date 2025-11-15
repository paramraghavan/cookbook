@echo off
REM Vegetarian Cookbook PWA Generator - Quick Run Script for Windows

echo.
echo 🌱 Vegetarian Cookbook PWA Generator
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if markdown is installed
echo Checking dependencies...
python -c "import markdown" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  markdown package not found. Installing...
    python -m pip install markdown
    if errorlevel 1 (
        echo ❌ Failed to install markdown. Please run: pip install markdown
        pause
        exit /b 1
    )
)

echo ✓ Dependencies OK
echo.

REM Check if build folder exists
if not exist "build" (
    echo ⚠️  'build' folder not found. Creating it...
    mkdir build
    echo ✓ Created 'build' folder
    echo.
    echo 📝 Next steps:
    echo   1. Add your recipe folders inside 'build\' ^(e.g., build\snacks\^)
    echo   2. Add recipe files ^(.md or .html^) to each folder
    echo   3. Run this script again
    echo.
    pause
    exit /b 0
)

REM Check for recipes
set recipe_count=0
for /r build %%f in (*.md *.html) do set /a recipe_count+=1

if %recipe_count%==0 (
    echo ⚠️  No recipes found in 'build' folder
    echo.
    echo 📝 To add recipes:
    echo   1. Create category folders in 'build\' ^(e.g., build\snacks\^)
    echo   2. Add recipe files ^(.md or .html^) to each folder
    echo   3. Run this script again
    echo.
    pause
    exit /b 0
)

echo Found: %recipe_count% recipes
echo.
echo Starting generation...
echo.

REM Run the generator
python cookbook_generator.py

if errorlevel 1 (
    echo.
    echo ❌ Generation failed. Check the errors above.
    pause
    exit /b 1
)

echo.
echo 🎉 Success!
echo.
echo To test your cookbook:
echo   cd deploy
echo   python -m http.server 8000
echo   Open: http://localhost:8000
echo.
pause
