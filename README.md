🚀 Cliq Summary Bot
An AI-powered Zoho Cliq bot that converts long chats into clear, concise summaries.

🧠 What is Cliq Summary Bot?

Cliq Summary Bot is an intelligent summarization assistant for Zoho Cliq.
It automatically condenses long conversations, documents, or messages into short, readable summaries using LLM/NLP-based APIs.

Perfect for teams that want to save time, improve clarity, and boost productivity.

🖼️ Architecture Diagram
           ┌──────────────────────┐
           │        User          │
           │  sends message/text  │
           └──────────┬───────────┘
                      │
                      ▼
           ┌──────────────────────┐
           │   Zoho Cliq Bot      │
           │ (Slash Cmd / Mention)│
           └──────────┬───────────┘
                      │ Forwards text
                      ▼
           ┌──────────────────────┐
           │ Backend Server       │
           │ Node/Python Handler  │
           └──────────┬───────────┘
                      │ Sends to API
                      ▼
           ┌──────────────────────┐
           │ Hugging Face API     │
           │  (LLM Summarizer)    │
           └──────────┬───────────┘
                      │ Returns summary
                      ▼
           ┌──────────────────────┐
           │  Zoho Cliq Response  │
           │  Clean Summary Text  │
           └──────────────────────┘
           

🖼️ Workflow Diagram (User Perspective)
User → Types "@summarybot summarize message"
        ↓
Bot Receives Text  
        ↓  
Bot Sends Text → Hugging Face Summarizer  
        ↓  
Receives Summary  
        ↓  
Bot Replies in Cliq with Clean Output  

📸 Image Placeholders (replace with real screenshots)
Bot in Action

Zoho Cliq Slash Command UI

✨ Features

✔ Summarizes long chats, threads, and docs

✔ Short / Medium / Detailed summary modes

✔ No heavy ML dependencies (no PyTorch / no spaCy)

✔ Uses cloud inference APIs

✔ Works via @mention or slash commands

✔ Lightweight and easy to deploy

⚙️ Tech Stack
Component	Technology
Bot Platform	Zoho Cliq
Backend	Node.js / Python
AI Engine	Hugging Face Inference API
Auth	API Key
Deployment	Local / Cloud (Render, Railway, etc.)
🚧 Deployment Status

The bot is currently not deployed.
A live server link will be added in the next update.

You can still:

Run it locally

Explore the code

Replace with your API key

Deploy your own backend anytime

🔧 Local Installation
git clone https://github.com/<username>/cliq_summary_bot.git
cd cliq_summary_bot
npm install   # or pip install -r requirements.txt


Add your Hugging Face key:

HF_API_KEY=your_key_here


Run:

npm start   # or python app.py

🧪 Usage

In Zoho Cliq:

/summarize The meeting discussion goes here...


or

@summarybot summarize the last 20 messages

📂 Project Structure
cliq_summary_bot/
│── src/
│   ├── api_handler.js
│   ├── cliq_handler.js
│   └── utils.js
│── config/
│   └── env.example
│── assets/
│   └── images (screenshots)
│── README.md
│── package.json
└── .env

🤝 Team

Team Z CODE

📄 License

MIT License
