#!/usr/bin/env python3
"""
Vegetarian Cookbook PWA Generator
Converts folders of recipes (markdown/html) into a Progressive Web App
"""

import os
import shutil
from pathlib import Path
import markdown
import json

force_refresh_html = """
<style>
.force-refresh-btn {
  position: fixed;
  top: 18px;
  right: 18px;
  z-index: 9999;
  background: #fff;
  color: #222;
  border: none;
  border-radius: 50%;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.18);
  cursor: pointer;
  font-size: 1.7rem;
  transition: background 0.16s;
}
.force-refresh-btn:active {
  background: #eee;
}
.force-refresh-btn svg {
  width: 28px;
  height: 28px;
  fill: #222;
}
</style>

<button class="force-refresh-btn" onclick="forceRefresh()" aria-label="Force Refresh">
  <svg viewBox="0 0 24 24"><path d="M12 4V1L8 5l4 4V6c3.31 0 6 2.69 6 6a5.998 5.998 0 0 1-6 6c-2.76 0-5.13-2.12-5.84-4.74l-1.97.51C5.54 18.37 8.53 21 12 21c4.42 0 8-3.58 8-8s-3.58-8-8-8z"></path></svg>
</button>

<script>
function forceRefresh() {
  window.location.href = window.location.pathname + "?refresh=" + new Date().getTime();
}
</script>
"""

share_link_html="""
<style>
.share-btn {
  position: fixed;
  top: 18px;
  right: 72px;  /* to the left of refresh */
  z-index: 9999;
  background: #2D5F3F;
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.18);
  cursor: pointer;
  font-size: 1.3rem;
  transition: background 0.16s;
}
.share-btn:active {
  background: #244c32;
}
</style>
<button class="share-btn" onclick="shareRecipe()" aria-label="Share Recipe">
  ⇪
</button>
"""


class CookbookGenerator:
    def __init__(self, build_dir='build', deploy_dir='deploy'):
        self.build_dir = Path(build_dir)
        self.deploy_dir = Path(deploy_dir)
        self.recipes = {}

    def clean_deploy_dir(self):
        """Clean and create deploy directory"""
        if self.deploy_dir.exists():
            shutil.rmtree(self.deploy_dir)
        self.deploy_dir.mkdir(parents=True)

    def scan_recipes(self):
        """Scan all folders and recipes"""
        print("Scanning recipes...")
        excluded_files = ['readme', 'index']  # Files to exclude (case-insensitive)

        for folder in self.build_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith('.'):
                folder_name = folder.name
                self.recipes[folder_name] = []

                for recipe_file in folder.iterdir():
                    if recipe_file.suffix in ['.md', '.html']:
                        recipe_name = recipe_file.stem

                        # Skip README and index files
                        if recipe_name.lower() in excluded_files:
                            print(f"  Skipping '{recipe_file.name}' in '{folder_name}'")
                            continue

                        self.recipes[folder_name].append({
                            'name': recipe_name,
                            'file': recipe_file,
                            'type': recipe_file.suffix
                        })

                print(f"  Found {len(self.recipes[folder_name])} recipes in '{folder_name}'")

    def convert_markdown_to_html(self, md_content):
        """Convert markdown to HTML"""
        return markdown.markdown(md_content, extensions=['extra', 'nl2br'])

    def read_recipe_content(self, recipe):
        """Read and convert recipe content to HTML"""
        with open(recipe['file'], 'r', encoding='utf-8') as f:
            content = f.read()

        if recipe['type'] == '.md':
            return self.convert_markdown_to_html(content)
        else:
            return content

    def generate_recipe_page(self, category, recipe):
        """Generate individual recipe page"""
        content = self.read_recipe_content(recipe)
        recipe_id = f"{category}_{recipe['name']}".replace(' ', '_')

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#2D5F3F">
    <title>{recipe['name']} - Vegetarian Cookbook</title>
    <link rel="manifest" href="../manifest.json">
    <link rel="stylesheet" href="../styles.css">
    <link rel="icon" type="image/png" href="../icon-192.png">
