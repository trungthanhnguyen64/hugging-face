from transformers import pipeline
import gradio as gr

# Khởi tạo mô hình tóm tắt văn bản
summarizer = pipeline("summarization")

# Hàm xử lý văn bản đầu vào
def summarize(text):
    if not text.strip():
        return "⚠️ Vui lòng nhập nội dung để tóm tắt."
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]["summary_text"]

# Giao diện Gradio
with gr.Blocks() as demo:
    gr.Markdown("## ✨ Text Summarization App\nNhập đoạn văn để được tóm tắt tự động.")
    
    input_text = gr.Textbox(
        placeholder="Nhập đoạn văn bản cần tóm tắt...",
        lines=6,
        label="Văn bản gốc"
    )
    
    summarize_button = gr.Button("Tóm tắt")
    
    output_text = gr.Textbox(
        label="Kết quả tóm tắt",
        lines=4
    )

    # Submit khi nhấn Enter
    input_text.submit(fn=summarize, inputs=input_text, outputs=output_text)
    
    # Submit khi nhấn nút
    summarize_button.click(fn=summarize, inputs=input_text, outputs=output_text)

# Khởi chạy ứng dụng
if __name__ == "__main__":
    demo.launch()

