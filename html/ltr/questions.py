#!C:\Python312\python.exe
import user_header
print('''
      <script>
       var username = localStorage.getItem("User_Name");
       if (username === null || username === "") {
           alert("Login first");
           window.location.href = "home.py";
       }
      </script>''')

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Page</title>
    <!-- Add your CSS files here -->
    <link rel="stylesheet" href="path/to/your/styles.css">
    <style>
        .question-container {
            display: none;
        }
        .question-container.active {
            display: block;
        }
        .btn-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<section class="page-title bg-2">
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="block text-center">
                    <span class="text-white">Questionaries</span>
                    <h1 class="text-capitalize mb-5 text-lg">Quiz</h1>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="quiz section">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 offset-lg-2">
                <div class="quiz-wrap mt-5">
                    <h2 class="mb-4 title-color">Assesment Test</h2>
                    <p class="mb-4">Answer the following questions to test your understanding of the topic.</p>
                    <form id="quiz-form" class="quiz-form" method="post" action="quizbackend.py">
                        <div id="question-container">
                            <!-- Question 1 -->
                            <div class="question-container active">
                                <h3 class="form-label">1. What is the capital of France?</h3>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q1" id="q1a" value="Paris" required>
                                    <label class="form-check-label" for="q1a">Paris</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q1" id="q1b" value="London">
                                    <label class="form-check-label" for="q1b">London</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q1" id="q1c" value="Berlin">
                                    <label class="form-check-label" for="q1c">Berlin</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q1" id="q1d" value="Madrid">
                                    <label class="form-check-label" for="q1d">Madrid</label>
                                </div>
                            </div>

                            <!-- Question 2 -->
                            <div class="question-container">
                                <h3 class="form-label">2. Which planet is known as the Red Planet?</h3>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q2" id="q2a" value="Earth" required>
                                    <label class="form-check-label" for="q2a">Earth</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q2" id="q2b" value="Mars">
                                    <label class="form-check-label" for="q2b">Mars</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q2" id="q2c" value="Jupiter">
                                    <label class="form-check-label" for="q2c">Jupiter</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q2" id="q2d" value="Saturn">
                                    <label class="form-check-label" for="q2d">Saturn</label>
                                </div>
                            </div>

                            <!-- Question 3 -->
                            <div class="question-container">
                                <h3 class="form-label">3. What is the chemical symbol for gold?</h3>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q3" id="q3a" value="Au" required>
                                    <label class="form-check-label" for="q3a">Au</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q3" id="q3b" value="Ag">
                                    <label class="form-check-label" for="q3b">Ag</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q3" id="q3c" value="Pb">
                                    <label class="form-check-label" for="q3c">Pb</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="q3" id="q3d" value="Fe">
                                    <label class="form-check-label" for="q3d">Fe</label>
                                </div>
                            </div>
                        </div>
                        <div class="btn-container">
                            <button type="button" id="prev-btn" class="btn btn-secondary">Previous</button>
                            <button type="button" id="next-btn" class="btn btn-primary">Next</button>
                            <button type="submit" id="submit-btn" class="btn btn-main btn-round-full" style="display: none;">Submit Quiz</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const questions = document.querySelectorAll('.question-container');
        let currentQuestion = 0;

        function showQuestion(index) {
            questions.forEach((question, i) => {
                question.classList.toggle('active', i === index);
            });
            document.getElementById('prev-btn').style.display = index === 0 ? 'none' : 'inline-block';
            document.getElementById('next-btn').style.display = index === questions.length - 1 ? 'none' : 'inline-block';
            document.getElementById('submit-btn').style.display = index === questions.length - 1 ? 'inline-block' : 'none';
        }

        document.getElementById('prev-btn').addEventListener('click', () => {
            if (currentQuestion > 0) {
                currentQuestion--;
                showQuestion(currentQuestion);
            }
        });

        document.getElementById('next-btn').addEventListener('click', () => {
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                showQuestion(currentQuestion);
            }
        });

        showQuestion(currentQuestion);
    });
</script>

</body>
</html>
''')
import user_footer
