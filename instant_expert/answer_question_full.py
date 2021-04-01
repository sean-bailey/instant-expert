from instant_expert.answer_question_class import *
from transformers import pipeline

def getquestionanswered(question,context,model="bert-large-uncased"):
    reader=DocumentReader(model)
    reader.tokenize(question,context)
    answers=reader.get_answer().replace('/','')
    summarizer=pipeline("summarization")
    return summarizer(answers,min_length=len(answers.split(' '))//7,max_length=len(answers.split(' '))//3)