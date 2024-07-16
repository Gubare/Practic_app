import os.path
import random
import webbrowser
from django.core.paginator import Paginator
from django.shortcuts import render
import json


current_dir = os.path.dirname(os.path.abspath(__file__))
json_base_path = os.path.join(current_dir, 'country-by-languages.json')
with open(json_base_path) as json_file:
    country_bd = json.load(json_file)
# кодировка ЮТФ-8, тк в джисоне есть русские слова
json_info_path = os.path.join(current_dir, 'country_info.json')
with open(json_info_path, encoding="UTF-8") as json_info:
    info_db = json.load(json_info)


primer = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'


def iam(request):
    country_list = []
    for unit in info_db:
        country_list.append(unit['name'])
    main_unit = random.choice(country_list)
    for info in info_db:
        if main_unit == info['name']:
            full_name = info['english']
            short_name = info['alpha2'].lower()

    flag_path = os.path.join(current_dir, f'static\\{short_name}.webp')
    # os.startfile(flag_path)
    # webbrowser.open(current_dir, f'static/{short_name}')
    return render(request, 'html/iam.html',
                  {"unit": main_unit, "short": short_name, "full": full_name, "link": flag_path})


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

        for unit in info_db:
            if last == unit['english']:
                link = unit['alpha2'].lower()
                break
        return render(request, 'html/country_max.html',
                      {'masiv': masiv, 'primer': primer, 'last': last, 'link': link})
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



