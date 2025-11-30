print("Starting Flask App...")
from flask import Flask, request, jsonify
import os
os.environ["SPACY_WARNING_IGNORE"] = "W108"
os.environ["SPACY_DISABLE_BLIS"] = "true"
import spacy
from transformers import pipeline

app = Flask(__name__)

import subprocess

try:
    import en_core_web_sm
except:
    subprocess.run(["python3", "-m", "spacy", "download", "en_core_web_sm"])

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "tagger"])
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/process_message", methods=["POST"])
def process_message():
    data = request.get_json()
    conversation = data["conversation"]

    doc = nlp(conversation)
    persons = []
    dates = []
    verbs = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.append(ent.text)
        if ent.label_ == "DATE":
            dates.append(ent.text)

    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_)

    summary = summarizer(conversation, max_length=80, min_length=20, do_sample=False)

    response = {
        "summary": summary[0]["summary_text"],
        "people": list(set(persons)),
        "dates": list(set(dates)),
        "actions": list(set(verbs))
    }

    return jsonify(response)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
