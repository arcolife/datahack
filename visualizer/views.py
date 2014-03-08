# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def mortality(request):
    if request.method == 'GET':
        return render_to_response('heatmap.html', {})
        #return render('heatmap.html',{} ,request)
    else:
        return HttpResponse('Mortal mar gaya..')

def visualizer(request):
    if request.method == 'GET':
        return render_to_response('index.html', {})
        #return render('index.html', {},request)
    else:
        return HttpResponse('POST not allowed!')
