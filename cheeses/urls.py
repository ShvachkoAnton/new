from django.urls import path

from .views import CheeseListView,CheeseDetailView


urlpatterns=[path('', CheeseListView.as_view(), name='list' ),
path("<slug:slug>",CheeseDetailView.as_view(), name='detail')

]