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

    function animate() {
        ctx.fillStyle = 'rgba(13, 17, 23, 0.04)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#58a6ffa8';
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
            const text = binary.charAt(Math.floor(Math.random() * binary.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }

        //requestAnimationFrame(animate);
        setTimeout(() => requestAnimationFrame(animate), 50);  // 50ms delay ~20fps

    }

    setTimeout(() => {
        canvas.style.opacity = '0.3';
        animate();
    }, 300);
}

document.addEventListener('DOMContentLoaded', () => initMatrixAnimation());