</head>
<body>
    {share_link_html}
    <button class="back-btn" onclick="history.back()">Back</button>
    
    <header>
        <h1>{recipe['name']}</h1>
    </header>
    
    <main class="recipe-content">
        {content}
    </main>
    
    <footer>
        <p>Made with <span class="heart">❤️</span> by a <a href="../index.html">Foodie</a></p>
    </footer>
    
    <script src="../app.js"></script>
</body>
</html>'''

        # Create category folder in deploy
        category_dir = self.deploy_dir / category
        category_dir.mkdir(exist_ok=True)

        # Write recipe file
        recipe_path = category_dir / f"{recipe['name'].replace(' ', '_')}.html"
        with open(recipe_path, 'w', encoding='utf-8') as f:
            f.write(html)

        return recipe_id

    def generate_index_page(self):
        """Generate main index page"""
        # Category icons mapping - using emoji icons
        category_icons = {
            'vegetarian': '🌿',
            'vegan': '🌱',
            'snacks': '🥜',
            'snack': '🥜',
            'bakery': '🥐',
            'bread': '🍞',
            'breads': '🍞',
            'beverages': '🥤',
            'beverage': '☕',
            'drinks': '🥤',
            'desserts': '🍰',
            'dessert': '🍰',
            'sweets': '🍬',
            'main_dishes': '🍲',
            'maindishes': '🍲',
            'main': '🍲',
            'curry': '🍛',
            'rice': '🍚',
            'pickles': '🥒',
            'pickle': '🥒',
            'chutney': '🥣',
            'soup': '🥘',
            'salad': '🥗',
            'breakfast': '🥯',
            'lunch': '🍱',
            'dinner': '🍽️',
            'appetizers': '🥙',
            'sides': '🥙',
            'icecream': '🍦',
            'papad': '🌕'
        }

        categories_html = ""

        for category, recipes in sorted(self.recipes.items()):
            recipe_count = len(recipes)
            category_display = category.replace('_', ' ').title()

            # Get icon for category (default to recipe book emoji if not found)
            category_lower = category.lower().replace('_', '').replace(' ', '')
            icon = category_icons.get(category_lower, '📖')

            categories_html += f'''
            <div class="category-card" onclick="showCategory('{category}')">
                <div class="category-icon">{icon}</div>
                <h2>{category_display}</h2>
                <p>{recipe_count} recipe{'s' if recipe_count != 1 else ''}</p>
            </div>
            '''

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#2D5F3F">
    <meta name="description" content="A collection of delicious vegetarian recipes">
    <title>Vegetarian Cookbook</title>
    <link rel="manifest" href="manifest.json">
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/png" href="icon-192.png">
    <link rel="apple-touch-icon" href="icon-192.png">
</head>
<body>
    {force_refresh_html}
    <button class="back-btn" id="backBtn" style="display: none;" onclick="showCategories()">Back</button>
    
    <header>
        <h1>🌱 Vegetarian Cookbook</h1>
    </header>
    
    <main>
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Search recipes..." onkeyup="searchRecipes()">
        </div>
        
        <div id="categoriesView" class="categories-grid">
            {categories_html}
        </div>
        
        <div id="recipesView" class="recipes-view" style="display: none;">
            <h2 id="categoryTitle"></h2>
            <div id="recipesList" class="recipes-grid"></div>
        </div>
    </main>
    
    <footer>
        <p>Made with <span class="heart">❤️</span> by a <a href="#" onclick="return false;">Foodie</a></p>
    </footer>
    
    <div id="installPrompt" class="install-prompt" style="display: none;">
        <p>📱 Install this app for quick access!</p>
        <button onclick="installApp()">Install</button>
        <button onclick="dismissInstall()">Later</button>
    </div>
    
    <div id="iosInstallModal" class="ios-install-modal" style="display: none;">
        <div class="ios-install-content">
            <h3>📱 Install App</h3>
            <p>Add this cookbook to your home screen for quick access!</p>
            
            <div class="ios-install-steps">
                <div class="ios-install-step">
                    <div class="step-number">1</div>
                    <div class="step-text">Tap the Share button <span class="step-icon">⎋</span> at the bottom of Safari</div>
                </div>
                <div class="ios-install-step">
                    <div class="step-number">2</div>
                    <div class="step-text">Scroll down and tap <strong>"Add to Home Screen"</strong> <span class="step-icon">➕</span></div>
                </div>
                <div class="ios-install-step">
                    <div class="step-number">3</div>
                    <div class="step-text">Tap <strong>"Add"</strong> in the top right corner</div>
                </div>
            </div>
            
            <button onclick="closeIosModal()">Got It!</button>
            <span class="dont-show-again" onclick="dontShowAgain()">Don't show again</span>
        </div>
    </div>
    
    <script>
        const recipesData = {json.dumps(self.recipes, default=str)};
    </script>
    <script src="app.js"></script>
</body>
</html>'''

        with open(self.deploy_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)

    def generate_styles(self):
        """Generate CSS styles"""
        css = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #2D5F3F;
    --primary-light: #4A8B5C;
    --primary-dark: #1A3A28;
    --secondary-color: #D97D54;
    --accent-color: #F4A460;
    --background: #FAF8F3;
    --background-pattern: #F5F1E8;
    --card-bg: #FFFFFF;
    --card-border: #E8E3D6;
    --text-primary: #2C2C2C;
    --text-secondary: #6B6B6B;
    --shadow: 0 2px 12px rgba(45, 95, 63, 0.08);
    --shadow-hover: 0 6px 20px rgba(45, 95, 63, 0.12);
    --gradient-start: #2D5F3F;
    --gradient-end: #4A8B5C;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, var(--background) 0%, var(--background-pattern) 100%);
    background-attachment: fixed;
    color: var(--text-primary);
    line-height: 1.6;
    padding-bottom: 2rem;
    position: relative;
}

