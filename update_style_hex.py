import re

style_path = r'c:\Users\M.U.SAJAN KUMARAN\OneDrive\Desktop\PROGRAMS\WEB APPLICATIONS\my profile2\style.css'

with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

hex_css = """/* Futuristic Cyber-Hex HUD */
.cyber-hex-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px 0;
}

.hex-wrapper {
    position: relative;
    width: 140px;
    height: 160px;
    filter: drop-shadow(0 0 8px rgba(0, 243, 255, 0.2));
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
}

.hex-wrapper:hover {
    filter: drop-shadow(0 0 15px rgba(255, 0, 234, 0.6));
    transform: translateY(-10px) scale(1.05);
}

.hex-node {
    width: 100%;
    height: 100%;
    background: var(--neon-cyan);
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.hex-wrapper:hover .hex-node {
    background: var(--neon-pink);
}

.hex-inner {
    position: absolute;
    top: 2px;
    left: 2px;
    right: 2px;
    bottom: 2px;
    background: rgba(10, 10, 25, 0.95);
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 2;
}

.hud-svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-90deg);
    width: 90px;
    height: 90px;
    z-index: 1;
}

.hud-bg {
    fill: none;
    stroke: rgba(255, 255, 255, 0.05);
    stroke-width: 4;
}

.hud-ring {
    fill: none;
    stroke: var(--neon-cyan);
    stroke-width: 4;
    stroke-dasharray: 276.46;
    stroke-dashoffset: 276.46;
    transition: stroke-dashoffset 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), stroke 0.4s ease;
    stroke-linecap: round;
}

.hex-wrapper:hover .hud-ring {
    stroke: var(--neon-pink);
}

.hex-inner i {
    font-size: 2.5rem;
    z-index: 3;
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.2));
    transition: all 0.4s ease;
    margin-bottom: 10px;
}

.hex-wrapper:hover .hex-inner i {
    filter: drop-shadow(0 0 10px var(--neon-pink));
    transform: scale(1.1);
}

.hex-title {
    position: absolute;
    bottom: 25px;
    font-family: var(--font-heading);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--text-main);
    opacity: 0.8;
    z-index: 3;
    transition: all 0.4s ease;
}

.hex-wrapper:hover .hex-title {
    color: var(--neon-pink);
    opacity: 1;
    bottom: 30px;
}

.hex-percent {
    position: absolute;
    bottom: 12px;
    font-family: var(--font-heading);
    font-size: 0.65rem;
    color: var(--neon-cyan);
    opacity: 0;
    z-index: 3;
    transition: all 0.4s ease;
}

.hex-wrapper:hover .hex-percent {
    opacity: 1;
    color: var(--neon-pink);
}
/* End Hex HUD */
"""

# The section we want to replace starts at /* Skills Orbit Environment */ and goes until /* Cybersecurity Zone */ minus any reveal css we appended recently if it's there. 
# Wait, the reveal CSS might have been before Cybersecurity Zone, let's just regex correctly.

# The string to look for starts with /* Skills Orbit Environment */
# We want to replace everything down to just before /* Cybersecurity Zone */ OR /* Scroll Reveal Classes */ 

pattern1 = r'/\* Skills Orbit Environment \*/[\s\S]*?/\* Scroll Reveal Classes \*/'
new_content, count = re.subn(pattern1, hex_css + '\n/* Scroll Reveal Classes */', content)

if count == 0:
    # try replacing down to /* Cybersecurity Zone */
    pattern2 = r'/\* Skills Orbit Environment \*/[\s\S]*?/\* Cybersecurity Zone \*/'
    new_content, count = re.subn(pattern2, hex_css + '\n/* Cybersecurity Zone */', content)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS updated successfully", count)
