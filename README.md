# 🤖 OpenAI GPT-3 Interaction Script

This script is designed to **interact with the OpenAI GPT-3 model** to generate responses based on user input. It operates in a continuous loop, prompting the user to specify a program. The user's input is then used to form a prompt for the GPT-3 model, asking it to solve a problem in Python using optimized data structures. 🐍

Once the GPT-3 model generates a response, the script opens Notepad and uses the `pyautogui` library to automatically type the response into Notepad. After the typing is completed, a pop-up alert notifies the user that the task is complete. 📝

The script then saves the typed content as a Python file. The filename is generated based on the current GMT time. The process repeats until the script is manually stopped. ⏱️

This script essentially automates the process of getting solutions from the GPT-3 model, typing them into Notepad, and saving them as Python files. It's a handy tool for anyone who frequently uses the GPT-3 model to generate Python code. However, remember to replace `'Your-API-KEY'` with your actual OpenAI API key before running the script. 🔑


# REQUIRMENT 
pyautogui


openai


time
