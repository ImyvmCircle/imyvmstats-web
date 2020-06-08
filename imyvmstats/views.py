import json
import os
import uuid
from datetime import datetime
from fnmatch import filter
from os.path import join

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from imyvmstats.forms import LogMessageForm
from imyvmstats.models import EcoAccounts, Eventlog
from imyvmstats.utils.playerdata import playersData
from web_project.settings import STATIC_ROOT

# global
try:
    with open(os.path.join(STATIC_ROOT, 'latest.json'), 'r') as f:
        playersInfo = json.load(f)
except:
    playersInfo = list()

def playerinfos(request):
    InfobylastPlayed = sorted(playersInfo, key=lambda k: k.get('lastPlayed', 0), reverse=True)
    paginator = Paginator(InfobylastPlayed, 20) # Show 15 players per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'imyvmstats/about.html', {'page_obj': page_obj})
    

def accountDetail(request):
    details = Eventlog.objects.using('imyvmServer').filter(uuid=request.GET.get('uuid')).order_by('-eventtime')
    paginator = Paginator(details, 20) # Show 15 players per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'imyvmstats/accountDetail.html', {'page_obj': page_obj, 'uuid':request.GET.get('uuid')})

def accountListing(request):
    players = EcoAccounts.objects.using('imyvmServer').order_by("-money")
    paginator = Paginator(players, 20) # Show 15 players per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'imyvmstats/home.html', {'page_obj': page_obj})

# def about(request):
#     return render(request, "imyvmstats/about.html")

def contact(request):
    return render(request, "imyvmstats/contact.html")

@login_required(login_url='/admin/')
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        playersdata = playersData()
        with open(os.path.join(STATIC_ROOT, 'latest.json'), 'w') as fp:
            json.dump(
                playersdata.players, 
                fp, 
                indent=1, 
                cls=DjangoJSONEncoder)
        # if form.is_valid():
        #     message = form.save(commit=False)
        #     message.log_date = datetime.now()
        #     message.save()
        return redirect("home")
    else:
        return render(request, "imyvmstats/log_message.html", {"form": form})

def imyvmstats_there(request, name):
    return render(
        request,
        'imyvmstats/imyvmstats_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )