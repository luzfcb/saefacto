from braces.views import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'

class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'


class MailNotifyView(generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/mail.html'

mail = MailNotifyView.as_view()

class NotificationsNotifyView(generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/notifications.html'

notifications = NotificationsNotifyView.as_view()

class TaskNotifyView(generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/tasks.html'

task = TaskNotifyView.as_view()
