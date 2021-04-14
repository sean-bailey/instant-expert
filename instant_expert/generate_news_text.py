import newsRipper2 as nr
import pdfplumber
from wrapt_timeout_decorator import *
import textract
import os

def geturls(myquery):
    results=nr.searchnews(query=myquery).results
    myurls=results.links()
    returndict={}
    for url in myurls:
        returndict[url]=1
    myurls=[]
    myurls=list(returndict.keys())
    return myurls

@timeout(6)
def getparsednews(url):
    return nr.parsenews(url)

@timeout(30)
def getpdf(url):
    #print("url contains pdf, more time for processing required...")
    text=""
    with pdfplumber.open(url) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def savenews(myurls,outfilename):
    urlcounter=len(myurls)
    for count, url in enumerate(myurls):
        #print(url)
        try:
            news=getparsednews(url)
            if news.date_publish is not None or news.article is not None:
                article=news.article
                summary=news.summary
                print(str(count)+"/"+str(urlcounter))
                with open(outfilename,'a') as myfile:
                    myfile.write(article)
                    myfile.write('\n')
                    myfile.write('\n')
            elif str(url).split('.')[-1] == '.pdf':
                text=getpdf(url)
                with open(outfilename, 'a') as myfile:
                    myfile.write(text)
                    myfile.write('\n')

                with open(outfilename,'a') as myfile:
                    myfile.write('\n')
                    myfile.write('\n')

        except Exception as e:
            print(e)


def getnews(myurls):
    counter = 0
    returnstring=""
    urlcounter = len(myurls)
    for count, url in enumerate(myurls):
        #print(url)
        try:
            news=getparsednews(url)
            if news.date_publish is not None or news.article is not None:
                article=news.article
                print(str(count)+"/"+str(urlcounter))
                returnstring+=article+'\n'+'\n'
            elif str(url).split('.')[-1] == '.pdf':
                returnstring+=getpdf(url)+"\n"+"\n"
        except Exception as e:
            print(e)
    return returnstring

def getraw(myurls):
    returnstring=""
    for count, url in enumerate(myurls):
        try:
            rawtext = nr.rawnews(url).results
            print(str(count) + "/" + str(len(myurls)))
            returnstring+=rawtext+"\n"+"\n"

        except Exception as e:
            print(e)


def saveraw(myurls,outfilename):
    for url in myurls:
        try:
            rawtext=nr.rawnews(url).results
            with open(outfilename,'a') as myfile:
                myfile.write(rawtext)
                myfile.write('\n')
                myfile.write('\n')
        except Exception as e:
            print(e)

def loadtext(infilename):
    return textract.process(infilename).decode("utf-8")
    #with open(infilename,'r') as myfile:
    #    return myfile.readlines()


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r