from flask import Flask, render_template, request
import os
from utils.file_parser import extract_text
from utils.topic_extractor import extract_topics
from utils.question_generator import generate_hots_questions

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        text = extract_text(path)
        topics = extract_topics(text)

        for topic in topics:
            results[topic] = generate_hots_questions(topic)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
