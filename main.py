# open the whtsappp web at any browser and run the python program

import pyautogui
import pyperclip
import time
import openai



openai.api_key="YOUR API_KEY"
# pyautogui.click(1639, 1412)

def chat_with_gpt(prompt):
    """Send user input to OpenAI API and get a response."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" if needed
        messages=[{"role": "system", "content": "i am a friend from  india ,  chatting with my friend try to make funny indian(desi) messages."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"]


"""Type the message at specified coordinates."""

def type_message_at_coordinates(message, x, y):
    pyautogui.click(x, y)  # Move the mouse to the position
    time.sleep(0.5)  # Give time for the focus to change (optional)
    pyautogui.write(message, interval=0.1)  # Type the message

"""CLICK AT A THE SEND"""

def send_message():
    time.sleep(1)  # Small delay to prevent misclicks
    pyautogui.click(1850, 1016)


while True:
    time.sleep(3)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(695,216)
    pyautogui.dragTo(1637, 947, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')


    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied conversation if you want
    # print(chat_history) 
    if "bye" in chat_history:
        break    
    x=chat_with_gpt(chat_history)
    type_message_at_coordinates(x,1354,1010)
    send_message()



   
  

