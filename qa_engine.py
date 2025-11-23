from transformers import pipeline

# HuggingFace small instruction model
qa_model = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.3",
    max_new_tokens=200,
    device_map="auto"
)

def generate_answer(question, context):
    prompt = f"""
You are a PDF assistant. Answer based only on the following text.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
    response = qa_model(prompt)[0]["generated_text"]
    return response.replace(prompt, "").strip()
