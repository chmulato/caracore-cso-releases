// Contador regressivo para 08/11/2026
const targetDate = new Date('2026-11-08T00:00:00').getTime();
const countdownElement = document.getElementById('countdown');

function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance > 0) {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    } else {
        countdownElement.innerHTML = 'Lançamento Disponível!';
    }
}

setInterval(updateCountdown, 1000);

// Formulário de feedback
document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const title = encodeURIComponent(document.getElementById('title').value);
    const body = encodeURIComponent(document.getElementById('body').value);
    const url = `https://github.com/chmulato/caracore-cso-releases/issues/new?title=${title}&body=${body}&labels=feedback`;
    window.open(url, '_blank');
});