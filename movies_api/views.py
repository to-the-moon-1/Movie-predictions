import json
import pickle
import pandas as pd
from urllib.parse import unquote
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from movies_api.forms import MoviesForm
from movies_api.models import Movies
from movies_prediction.settings import BASE_DIR


model_path = str(BASE_DIR) + '/movies_api/static/model.pkl'


def index_view(request):
    form = MoviesForm()
    data = Movies.objects.all()
    return render(request, 'movies.html', {'form': form, 'data': data})


def movies_data(request):
    if request.method == 'POST':
        encode_data = request.POST.get('form_data')
        decode_data = unquote(encode_data)

        df = preparation(decode_data)

        result = predict(df)
        prediction = ''

        if result == 0:
            prediction = 'is not recommended'
        elif result == 1:
            prediction = 'is recommended'

        return HttpResponse(
            json.dumps(prediction, default=str),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def preparation(data):
    arr_data = data.split('&')

    nested_arr_data = []

    for i in arr_data:
        nested_arr_data.append(i.split('='))

    df = pd.DataFrame()

    genres = ['action', 'adventure', 'sci_fi', 'fantasy', 'western', 'drama', 'horror', 'romance', 'mystery',
              'crime']
    studios = ['disney', 'marvel', 'netflix', 'other']

    active_genres = []
    ind_genres = []

    for i in nested_arr_data:
        for j in i:
            if j == 'genre':
                active_genres.append(i[1])
                ind_genres.append(nested_arr_data.index(i))

    if len(ind_genres) > 1:
        del nested_arr_data[ind_genres[0]:ind_genres[-1]]

    for i in nested_arr_data:
        if i[0] == 'name':
            df[i[0]] = [i[1]]
        elif i[0] == 'studio':
            for j in studios:
                if j == i[1]:
                    df[i[1]] = 1
                else:
                    df[j] = 0
        elif i[0] == 'genre':
            for j in genres:
                if j in active_genres:
                    df[j] = 1
                else:
                    df[j] = 0
        elif i[0] == 'metascore' or i[0] == 'tomatometer':
            if int(i[1]) > 55:
                df[i[0]] = 1
            else:
                df[i[0]] = 0
        elif i[0] == 'audience_score' or i[0] == 'liked_this_film':
            if int(i[1]) > 65:
                df[i[0]] = 1
            else:
                df[i[0]] = 0
        elif i[0] == 'imdb' or i[0] == 'user_score':
            if float(i[1]) > 6:
                df[i[0]] = 1
            else:
                df[i[0]] = 0
        elif i[0] == 'audience_rating_summary':
            if float(i[1]) > 3:
                df[i[0]] = 1
            else:
                df[i[0]] = 0
        elif i[0] == 'budget' or i[0] == 'box_office':
            if i[1] == '':
                df[i[0]] = 0
            else:
                df[i[0]] = float(i[1])
        else:
            df[i[0]] = i[1]

    return df


def predict(df):
    df['roi'] = df['box_office'] - df['budget']
    df['roi'] = df['roi'].apply(lambda x: round(x))

    df['actors'] = df['actors'].apply(lambda x: int(x))

    df.drop(['name', 'crime', 'budget', 'box_office'], axis=1, inplace=True)

    try:
        model = pickle.load(open(model_path, 'rb'))
        prediction = model.predict(df)

        return prediction

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