body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.03;
    z-index: -1;
    background-image: 
        repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(45, 95, 63, 0.03) 35px, rgba(45, 95, 63, 0.03) 70px);
    pointer-events: none;
}

header {
    background: linear-gradient(135deg, var(--gradient-start) 0%, var(--gradient-end) 100%);
    color: white;
    padding: 1rem 1rem;
    text-align: center;
    box-shadow: var(--shadow);
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 3px solid var(--secondary-color);
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 60px;
}

header h1 {
    font-size: 1.5rem;
    margin: 0;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.subtitle {
    display: none;
}

main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.search-box {
    margin-bottom: 2.5rem;
}

.search-box input {
    width: 100%;
    padding: 1.2rem 1.5rem;
    border: 2px solid var(--card-border);
    border-radius: 50px;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: var(--card-bg);
    box-shadow: var(--shadow);
}

.search-box input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 4px rgba(45, 95, 63, 0.1);
    transform: translateY(-2px);
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
}

.category-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 2rem 1.5rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: var(--shadow);
    border: 2px solid var(--card-border);
    position: relative;
    overflow: hidden;
}

.category-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.category-card:hover::before {
    transform: scaleX(1);
}

.category-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-hover);
    border-color: var(--primary-light);
}

.category-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    display: block;
    filter: grayscale(20%);
    transition: all 0.3s ease;
}

.category-card:hover .category-icon {
    filter: grayscale(0%);
    transform: scale(1.1);
}

.category-card h2 {
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    font-weight: 600;
}

.category-card p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    font-weight: 500;
}

.recipes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
}

#categoryTitle {
    color: var(--primary-color);
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
    padding-top: 0.5rem;
}

