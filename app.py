from flask import Flask, request, jsonify
from transformers import pipeline
import re

app = Flask(__name__)

print("Starting Flask App...")
print("Loading model: facebook/bart-large-cnn...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Model loaded successfully!")

def extract_action_items(text):
    """Extract action items from conversation text"""
    action_patterns = [
        r'(?:will|should|need to|must|have to|going to)\s+(.+?)(?:\.|$)',
        r'(?:todo|task|action item):\s*(.+?)(?:\.|$)',
        r'(?:decide[d]?|agree[d]?|plan)\s+to\s+(.+?)(?:\.|$)'
    ]
    
    action_items = []
    for pattern in action_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            item = match.group(1).strip()
            if len(item) > 10 and item not in action_items:
                action_items.append(item)
    
    return action_items[:5]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "running",
        "message": "Cliq Summary Bot API is active",
        "endpoints": {
            "/process_message": "POST - Process conversation and return summary + action items"
        }
    })

@app.route('/process_message', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        
        if not data or 'conversation' not in data:
            return jsonify({"error": "No conversation text provided"}), 400
        
        conversation = data['conversation']
        
        if len(conversation) < 50:
            return jsonify({"error": "Conversation too short to summarize"}), 400
        
        summary_result = summarizer(
            conversation,
            max_length=150,
            min_length=30,
            do_sample=False
        )
        summary = summary_result[0]['summary_text']
        
        action_items = extract_action_items(conversation)
        
        return jsonify({
            "summary": summary,
            "action_items": action_items
        })
    
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
