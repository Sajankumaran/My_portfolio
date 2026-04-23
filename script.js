// ----- Typewriter Effect -----
const typewriterElement = document.getElementById('typewriter');
const phrases = [
    "Computer Science Student",
    "Web Developer",
    "Cybersecurity Enthusiast",
    "System Administrator",
    "Creative Problem Solver"
];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeWriter() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
    }

    let typeSpeed = isDeleting ? 50 : 100;

    if (!isDeleting && charIndex === currentPhrase.length) {
        typeSpeed = 2000; // Pause at end
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; // Pause before new phrase
    }

    setTimeout(typeWriter, typeSpeed);
}

// Initialize Typewriter
setTimeout(typeWriter, 1000); // Start after 1 second

// ----- System Uptime -----
const uptimeElement = document.getElementById('uptime');
const startTime = new Date();

function updateUptime() {
    const now = new Date();
    const diff = Math.floor((now - startTime) / 1000);

    const d = Math.floor(diff / (3600 * 24));
    const h = Math.floor(diff % (3600 * 24) / 3600);
    const m = Math.floor(diff % 3600 / 60);
    const s = Math.floor(diff % 60);

    uptimeElement.textContent = `${d}d ${h}h ${m}m ${s}s`;
}

setInterval(updateUptime, 1000);

// ----- Steganography Interactive Demo -----
const stegDemo = document.getElementById('steg-demo');
if (stegDemo) {
    stegDemo.addEventListener('click', () => {
        const cipher = stegDemo.querySelector('.demo-cipher');
        const clear = stegDemo.querySelector('.demo-clear');

        cipher.textContent = 'DECRYPTING...';
        cipher.style.color = '#ff00ea';

        let glitchInterval = setInterval(() => {
            let randomStr = '';
            const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()';
            for (let i = 0; i < 15; i++) randomStr += chars.charAt(Math.floor(Math.random() * chars.length));
            cipher.textContent = randomStr;
        }, 50);

        setTimeout(() => {
            clearInterval(glitchInterval);
            cipher.classList.add('hidden');
            clear.classList.remove('hidden');
        }, 1500);
    });
}

// ----- Cybersecurity Threat Streams -----
// Nmap Scanner Simulation
const nmapStream = document.getElementById('nmap-stream');
const ipPrefixes = ['192.168.1.', '10.0.0.', '172.16.254.', '198.51.100.'];
const ports = [{ p: 22, s: 'ssh' }, { p: 80, s: 'http' }, { p: 443, s: 'https' }, { p: 3306, s: 'mysql' }];
let nmapLines = [];

function addNmapLine() {
    if (nmapLines.length > 15) {
        nmapLines.shift();
    }
    const ip = ipPrefixes[Math.floor(Math.random() * ipPrefixes.length)] + Math.floor(Math.random() * 255);
    const portObj = ports[Math.floor(Math.random() * ports.length)];
    const state = Math.random() > 0.3 ? 'open' : 'filtered';

    nmapLines.push(`Discovered open port ${portObj.p}/${portObj.s} on ${ip}`);

    let html = '';
    nmapLines.forEach(line => {
        html += `<div>${line}</div>`;
    });
    nmapStream.innerHTML = html;
}
setInterval(addNmapLine, 1200);

// Wireshark Simulation
const packetStream = document.getElementById('packet-stream');
let packetCounter = 1;
let packets = [];

function addPacket() {
    if (packets.length > 20) {
        packets.shift();
    }

    const protocols = ['TCP', 'UDP', 'ICMP', 'TLSv1.2', 'HTTP'];
    const proto = protocols[Math.floor(Math.random() * protocols.length)];
    const srcip = `192.168.1.${Math.floor(10 + Math.random() * 90)}`;
    const dstip = `10.0.0.${Math.floor(10 + Math.random() * 90)}`;
    const time = (packetCounter * 0.045).toFixed(4);

    let info = '';
    let rowClass = '';
    if (proto === 'TCP') { info = `443 > 5214 [ACK] Seq=1 Ack=1 Win=65535 Len=0`; rowClass = 'tcp'; }
    else if (proto === 'UDP') { info = `Source port: 53 Destination port: 5231`; rowClass = 'udp'; }
    else if (proto === 'ICMP') { info = `Echo (ping) request id=0x1a2b seq=1/256`; rowClass = 'icmp'; }
    else { info = 'Application Data'; }

    const row = `<div class="packet-row ${rowClass}">
        <span>${packetCounter}</span>
        <span>${time}</span>
        <span>${srcip}</span>
        <span>${dstip}</span>
        <span>${proto}</span>
        <span>${info}</span>
    </div>`;

    packets.push(row);
    packetStream.innerHTML = packets.join('');
    packetCounter++;
}
setInterval(addPacket, 400);

