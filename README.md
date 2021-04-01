# instant-expert

---

This project is designed to allow for a simple interface to answer questions based on broad research.
Instant expert will leverage search engine scraping to broadly research any topic the user wants to know about.
On top of that, it provides the ability to use huggingface transformer models (BERT,alBERTa, RoBERT) designed for 
question answering and summarization to provide an answer interface based on the information provided. 

No longer do you need to spend hours researching a topic -- let the machine do it for you, and ask the specific
things you'd like to know later on!

If you already have a text corprus, this works as well. Simply provide the file location, or the directory, and 
instant-expert will load the data into memory and prepare it for processing.

Note: This is a rather compute and memory intensive task, and does take time to complete, so "instant" is a moniker
of sorts. It logically, however, performs relevant research faster than humans would, and is excellent for enabling
end users to have their questions on your information answered without consuming the time of your experts.
Speeding up research isn't quite achievable, but improving question answer speed scales with machine ram and compute
capabilities. You can also specify "heavier" and "lighter" models to perform the question and answering process against.


---
###Prerequisites


You'll need 
-Python3.7+
-mysql drivers for your operating system

---


###Installation:


Either download the repo and use
```pip3 install .```

or
```pip3 install https://github.com/sean-bailey/instant-expert/archive/refs/heads/main.zip```

---

###Usage



`instant-expert` is designed to be called either via command line or as a standard python module.

If you are using it as a Python Module:

```
import instant_expert as expert

##If you would like to perform research on a particular topic...

finalresearch=expert.researchtopic(topic="Brazil in World War 2").finaltext

#Arguments:
#topic -- you must provide a research topic (string)
#savefile -- you can supply a filename you'd like it to write results to (string) (optional)
#raw -- you can specify if you'd like the raw data (essentially raw html) or if you'd like it processed first (Boolean) (Optional)

##If you would like to ask a question against a particular corprus of text...
finalanswer=expert.answer(question="How many troops did Brazil send in total?").answer

#Arguments:
#question -- you must provide a question to ask (string)
#context -- if specified, will be part of the context added. if context is not specified, fromfile must be specified (string)
#fromfile -- if specified, will check the file or directory for files containting data to be loaded into context. If it is not specified, context must be specified (string)
#model -- specify the huggingface model you'd like to load. defautls to "bert-large-uncased" (optional) (string)

```

If you would prefer to use a command line interface:

```
python3 expert.py -h

```
This basically provides a command line wrapper to the module, allowing you to use it purely in CLI.

---

###Contributing



Any contributions can be made by
1) Submit an issue request
2) Fork this repo
3) make a branch with a relevant name to it
4) commit your changes to that branch
5) Do a pull request to this repo

---