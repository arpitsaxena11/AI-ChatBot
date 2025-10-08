# 📩 WhatsApp Roast Bot 🤖🔥

This is an automated Python bot that monitors chat messages (e.g., from WhatsApp Web), detects messages from a specific sender, and responds with funny roasts using OpenAI's GPT-3.5-turbo via OpenRouter. It's built with automation libraries like `pyautogui` and `pyperclip`.

---

## 📦 Features

- ✅ Automatically detects the latest message from a specific user (e.g., "DC")
- 🔁 Generates funny roast replies based on chat context
- ✍️ Responds using a friendly, bilingual (Hindi + English) persona
- 🕔 Stops responding if no new message is detected within 10 seconds
- 🤖 Powered by GPT-3.5-Turbo via [OpenRouter](https://openrouter.ai)

---

## 🚀 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/roast-bot.git
cd roast-bot

2. Install requirements
pip install pyautogui pyperclip openai

3. Get API Key

Sign up at OpenRouter

Get your API key and replace it in the script:

api_key="your-api-key-here"




The bot selects the chat window using screen coordinates.

It copies the chat content using mouse drag and Ctrl+C.

If the last message is from the target sender (sender_name), it sends the chat history to GPT-3.5.

The generated response is copied and pasted into the message input box.

The bot sends the response.

If no new message from sender is detected for more than 10 seconds, it exits.

⚠️ Important Notes

This bot uses screen coordinates, which are specific to your display setup. Update the coordinates in the script if needed:

Chat area drag

Input field click

App icon click, etc.

Works best with consistent screen resolution and window positions.

Designed for educational and fun use only. Do not use it for spamming or malicious purposes.

🛡️ Disclaimer

This tool is provided for educational and entertainment purposes. You are responsible for how you use it. The developer is not liable for any misuse.

📄 License

MIT License
