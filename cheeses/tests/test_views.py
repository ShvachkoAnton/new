import pytest
from pytest_django.asserts import (
assertContains,
assertRedirects
)
from django.urls import reverse
from django.contrib.sessions.middleware \
import SessionMiddleware
from django.test import RequestFactory
from my_awesome_project.users.models import User

from cheeses.models import Cheese
from cheeses.views import(CheeseCreateView,
CheeseListView,
CheeseDetailView)


from factories import CheeseFactory
pytestmark = pytest.mark.django_db
def test_good_cheese_list_view_expanded(rf):
# Determine the URL
    url = reverse("list")
    # rf is pytest shortcut to django.test.RequestFactory
    # We generate a request as if from a user accessing
    # the cheese list view
    request = rf.get(url)
    # Call as_view() to make a callable object
    # callable_obj is analogous to a function-based view
    callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj to get an
    # HTTP response served up by Django
    response = callable_obj(request)
    # Test that the HTTP response has 'Cheese List' in the
    # HTML and has a 200 response code
    assertContains(response, 'Cheese List')
