from django import forms
from movies_api.models import Movies
from movies_api.form_options import GENRE_OPTIONS, STUDIO_OPTIONS, ACTORS_OPTIONS


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

    name = forms.CharField(label='Title', max_length=55,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
    genre = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-size': '5', 'data-max-options': '3'}),
        choices=GENRE_OPTIONS)
    studio = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selectpicker'}), choices=STUDIO_OPTIONS)
    actors = forms.ChoiceField(widget=forms.RadioSelect, choices=ACTORS_OPTIONS)
    imdb = forms.FloatField(label='IMDb', max_value=10, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Enter IMDb rating'}))

    metascore = forms.IntegerField(max_value=100, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter metascore'}))
    user_score = forms.FloatField(max_value=10, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Enter user score'}))

    tomatometer = forms.IntegerField(max_value=100, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter tomatometer'}))
    audience_score = forms.IntegerField(max_value=100, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter audience score'}))

    liked_this_film = forms.IntegerField(max_value=100, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Google liked'}))
    audience_rating_summary = forms.FloatField(max_value=5, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Enter Google rating'}))

    budget = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter budget'}),
                              required=False)
    box_office = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter box office'}), required=False)
