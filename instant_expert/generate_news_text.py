import newsRipper2 as nr
import pdfplumber
import timeout_decorator
import textract


def geturls(myquery):
    results=nr.searchnews(query=myquery).results
    myurls=results.links()
    returndict={}
    for url in myurls:
        returndict[url]=1
    myurls=[]
    myurls=list(returndict.keys())
    return myurls

@timeout_decorator.timeout(6)
def getnews(url):
    return nr.parsenews(url)

@timeout_decorator.timeout(30)
def getpdf(url):
    text=""
    with pdfplumber.open(url) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def savenews(myurls,outfilename):
    counter = 0
    for url in myurls:
        #print(url)
        try:
            news=getnews(url)
            counter+=1
            if news.date_publish is not None or news.article is not None:
                article=news.article
                summary=news.summary
                print(str(counter)+"/"+str(len(myurls)))
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
    for url in myurls:
        #print(url)
        try:
            news=getnews(url)
            counter+=1
            if news.date_publish is not None or news.article is not None:
                article=news.article
                print(str(counter)+"/"+str(len(myurls)))
                returnstring+=article+'\n'+'\n'
            elif str(url).split('.')[-1] == '.pdf':
                returnstring+=getpdf(url)+"\n"+"\n"
        except Exception as e:
            print(e)
    return returnstring

def getraw(myurls):
    counter=0
    returnstring=""
    for url in myurls:
        try:
            rawtext = nr.rawnews(url).results
            counter += 1
            print(str(counter) + "/" + str(len(myurls)))
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