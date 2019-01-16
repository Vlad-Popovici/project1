from django.shortcuts import render

#Create views here:

def animal_detail_view(request):
    context = {}
    return render(request, 'animal_detail.html', context)

