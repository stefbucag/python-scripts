from django.views.generic import TemplateView
from django.conf.urls import include, url

from django.contrib import admin
from django.conf import settings

from project_sample.views import Appointment


admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"),),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    url(r'^schedule/', include('schedule.urls'), name='scheduler'),
    url(r'^appointment/', Appointment.as_view(), name='appointment'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
