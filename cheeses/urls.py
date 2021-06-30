from django.urls import path

from .views import CheeseListView,CheeseDetailView, CheeseCreateView,CheeseUpdateView


urlpatterns=[path('', CheeseListView.as_view(), name='list' ),
path('add/',CheeseCreateView.as_view(),name='create'),
path("<slug:slug>/",CheeseDetailView.as_view(), name='detail'),
path('<slug:slug>/update/', CheeseUpdateView.as_view(),name='update')

]