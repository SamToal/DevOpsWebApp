from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm, HomeDetailsForm, VacantHomesForm
from . models import Home, VacantHome
import datetime
import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "myapp/index.html", {})


def login(request):
    return render(request, 'myapp/login.html', {})


# Function for creating homes
def createhome(request):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # If user is logged in displays the create home form
    if request.method == "POST":
        form = HomeDetailsForm(request.POST)
        # If the form is valid saves it to the database as a new home and displays the user a success message
        if form.is_valid():
            form.save()
            messages.success(request, f'Home account created successfully!')
            return redirect('../homeslist/')
    else:
        # If the form isn't valid resets the form and logs an error
        logger.warning('Error with Home Creation at ' + str(datetime.datetime.now()) + ' hours!')
        form = HomeDetailsForm()
    return render(request, 'myapp/createhome.html', {'form': form})


# Function for editing homes
def edithome(request, id):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Gets the details of the selected home to fill the form
    home = get_object_or_404(Home, id=id)

    if request.method == 'GET':
        context = {'form': HomeDetailsForm(instance=home), 'id': id}
        return render(request, 'myapp/edithome.html', context)

    elif request.method == 'POST':
        # Saved the updated home and posts a success message
        form = HomeDetailsForm(request.POST, instance=home)
        if form.is_valid():
            form.save()
            messages.success(request, 'The home has been updated successfully.')
            return redirect('/homeslist/')
        else:
            # Logs and displays any error with the form
            logger.warning('Error with Home Editing at ' + str(datetime.datetime.now()) + ' hours!')
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'myapp/edithome.html', {'form': form})


# Function for deleting homes
def deletehome(request, homeid):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Deletes the home and shows a success message to the user
    Home.objects.get(id=homeid).delete()
    messages.success(request, 'The home has been deleted successfully.')
    return redirect('/homeslist/')


# Function for creating vacant homes
def createvacanthome(request):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    if request.method == "POST":
        form = VacantHomesForm(request.POST)
        # If the form is valid saves it to the database as a new home and displays the user a success message
        if form.is_valid():
            form.save()
            messages.success(request, f'Vacant Home account created successfully!')
            return redirect('../vacanthomelist/')

    else:
        # If the form isn't valid resets the form and logs an error
        logger.warning('Error with Vacant Home Creation at ' + str(datetime.datetime.now()) + ' hours!')
        form = VacantHomesForm()
    return render(request, 'myapp/createvacanthome.html', {'form': form})


# Function for editing vacant homes
def editvacanthome(request, id):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Gets the details of the selected home to fill the form
    vacanthome = get_object_or_404(VacantHome, id=id)

    if request.method == 'GET':
        context = {'form': VacantHomesForm(instance=vacanthome), 'id': id}
        return render(request, 'myapp/editvacanthome.html', context)

    elif request.method == 'POST':
        # Saved the updated home and posts a success message
        form = VacantHomesForm(request.POST, instance=vacanthome)
        if form.is_valid():
            form.save()
            messages.success(request, 'The home has been updated successfully.')
            return redirect('/vacanthomelist/')
        else:
            # Logs and displays any error with the form
            logger.warning('Error with Vacant Home Editing at ' + str(datetime.datetime.now()) + ' hours!')
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'myapp/editvacanthome.html', {'form': form})


# Function for deleting vacant homes
def deletevacanthome(request, homeid):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Deletes a vacant home and shows the user a success message
    VacantHome.objects.get(id=homeid).delete()
    messages.success(request, 'The home has been deleted successfully.')
    return redirect('/vacanthomelist/')


# Function for viewing list of homes
def homeslist(request):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Displays all homes
    home = Home.objects.all()
    return render(request, 'myapp/homeslist.html', {'home': home})


# Function for viewing list of vacant homes
def vacanthomelist(request):
    # Checks that the user is logged in and if not redirects to login page
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Log In or Create Account to view this page.')
        return redirect('/login/')
    # Displays all vacant homes
    vacanthome = VacantHome.objects.all()
    return render(request, 'myapp/vacanthomes.html', {'vacanthome': vacanthome})


# Function for registering a new user
def register(request):
    # Sets up registration form
    form = UserRegisterForm(request.POST)
    # If form is valid saves to create a user, shows a success message, and redirects to login page
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}, your account was created successfully! Please now Log In.')
            return redirect('../login/')
    else:
        # Logs and displays any error with the form
        logger.warning('Error with Registration at ' + str(datetime.datetime.now()) + ' hours!')
        messages.error(request, 'Please correct the following errors:')
        form = UserRegisterForm()

    return render(request, 'myapp/register.html', {'form': form})
