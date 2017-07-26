from django.shortcuts import render


def event_list(request):
    events= Event.objects.all()
    return render (request,'event/list.html' , {'events':events})
