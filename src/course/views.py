from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Course
# Create your views here.
class CourseDetailView(View):
	template_name = 'course/course_detail.html'

	def get(self,request, id = None, *args, **kwargs):
		my_context = {}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			my_context['object'] = obj
		return render(request, self.template_name,my_context)
