import os
import re

html_path = r'c:\Users\M.U.SAJAN KUMARAN\OneDrive\Desktop\PROGRAMS\WEB APPLICATIONS\my profile2\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_power_level(match):
    dots_block = match.group(1)
    active_count = dots_block.count('active')
    width = active_count * 20
    return f'<div class="neo-power-bar">\n                        <div class="bar-fill" data-width="{width}%"></div>\n                    </div>'

pattern = r'<div class="neo-power-level">([\s\S]*?)</div>'
content = re.sub(pattern, replace_power_level, content)

classes_to_reveal = [
    'section-title text-glow',
    'holographic-card',
    'project-card',
    'skill-card-neo',
    'flip-card',
    'cyber-dashboard',
    'terminal-contact'
]

for cls in classes_to_reveal:
    content = content.replace(f'class="{cls}"', f'class="{cls} reveal"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML update complete!")
