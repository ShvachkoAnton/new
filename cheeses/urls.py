from django.urls import path

from .views import CheeseListView


urlpatterns=[path('', CheeseListView.as_view(), name='list' ),

]