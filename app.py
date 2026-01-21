print("Starting Flask App...")
from flask import Flask, request, jsonify
import os
from transformers import pipeline

app = Flask(__name__)

# Only use the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/process_message", methods=["POST"])
def process_message():
    data = request.get_json()
    conversation = data["conversation"]
    
    # Generate summary
    summary = summarizer(conversation, max_length=80, min_length=20, do_sample=False)
    
    response = {
        "summary": summary[0]["summary_text"],
        "people": [],  # Can add basic regex extraction if needed
        "dates": [],
        "actions": []
    }
    return jsonify(response)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
