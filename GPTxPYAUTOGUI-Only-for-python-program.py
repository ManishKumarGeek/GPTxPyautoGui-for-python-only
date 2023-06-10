import openai
from subprocess import * #import all from subprocess
import pyautogui #pip install pyautogui 
import time
import calendar

current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
js= str(ts)
openai.api_key = 'Your-API-KEY'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
while True:
	message = input("Specify the program: ")
	finaly = """Solve this in PROGRAMMING_LANGUAGE Python using optimized data structures for efficient time and space complexity, while explaining your code in an elegant yet descriptive manner & every thing you explain should be comment out for the first word to last :
 & before starting write #This Prompt is created by Manish, & line break with line divider.""" + message
	formt = input("language serfix Example : .py ")
	if message:
		messages.append(
			{"role": "user", "content": finaly },
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	process =Popen('C:\\Windows\system32/notepad.exe' ) #open notepad automatic
	time.sleep(2) #after 2 sec
	pyautogui.write(reply, interval=0.01) #input from writer
	pyautogui.alert('Auto Typer Task Completed') #popup of task complete
	#a= pyautogui.prompt('Save file as Name') #file name
	pyautogui.hotkey('ctrl','s') #save  hotkey
	time.sleep(2) #after 2 sec
	pyautogui.write(js)
	time.sleep(2)
	pyautogui.write(".py")
	pyautogui.press('enter') #press enter
#process.terminate()
#github.com/Manish00322