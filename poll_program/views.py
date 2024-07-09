from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Option, Select

def home(request):
    """
    Render the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request , "poll_frontend/home.html")

def poll_list(request):
    """
    Render a list of all polls.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered poll list page with all polls.
    """
    polls = Poll.objects.all()
    return render(request, 'poll_frontend/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    """
    Render the details of a specific poll.

    Args:
        request (HttpRequest): The request object.
        poll_id (int): The id of the poll.

    Returns:
        HttpResponse: The rendered poll detail page with the specified poll.
    """
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll_frontend/poll_detail.html', {'poll': poll})

@login_required
def vote(request, poll_id):
    """
    Handle voting for a specific poll.

    Args:
        request (HttpRequest): The request object.
        poll_id (int): The id of the poll.

    Returns:
        HttpResponse: Redirects to the poll detail page if the vote is successful,
                      otherwise renders the poll detail page with an error message.
    """
    poll = get_object_or_404(Poll, id=poll_id)
    option_id = request.POST.get('option')
    if option_id:
        option = get_object_or_404(Option, id=option_id, poll=poll)
        Select.objects.create(user=request.user, option=option)
        return redirect('poll_detail', poll_id=poll_id)
    return render(request, 'poll_frontend/poll_detail.html', {'poll': poll, 'error': 'You didn\'t select a choice.'})
