from django.shortcuts import render, get_object_or_404
from apps.ministries.models import Ministries


def ministries_list(request):
    ministries = Ministries.objects.all()
    return render(request, "events/ministries_list.html", {"ministries": ministries})


def ministry_detail(request,ministry_id):
    ministry = get_object_or_404(Ministries,id=ministry_id)
    goals = ministry.goals.all()
    return render(request,'events/ministry_detail.html',{"ministry":ministry,"goals":goals})
