import ollama
import gradio as g
with open('marks.csv', 'r', encoding = 'utf-8') as f:
    data = f.read()
prompt = f""""
You are a AI marks assistant. Your role is to answer qeries based on marks alone from the data given below. 
You can use external knowledge to explain why you are reccomending the destination only.You can not use external knowledge if the querstion is totlly irrelevent to the data given. If the question in irrelevent say
"I am unable to answer". 
{data}
"""
def func(message, history):
    messages = [{'role': 'system', 'content' : prompt},{'role':'user', 'content' : message}]
    resp = ollama.chat(model = 'qwen2.5:0.5b', messages = messages)
    return resp['message']['content']
while True:
    inp = input()
    res = func(inp, None)
    print(res)
