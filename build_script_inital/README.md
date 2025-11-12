# 🌱 Vegetarian Cookbook PWA Generator

Convert your collection of vegetarian recipes into a beautiful, mobile-friendly Progressive Web App!

## 📁 Folder Structure

```
your-project/
├── cookbook_generator.py    # The main script (this file)
├── requirements.txt          # Python dependencies
├── build/                    # Your recipe folders go here
│   ├── snacks/
│   │   ├── samosa.md
│   │   ├── pakora.html
│   │   └── spring_rolls.md
│   ├── icecream/
│   │   ├── vanilla.md
│   │   └── mango.md
│   ├── pickle/
│   │   └── lemon_pickle.md
│   └── papad/
│       └── masala_papad.html
└── deploy/                   # Generated PWA (created by script)
    ├── index.html
    ├── styles.css
    ├── app.js
    ├── manifest.json
    ├── sw.js
    └── [recipe folders]
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install markdown
```

### 2. Organize Your Recipes

Create a `build/` folder and add your recipe categories as subfolders:

```bash
mkdir -p build/snacks build/icecream build/pickle build/papad
```

Add your recipes as `.md` (Markdown) or `.html` files in each folder.

### 3. Run the Generator

```bash
python cookbook_generator.py
```

### 4. Test Your PWA

```bash
cd deploy
python -m http.server 8000
```

Open your browser to: `http://localhost:8000`

## 📝 Recipe File Formats

### Markdown (.md)
```markdown
# Vegetable Samosa

## Ingredients
- 2 cups all-purpose flour
- 4 potatoes, boiled and mashed
- 1 cup peas
- Spices: cumin, coriander, turmeric

## Instructions
1. Make the dough with flour and water
2. Prepare the filling with potatoes and spices
3. Shape into triangles
4. Deep fry until golden brown

## Tips
- Serve hot with mint chutney
- Can be frozen for later use
```

### HTML (.html)
```html
<h1>Mango Ice Cream</h1>

<h2>Ingredients</h2>
<ul>
    <li>2 ripe mangoes</li>
    <li>2 cups heavy cream</li>
    <li>1 cup condensed milk</li>
</ul>

<h2>Instructions</h2>
<ol>
    <li>Puree the mangoes</li>
    <li>Whip the cream until stiff</li>
    <li>Fold everything together</li>
    <li>Freeze for 6 hours</li>
</ol>
```

## ✨ Features

- **📱 Mobile-First Design**: Works beautifully on phones and tablets
- **🔍 Search Functionality**: Quickly find any recipe
- **📂 Category Organization**: Recipes organized by type
- **💾 Offline Support**: Works without internet (PWA)
- **⚡ Fast & Responsive**: Smooth navigation
- **🎨 Beautiful UI**: Clean, modern design
- **📥 Installable**: Can be installed as an app on mobile devices

## 🎨 Customization

### Change Colors
Edit the CSS variables in `deploy/styles.css`:

```css
:root {
    --primary-color: #4CAF50;    /* Main green color */
    --primary-dark: #388E3C;     /* Darker green */
    --secondary-color: #FF9800;  /* Orange accent */
}
```

### Add Icons
Replace these placeholder files with actual PNG images:
- `deploy/icon-192.png` (192x192 pixels)
- `deploy/icon-512.png` (512x512 pixels)

You can create icons at: https://favicon.io/

### Modify Emojis
Change category icons in the script or CSS.

## 📤 Deployment

### GitHub Pages
1. Push the `deploy/` folder to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Your cookbook is now live!

### Netlify/Vercel
1. Drag and drop the `deploy/` folder
2. Your site is deployed instantly!

### Any Web Host
Simply upload the contents of the `deploy/` folder to your web server.

## 🔧 Troubleshooting

**No recipes found?**
- Make sure recipes are in `build/` folder
- Check file extensions are `.md` or `.html`
- Folder names should not start with `.`

**Markdown not rendering?**
- Install markdown: `pip install markdown`
- Check your markdown syntax

**Icons not showing?**
- Add `icon-192.png` and `icon-512.png` to the deploy folder
- Use square images (192x192 and 512x512 pixels)

## 📋 Recipe Template

Create new recipes quickly with this template:

```markdown
# Recipe Name

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
- Helpful tip 1
- Helpful tip 2

## Nutrition (Optional)
- Calories: 250
- Protein: 10g
- Carbs: 30g
```

## 🤝 Contributing

Feel free to customize this script for your needs! Some ideas:
- Add recipe ratings
- Include cooking time and servings
- Add ingredient scaling
- Include nutritional information
- Add photo galleries
- Implement recipe sharing

## 📄 License

Free to use and modify for your personal or commercial projects!

---

**Happy Cooking! 🍽️**

Made with ❤️ for vegetarian food lovers
