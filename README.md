

# 💬 Cliq Summary Bot

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Gradio](https://img.shields.io/badge/gradio-4.16.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)

An AI-powered conversation summarization bot that automatically extracts summaries and action items from text conversations. Built with Gradio, Hugging Face Transformers, and DistilBART model.

## ✨ Features

- 📝 **Smart Summarization** - Generates concise summaries from long conversations
- ✅ **Action Item Extraction** - Automatically identifies tasks, decisions, and to-dos
- 🌐 **REST API** - Easy integration with any platform via HTTP API
- 🎨 **Web Interface** - Beautiful Gradio UI for interactive testing
- 🚀 **Fast Processing** - Optimized model for quick responses (2-5 seconds)
- 🆓 **Free Deployment** - Deploy on Hugging Face Spaces with 2GB RAM

## 🎯 Live Demo

Try the live demo here: https://rish06jha-cliq-summary-bot.hf.space

> **Note:** Replace the URL above with your actual deployed Space URL after deployment.

## 📸 Screenshots

### Web Interface
The Gradio interface provides an easy-to-use web UI for testing:

- Input conversation text (minimum 50 characters)
- Click "Generate Summary" button
- Get instant summary and action items
- Try example conversations with one click

## 🚀 Quick Start

### Option 1: Use the Live Demo

Simply visit the (https://huggingface.co/spaces/Rish06jha/cliq-summary-bot) and start using it immediately!

### Option 2: Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cliq-summary-bot.git
   cd cliq-summary-bot
Create virtual environment (recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Open your browser

Navigate to http://localhost:7860

Option 3: Deploy to Hugging Face Spaces
Create a new Space at huggingface.co/new-space
Select Gradio as the SDK
Choose CPU basic (free tier)
Upload all files from this repository
Your app will be live in 3-5 minutes!
📡 API Usage
The bot provides a REST API endpoint for programmatic access.

Python Example
python
import requests

API_URL = "https://your-space-url.hf.space/api/predict"

def summarize_conversation(text):
    """
    Summarize a conversation and extract action items
    
    Args:
        text (str): Conversation text (minimum 50 characters)
    
    Returns:
        dict: Contains 'summary' and 'action_items'
    """
    response = requests.post(
        API_URL,
        json={"data": [text]}
    )
    
    if response.status_code == 200:
        result = response.json()
        return {
            "summary": result['data'][0],
            "action_items": result['data'][1]
        }
    else:
        raise Exception(f"API Error: {response.status_code}")

# Example usage
conversation = """
John met Sarah yesterday at the park to discuss the new project plan. 
They decided to meet again next Monday to finalize the details and 
assign tasks to the team members. Sarah will prepare the initial draft.
"""

result = summarize_conversation(conversation)
print("Summary:", result['summary'])
print("Action Items:", result['action_items'])
cURL Example
bash
curl -X POST https://your-space-url.hf.space/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "data": ["John met Sarah yesterday at the park to discuss the new project plan. They decided to meet again next Monday to finalize the details."]
  }'
Response:

json
{
  "data": [
    "John and Sarah met at the park yesterday to discuss the new project plan. They will meet next Monday to finalize details.",
    "• meet again next Monday to finalize the details"
  ],
  "duration": 2.34
}
JavaScript/Node.js Example
javascript
async function summarizeConversation(text) {
    const API_URL = 'https://your-space-url.hf.space/api/predict';
    
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            data: [text]
        })
    });
    
    const result = await response.json();
    return {
        summary: result.data[0],
        actionItems: result.data[1]
    };
}

// Usage
const conversation = "John met Sarah yesterday...";
const result = await summarizeConversation(conversation);
console.log('Summary:', result.summary);
console.log('Action Items:', result.actionItems);
🔗 Integration Examples
Zoho Cliq Bot
Create a bot in Zoho Cliq with this message handler:

javascript
// Zoho Cliq Bot Handler
info Map:info = {
    "apiURL": "https://your-space-url.hf.space/api/predict"
};

// Get conversation text from message
message_text = message.get("text");

// Validate minimum length
if(message_text.length() < 50) {
    return {
        "text": "❌ Please provide at least 50 characters of conversation text."
    };
}

// Call the summarization API
response = invokeurl
[
    url: info.get("apiURL")
    type: POST
    parameters: {"data": [message_text]}
    detailed: false
];

// Extract summary and action items
summary = response.get("data").get(0);
action_items = response.get("data").get(1);

// Format and return the response
reply_text = "**📋 Summary:**\n" + summary + "\n\n**✅ Action Items:**\n" + action_items;

return {
    "text": reply_text,
    "card": {
        "title": "Conversation Summary",
        "theme": "modern-inline"
    }
};
Slack Bot
python
from slack_bolt import App
import requests

app = App(token="your-bot-token")
API_URL = "https://your-space-url.hf.space/api/predict"

