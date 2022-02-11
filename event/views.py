import json

from django.http import HttpResponse
from season.models import Season
from .models import Event
from referee.models import Referee


# Create your views here.
def get_event_url(request, user_id):
    list_events = []
    if request.user.id == user_id:
        list_events = [e.as_json(title=request.user.referee.event_text) for e in request.user.referee.get_events()]
    return HttpResponse(json.dumps(list_events))


def event_add(request):
    season = Season.objects.filter(active=True)[0]
    e = Event(start=request.GET["start"], end=request.GET["end"], user=request.user, season=season)
    e.save()
    ref = Referee.objects.get(user=request.user)
    ref.events.add(e)
    return HttpResponse("OK")


def event_remove(request):
    season = Season.objects.filter(active=True)[0]
    e = Event.objects.get(start=request.GET["start"], end=request.GET["end"], user=request.user, season=season)
    ref = Referee.objects.get(user=request.user)
    ref.events.remove(e)
    e.delete()
    return HttpResponse("OK")