.recipe-card {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 1.8rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: var(--shadow);
    border-left: 4px solid var(--primary-color);
    border: 2px solid var(--card-border);
    border-left: 4px solid var(--primary-color);
}

.recipe-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-hover);
    border-left-color: var(--secondary-color);
}

.recipe-card h3 {
    color: var(--text-primary);
    font-size: 1.3rem;
    font-weight: 600;
}

.back-btn {
    position: fixed;
    top: 10px;
    left: 10px;
    background: rgba(255, 255, 255, 0.95);
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
    padding: 0.6rem 1rem;
    border-radius: 50px;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 600;
    box-shadow: var(--shadow);
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}

.back-btn:hover {
    background: var(--primary-color);
    color: white;
    transform: translateX(-4px);
    box-shadow: var(--shadow-hover);
}

.back-btn::before {
    content: "←";
    font-size: 1.1rem;
}

.recipe-content {
    background: var(--card-bg);
    max-width: 800px;
    margin: 2rem auto;
    padding: 2.5rem;
    border-radius: 16px;
    box-shadow: var(--shadow-hover);
    border: 2px solid var(--card-border);
}

.recipe-content h1, .recipe-content h2, .recipe-content h3 {
    color: var(--primary-color);
    margin-top: 1.8rem;
    margin-bottom: 1rem;
}

.recipe-content h1 {
    font-size: 2.2rem;
    margin-top: 0;
    color: var(--primary-dark);
    border-bottom: 3px solid var(--secondary-color);
    padding-bottom: 0.8rem;
}

.recipe-content h2 {
    font-size: 1.6rem;
    margin-top: 2rem;
}

.recipe-content ul, .recipe-content ol {
    margin-left: 1.5rem;
    margin-bottom: 1.2rem;
}

.recipe-content li {
    margin-bottom: 0.6rem;
    line-height: 1.8;
}

.recipe-content p {
    margin-bottom: 1.2rem;
    line-height: 1.8;
}

.recipe-content img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    margin: 1.5rem 0;
    box-shadow: var(--shadow);
}

.recipe-content strong {
    color: var(--primary-dark);
    font-weight: 600;
}

.install-prompt {
    position: fixed;
    bottom: 1.5rem;
    left: 50%;
    transform: translateX(-50%);
    background: var(--card-bg);
    padding: 1.2rem 2rem;
    border-radius: 50px;
    box-shadow: 0 8px 24px rgba(45, 95, 63, 0.2);
    display: flex;
    align-items: center;
    gap: 1rem;
    z-index: 1000;
    border: 2px solid var(--primary-light);
}

.install-prompt button {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    color: white;
    border: none;
    padding: 0.6rem 1.3rem;
    border-radius: 50px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
}

.install-prompt button:hover {
    background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
    transform: scale(1.05);
}

.install-prompt button:last-child {
    background: transparent;
    color: var(--text-secondary);
}

.install-prompt button:last-child:hover {
    background: rgba(45, 95, 63, 0.05);
    color: var(--primary-color);
}

.ios-install-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
    backdrop-filter: blur(5px);
}

