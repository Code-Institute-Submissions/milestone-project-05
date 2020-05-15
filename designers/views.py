from django.shortcuts import render
from profiles.models import RegisteredUserProfile
# from django.contrib.auth.models import User

from prints.models import Print


# Create your views here.

def all_designers(request):
    """ A view to return the all designers page """
    checked_designers = []
    all_designers = RegisteredUserProfile.objects.all()
    for designer in all_designers:
        complete = all([designer.first_name,
                        designer.last_name,
                        designer.bio,
                        designer.country,
                        designer.register_as_designer])
        if complete:
            checked_designers.append(designer)
    context = {
        'designers': checked_designers,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def individual_designer(request, designer_id):
    """ A view to return a page focusing on 1 x designer """
    the_designer = RegisteredUserProfile.objects.get(id=designer_id)
    the_designers_prints = Print.objects.filter(designer_id=the_designer)

    context = {
        'the_designer': the_designer,
        'prints': the_designers_prints,
    }

    return render(request,
                  'designers/individual_designer.html',
                  context)
