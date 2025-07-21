from transformers import pipeline
import gradio as gr
import torch  # Bắt buộc để PyTorch backend hoạt động

model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")  # ép dùng PyTorch

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

demo = gr.Interface(fn=predict, inputs=gr.Textbox(lines=4), outputs="text")
demo.launch()
