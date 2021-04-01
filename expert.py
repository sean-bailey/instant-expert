"""
This file will be the command line interface file to allow for question and answer capabilities against a corprus, or
to provide generalized research capabilities for a topic.

"""

import argparse
import instant_expert as expert
research=None
answer=None
#we need to be able to take in arguments and intelligently parse them and provide output based on them.
parser=argparse.ArgumentParser(description="This python script enables broad automated research on a topic and machine learning powered question answers on a given set of data.")

parser.add_argument('-t','--topic',default=None,help="Topic to research")
parser.add_argument('-q','--question',default=None,help="Question asked against corprus")
parser.add_argument('-s','--savefile',default=None,help="File to save research to.")
parser.add_argument('-l','--load',default=None,help="file or directory to load context from")
parser.add_argument('-c','--context',default=None,help="Context for asking a question against")
parser.add_argument('-m','--model',default="bert-large-uncased",help="huggingface model for question answering, default bert-large-uncased")
parser.add_argument('-r','--raw',default='0',help="Whether to get the raw results from research or not (either 1 or 0, default 0)")

args=parser.parse_args()
#first, the research phase
if args['topic'] is not None:
    research=expert.resarchtopic(topic=args['topic'],savefile=args['savefile'],raw=int(args['raw']))
if args['question'] is not None:
    if args['context'] is None and args['load'] is None and research is not None:
        answer=expert.answer(question=args['question'],context=research.finaltext,fromfile=args['load'],model=args['model']).answer
    else:
        answer=expert.answer(question=args['question'],context=args['context'],fromfile=args['load'],model=args['model']).answer
    print(answer)
else:
    if args['savefile'] is not None and args['topic'] is not None:
        print("saved to "+args['savefile'])
    else:
        print(research.finaltext)
