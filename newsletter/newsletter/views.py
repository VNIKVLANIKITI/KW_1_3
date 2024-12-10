from django.shortcuts import render


def health_check(request):
    #return HttpResponse("service general is alive")
    return render(request, 'letters/general_page.html')
