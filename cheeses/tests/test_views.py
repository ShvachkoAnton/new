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

