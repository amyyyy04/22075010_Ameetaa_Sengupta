from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
from .utils import generate_unique_short_code
from .forms import ShortenURLForm
from django.shortcuts import get_object_or_404

def shorten_url(request):
    form = ShortenURLForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        long_url = form.cleaned_data['long_url']
        
        existing_url_object = URL.objects.filter(long_url=long_url).first()
        if existing_url_object:
            short_code = existing_url_object.short_code
        else:
            short_code = generate_unique_short_code()
            URL.objects.create(long_url=long_url, short_code=short_code)
        
        short_url = request.build_absolute_uri(f'/{short_code}') 
        return render(request, 'urlshortener_app/shorten_url.html', {'short_url': short_url, 'short_code': short_code})

    return render(request, 'urlshortener_app/shorten_url.html', {'form': form})


def redirect_to_original_url(request, short_code):
    url_object = get_object_or_404(URL, short_code=short_code)
    return redirect(url_object.long_url)

def short_url_list(request):
    urls = URL.objects.all()
    return render(request, 'urlshortener_app/short_url_list.html', {'urls': urls})