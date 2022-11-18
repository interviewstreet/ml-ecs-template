from flask import Flask, request
import spacy
import json

## load model into spacy, so we would use boto to call s3 to pull the model files from their location

nlp = spacy.load('') #put model location here

app = Flask(__name__)
app.run(host="0.0.0.0", port='8080')

@app.route("/predict/", methods=['POST'])
def predict():
    error = None
    try:
        if request.method == 'POST':
            req = request.get_json()
            text = req['text']
            response = nlp.pipe()
            return json.loads(response)
    except Exception as e:
        return e