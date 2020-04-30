from django.urls import path
from learn_app import views

#template tagging
app_name= 'learn_app'

urlpatterns=[
    path('relative_url_templates/',views.relative_url_templates,name='relative_url_templates'),
    path('others/',views.others,name='others'),
]
