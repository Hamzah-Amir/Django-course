from django.shortcuts import render
from django.http import HttpResponse
import string

def index(request):
    return render(request, 'home.html')

def analyze(request):
    # Get the text and options from the request
    text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalizefirst = request.GET.get('capitalizefirst', 'off')
    charcount = request.GET.get('charcount', 'off')

    # Remove punctuation
    punctuations = string.punctuation
    analyzed = ''
    purpose = 'None'
    if removepunc == 'on':
        purpose = "Removed Punctuations"
        for char in text:
            if char not in punctuations:
                analyzed += char
    elif capitalizefirst == 'on':
        purpose = "Capitalized First Letter"
        if len(text) > 0:
            analyzed = text[0].upper() + text[1:]
        else:
            analyzed = text
    elif charcount == 'on':
        purpose = "Character Count"
        analyzed = str(len(text))
    params = {'purpose': purpose, 'preanalyzed_text': text, 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)