// ----- Terminal Contact Form -----
const cyberForm = document.getElementById('cyber-form');
const formOutput = document.getElementById('form-output');

if (cyberForm) {
    cyberForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const submitBtn = document.getElementById('submit-ping');

        submitBtn.textContent = 'EXECUTING...';
        submitBtn.disabled = true;

        let processingSteps = [
            `> Initiating secure handshake with mailserver...`,
            `> Encrypting payload via RSA-2048...`,
            `> Transmission established...`,
            `> Payload delivered successfully.`,
            `> Server response: 200 OK. Connection terminated.`
        ];

        let step = 0;
        formOutput.innerHTML = '';

        let processInterval = setInterval(() => {
            if (step < processingSteps.length) {
                formOutput.innerHTML += `<div>${processingSteps[step]}</div>`;
                step++;
            } else {
                clearInterval(processInterval);
                formOutput.innerHTML += `<div style="color:#0f0; margin-top:10px;">SUCCESS: Message from ${name} recorded. Thank you.</div>`;
                submitBtn.textContent = './execute_ping.sh';
                submitBtn.disabled = false;
                cyberForm.reset();
            }
        }, 600);
    });
}

// Skills representation has been updated to a pure CSS Matrix layout.

// ----- UI Transitions & Animations -----

// Navbar Scroll Effect
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });
}

// Intersection Observer for Reveal Elements & Skill Bars
const revealElements = document.querySelectorAll('.reveal');

const revealOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
};

const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Add the visible class for standard reveal
            entry.target.classList.add('reveal-active');
            
            // If it's a hex wrapper, trigger the hud ring animation
            if (entry.target.classList.contains('hex-wrapper')) {
                const hexNode = entry.target.querySelector('.hex-node');
                const hudRing = entry.target.querySelector('.hud-ring');
                if (hexNode && hudRing) {
                    const percent = parseInt(hexNode.getAttribute('data-percent'), 10);
                    // Circle circumference for r=44 is ~276.46
                    const offset = 276.46 - (276.46 * percent / 100);
                    setTimeout(() => {
                        hudRing.style.strokeDashoffset = offset;
                    }, 200);
                }
            }
            
            // Stop observing once revealed to retain state
            observer.unobserve(entry.target);
        }
    });
}, revealOptions);

revealElements.forEach(el => {
    revealObserver.observe(el);
});

// Interactive Background Environment
const cursorGlow = document.getElementById('cursor-glow');
let interactionTimeout;
let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let isMoving = false;

if (cursorGlow) {
    // Decouple mouse tracking from heavy render computations
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        isMoving = true;
        cursorGlow.style.opacity = '1';

        // Auto-hide elements to maintain dark minimum profile when idle
        clearTimeout(interactionTimeout);
        interactionTimeout = setTimeout(() => {
            isMoving = false;
            cursorGlow.style.opacity = '0';
        }, 800); // Fades completely to black after 800ms
    });

    // Dedicated smooth render loop using hardware-accelerated Transform
    function renderGlow() {
        if (isMoving) {
            cursorGlow.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
        }
        requestAnimationFrame(renderGlow);
    }
    requestAnimationFrame(renderGlow);

    // Ripple click interaction
    window.addEventListener('click', (e) => {
        const ripple = document.createElement('div');
        ripple.classList.add('click-ripple');
        // Set coordinates based on click event
        ripple.style.left = e.clientX + 'px';
        ripple.style.top = e.clientY + 'px';
        
        // Append to DOM, rippleAnim keyframe will handle the rest
        document.body.appendChild(ripple);

        // Perform clean up automatically after 800ms
        setTimeout(() => {
            ripple.remove();
        }, 800);
    });
}
