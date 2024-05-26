from django.shortcuts import render, get_object_or_404
from . import models as m, forms as f


def error_404(request, exception):
    return render(request, '404.html')


def main(request):
    books = m.Book.objects.all()
    modules = m.Module.objects.filter(page=m.Module.PAGES[0][1])
    slider = m.Slider.objects.filter(page=m.Slider.PAGES[0][1]).first()

    return render(request, 'index.html', {'books': books, 'modules': modules, 'slider': slider})


def institute(request):
    modules = m.Module.objects.filter(page=m.Module.PAGES[1][1])
    slider = m.Slider.objects.filter(page=m.Slider.PAGES[1][1]).first()
    return render(request, 'institute.html', {'modules': modules, 'slider': slider})


def about(request):
    if request.method == 'POST':
        form = f.MessageForm(request.POST)
        if form.is_valid():
            form.save()

    review_form = f.MessageForm()
    return render(request, 'about.html', {'form': review_form})
