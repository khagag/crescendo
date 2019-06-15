from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# from .forms import RegistForm

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
def index(request):
    # RForm = RegistForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     RForm = RegistForm()
    context={
        # 'RForm': RForm,
    }
    return render(request, 'music_blog/index.html', context)

def admin_index(request):
    context={}
    return render(request,'music_blog/admin_index.html')
