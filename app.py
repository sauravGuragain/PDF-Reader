import gradio as gr
from ocr_reader import extract_pdf_text
from vector_store import create_chunks, build_faiss_index, search
from qa_engine import generate_answer

index = None
chunks = None
pdf_text = ""

def upload_pdf(pdf_file):
    global index, chunks, pdf_text

    pdf_path = pdf_file.name
    pdf_text = extract_pdf_text(pdf_path)

    chunks = create_chunks(pdf_text)
    index, chunks_list = build_faiss_index(chunks)

    return "PDF processed successfully! You can now ask questions."

def ask_question(question):
    global index, chunks, pdf_text
    
    if index is None:
        return "❗ Upload a PDF first."

    results = search(question, index, chunks)
    combined_context = "\n\n".join(results)

    answer = generate_answer(question, combined_context)
    return answer

with gr.Blocks() as demo:
    gr.Markdown("# 📄 Chat with OCR PDF (Hybrid System)")
    
    with gr.Row():
        upload = gr.File(label="Upload PDF")
    
    upload_btn = gr.Button("Process PDF")
    status = gr.Textbox(label="Status")

    question = gr.Textbox(label="Ask your question")
    answer = gr.Textbox(label="Answer", lines=5)

    upload_btn.click(upload_pdf, inputs=[upload], outputs=[status])
    question.submit(ask_question, inputs=[question], outputs=[answer])

demo.launch()
