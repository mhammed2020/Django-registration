from django.shortcuts import render,redirect
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
# Create your views here.

def sign_up(request):
    if request.method == 'POST' : #save form
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)

            return redirect('/accounts/profile')




    else : #show form SignUpForm
        form = SignUpForm()
    context = {'form':form}
    return render(request,'registration/signup.html',context)



def profile(request):

    profile = Profile.objects.get(user = request.user)

    return render(request,'profile/profile.html',{'profile':profile})




def profile_edit(request):

    return render(request,'profile/profile_edit.html',{'profile':profile})

