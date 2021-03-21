from django.shortcuts import render
from .models import Services, TeamMember

# Create your views here.
def index(request):
    services = Services.objects.all()
    team_member = TeamMember.objects.all()
    context = {
        'services': services,
        'team_member': team_member
    }

    return render(request, 'index.html', context)
    