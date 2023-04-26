from django.shortcuts import render, redirect
from .models import Kid
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def kids_index(request):
    kids = Kid.objects.filter(user=request.user)
    return render(request, 'kids/index.html', {'kids': kids})

@login_required
def kid_detail(request, kid_id):
    kid = Kid.objects.get(id=kid_id)
    feeding_form = FeedingForm()
    return render(request, 'kids/detail.html', {
        'kid': kid,
        'feeding_form': feeding_form,
    })

@login_required
def add_feeding(request, kid_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.kid_id = kid_id
        new_feeding.save()
    else:
        print(form.errors)
    return redirect('kid_detail', kid_id=kid_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('kids_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class KidCreate(LoginRequiredMixin, CreateView):
    model = Kid
    fields = ('name', 'age')
    template_name = 'kids/kid_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class KidUpdate(LoginRequiredMixin, UpdateView):
    model = Kid
    fields = '__all__'
    template_name = 'kids/kid_form.html'

class KidDelete(LoginRequiredMixin, DeleteView):
    model = Kid
    success_url = '/kids/'
    template_name = 'kids/kid_confirm_delete.html'