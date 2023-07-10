import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as palm

palm.configure(api_key="INSERT YOUR API KEY HERE")

def process_input():
    user_message = user_input.get("1.0", tk.END).strip()
    
    if user_message:
        chat_history.insert(tk.END, "You: " + user_message + "\n")
        
        messages.append(user_message)
        
        response = palm.chat(**defaults, context=context, examples=examples, messages=messages)
        
        chatbot_response = response.last
        
        if chatbot_response is not None:
            type_chatbot_response(chatbot_response)
        
        user_input.delete("1.0", tk.END)

def regenerate_response():
    response = palm.chat(**defaults, context=context, examples=examples, messages=messages)
    
    chatbot_response = response.last
    
    if chatbot_response is not None:
        type_chatbot_response(chatbot_response)

def type_chatbot_response(response):
    chat_history.insert(tk.END, "Chatbot: ")
    for char in response:
        chat_history.insert(tk.END, char)
        chat_history.see(tk.END)  
        window.update()  
        window.after(12)  
    chat_history.insert(tk.END, "\n")


window = tk.Tk()
window.title("Google PaLM")
window.configure(bg="black")

# Add shadow effect to input textbox and response background
shadow_style = {"background": "#808080", "highlightbackground": "black", "highlightcolor": "black"}

chat_history = scrolledtext.ScrolledText(window, width=100, height=30, bg="black", fg="white", font=("Arial", 12),
                                         **shadow_style)
chat_history.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

user_input = tk.Text(window, height=3, width=50, bg="white", fg="black", font=("Arial", 12),
                     **shadow_style)
user_input.grid(column=0, row=1, padx=10, pady=10)

send_button = tk.Button(window, text=">", command=process_input, width=2, height=3, bg="teal", fg="white",
                        font=("Arial", 12, "bold"), relief=tk.RAISED, bd=0)
send_button.grid(column=1, row=1, padx=10, pady=10)

regenerate_button = tk.Button(window, text="Regenerate", command=regenerate_response, width=15, height=3, bg="teal",
                              fg="white", font=("Arial", 12, "bold"), relief=tk.SUNKEN, bd=0)
regenerate_button.grid(column=0, row=2, padx=10, pady=10)

defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}
context = ""
examples = []
messages = []

window.mainloop()