@app.message("summarize")
def summarize_thread(message, say):
    # Get thread messages
    thread = app.client.conversations_replies(
        channel=message['channel'],
        ts=message['thread_ts']
    )
    
    # Combine messages
    conversation = "\n".join([msg['text'] for msg in thread['messages']])
    
    # Call API
    response = requests.post(API_URL, json={"data": [conversation]})
    result = response.json()
    
    # Send summary
    say(f"📋 *Summary:* {result['data'][0]}\n\n✅ *Action Items:*\n{result['data'][1]}")

app.start(port=3000)
🤖 Model Details
Architecture
Model: sshleifer/distilbart-cnn-12-6
Type: Distilled BART (Bidirectional and Auto-Regressive Transformer)
Task: Abstractive Text Summarization
Language: English
Model Size: ~1.2 GB
Parameters: ~406M (distilled from 12-layer to 6-layer)
Performance
Metric	Value
Memory Usage	~1.5 GB RAM
Processing Time	2-5 seconds per request
Max Input Length	1024 tokens (~750 words)
Output Length	30-130 tokens
Accuracy	Optimized for conversational text
Action Item Extraction
The bot uses regex pattern matching to identify action items:

Future actions: "will", "should", "need to", "must", "have to", "going to"
Explicit tasks: "todo", "task", "action item"
Decisions: "decided", "agreed", "plan"
📊 Use Cases
1. Team Meetings
Summarize meeting notes
Extract action items and decisions
Share with team members who missed the meeting
2. Customer Support
Quickly summarize support conversations
Identify customer commitments and next steps
Create follow-up task lists
3. Project Management
Extract tasks from project discussions
Track decisions and agreements
Generate status update summaries
4. Email Threads
Condense long email chains
Identify action items for team members
Create executive summaries
5. Sales Calls
Summarize client conversations
Extract next steps and commitments
Share with sales team
🛠️ Technical Stack
Component	Technology	Version
Language	Python	3.11.0
UI Framework	Gradio	4.16.0
ML Framework	PyTorch	2.5.0
NLP Library	Transformers	4.36.0
Tokenizer	SentencePiece	0.1.99
Deployment	Hugging Face Spaces	-
📁 Project Structure
text
cliq-summary-bot/
├── app.py              # Main Gradio application
├── requirements.txt    # Python dependencies
├── runtime.txt        # Python version specification
├── README.md          # This file
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License
🔧 Configuration
Environment Variables
No environment variables required for basic usage. The model is loaded automatically from Hugging Face Hub.

Model Selection
To use a different model, edit app.py:

python
# Line 6-9 in app.py
summarizer = pipeline(
    "summarization", 
    model="sshleifer/distilbart-cnn-12-6",  # Change this
    device=-1  # -1 for CPU, 0 for GPU
)
Alternative models:

facebook/bart-large-cnn - Larger, more accurate (requires more RAM)
facebook/bart-large-cnn-samsum - Optimized for conversations
google/pegasus-xsum - Good for extreme summarization
🧪 Testing
Manual Testing
Run the app locally
Open http://localhost:7860
Use the example conversations provided
Try your own conversation text
API Testing
bash
# Test the API endpoint
curl -X POST http://localhost:7860/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "data": ["Test conversation text here with at least 50 characters to meet the minimum requirement."]
  }'
🤝 Contributing
Contributions are welcome! Here's how you can help:

Reporting Bugs
Check if the bug is already reported in Issues
Create a new issue with:
Clear title and description
Steps to reproduce
Expected vs actual behavior
Screenshots if applicable
Suggesting Features
Check Issues for existing suggestions
Create a new issue with:
Feature description
Use case / motivation
Possible implementation approach
Pull Requests
Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Make your changes
Test thoroughly
Commit with clear messages (git commit -m 'Add AmazingFeature')
Push to your fork (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
🙏 Acknowledgments
Model: DistilBART by Sam Shleifer
Framework: Hugging Face Transformers
UI: Gradio
Hosting: Hugging Face Spaces
Inspiration: Built for better conversation management and productivity
📞 Support
Documentation: This README
Issues: GitHub Issues
Discussions: GitHub Discussions
Hugging Face Community: HF Forums
🗺️ Roadmap
 Basic summarization functionality
 Action item extraction
 Gradio web interface
 REST API endpoint
 Multi-language support
 Sentiment analysis
 Entity recognition (people, dates, locations)
 Custom model fine-tuning
 Batch processing
 Export to various formats (PDF, Markdown, etc.)
⭐ Star History
If you find this project useful, please consider giving it a star! It helps others discover the project.

Star History Chart

📈 Stats
GitHub repo size
GitHub stars
GitHub forks
GitHub issues

Made with ❤️ for better conversation management

Last updated: January 2026

text

---

1. **`rishabhdkmjha`**
2. **`(https://huggingface.co/spaces/Rish06jha/cliq-summary-bot)`**
3. **`2026`** 
