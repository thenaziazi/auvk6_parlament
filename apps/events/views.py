from datetime import date
from django.shortcuts import get_object_or_404,render

from apps.events.models import Events, EventsToOrganize
from apps.ministries.models import Ministries,MinistryGoals
from apps.users.models import CustomUser



def index(request):
    events = Events.objects.all()[:6]
    return render(request, "index.html", {"events": events})


def events_list_public(request):
    events = Events.objects.all()
    return render(request, "events/events_list_public.html", {"events": events})


def event_detail_public(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    return render(request,"events/event_detail_public.html",{"event": event})


def archive_list(request):
    events = Events.objects.all()
    return render(request, "events/archive_list.html", {"events": events})


def archive_detail(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    return render(request, "events/archive_detail.html", {"event": event})


def year_plan(request):
    events = EventsToOrganize.objects.all().order_by("date", "-created_at")
    return render(request, "events/year_plan.html", {"events": events})


def ministries_list(request):
    ministries = Ministries.objects.all()
    return render(request, "events/ministries_list.html", {"ministries": ministries})


def ministry_detail(request,ministry_id):
    ministry = get_object_or_404(Ministries,id=ministry_id)
    goals = ministry.goals.all()
    return render(request,'events/ministry_detail.html',{"ministry":ministry,"goals":goals})


