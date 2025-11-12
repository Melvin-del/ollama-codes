import gradio as gr
import ollama
with open('marks.csv', 'r', encoding='utf-8') as f:
    marks_data_string = f.read()
SYSTEM_PROMPT = f"""
You are a helpful AI marks assistant.
You must give marks recommendations based based on the following data.
When you recommend a movie, explain *why* based on the data.
You can use external knowledge if it is relevant to the content asked. If the answer is not related this data,
say "I'm sorry, I don't have that information."
{marks_data_string}"""
def marks_chat(message, history):
    messages = [{'role': 'system', 'content': SYSTEM_PROMPT},{'role': 'user', 'content': message}]
    response = ollama.chat(model='qwen2.5:0.5b', messages=messages)
    return response['message']['content']
print("Launching AI marks Assistant...")
gr.ChatInterface(fn=marks_chat, title="AI marks Assistant").launch()
