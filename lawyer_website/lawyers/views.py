from django.shortcuts import render, get_object_or_404
from .models import Lawyer


def lawyer_list(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'lawyers/lawyer_list.html', {'lawyers': lawyers})


def lawyer_detail(request, pk):
    lawyer = get_object_or_404(Lawyer, pk=pk)
    return render(request, 'lawyers/lawyer_detail.html', {'lawyer': lawyer})

