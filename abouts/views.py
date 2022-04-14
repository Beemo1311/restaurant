from django.shortcuts import render

from .models import AboutUs, WhyChoiceUs, Chef


def about_list(request):
    about = AboutUs.objects.all()
    why_choice_us = WhyChoiceUs.objects.all()
    chef = Chef.objects.all()
    context = {
        'about': about,
        'why_choice_us' : why_choice_us,
        'chef': chef
    }
    return render(request, 'about.html', context)