document.addEventListener('DOMContentLoaded', () => {

    // Serviços (múltipla seleção)
    document.querySelectorAll('.service').forEach(s => {
        s.addEventListener('click', () => {
            const checkbox = s.querySelector('input[type="checkbox"]');
            if (!checkbox) return;

            checkbox.checked = !checkbox.checked;
            s.classList.toggle('selected', checkbox.checked);
        });
    });

    // Horários (apenas um)
    document.querySelectorAll('.time-btn').forEach(t => {
        t.addEventListener('click', () => {
            document.querySelectorAll('.time-btn').forEach(x => x.classList.remove('selected'));
            t.classList.add('selected');

            const radio = t.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

});
