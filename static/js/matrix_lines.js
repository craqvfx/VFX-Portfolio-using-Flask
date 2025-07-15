function initMatrixAnimation(canvasId = 'matrix-explosion') {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const binary = '01';
    const fontSize = 18;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(0);

    // Animation timing control
    const startTime = Date.now();
    const transitionDuration = 3000; // 3 seconds
    const minDelay = 1;
    const maxDelay = 50;

    function getCurrentDelay() {
        const elapsed = Date.now() - startTime;
        if (elapsed >= transitionDuration) {
            return maxDelay; // Floor at 50ms after transition
        }
        // Linear transition from minDelay to maxDelay
        return minDelay + (maxDelay - minDelay) * (elapsed / transitionDuration);
    }

    function animate() {
        ctx.fillStyle = 'rgba(13, 17, 23, 0.04)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#58a6ffff';
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
            const text = binary.charAt(Math.floor(Math.random() * binary.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }

        const currentDelay = getCurrentDelay();
        setTimeout(() => requestAnimationFrame(animate), currentDelay);
    }

    setTimeout(() => {
        canvas.style.opacity = '0.5';
        animate();
    }, 300);
}

document.addEventListener('DOMContentLoaded', () => initMatrixAnimation());