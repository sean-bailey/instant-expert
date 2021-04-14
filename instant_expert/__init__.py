from instant_expert.generate_news_text import *
from instant_expert.answer_question_full import *
import os

acceptable_file_extensions=['csv', 'doc', 'docx', 'eml', 'epub', 'gif', 'htm', 'html', 'jpeg', 'jpg', 'json', 'log', 'mp3', 'msg', 'odt', 'ogg', 'pdf', 'png', 'pptx', 'ps', 'psv', 'rtf', 'tff', 'tif', 'tiff', 'tsv', 'txt', "wav", "xls", "xlsx"]

class resarchtopic:

    def __init__(self,topic=None,savefile=None,raw=False):
        self.topic=topic
        self.savefile=savefile
        self.raw=raw
        self.urllist=None
        self.finaltext=""
        if self.topic is not None:
            self.urllist=geturls(self.topic)

            if self.savefile is not None:
                if self.raw:
                    saveraw(self.urllist,self.savefile)
                else:
                    savenews(self.urllist,self.savefile)
            else:
                if self.raw:
                    self.finaltext=getraw(self.urllist)
                else:
                    self.finaltext=getnews(self.urllist)
        else:
            raise ValueError("Please provide a topic for the research. Useage is researchtopic(topic='my research topic',savefile=(optional)'/my/file/path',raw=boolean)")


class answer:

   def __init__(self,question=None,context=None,fromfile=None,model="bert-large-uncased"):
        self.question=question
        self.context=context
        self.fromfile=fromfile
        self.model=model
        self.answer=""
        if self.context is not None:
            temptext = ""
            if self.fromfile is not None:

                if os.path.isdir(fromfile):
                    filelist = list_files(fromfile)
                    for filename in filelist:
                        try:
                            if str(filename).split('.')[-1] in acceptable_file_extensions:
                                temptext += loadtext(filename)
                        except Exception as e:
                            print(filename)
                            print(e)
                else:
                    temptext = loadtext(fromfile)
            self.context += temptext

        else:
            if self.fromfile is not None:
                temptext = ""
                if os.path.isdir(fromfile):
                    filelist = list_files(fromfile)
                    for filename in filelist:
                        try:
                            if str(filename).split('.')[-1] in acceptable_file_extensions:
                                temptext += loadtext(filename)
                        except Exception as e:
                            print(filename)
                            print(e)
                else:
                    temptext = loadtext(fromfile)
                self.context = temptext
            else:
                raise ValueError("Incorrect usage. You must specify context or the file to load the context from")
        if self.question is not None:

            self.answersum=getquestionanswered(self.question, self.context, self.model)
            self.answer = getquestionsummarized(self.answersum)
        else:
            raise ValueError("Incorrect usage. You must specify a question")

