import gradio as gr
from transformers import pipeline
import re

print("Loading summarization model...")
summarizer = pipeline(
    "summarization", 
    model="sshleifer/distilbart-cnn-12-6",
    device=-1
)
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

def process_conversation(conversation):
    """Process conversation and return summary + action items"""
    try:
        if len(conversation) < 50:
            return "❌ Error: Conversation too short (minimum 50 characters)", ""
        
        max_input_length = 1024
        if len(conversation) > max_input_length:
            conversation = conversation[:max_input_length]
        
        summary_result = summarizer(
            conversation,
            max_length=130,
            min_length=30,
            do_sample=False,
            truncation=True
        )
        summary = summary_result[0]['summary_text']
        
        action_items = extract_action_items(conversation)
        
        action_items_text = "\n".join([f"• {item}" for item in action_items]) if action_items else "No action items detected"
        
        return summary, action_items_text
    
    except Exception as e:
        return f"❌ Error: {str(e)}", ""

with gr.Blocks(title="Cliq Summary Bot") as demo:
    gr.Markdown(
        """
        # 💬 Cliq Summary Bot
        
        Automatically summarize conversations and extract action items!
        
        **How to use:**
        1. Paste your conversation text below (minimum 50 characters)
        2. Click "Generate Summary"
        3. Get instant summary + action items
        """
    )
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="📝 Conversation Text",
                placeholder="Paste your conversation here...",
                lines=10
            )
            submit_btn = gr.Button("🚀 Generate Summary", variant="primary")
        
        with gr.Column():
            summary_output = gr.Textbox(
                label="📋 Summary",
                lines=5
            )
            action_items_output = gr.Textbox(
                label="✅ Action Items",
                lines=5
            )
    
    gr.Examples(
        examples=[
            ["John met Sarah yesterday at the park to discuss the new project plan. They decided to meet again next Monday to finalize the details and assign tasks to the team members."],
            ["The team discussed the quarterly budget during the meeting. They agreed to increase marketing spend by 15% and will need to submit the proposal by Friday. Sarah will prepare the financial report."],
            ["During the client call, we reviewed the project timeline. The client requested changes to the design mockups. We need to revise the wireframes and schedule a follow-up meeting next week to present the updated designs."]
        ],
        inputs=input_text,
        label="📚 Example Conversations"
    )
    
    submit_btn.click(
        fn=process_conversation,
        inputs=input_text,
        outputs=[summary_output, action_items_output]
    )

if __name__ == "__main__":
    demo.launch()
