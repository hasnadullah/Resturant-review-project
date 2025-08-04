import gradio as gr
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Load model
model = OllamaLLM(model="llama3.2")

# Define prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Gradio function
def answer_question(question):
    reviews = retriever.invoke(question)
    review_text = "\n".join([doc.page_content for doc in reviews])
    result = chain.invoke({"reviews": review_text, "question": question})
    return str(result)

# Launch Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=2, placeholder="Ask your question about the restaurant..."),
    outputs="text",
    title="🍕 Pizza Restaurant Assistant",
    description="Ask anything about the restaurant based on real customer reviews."
)

iface.launch()
