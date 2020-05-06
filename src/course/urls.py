from django.urls import path
from .views import CourseDetailView

app_name = 'course'
urlpatterns = [
	path('', CourseDetailView.as_view(template_name='contact.html'), name = 'course-list'),
	path('<int:id>/', CourseDetailView.as_view(), name = 'course-detail')
]