.ios-install-content {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 20px;
    max-width: 400px;
    margin: 1rem;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    text-align: center;
    animation: slideUp 0.3s ease;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.ios-install-content h3 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.ios-install-content p {
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

.ios-install-steps {
    background: var(--background);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    text-align: left;
}

.ios-install-step {
    display: flex;
    align-items: start;
    gap: 1rem;
    margin-bottom: 1rem;
    padding: 0.5rem;
}

.ios-install-step:last-child {
    margin-bottom: 0;
}

.step-number {
    background: var(--primary-color);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
}

.step-text {
    color: var(--text-primary);
    font-size: 0.95rem;
    line-height: 1.5;
    padding-top: 0.2rem;
}

.step-icon {
    font-size: 1.3rem;
    margin: 0 0.3rem;
}

.ios-install-content button {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    border-radius: 50px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    width: 100%;
    margin-top: 1rem;
}

.ios-install-content button:hover {
    background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
    transform: translateY(-2px);
}

.dont-show-again {
    display: block;
    margin-top: 1rem;
    color: var(--text-secondary);
    font-size: 0.9rem;
    cursor: pointer;
    text-decoration: underline;
}

.dont-show-again:hover {
    color: var(--primary-color);
}

footer {
    text-align: center;
    padding: 3rem 1rem 2rem;
    margin-top: 4rem;
    color: var(--text-secondary);
    font-size: 1rem;
    border-top: 2px solid var(--card-border);
    background: var(--background-pattern);
}

footer p {
    margin: 0.5rem 0;
}

footer .heart {
    color: var(--secondary-color);
    display: inline-block;
    animation: heartbeat 1.5s infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    10% { transform: scale(1.1); }
    20% { transform: scale(1); }
}

footer a {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.3s ease;
}

footer a:hover {
    color: var(--secondary-color);
}


@media (max-width: 768px) {
    header h1 {
        font-size: 1.2rem;
    }
    
    .categories-grid {
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 1rem;
    }
    
    .recipes-grid {
        grid-template-columns: 1fr;
    }
    
    .recipe-content {
        padding: 1.5rem;
        margin: 1rem;
    }
    
    .back-btn {
        top: 8px;
        left: 8px;
        padding: 0.5rem 0.8rem;
        font-size: 0.85rem;
    }
    
    #categoryTitle {
        font-size: 1.4rem;
    }
    
    .install-prompt {
        flex-direction: column;
        left: 1rem;
        right: 1rem;
        transform: none;
    }
    
    .ios-install-content {
        margin: 1rem;
        padding: 1.5rem;
        max-width: calc(100% - 2rem);
    }
    
    .ios-install-content h3 {
        font-size: 1.3rem;
    }
    
    .ios-install-steps {
        padding: 1rem;
    }
    
    .ios-install-step {
        gap: 0.8rem;
    }
    
    .step-text {
        font-size: 0.9rem;
    }
}'''

        with open(self.deploy_dir / 'styles.css', 'w', encoding='utf-8') as f:
            f.write(css)

    def generate_javascript(self):
        """Generate JavaScript for interactivity"""
        js = '''// iOS Detection and Install Prompt
function isIOS() {
    return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
}

function isInStandaloneMode() {
    return window.matchMedia('(display-mode: standalone)').matches || 
           window.navigator.standalone === true;
}

function shouldShowIOSPrompt() {
    // Don't show if already installed
    if (isInStandaloneMode()) return false;
    
    // Don't show if user dismissed it
    if (localStorage.getItem('iosInstallDismissed') === 'true') return false;
    
    // Don't show if shown in last 7 days
    const lastShown = localStorage.getItem('iosInstallLastShown');
    if (lastShown) {
        const daysSinceLastShown = (Date.now() - parseInt(lastShown)) / (1000 * 60 * 60 * 24);
        if (daysSinceLastShown < 7) return false;
    }
    
    return true;
}

// Show iOS install prompt on first visit
window.addEventListener('load', () => {
    if (isIOS() && shouldShowIOSPrompt()) {
        // Show after a short delay so page loads first
        setTimeout(() => {
            document.getElementById('iosInstallModal').style.display = 'flex';
            localStorage.setItem('iosInstallLastShown', Date.now().toString());
        }, 2000); // 2 second delay
    }
});

function closeIosModal() {
    document.getElementById('iosInstallModal').style.display = 'none';
}

function dontShowAgain() {
    localStorage.setItem('iosInstallDismissed', 'true');
    closeIosModal();
}

// Service Worker Registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js')
        .then(reg => console.log('Service Worker registered'))
        .catch(err => console.log('Service Worker registration failed'));
}

