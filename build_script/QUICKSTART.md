# 🚀 QUICK START - Get Your Cookbook Running in 5 Minutes!

## ⚡ Super Quick Version

### 1. Install Python
If you don't have Python, download from: https://www.python.org/downloads/

### 2. Install Dependencies
```bash
pip install markdown
```

### 3. Run the Easy Script

**On Mac/Linux:**
```bash
./generate.sh
```

**On Windows:**
Double-click `generate.bat` or run:
```cmd
generate.bat
```

### 4. View Your Cookbook
```bash
cd deploy
python -m http.server 8000
```
Open: http://localhost:8000

---

## 📁 Files Included

- **cookbook_generator.py** - Main script (the brain)
- **generate.sh** - Easy run script for Mac/Linux
- **generate.bat** - Easy run script for Windows
- **requirements.txt** - Dependencies list
- **README.md** - Full documentation
- **SETUP_GUIDE.md** - Step-by-step setup instructions
- **example_build/** - Sample recipes to get you started

---

## 📝 Adding Your Recipes

### File Structure:
```
your-project/
├── cookbook_generator.py
├── generate.sh or generate.bat
├── build/                    ← Create this!
│   ├── snacks/              ← Your categories
│   │   ├── samosa.md
│   │   └── pakora.md
│   ├── desserts/
│   │   └── ice_cream.md
│   └── main_dishes/
│       └── curry.md
└── deploy/                   ← Generated automatically
```

### Recipe Format (Markdown):
```markdown
# Recipe Name

## Ingredients
- Item 1
- Item 2

## Instructions
1. Step one
2. Step two

## Tips
- Helpful tip
```

Or use HTML if you prefer!

---

## ⚠️ Troubleshooting

**"No module named 'markdown'"**
```bash
pip install markdown
```

**"No recipes found"**
- Make sure you have a `build/` folder
- Add category folders inside it (e.g., `build/snacks/`)
- Add .md or .html files to those folders

**Want to see examples?**
Check the `example_build/` folder for sample recipes!

---

## 🎨 What You Get

✅ Beautiful, mobile-friendly web app
✅ Works offline (PWA)
✅ Searchable recipes
✅ Category organization
✅ Can be installed as an app
✅ Fast and responsive

---

## 📤 Next Steps After Generation

1. **Test locally** (as shown above)
2. **Customize colors** in `deploy/styles.css` if you want
3. **Add icons** (icon-192.png and icon-512.png) to `deploy/` folder
4. **Deploy** to GitHub Pages, Netlify, or any web host

---

## 🆘 Need Help?

1. Read **README.md** for full documentation
2. Read **SETUP_GUIDE.md** for detailed setup steps
3. Check **example_build/** folder for recipe examples

---

## 🎉 That's It!

You now have a modern, professional cookbook web app!

**Enjoy cooking! 🍽️**
