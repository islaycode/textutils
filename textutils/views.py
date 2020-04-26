from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
    params= {'name':'nikhil','place':'delhi'}
    return render(request,'index.html',params)
    
def anaylze(request):
    #Get Text
    djtext = request.GET.get('text','default')
    # Check checkbox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    newlineremover = request.GET.get('newlineremover','off')
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
   
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose':"New line removed",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':"New line removed",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)          
              
    else:
       return HttpResponse("Error")

def count(request):
    data = request.GET['fulltextarea']
    word_list=data.split()
    list_length=len(word_list)
    
    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':data,'words':list_length,'dict':sortedwords})



# def about(request):
#     return HttpResponse("about us")

# def removepunc(request):
#     #GET TEXT
#     djtext=request.GET.get('text','default')
#     #analyze text
#     print(djtext)
#     return HttpResponse("Remove punc")

# def capfirst(request):
#     return HttpResponse("Capitalize first ")    

# def firstlineremove(request):
#     return HttpResponse("Remove firts line")    

# def newlineremove(request):
#     return HttpResponse("Remove new line")

# def charcount(request):
#     return HttpResponse("Counting characters")

