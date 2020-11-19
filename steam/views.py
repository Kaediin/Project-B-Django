import json
import os

from django.shortcuts import render

# Create your views here.
keys = [
    'appid',
    'name',
    'release_date',
    'english',
    'developer',
    'publisher',
    'platforms',
    'required_age',
    'categories',
    'genres',
    'steamspy_tags',
    'achievements',
    'positive_ratings',
    'negative_ratings',
    'average_playtime',
    'median_playtime',
    'owners',
    'price'
]

with open(os.path.abspath('steam.json'), 'r') as f:
    jsonData = json.load(f)


# Sorteer een gegeven list van dicts op basis van een gegeven key (string).
# Returns: gesorteerde list van dicts
def sort(data_list, key):
    data_list.sort(key=lambda e: e[key])
    return data_list


def index(request):
    return render(request, 'index.html', {
        'keys': keys,
        'data': json.dumps(jsonData, indent=4),
        'filter': 'none'
    })


def filter(request):
    key = request.GET.get('key')
    data = sort(jsonData, key)
    value = keys.index(key)

    return render(request, 'index.html', {
        'keys': keys,
        'data': json.dumps(data, indent=4),
        'filter': key,
        'option_value': value
    })
