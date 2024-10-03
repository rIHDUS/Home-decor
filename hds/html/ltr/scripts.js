document.addEventListener('DOMContentLoaded', function () {
    fetch('/question')
        .then(response => response.json())
        .then(data => {
            const form = document.getElementById('questionnaire-form');
            data.question.forEach((question, index) => {
                const questionHTML = `
                    <div class="question">
                        <p>${index + 1}. ${question.text}</p>
                        ${question.options.map((option, i) => `
                            <label>
                                <input type="radio" name="q${index}" value="${i}">
                                ${option}
                            </label>
                        `).join('')}
                    </div>
                `;
                form.insertAdjacentHTML('beforeend', questionHTML);
            });
        });

    document.getElementById('submit-btn').addEventListener('click', function () {
        const formData = new FormData(document.getElementById('questionnaire-form'));
        const answers = {};
        formData.forEach((value, key) => {
            answers[key] = value;
        });

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(answers)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `Your score: ${data.score}`;
        });
    });
});
