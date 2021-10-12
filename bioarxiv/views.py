from django.shortcuts import render
from .models import Paper

def paper_list(request):
    papers = Paper.objects.all()
    return render(request,
                  'bioarxiv/paper/list.html',
                  {'papers': papers})
