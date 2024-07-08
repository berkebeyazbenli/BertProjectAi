from transformers import TFDistilBertForQuestionAnswering, DistilBertTokenizer
import tensorflow as tf

class QuestionAnsweringModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        try:
            self.model = TFDistilBertForQuestionAnswering.from_pretrained(self.model_name)
            self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
            print("Model and tokenizer loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")

    def predict_answer(self, question, context):
        if self.model is None or self.tokenizer is None:
            return "Error: Model or tokenizer not loaded"

        inputs = self.tokenizer(question, context, return_tensors='tf')
        outputs = self.model(inputs)
        answer_start_index = tf.argmax(outputs.start_logits, axis=1).numpy()[0]
        answer_end_index = tf.argmax(outputs.end_logits, axis=1).numpy()[0]
        answer = self.tokenizer.decode(inputs['input_ids'][0][answer_start_index:answer_end_index+1])
        return answer
