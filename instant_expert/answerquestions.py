from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("deepset/xlm-roberta-large-squad2")

model = AutoModelForQuestionAnswering.from_pretrained("deepset/xlm-roberta-large-squad2")

def answerquestion_pipeline(question,context):
    question_answerer=pipeline('question-answering',model=model,tokenizer=tokenizer)
    return question_answerer({
        'question':question,
        'context':context
    })

