from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Option, Select

def home(request):
    return render(request , "poll_frontend/home.html")
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll_frontend/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll_frontend/poll_detail.html', {'poll': poll})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    option_id = request.POST.get('option')
    if option_id:
        option = get_object_or_404(Option, id=option_id, poll=poll)
        Select.objects.create(user=request.user, option=option)
        return redirect('poll_detail', poll_id=poll_id)
    return render(request, 'poll_frontend/poll_detail.html', {'poll': poll, 'error': 'You didn\'t select a choice.'})
