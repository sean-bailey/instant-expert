from transformers import pipeline

def summarizeText(inputtext):
    summarizer=pipeline("summarization")
    return summarizer(inputtext)