from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile, Movie

class CreateProfileForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Profile
        fields = ('phone_number', 'card_number')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email')
        exclude = ('password',)


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'card_number',
        )


class SearchBarForm(forms.Form):
    search = forms.CharField(required=False, label="",  widget=forms.TextInput(attrs={'placeholder': 'Search ..',
                                                                                      'id': 'searchbar'}))


class SearchMovieFormAux(forms.Form):
    TYPE_CHOICE = (
        (1, 'For a director'),
        (2, 'For a exact year'),
        (3, 'For a ragen of years'),
        (4, 'For category'),
    )
    type = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=TYPE_CHOICE, label='Type search')


class SearchMovieForm(forms.Form):

    CATEGORY_CHOICE = (
        ('', '----'),
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('FANTASY', 'Fantasy'),
        ('HISTORY', 'History'),
        ('MYSTERY', 'Mystery'),
        ('ROMANCE', 'Romance'),
        ('SCIENCE FICTION', 'Science fiction)'),
        ('THRILLER', 'Thriller'),
    )

    search_director = forms.CharField(required=False, label='Search director',  widget=forms.TextInput(attrs={'placeholder' : 'Director name..'}))

    search_year_exact = forms.IntegerField(required=False, label='Search year (exact match)!')
    search_year_min = forms.IntegerField(required=False, label='Min year')
    search_year_max = forms.IntegerField(required=False, label='Max year')

    search_category = forms.ChoiceField(required=False, widget=forms.Select, choices=CATEGORY_CHOICE, label='Search category')
