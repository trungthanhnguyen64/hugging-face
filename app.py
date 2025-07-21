from transformers import pipeline
import gradio as gr

# Tạo mô hình tóm tắt
model = pipeline("summarization")

# Hàm xử lý đầu vào
def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Tạo giao diện bằng Gradio
with gr.Blocks() as demo:
    textbox = gr.Textbox(
        placeholder="Enter text block to summarize",
        lines=4,
        label="Input Text"
    )
    output = gr.Textbox(label="Summary")

    textbox.submit(fn=predict, inputs=textbox, outputs=output)
    gr.Button("Summarize").click(fn=predict, inputs=textbox, outputs=output)

# Chạy ứng dụng
demo.launch()
