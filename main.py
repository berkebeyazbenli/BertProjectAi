from flask import Flask, request, render_template
from models.model import QuestionAnsweringModel
from data.dataProcessing import read_pdf

app = Flask(__name__, template_folder='web')
model = QuestionAnsweringModel('distilbert-base-uncased-distilled-squad')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load-pdf')
def load_pdf():
    file_path = request.args.get('file_path')
    pdf_text = read_pdf(file_path)
    return pdf_text

@app.route('/ask')
def ask_question():
    try:
        question = request.args.get('question')
        context = request.args.get('context', '')
        
        if not question.strip():
            return "Error: Question is empty"

        answer = model.predict_answer(question, context)
        return answer

    except Exception as e:
        print(f"Error during question answering: {e}")
        return "Error during question answering"

if __name__ == '__main__':
    app.run(debug=True)
