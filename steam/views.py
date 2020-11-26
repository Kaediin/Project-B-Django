import json
import os

from django.shortcuts import render

# Create your views here.

# Define all the keys to filer on
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

# open thhe file and load it into JSON
with open(os.path.abspath('steam.json'), 'r') as f:
    jsonData = json.load(f)


# Sorteer een gegeven list van dicts op basis van een gegeven key (string).
# Returns: gesorteerde list van dicts
def sort(data_list, key):
    data_list.sort(key=lambda e: e[key])
    return data_list


# Runs on startup and loads the template (unfiltered)
def index(request):

    # Render template and pass the values on onto it
    return render(request, 'index.html', {
        'keys': keys,
        'data': jsonData,
        'filter': 'none'
    })

# Handles the filter request
def filter(request):
    # Retrieve the key from the view
    key = request.GET.get('key')

    # Sort the data with the key
    data = sort(jsonData, key)

    # Retrieve the key index value
    value = keys.index(key)

    # Render template and pass the values on onto it
    return render(request, 'index.html', {
        'keys': keys,
        'data': data,
        'filter': key,
        'option_value': value
    })