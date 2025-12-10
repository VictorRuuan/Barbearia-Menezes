// Pequenas interações visuais (hover etc já no CSS)
document.addEventListener('DOMContentLoaded', () => {
    // destacar linhas de serviço clicadas (apenas UX)
    document.querySelectorAll('.service').forEach(s => {
        s.addEventListener('click', () => {
            document.querySelectorAll('.service').forEach(x => x.classList.remove('selected'));
            s.classList.add('selected');
            // se houver input radio dentro, seleciona
            const radio = s.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

    document.querySelectorAll('.time-btn').forEach(t => {
        t.addEventListener('click', () => {
            document.querySelectorAll('.time-btn').forEach(x => x.classList.remove('selected'));
            t.classList.add('selected');
            const r = t.querySelector('input[type="radio"]');
            if (r) r.checked = true;
        });
    });
});
