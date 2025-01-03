import openai
import customtkinter as ctk
from tkinter import messagebox

openai.api_key = "your_openai_api_key"
def summarize_text(input_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize this text: {input_text}"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def summarize():
    input_text = text_input.get("1.0", "end").strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter some text to summarize.")
        return
    summary = summarize_text(input_text)
    summary_output.delete("1.0", "end")
    summary_output.insert("end", summary)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("AI Text Summarizer")
root.geometry("700x500")
input_label = ctk.CTkLabel(
    root, 
    text="Enter Text to Summarize:", 
    font=("Arial", 16, "bold")
)
input_label.pack(pady=10)
text_input = ctk.CTkTextbox(
    root, 
    width=650, 
    height=150, 
    font=("Arial", 14, "bold"),
    fg_color="#000000",
    text_color="#ffffff"
)
text_input.pack(pady=10)
summarize_button = ctk.CTkButton(
    root, 
    text="Summarize", 
    font=("Arial", 14, "bold"), 
    command=summarize,
    text_color="#ffffff"
)
summarize_button.pack(pady=10)

output_label = ctk.CTkLabel(
    root, 
    text="Summary Output:", 
    font=("Arial", 16, "bold")
)
output_label.pack(pady=10)
summary_output = ctk.CTkTextbox(
    root, 
    width=650, 
    height=150, 
    font=("Arial", 14, "bold"),
    fg_color="#000000",
    text_color="#ffffff"
)
summary_output.pack(pady=10)
root.mainloop()
