from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import UserRegistrationCreateForm
from .models import UserRegistration

# Create your views here.

class HomeView(View):
	def get(self,request,*args,**kwargs):
		context={}
		return render(request,"base.html",context)

class UserRegistrationFormView(CreateView):
	form_class = UserRegistrationCreateForm
	template_name = 'forms.html'
	success_url ='/home/'

