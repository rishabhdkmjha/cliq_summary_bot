Cliq Summary Bot

A smart, lightweight summarization bot for Zoho Cliq that condenses long messages, chats, or documents into short, clear summaries using NLP/LLM-powered text processing.

Built by Team Z CODE.

🌐 Deployment Status

This project is currently not deployed.
A live hosted endpoint will be added soon.

In the meantime, you can:

Explore the code in the repository

Run the bot locally

Modify the config to integrate your own API keys

Use the included scripts to test summarization via Hugging Face API

If you want to set up your own deployment, instructions are included below.

✨ Features

Summarizes long texts, conversations, or uploaded docs

Supports short, medium, and detailed summaries

Lightweight — no heavy ML libraries (no PyTorch / no spaCy)

Uses external APIs (Hugging Face) for inference

Works with Zoho Cliq slash commands or bot mentions

🛠️ Tech Stack

Zoho Cliq Bot SDK

Node.js / Python backend (your choice)

Hugging Face Inference API

Webhook integration for message handling

📦 Installation (Local)

Clone the repo:

git clone https://github.com/<username>/cliq_summary_bot.git
cd cliq_summary_bot


Install dependencies:

npm install


(or pip install -r requirements.txt if Python)

Add your Hugging Face API key in .env:

HF_API_KEY=your_key_here


Run locally:

npm start

📘 Usage

Inside Zoho Cliq, after connecting the bot:

@summarybot summarize <text>


or

/summarize <message>

📄 License

This project is open-source under the MIT License.

🤝 Contributing

Feel free to open issues or submit pull requests.
