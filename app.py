from transformers import pipeline
import gradio as gr
import torch  # ✅ Quan trọng: tránh lỗi NameError

model = pipeline("summarization", model="google-t5/t5-small")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Dùng Interface đơn giản
demo = gr.Interface(fn=predict, inputs=gr.Textbox(lines=4, placeholder="Enter text block to summarize"), outputs="text")
demo.launch()