// PWA Install Prompt (for Android/Desktop)
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    // Only show for non-iOS devices
    if (!isIOS()) {
        document.getElementById('installPrompt').style.display = 'flex';
    }
});

function installApp() {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
            deferredPrompt = null;
            document.getElementById('installPrompt').style.display = 'none';
        });
    }
}

function dismissInstall() {
    document.getElementById('installPrompt').style.display = 'none';
}

// Navigation Functions
function showCategory(category) {
    document.getElementById('categoriesView').style.display = 'none';
    document.getElementById('recipesView').style.display = 'block';
    const backBtn = document.getElementById('backBtn');
    if (backBtn) backBtn.style.display = 'flex';
    
    const categoryTitle = category.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
    document.getElementById('categoryTitle').textContent = categoryTitle;
    
    const recipes = recipesData[category] || [];
    const recipesList = document.getElementById('recipesList');
    recipesList.innerHTML = '';
    
    recipes.forEach(recipe => {
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        recipeCard.onclick = () => {
            window.location.href = `${category}/${recipe.name.replace(/ /g, '_')}.html`;
        };
        
        const recipeName = recipe.name.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
        recipeCard.innerHTML = `<h3>${recipeName}</h3>`;
        recipesList.appendChild(recipeCard);
    });
}

function showCategories() {
    document.getElementById('categoriesView').style.display = 'grid';
    document.getElementById('recipesView').style.display = 'none';
    const backBtn = document.getElementById('backBtn');
    if (backBtn) backBtn.style.display = 'none';
    document.getElementById('searchInput').value = '';
}

// Search Function
function searchRecipes() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const backBtn = document.getElementById('backBtn');
    
    if (searchTerm.length === 0) {
        document.getElementById('categoriesView').style.display = 'grid';
        document.getElementById('recipesView').style.display = 'none';
        if (backBtn) backBtn.style.display = 'none';
        return;
    }
    
    document.getElementById('categoriesView').style.display = 'none';
    document.getElementById('recipesView').style.display = 'block';
    if (backBtn) backBtn.style.display = 'flex';
    document.getElementById('categoryTitle').textContent = 'Search Results';
    
    const recipesList = document.getElementById('recipesList');
    recipesList.innerHTML = '';
    
    let resultsFound = false;
    
    Object.keys(recipesData).forEach(category => {
        recipesData[category].forEach(recipe => {
            const recipeName = recipe.name.toLowerCase();
            if (recipeName.includes(searchTerm)) {
                resultsFound = true;
                const recipeCard = document.createElement('div');
                recipeCard.className = 'recipe-card';
                recipeCard.onclick = () => {
                    window.location.href = `${category}/${recipe.name.replace(/ /g, '_')}.html`;
                };
                
                const displayName = recipe.name.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
                const categoryName = category.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
                recipeCard.innerHTML = `
                    <h3>${displayName}</h3>
                    <p style="color: var(--text-secondary); font-size: 0.9rem;">${categoryName}</p>
                `;
                recipesList.appendChild(recipeCard);
            }
        });
    });
    
    if (!resultsFound) {
        recipesList.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No recipes found</p>';
    }
}

