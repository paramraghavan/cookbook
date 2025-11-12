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
        for folder in self.build_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith('.'):
                folder_name = folder.name
                self.recipes[folder_name] = []
                
                for recipe_file in folder.iterdir():
                    if recipe_file.suffix in ['.md', '.html']:
                        recipe_name = recipe_file.stem
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
    <meta name="theme-color" content="#4CAF50">
    <title>{recipe['name']} - Vegetarian Cookbook</title>
    <link rel="manifest" href="../manifest.json">
    <link rel="stylesheet" href="../styles.css">
    <link rel="icon" type="image/png" href="../icon-192.png">
</head>
<body>
    <header>
        <button class="back-btn" onclick="history.back()">← Back</button>
        <h1>{recipe['name']}</h1>
    </header>
    
    <main class="recipe-content">
        {content}
    </main>
    
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
        categories_html = ""
        
        for category, recipes in sorted(self.recipes.items()):
            recipe_count = len(recipes)
            category_display = category.replace('_', ' ').title()
            
            categories_html += f'''
            <div class="category-card" onclick="showCategory('{category}')">
                <div class="category-icon">🥗</div>
                <h2>{category_display}</h2>
                <p>{recipe_count} recipe{'s' if recipe_count != 1 else ''}</p>
            </div>
            '''
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#4CAF50">
    <meta name="description" content="A collection of delicious vegetarian recipes">
    <title>Vegetarian Cookbook</title>
    <link rel="manifest" href="manifest.json">
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/png" href="icon-192.png">
    <link rel="apple-touch-icon" href="icon-192.png">
</head>
<body>
    <header>
        <h1>🌱 Vegetarian Cookbook</h1>
        <p class="subtitle">Delicious plant-based recipes</p>
    </header>
    
    <main>
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Search recipes..." onkeyup="searchRecipes()">
        </div>
        
        <div id="categoriesView" class="categories-grid">
            {categories_html}
        </div>
        
        <div id="recipesView" class="recipes-view" style="display: none;">
            <button class="back-btn" onclick="showCategories()">← Back to Categories</button>
            <h2 id="categoryTitle"></h2>
            <div id="recipesList" class="recipes-grid"></div>
        </div>
    </main>
    
    <div id="installPrompt" class="install-prompt" style="display: none;">
        <p>📱 Install this app for quick access!</p>
        <button onclick="installApp()">Install</button>
        <button onclick="dismissInstall()">Later</button>
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
    --primary-color: #4CAF50;
    --primary-dark: #388E3C;
    --secondary-color: #FF9800;
    --background: #f5f5f5;
    --card-bg: #ffffff;
    --text-primary: #212121;
    --text-secondary: #757575;
    --shadow: 0 2px 8px rgba(0,0,0,0.1);
    --shadow-hover: 0 4px 16px rgba(0,0,0,0.15);
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: var(--background);
    color: var(--text-primary);
    line-height: 1.6;
    padding-bottom: 2rem;
}

header {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
    color: white;
    padding: 2rem 1rem;
    text-align: center;
    box-shadow: var(--shadow);
    position: sticky;
    top: 0;
    z-index: 100;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.subtitle {
    opacity: 0.9;
    font-size: 1rem;
}

main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.search-box {
    margin-bottom: 2rem;
}

.search-box input {
    width: 100%;
    padding: 1rem;
    border: 2px solid #e0e0e0;
    border-radius: 50px;
    font-size: 1rem;
    transition: all 0.3s;
}

.search-box input:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
}

.category-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: var(--shadow);
}

.category-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-hover);
}

.category-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.category-card h2 {
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.category-card p {
    color: var(--text-secondary);
}

.recipes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
}

.recipe-card {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 1.5rem;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: var(--shadow);
    border-left: 4px solid var(--primary-color);
}

.recipe-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-hover);
    border-left-color: var(--secondary-color);
}

.recipe-card h3 {
    color: var(--text-primary);
    font-size: 1.25rem;
}

.back-btn {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    font-size: 1rem;
    cursor: pointer;
    margin-bottom: 1.5rem;
    transition: all 0.3s;
    font-weight: 500;
}

.back-btn:hover {
    background: var(--primary-dark);
    transform: translateX(-4px);
}

.recipe-content {
    background: var(--card-bg);
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: var(--shadow);
}

.recipe-content h1, .recipe-content h2, .recipe-content h3 {
    color: var(--primary-color);
    margin-top: 1.5rem;
    margin-bottom: 1rem;
}

.recipe-content ul, .recipe-content ol {
    margin-left: 1.5rem;
    margin-bottom: 1rem;
}

.recipe-content li {
    margin-bottom: 0.5rem;
}

.recipe-content p {
    margin-bottom: 1rem;
}

.recipe-content img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 1rem 0;
}

.install-prompt {
    position: fixed;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    background: var(--card-bg);
    padding: 1rem 2rem;
    border-radius: 50px;
    box-shadow: var(--shadow-hover);
    display: flex;
    align-items: center;
    gap: 1rem;
    z-index: 1000;
}

.install-prompt button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    cursor: pointer;
    font-weight: 500;
}

.install-prompt button:last-child {
    background: transparent;
    color: var(--text-secondary);
}

@media (max-width: 768px) {
    header h1 {
        font-size: 1.5rem;
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
    
    .install-prompt {
        flex-direction: column;
        left: 1rem;
        right: 1rem;
        transform: none;
    }
}'''
        
        with open(self.deploy_dir / 'styles.css', 'w', encoding='utf-8') as f:
            f.write(css)
    
    def generate_javascript(self):
        """Generate JavaScript for interactivity"""
        js = '''// Service Worker Registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js')
        .then(reg => console.log('Service Worker registered'))
        .catch(err => console.log('Service Worker registration failed'));
}

// PWA Install Prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    document.getElementById('installPrompt').style.display = 'flex';
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
    document.getElementById('searchInput').value = '';
}

// Search Function
function searchRecipes() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    
    if (searchTerm.length === 0) {
        document.getElementById('categoriesView').style.display = 'grid';
        document.getElementById('recipesView').style.display = 'none';
        return;
    }
    
    document.getElementById('categoriesView').style.display = 'none';
    document.getElementById('recipesView').style.display = 'block';
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
            "start_url": "/",
            "display": "standalone",
            "background_color": "#ffffff",
            "theme_color": "#4CAF50",
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
    <rect width="512" height="512" fill="#4CAF50"/>
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
