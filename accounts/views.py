from django.shortcuts import render,redirect
from .models import Profile
from .forms import SignUpForm,ProfileForm,UserForm
from django.contrib.auth import authenticate, login
# Create your views here.

def sign_up(request):
    if request.method == 'POST' : #save SignUpForm
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('/accounts/profile')

    else : #show  SignUpForm
        form = SignUpForm()
    context = {'form':form}
    return render(request,'registration/signup.html',context)



def profile(request):

    profile = Profile.objects.get(user = request.user)

    return render(request,'profile/profile.html',{'profile':profile})


def profile_edit(request):

    profile = Profile.objects.get(user = request.user)


    if request.method == 'POST':
        userform = UserForm(request.POST,instance =request.user)
        profileform = ProfileForm(request.POST,instance =profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()

            myform = profileform.save(commit = False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')

    else :
        userform = UserForm(instance = request.user)
        profileform = ProfileForm(instance = profile)

    return render(request,'profile/profile_edit.html',
    {'userform':userform,
    'profileform':profileform
    })

