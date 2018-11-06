import datetime

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile, Movie


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('email',)

    username = forms.EmailField(max_length=254,
                                help_text="The person's email address.")

    def clean_email(self):
        email = self.cleaned_data['username']
        return email


class CreateProfileForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Profile
        fields = ('phone_number', 'card_number')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='', required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Firste name ..',
                                                               'id': 'searchbar'}))
    last_name = forms.CharField(max_length=30, label='', required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name  ..',
                                                              'id': 'searchbar'}))
    username = forms.EmailField(max_length=254, required=True, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Email ..',
                                                              'id': 'searchbar'}))
    password1 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password ..',
                                                                                           'id': 'searchbar'}))
    password2 = forms.CharField(label='', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation ..',
                                                                  'id': 'searchbar'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['username']
        return email


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='', required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Firste name ..',
                                                               'id': 'searchbar'}))
    last_name = forms.CharField(max_length=30, label='', required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name  ..',
                                                              'id': 'searchbar'}))
    username = forms.EmailField(max_length=254, required=False, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Email ..',
                                                              'id': 'searchbar'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['username']
        return email


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=9, min_length=9, label='', required=True,
                                   widget=forms.NumberInput(attrs={'placeholder': 'Phone number ..',
                                                                   'id': 'searchbar', }))
    card_number = forms.CharField(max_length=15, label='', required=True,
                                  widget=forms.NumberInput(attrs={'placeholder': 'Credit card number ..',
                                                                  'id': 'searchbar', }))

    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'card_number',
        )


class EditProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=9, min_length=9, label='', required=False,
                                   widget=forms.NumberInput(attrs={'placeholder': 'phone_number',
                                                                   'id': 'searchbar', }))
    card_number = forms.CharField(max_length=15, label='', required=False,
                                  widget=forms.NumberInput(attrs={'placeholder': 'Credit card number ..',
                                                                  'id': 'searchbar', }))

    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'card_number',
        )


class SearchBarForm(forms.Form):
    search = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Search ..',
                                                                                     'id': 'searchbar'}))


class SearchMovieForm(forms.Form):
    TYPE_CHOICE = (
        (0, 'Type Search ..'),
        (1, 'For a director'),
        (2, 'For a exact year'),
        (3, 'For a ragen of years'),
        (4, 'For category'),
    )
    type = forms.ChoiceField(required=False, widget=forms.Select(attrs={'id': 'select'}), choices=TYPE_CHOICE, label='',
                             initial=0, )


class SearchDirectorForm(forms.Form):
    search_director = forms.CharField(required=False, label='',
                                      widget=forms.TextInput(attrs={'placeholder': 'Director name..',
                                                                    'id': 'searchbar'}))


def year_choices():
    return [(r, r) for r in range(datetime.date.today().year, 1950, -1)]


class SearchYearExactForm(forms.Form):
    search_year_exact = forms.ChoiceField(choices=year_choices, required=False,
                                          widget=forms.Select(attrs={'onChange': 'form.submit();', 'id': 'select'}),
                                          label='')


class SearchCategoryForm(forms.Form):
    CATEGORY_CHOICE = (
        ('', 'Category ..'),
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

    search_category = forms.ChoiceField(required=False,
                                        widget=forms.Select(attrs={'onChange': 'form.submit();', 'id': 'select'}),
                                        choices=CATEGORY_CHOICE,
                                        label='')


class SearchYearForm(forms.Form):
    search_year_min = forms.ChoiceField(choices=year_choices, required=False,
                                        widget=forms.Select(attrs={'onChange': 'form.submit();', 'id': 'select'}),
                                        label='Min:')
    search_year_max = forms.ChoiceField(choices=year_choices, required=False,
                                        widget=forms.Select(attrs={'onChange': 'form.submit();', 'id': 'select'}),
                                        label='Max:')
