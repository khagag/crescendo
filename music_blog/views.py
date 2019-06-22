from django.http import Http404
from django.shortcuts import (
                                render ,
                                redirect,
                                get_object_or_404,
                                )
from django.urls import reverse_lazy
from django.views import generic
from .forms import (
                        UserForm ,
                        UserInfoForm,
                        CustomUserChangeForm
                        )
from pprint import pprint
from django.contrib.auth.models import User

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from music_blog import models

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationFor
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def index(request):
    context={
    }

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        # profile_form = UserInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() :#and profile_form.is_valid()

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            # user.set_password(user.password)
            # print(" ")
            # Update with Hashed password
            user.save()
            print("saved : ",user.first_name)
            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            # profile = profile_form.save()
            # profile = profile_form.save(commit=False)
            # userInfo = models.UserInfo.objects.get(pk=user.pk)
            # userInfo.profile_pic = request.FILES['profile_pic']
            # userInfo.save(['profile_pic'])
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            # profile.user = user.id

            # Check if they provided a profile picture
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     # If yes, then grab it from the POST form reply
            #     profile.profile_pic = request.FILES['profile_pic']
            #
            # # Now save model
            # profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserInfoForm()
    user_data=object()
    if request.user.is_authenticated :
        user = models.User.objects.get(pk=request.user.pk)
        user_data = models.UserInfo.objects.get(user=user)
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    # print(type(user_data))
    # print(user_data)
    return render(request,'music_blog/index.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'user':request.user,
                           'user_data':user_data
                           })
    # return render(request, 'music_blog/index.html', context)'pic':user_data.profile_pic


@login_required
def adminstration(request):

    user_data=object()
    if request.user.is_authenticated :
        # print(request.user.pk)
        user = models.User.objects.get(pk=request.user.pk)
        # print(user)
        # pprint(user)
        user_data = models.UserInfo.objects.get(user=user)
        # user_data = user.UserInfo
        # user_data = models.UserInfo.objects.get(pk=request.user.id)#models.UserInfo.objects.get(pk=request.user.pk)


        # user_data = models.UserInfo.objects.get(id=request.user.pk)
    # print(request.user.UserInfo.profile_pic)
    # print(type(user_data))
    # # print(dir(user_data.objects))
    # print(dir(user_data))
    # print("profile Pic :",user_data.profile_pic)
    # pprint(user_data)
    context={'user':request.user,
             'user_data':user_data}
    # {'user':request.user}
    return render(request,'music_blog/admin/index.html',context)

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    print("text")
    return HttpResponseRedirect(reverse('index'))

from django.contrib.auth.forms import UserChangeForm
@login_required
def profile_settings(request,*args,**kwargs):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # return redirect(reverse('music_blog:settings'))
        context = {
            'user':request.user,
            'form':form
            ## TODO: add a state to add a notification about the process status
        }
        return render(request,'music_blog/admin/settings.html',context)
        # return redirect('/settings')
    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'user':request.user,
            'form':form
        }
        return render(request,'music_blog/admin/settings.html',context)

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user is not None:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'music_blog/index.html', {})

def admin_index(request):
    user_data=object()
    if request.user.is_authenticated :
        user_data = models.UserInfo.objects.get(id=request.user.id)
    context={'user_data':user_data}
    return render(request,'music_blog/admin_index.html',context)

def regist(request):
    context={}
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'music_blog/reg.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
    # return render(request,'music_blog/reg.html')
# def user_is_not_logged_in(user):
#     return not user.is_authenticated()

# @user_passes_test(user_is_not_logged_in, login_url='/')
def social_user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user is not None:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'music_blog/admin/login.html', {})


# the profile of the composer_profile
def composer_profile(request,composer_id):
    composer = get_object_or_404(models.composer,pk=composer_id)
    context ={
        'user':request.user,
        'composer': composer
    }
    return render(request,'music_blog/composer.html',context)

def musical_pieces_settings(request):
    context={
        'user':request.user,

    }
    return render(request,'music_blog/admin/songs_upload.html',context)
