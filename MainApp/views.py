import os.path

from django.core.paginator import Paginator
from django.shortcuts import render
import json

json_path = '/home/artic/Denis/country-json1/country-by-languages.json'
if os.path.isfile(json_path):
    with open('/home/artic/Denis/country-json1/country-by-languages.json') as file:
        country_bd = json.load(file)
else:
    with open('/app/country-json1/country-by-languages.json') as file:
        country_bd = json.load(file)



primer = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y'


def iam(request):
    return render(request, 'html/iam.html')


def country(request):
    masiv = []
    for item in country_bd:
        masiv.append(item['country'])
    paginator = Paginator(masiv, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/country.html', {'masiv': page_obj, 'primer': primer})


def language(request):
    masiv = []
    for item in country_bd:
        for item2 in item['languages']:
            if item2 not in masiv:
                masiv.append(item2)
    masiv = sorted(masiv)
    paginator = Paginator(masiv, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/language.html', {'masiv': page_obj, 'primer': primer})


def country_max(request, id):
    masiv = []; last = ''
    if id not in primer:
        for item in country_bd:
            if item['country'] == id:
                masiv = item['languages']
                last = item['country']
                break
        return render(request, 'html/country_max.html', {'masiv': masiv, 'primer': primer, 'last': last})
    else:
        for item in country_bd:
            if item['country'][0] == id:
                masiv.append(item['country'])
        paginator = Paginator(masiv, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/country.html', {'masiv': page_obj, 'primer': primer})


def language_max(request, id):
    masiv = []
    if id in primer:
        for item in country_bd:
            for item2 in item['languages']:
                if item2 not in masiv and item2[0] == id:
                    masiv.append(item2)
        masiv = sorted(masiv)
        paginator = Paginator(masiv, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'html/language.html', {'masiv': page_obj, 'primer': primer})
    else:
        for item in country_bd:
            if id in item['languages']:
                masiv.append(item['country'])
        masiv = sorted(masiv)
        return render(request, 'html/language_max.html', {'masiv': masiv, 'primer': primer, 'last': id})



