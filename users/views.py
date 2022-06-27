from multiprocessing import context
from django.shortcuts import get_object_or_404, render

from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    top_skills = profile.skill_set.exclude(description__exact="") #exclude the empty description
    other_skills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'top_skills':top_skills, 'other_skills':other_skills}
    return render(request, 'users/user-profile.html', context)
