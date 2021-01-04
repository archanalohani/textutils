from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def ex1(request):
    sites=[''' <h1>for Entertainment </h1><a href=https://www.youtube.com >youtube video</a>'''
           ''' <h1>for Interaction <h1><a href="https://wwww.facebook</a>  '''
           ''' <h1>for insight</h1><a href="https://www.ted.com/talks</a>'''
           ''' <h1>for internship</h1>href="https://intershala.com">Internship</a>'''
          ]

    return HttpResponse((sites))



def analyze(request):
#get the first text
    djtext = request.GET.get('text', 'default')

    #check checkbox values

    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover','off')

#check which checkbox is on

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, ' .html', params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n":
               analyzed=analyzed+char
               params={'purpose':'RemoveNewLine','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('Error')