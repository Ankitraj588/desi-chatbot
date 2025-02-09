# push this code instead of openai for offline 

from gpt4all import GPT4All


model_path=r"C:\Users\GPT4All\mistral-7b-instruct-v0.1.Q4_0.gguf"
# makesure to install you model based on your ram (set path if facing problem search for .gguf)
# recommended model =""mistral-7b-instruct-v0.1.Q4_0.gguf""
model = GPT4All(model_path,allow_download=False)  # Change this to your downloaded model file

def chat_with_ai(user_message):
    response = model.generate("generate friendly indian response while analysing the chat sir", max_tokens=100)
    return response

if __name__ == "__main__":
    while True:
      # input is the selected text from the web using pyautogui
        user_input = input("You: ")
      
        if user_input.lower() == "exit":
            break
        print("Bot:", chat_with_ai(user_input))
