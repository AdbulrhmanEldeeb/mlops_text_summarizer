import gradio as gr
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define the summarization function with truncation
def summarize_text(article):
    # Truncate the input to 1024 tokens
    truncated_article = article[:1024]
    summary = summarizer(truncated_article, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Create the Gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs="textbox",  # User inputs a large article
    outputs="text",    # Output is the summary of the article
    title="Text Summarizer",
    description="Enter an article to get a summarized version."
)

# Launch the Gradio app
interface.launch()
