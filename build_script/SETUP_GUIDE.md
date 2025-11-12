# 🚀 Setup Guide - Vegetarian Cookbook PWA

## Step-by-Step Setup Instructions

### Step 1: Prepare Your Environment

1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Make sure Python 3.7+ is installed
   - Verify: `python --version`

2. **Download the Script Files**
   - `cookbook_generator.py` - Main script
   - `requirements.txt` - Dependencies
   - `README.md` - Documentation

### Step 2: Install Dependencies

Open your terminal/command prompt in the script folder and run:

```bash
pip install -r requirements.txt
```

Or install the markdown package directly:

```bash
pip install markdown
```

### Step 3: Organize Your Recipes

1. **Create the build folder** in the same directory as the script:
   ```bash
   mkdir build
   ```

2. **Create category folders** inside build/:
   ```bash
   mkdir build/snacks
   mkdir build/desserts
   mkdir build/main_dishes
   mkdir build/breads
   mkdir build/pickles
   ```
   
   Or create any category names you want!

3. **Add your recipes** to each folder:
   - Save as `.md` (Markdown) or `.html` files
   - Use descriptive filenames: `paneer_butter_masala.md`
   - File names will become recipe titles (with underscores replaced by spaces)

### Step 4: Run the Generator

```bash
python cookbook_generator.py
```

You should see output like:
```
🌱 Vegetarian Cookbook PWA Generator

1. Cleaning deploy directory...

2. Scanning recipes...
  Found 3 recipes in 'snacks'
  Found 5 recipes in 'desserts'
  Found 4 recipes in 'main_dishes'

3. Generating recipe pages...
  ✓ Generated 12 recipe pages

4. Generating index page...

5. Generating assets...
  Note: Created icon placeholders. Please add actual icon-192.png and icon-512.png images.

✅ Generation complete!

📁 Your PWA is ready in the 'deploy' folder
```

### Step 5: Test Your PWA Locally

1. **Navigate to the deploy folder:**
   ```bash
   cd deploy
   ```

2. **Start a local server:**
   ```bash
   python -m http.server 8000
   ```

3. **Open in browser:**
   - Go to: http://localhost:8000
   - Test on mobile: Use your computer's local IP (e.g., http://192.168.1.100:8000)

### Step 6: Add Custom Icons (Optional but Recommended)

1. **Create or find icons:**
   - Use https://favicon.io/ to generate icons
   - Or design your own in any graphics software
   - Need two sizes: 192x192 and 512x512 pixels

2. **Replace placeholder icons:**
   - Save as `icon-192.png` in the deploy folder
   - Save as `icon-512.png` in the deploy folder

### Step 7: Deploy to the Web

#### Option A: GitHub Pages (Free)

1. Create a new repository on GitHub
2. Upload the contents of the `deploy` folder
3. Go to Settings → Pages
4. Select main branch and root folder
5. Your cookbook is live at: `https://yourusername.github.io/cookbook`

#### Option B: Netlify (Free, Easiest)

1. Go to https://netlify.com
2. Drag and drop the `deploy` folder
3. Your site is live instantly!

#### Option C: Vercel (Free)

1. Go to https://vercel.com
2. Import your project
3. Deploy with one click

#### Option D: Your Own Web Hosting

1. Upload the contents of the `deploy` folder to your web server
2. Point your domain to the folder
3. Done!

## 📱 Installing as an App

Once deployed, users can install your cookbook as an app:

### On Android (Chrome)
1. Open the website
2. Tap the menu (three dots)
3. Select "Install app" or "Add to Home screen"

### On iOS (Safari)
1. Open the website
2. Tap the Share button
3. Select "Add to Home Screen"

### On Desktop (Chrome/Edge)
1. Open the website
2. Click the install icon in the address bar
3. Or use menu → Install

## 🎨 Customization Tips

### Change Colors
Edit `deploy/styles.css` and modify these variables:
```css
:root {
    --primary-color: #4CAF50;    /* Your main color */
    --primary-dark: #388E3C;     /* Darker shade */
    --secondary-color: #FF9800;  /* Accent color */
}
```

### Change Title and Description
Edit `deploy/manifest.json`:
```json
{
    "name": "My Family Cookbook",
    "short_name": "FamilyRecipes",
    "description": "Grandma's secret recipes"
}
```

### Add More Categories
Just create new folders in the `build` directory and run the script again!

## 🔄 Updating Your Cookbook

1. **Add new recipes** to the build folder
2. **Run the generator again:** `python cookbook_generator.py`
3. **Upload the new deploy folder** to your hosting

The script will regenerate everything fresh each time.

## ❓ Troubleshooting

### "No module named 'markdown'"
**Solution:** Install the markdown package:
```bash
pip install markdown
```

### "No recipe folders found"
**Solution:** Make sure:
- You have a `build` folder
- The `build` folder contains category folders
- Category folders contain .md or .html files

### Recipes not showing up
**Solution:** Check:
- File extensions are `.md` or `.html` (not `.txt`)
- Files are inside category folders (not in the root of build)
- Folder names don't start with a dot (.)

### Icons not displaying
**Solution:** Add actual PNG images:
- `icon-192.png` (192x192 pixels)
- `icon-512.png` (512x512 pixels)

### PWA not installing
**Solution:** PWAs require HTTPS:
- Use a hosting service (they provide HTTPS)
- Or use a local server for testing

## 📝 Quick Recipe Template

Copy this template for new recipes:

```markdown
# Recipe Name

Brief description of the dish.

## Ingredients
- Item 1
- Item 2
- Item 3

## Instructions
1. Step one
2. Step two
3. Step three

## Cooking Time
- Prep: 15 minutes
- Cook: 30 minutes
- Total: 45 minutes

## Servings
4 servings

## Tips
- Tip 1
- Tip 2
```

## 🎉 You're All Set!

Your vegetarian cookbook is now:
- ✅ Mobile-friendly
- ✅ Searchable
- ✅ Installable as an app
- ✅ Works offline
- ✅ Beautiful and easy to use

Enjoy cooking! 🍽️
