# from transformers import pipeline

# # Initialize the summarizer pipeline outside the function for efficiency
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(input_text):
#     if len(input_text.split()) > 10:
#         summary = summarizer(input_text, max_length=50, min_length=20, do_sample=False)
#         return summary[0]['summary_text']
#     else:
#         return "The input text is too short to summarize. Text need at least 20 words."

