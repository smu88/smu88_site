from django.views.generic import TemplateView, ListView

from .models import AboutInfo, Project, Innovation, Iframe


class IndexView(TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutInfo.objects.get(pk=1)

        return context


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'app_main/projects.html'


class FeedbackFormView(ListView):
    model = Iframe
    context_object_name = 'iframes'
    template_name = 'app_main/feedback_form.html'


class InnovationsListView(ListView):
    model = Innovation
    context_object_name = 'innovations'
    template_name = 'app_main/innovations.html'
