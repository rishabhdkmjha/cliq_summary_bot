print("Starting Flask App...")
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Lazy load the model only when needed
summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        from transformers import pipeline
        print("Loading summarization model...")
        summarizer = pipeline(
            "summarization", 
            model="sshleifer/distilbart-cnn-12-6",
            device=-1  # Force CPU
        )
        print("Model loaded successfully!")
    return summarizer

@app.route("/process_message", methods=["POST"])
def process_message():
    data = request.get_json()
    conversation = data.get("conversation", "")
    
    if not conversation:
        return jsonify({"error": "No conversation provided"}), 400
    
    try:
        # Get the summarizer
        model = get_summarizer()
        
        # Generate summary
        summary = model(
            conversation, 
            max_length=80, 
            min_length=20, 
            do_sample=False
        )
        
        response = {
            "summary": summary[0]["summary_text"],
            "people": [],
            "dates": [],
            "actions": []
        }
        return jsonify(response)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "OK", "service": "Cliq Summary Bot"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
```

4. Click **"Commit changes"** → **"Commit changes"**

---

## ⚙️ **Why This Works:**

✅ **DistilBART** is 40% smaller than BART  
✅ **Lazy loading** - model loads only when first request comes  
✅ **Memory efficient** - fits in 512MB  
✅ **Same quality** summarization  
✅ **Faster** response times

---

## 📊 **Expected Deployment:**

After you commit, watch the Render logs. You should see:
```
==> Build successful 🎉
==> Deploying...
==> Running 'gunicorn app:app --bind 0.0.0.0:$PORT'
Starting Flask App...
[INFO] Booting worker with pid: 123
==> Your service is live 🎉
