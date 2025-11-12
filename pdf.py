import gradio as gr
import ollama
from pypdf import PdfReader  
print("Loading text from PDF...")
reader = PdfReader("EX 6 melvin.pdf") 
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text() + "\n"
marks_data_string = pdf_text
print("...PDF loaded.")
SYSTEM_PROMPT = f"""
You are a helpful AI marks assistant.
You must give marks recommendations based on the following data.
When you recommend a *destination*, explain *why* based on the data.
You can use external knowledge if it is relevant. If the answer is not
related to this data, say "I'm sorry, I don't have that information."
--- MARKS DATA ---
{marks_data_string}
--- END OF DATA ---
"""
def marks_chat(message, history):
    messages = [{'role': 'system', 'content': SYSTEM_PROMPT},{'role': 'user', 'content': message}]
    response = ollama.chat(model='qwen2.5:0.5b', messages=messages)
    return response['message']['content']
print("Launching AI marks Assistant...")
gr.ChatInterface(fn=marks_chat, title="AI marks Assistant").launch()
