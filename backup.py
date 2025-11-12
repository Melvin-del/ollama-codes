import ollama
import gradio as gr

def query_ollama(prompt, model="qwen2.5:0.5b"):
    """Generic function to query local LLM using Ollama"""
    try:
        response = ollama.chat(model=model, messages=[
            {"role": "system", "content": "You are an intelligent AI assistant."},
            {"role": "user", "content": prompt}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def ai_experiment(task_type, user_input):
    """Generalized AI experiment handler"""
    if task_type == "Chatbot":
        prompt = f"You are a product assistant. Answer or recommend based on: {user_input}"
    elif task_type == "Blog Generator":
        prompt = f"Write a blog on: {user_input} in an engaging, structured way."
    elif task_type == "Email Assistant":
        prompt = f"Draft a professional reply for this customer message: {user_input}"
    elif task_type == "Recommender":
        prompt = f"User likes: {user_input}. Suggest 5 similar books/movies."
    elif task_type == "Document Analyzer":
        prompt = f"Summarize and analyze this document text: {user_input}"
    elif task_type == "Medical Assistant":
        prompt = f"""
        You are a friendly AI-powered medical assistant.
        Analyze these symptoms: {user_input}.
        Suggest likely common conditions, possible home remedies,
        and indicate when to consult a doctor.
        Always include a disclaimer: "This is not a medical diagnosis; consult a professional if symptoms persist."
        """
    else:
        prompt = f"Respond appropriately to: {user_input}"

    return query_ollama(prompt)

# ---- Simple UI ----
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Unified AI Experiment Interface (Now Includes Medical Assistant)")
    task = gr.Radio(["Chatbot", "Blog Generator", "Email Assistant", 
                     "Recommender", "Document Analyzer", "Medical Assistant"],
                    label="Select Experiment Type")
    user_input = gr.Textbox(label="Enter Input / Query", placeholder="Type your query or symptoms here...")
    output = gr.Textbox(label="AI Response", lines=10)
    btn = gr.Button("Generate / Analyze")
    btn.click(fn=ai_experiment, inputs=[task, user_input], outputs=output)

demo.launch()