// Share recipe function – uses main.recipe-content
async function shareRecipe() {
  const titleEl = document.querySelector("main.recipe-content h1");
  const recipeTitle = titleEl ? titleEl.textContent.trim() : document.title;

  // Get all visible text from recipe content area
  const mainEl = document.querySelector("main.recipe-content");
  const recipeText = mainEl ? mainEl.innerText.trim() : "";

  const shareText =
    recipeTitle + '     ' + recipeText + '     Recipe link: ' + window.location.href;

  if (navigator.share) {
    try {
      await navigator.share({
        title: recipeTitle,
        text: shareText,
        url: window.location.href,
      });
    } catch (err) {
      console.log("Share canceled or failed", err);
    }
  } else if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(shareText);
      alert("Recipe copied to clipboard!");
    } catch (err) {
      alert('Sharing not supported on this browser.');
    }
  } else {
    alert('Sharing not supported on this browser.');
  }
}'''

        with open(self.deploy_dir / 'app.js', 'w', encoding='utf-8') as f:
            f.write(js)

    def generate_service_worker(self):
        """Generate Service Worker for offline support"""
        sw = '''const CACHE_NAME = 'vegetarian-cookbook-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/styles.css',
    '/app.js',
    '/manifest.json',
    '/icon-192.png',
    '/icon-512.png'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => response || fetch(event.request))
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});'''

        with open(self.deploy_dir / 'sw.js', 'w', encoding='utf-8') as f:
            f.write(sw)

    def generate_manifest(self):
        """Generate PWA manifest"""
        manifest = {
            "name": "Vegetarian Cookbook",
            "short_name": "VegCookbook",
            "description": "A collection of delicious vegetarian recipes",
            "start_url": "./",
            "scope": "./",
            "display": "standalone",
            "background_color": "#FAF8F3",
            "theme_color": "#2D5F3F",
            "orientation": "portrait",
            "icons": [
                {
                    "src": "icon-192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                    "purpose": "any maskable"
                },
                {
                    "src": "icon-512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                    "purpose": "any maskable"
                }
            ]
        }

        with open(self.deploy_dir / 'manifest.json', 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

    def generate_icons(self):
        """Generate simple icon files"""
        # Create a simple SVG icon and save as PNG placeholder
        svg_icon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
    <rect width="512" height="512" fill="#2D5F3F"/>
    <text x="256" y="300" font-size="256" text-anchor="middle" fill="white">🌱</text>
</svg>'''

        with open(self.deploy_dir / 'icon.svg', 'w', encoding='utf-8') as f:
            f.write(svg_icon)

        # Create placeholder PNG files (user should replace with actual icons)
        icon_placeholder = f'''<!-- Icon Placeholder -->
<!-- Please replace icon-192.png and icon-512.png with actual PNG images -->
<!-- You can use the icon.svg as a reference -->
<!-- Or create icons using: https://favicon.io/ or similar tools -->
'''

        with open(self.deploy_dir / 'ICONS_README.txt', 'w', encoding='utf-8') as f:
            f.write(icon_placeholder)

        # Create minimal PNG placeholders (1x1 pixel)
        # Note: User should replace these with actual icons
        print("  Note: Created icon placeholders. Please add actual icon-192.png and icon-512.png images.")

    def generate(self):
        """Main generation process"""
        print("\n🌱 Vegetarian Cookbook PWA Generator\n")

        # Step 1: Clean deploy directory
        print("1. Cleaning deploy directory...")
        self.clean_deploy_dir()

        # Step 2: Scan recipes
        print("\n2. Scanning recipes...")
        self.scan_recipes()

        if not self.recipes:
            print("  ⚠️  No recipe folders found in 'build' directory!")
            return

        # Step 3: Generate recipe pages
        print("\n3. Generating recipe pages...")
        for category, recipes in self.recipes.items():
            for recipe in recipes:
                self.generate_recipe_page(category, recipe)
        print(f"  ✓ Generated {sum(len(r) for r in self.recipes.values())} recipe pages")

        # Step 4: Generate main index
        print("\n4. Generating index page...")
        self.generate_index_page()

        # Step 5: Generate assets
        print("\n5. Generating assets...")
        self.generate_styles()
        self.generate_javascript()
        self.generate_service_worker()
        self.generate_manifest()
        self.generate_icons()

        print("\n✅ Generation complete!")
        print(f"\n📁 Your PWA is ready in the '{self.deploy_dir}' folder")
        print("\nTo test locally:")
        print(f"  cd {self.deploy_dir}")
        print("  python -m http.server 8000")
        print("  Then open: http://localhost:8000\n")


if __name__ == '__main__':
    generator = CookbookGenerator()
    generator.generate()
