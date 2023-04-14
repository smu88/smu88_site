from django.urls import path
from django.views.decorators.cache import cache_page

from .views import IndexView, ProjectListView, FeedbackFormView, InnovationsListView


app_name = 'app_main'

urlpatterns = [
    path('', cache_page(30)(IndexView.as_view()), name='index'),
    path('projects/', cache_page(20)(ProjectListView.as_view()), name='projects'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('innovations/', cache_page(20)(InnovationsListView.as_view()), name='innovations'),
]
