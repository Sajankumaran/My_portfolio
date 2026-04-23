import re

html_path = r'c:\Users\M.U.SAJAN KUMARAN\OneDrive\Desktop\PROGRAMS\WEB APPLICATIONS\my profile2\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

skills = [
    ("JAVA", "devicon-java-plain colored", 80),
    ("PYTHON", "devicon-python-plain colored", 80),
    ("C / C++", "devicon-c-plain colored", 60),
    ("HTML5", "devicon-html5-plain colored", 100),
    ("CSS3", "devicon-css3-plain colored", 80),
    ("LINUX", "devicon-linux-plain", 80),
    ("SQL", "devicon-sqldeveloper-plain colored", 80),
    ("MYSQL", "devicon-mysql-plain colored", 80),
    ("MONGODB", "devicon-mongodb-plain colored", 60),
    ("WIRESHARK", "fas fa-network-wired cyber-icon", 80),
    ("NMAP", "fas fa-shield-halved cyber-icon", 80)
]

hex_html = '<div class="cyber-hex-grid">\n'
for name, icon, percent in skills:
    # Adding inline styles for SVG animation logic to utilize later or calculate via CSS
    hex_html += f'''            <div class="hex-wrapper reveal">
                <div class="hex-node" data-percent="{percent}">
                    <div class="hex-inner">
                        <svg class="hud-svg" viewBox="0 0 100 100">
                            <circle class="hud-bg" cx="50" cy="50" r="44"></circle>
                            <circle class="hud-ring" cx="50" cy="50" r="44"></circle>
                        </svg>
                        <i class="{icon}"></i>
                    </div>
                    <span class="hex-title">{name}</span>
                    <span class="hex-percent">{percent}%</span>
                </div>
            </div>\n'''
hex_html += '        </div>'

# Regex to safely replace the old container
pattern = r'<div class="skill-matrix-container">[\s\S]*?</div>\s*</section>'
replacement = f'{hex_html}\n    </section>'

new_content = re.sub(pattern, replacement, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hex Grid HTML correctly swapped.")
