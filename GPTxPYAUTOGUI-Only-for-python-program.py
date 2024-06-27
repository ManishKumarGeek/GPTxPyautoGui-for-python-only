import openai
import pyautogui
import time
import calendar
from subprocess import Popen

# Set OpenAI API key
openai.api_key = 'Your-API-KEY'

# Get current GMT time
current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
js = str(ts)

# Initialize messages
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

while True:
    # Get user input
    message = input("Specify the program: ")

    if message:
        # Prepare the prompt
        final_prompt = f"""
        # This Prompt is created by Manish
        ----------------------------------
        Solve this in Python using optimized data structures for efficient time and space complexity, while explaining your code in an elegant yet descriptive manner. Every thing you explain should be commented out from the first word to last: {message}
        """
        # Append user message
        messages.append({"role": "user", "content": final_prompt})

        # Create chat completion
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        # Get reply
        reply = chat.choices[0].message.content

        # Open notepad
        process = Popen('C:\\Windows\\system32\\notepad.exe')
        time.sleep(2)

        # Write reply in notepad
        pyautogui.write(reply, interval=0.01)

        # Show alert
        pyautogui.alert('Auto Typer Task Completed')

        # Save file
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.write(js)
        time.sleep(2)
        pyautogui.write(".py")
        pyautogui.press('enter')
#ManishKumarGeek
#Cleancode and Improvement
