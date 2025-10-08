import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="api-key",
)

def is_last_message_from_sender(chat_log, sender_name="DC"):
    messages = chat_log.strip().split("/2025] ")
    last_message = messages[-1] if messages else ""
    return sender_name in last_message

# Click on the Chrome icon (or relevant area)
pyautogui.click(704, 860)
time.sleep(1)

last_seen_time = time.time()  # Record current time

while True:
    time.sleep(5)

    # Select the chat window and copy the content
    pyautogui.moveTo(592, 178)
    pyautogui.dragTo(843, 776, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(823, 829)

    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        last_seen_time = time.time()  # Update last seen time

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Arpit who speaks Hindi and English. You are from India and are friendly by nature. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [4:38 pm, 7/10/2025] DC: "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(1510, 768)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

    # Stop if 10 seconds have passed without a new message from the sender
    if time.time() - last_seen_time > 10:
        print("No message from sender in the last 10 seconds. Stopping the bot.")
        break
