from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import EditProfileForm, SearchMovieForm, SearchBarForm, SearchMovieForm, \
    SignUpForm, SearchDirectorForm, SearchYearExactForm, SearchYearForm, SearchCategoryForm, ProfileForm, EditUserForm
from accounts.models import Profile, Movie


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form_info = ProfileForm(request.POST)
        if form.is_valid():
            email = form.clean_email()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
        form_info = ProfileForm()
    return render(request, 'signup.html', {'form': form, 'form_info': form_info})


def delete_user(request):
    user = User.objects.get(pk=request.user.pk)
    user.delete()
    messages.success(request, "The user is deleted")

    return redirect('home')


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('profile'))
    else:
        user = request.user
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        args = {
                'user_form': user_form,
                'profile_form': profile_form}
        return render(request, 'editprofile.html', args)


def view_list_movies(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'my_movie_list.html', args)


def search_bar(request, pk=None):
    form = SearchBarForm(request.GET)
    movies = list()
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    if form.is_valid():
        if form.cleaned_data['search']:
            movies = Movie.objects.filter(title__icontains=form.data['search'])

    usermovies = user.profile.movie_list.all()

    args = {'form': form, 'movies': movies, 'usermovies': usermovies}

    return render(request, 'search_bar.html', args)


def searche_director(request, pk=None):
    form = SearchDirectorForm(request.GET)
    movies = {}
    if form.is_valid():
        if form.cleaned_data['search_director']:
            movies = Movie.objects.filter(director__icontains=form.data['search_director'])

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    usermovies = user.profile.movie_list.all()

    args = {'form': form, 'movies': movies, 'usermovies': usermovies}
    return render(request, 'search_movie.html', args)


def searche_year_exact(request, pk=None):
    form = SearchYearExactForm(request.GET)
    movies = {}
    if form.is_valid():
        if form.cleaned_data['search_year_exact']:
            movies = Movie.objects.filter(year__exact=form.cleaned_data['search_year_exact'])

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    usermovies = user.profile.movie_list.all()

    args = {'form': form, 'movies': movies, 'usermovies': usermovies}
    return render(request, 'search_movie.html', args)


def searche_year(request, pk=None):
    form = SearchYearForm(request.GET)
    movies = {}
    if form.is_valid():
        if form.cleaned_data['search_year_min'] and form.cleaned_data['search_year_max']:
            movies = Movie.objects.filter(year__gte=form.cleaned_data['search_year_min'],
                                          year__lte=form.cleaned_data['search_year_max'])

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    usermovies = user.profile.movie_list.all()

    args = {'form': form, 'movies': movies, 'usermovies': usermovies}
    return render(request, 'search_movie.html', args)


def searche_catgegory(request, pk=None):
    form = SearchCategoryForm(request.GET)
    movies = {}
    if form.is_valid():
        if form.cleaned_data['search_category']:
            movies = Movie.objects.filter(category__exact=form.cleaned_data['search_category'])

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    usermovies = user.profile.movie_list.all()

    args = {'form': form, 'movies': movies, 'usermovies': usermovies}
    return render(request, 'search_movie.html', args)


def search_movies(request):
    form = {}
    print(request.method)

    if request.method == 'POST':
        type = request.POST['type']
        print(type)

        if type == '1':
            return redirect('searchdirector')

        if type == '2':
            return redirect('searchyearexact')

        if type == '3':
            return redirect('searchyear')

        if type == '4':
            return redirect('searchcategory')

    else:
        args = {'form': form}
        return render(request, 'search_movie.html', args)


def suggested_movies(request, pk=None):
    aux_movies = Movie.objects.all()
    list_c = list()
    i = 0
    for m in aux_movies:
        list_c.append([User.objects.filter(profile__movie_list=m).count(), i])
        i += 1

    list_c.sort()
    list_c.reverse()
    movies = list()
    for a, b in list_c:
        movies.append(aux_movies[b])

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user, 'movies': movies}

    return render(request, 'recommends.html', args)


def delete_movie(request, id=None):
    user = request.user
    movie = Movie.objects.get(id=id)
    user.profile.movie_list.remove(movie)

    path = request.META.get('HTTP_REFERER')

    return redirect(path)


def add_movie(request, id=None):
    user = request.user
    movie = Movie.objects.get(id=id)
    user.profile.movie_list.add(movie)

    path = request.META.get('HTTP_REFERER')

    return redirect(path)
