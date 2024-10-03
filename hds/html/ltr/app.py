from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',       # Update with your MySQL username
    'password': '',       # Update with your MySQL password
    'database': 'hearing'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/question', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM question')
    question = cursor.fetchall()
    cursor.close()
    conn.close()

    formatted_questions = [
        {
            'text': q['question'],
            'options': [q['option1'], q['option2'], q['option3'], q['option4']],
            'answer': q['coption']
        }
        for q in question
    ]

    return jsonify({'question': formatted_questions})

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM question')
    question = cursor.fetchall()
    cursor.close()
    conn.close()

    score = 0

    for key, value in data.items():
        question_index = int(key[1:])
        selected_option = int(value)
        correct_answer = question[question_index]['answer']

        if selected_option == correct_answer:
            score += 1

    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
