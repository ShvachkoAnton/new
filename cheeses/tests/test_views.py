from django.db.models.query_utils import Q
from django.views.generic.edit import CreateView
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
from cheeses.views import(
CheeseCreateView,
CheeseListView,
CheeseDetailView
)

from cheeses.tests.factories import CheeseFactory

pytestmark = pytest.mark.django_db

def test_cheese_create_form_valid(rf, admin_user):
# Submit the cheese add form
    form_data = {
    "name": "Paski Sir",
    "description": "A salty hard cheese",
    "firmness": Cheese.Firmness.HARD
    }
    request = rf.post(reverse("create"), form_data)

    request.user = admin_user
    response = CheeseCreateView.as_view()(request)
        # Get the cheese based on the name
    cheese = Cheese.objects.get(name="Paski Sir")
        # Test that the cheese matches our form
    assert cheese.description == "A salty hard cheese"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == admin_user
