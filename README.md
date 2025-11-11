# Chat with PDF

A Streamlit app to upload PDFs, extract text, and answer questions using a Hugging Face LLM and FAISS vector store.

## Setup
1. Clone the repository.
2. Create a virtual environment:
   `ash
   python -m venv venv
   `
3. Activate the virtual environment:
   - Windows: .\venv\Scripts\Activate.ps1`n   - Linux/Mac: source venv/bin/activate`n4. Install dependencies:
   `ash
   pip install -r requirements.txt
   `
5. Run the app:
   `ash
   streamlit run app.py
   `

## Usage
- Upload a PDF via the Streamlit interface.
- Ask questions about the PDF content.
- The app processes the PDF, stores embeddings in FAISS, and uses a Hugging Face LLM to answer.

## Dependencies
Listed in equirements.txt.

## Notes
- Ensure you have a compatible GPU for faster LLM inference (optional).
- Adjust the Hugging Face model in qa_engine.py as needed.
