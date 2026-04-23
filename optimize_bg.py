import re

style_path = r'c:\Users\M.U.SAJAN KUMARAN\OneDrive\Desktop\PROGRAMS\WEB APPLICATIONS\my profile2\style.css'
with open(style_path, 'r', encoding='utf-8') as f:
    style_content = f.read()

# Remove .cyber-bg-grid
style_content = re.sub(r'\.cyber-bg-grid\s*{[^}]*}', '', style_content)

new_glow_css = """
.cursor-glow {
    position: fixed;
    top: 0; left: 0;
    width: 600px;
    height: 600px;
    pointer-events: none;
    z-index: 10;
    opacity: 0;
    transition: opacity 0.5s ease;
    
    /* Hardware accelerated transform */
    transform: translate3d(var(--mouse-x, -500px), var(--mouse-y, -500px), 0) translate(-50%, -50%);
    
    /* Integrated grid pattern that stays fixed to the viewport while the div moves */
    background-image:
        linear-gradient(rgba(0, 243, 255, 0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 243, 255, 0.08) 1px, transparent 1px);
    background-size: 50px 50px;
    background-attachment: fixed;
    
    /* Static mask fading it out softly */
    -webkit-mask-image: radial-gradient(circle at center, black 0%, transparent 60%);
    mask-image: radial-gradient(circle at center, black 0%, transparent 60%);
}

.cursor-glow::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, rgba(0, 243, 255, 0.12) 0%, transparent 60%);
    border-radius: 50%;
}
"""

style_content = re.sub(r'\.cursor-glow\s*{[^}]*}', new_glow_css, style_content)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(style_content)


html_path = r'c:\Users\M.U.SAJAN KUMARAN\OneDrive\Desktop\PROGRAMS\WEB APPLICATIONS\my profile2\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# remove cyber-bg-grid
html_content = re.sub(r'<div id="cyber-bg-grid" class="cyber-bg-grid"></div>\n\s*', '', html_content)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Optimized CSS and HTML saved.")
