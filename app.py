# app.py
import gradio as gr
from transformers import pipeline

# Tải mô hình tóm tắt văn bản từ Hugging Face
summarizer = pipeline("summarization")

def summarize_text(text):
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]["summary_text"]

# Tạo giao diện Gradio
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Nhập văn bản cần tóm tắt..."),
    outputs="text",
    title="Ứng dụng Tóm tắt Văn bản",
    description="Ứng dụng dùng mô hình Hugging Face để tóm tắt văn bản dài."
)

# Chạy ứng dụng
if __name__ == "__main__":
    iface.launch()
