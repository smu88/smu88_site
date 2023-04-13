from django.urls import path


from .views import IndexView, ProjectListView, FeedbackFormView, InnovationsListView


app_name = 'app_main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('innovations/', InnovationsListView.as_view(), name='innovations'),
]
