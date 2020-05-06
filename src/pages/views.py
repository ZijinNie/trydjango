from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
	return render(request, "home.html",{})
def contact_view(request, *args, **kwargs):
	my_context = {
		'phone_num' : 123321,
		'contact_name' : 'niezijin',
		'my_list' : [1,2,3,5455]
	}
	return render(request, "contact.html",my_context)

class ContactView(View):
	def get(self,request, *args, **kwargs):
		my_context = {
			'phone_num' : 123321,
			'contact_name' : 'niezijin',
			'my_list' : [1,2,3,5455]
		}
		return render(request, "contact.html",my_context)


