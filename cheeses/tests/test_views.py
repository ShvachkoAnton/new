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
CheeseDetailView,
CheeseUpdateView,

)

from cheeses.tests.factories import CheeseFactory,cheese

pytestmark = pytest.mark.django_db
def test_good_cheese_update_view(rf, admin_user, cheese):
    form_data={
     'name':cheese.name,
     'description':'Something new',
     'firmness':cheese.firmness
    }
    url=reverse("update",
    kwargs={'slug':cheese.slug})
    request=rf.post(url,form_data)
    request.user=admin_user
    callable=CheeseUpdateView.as_view()
    response=callable(request,slug=cheese.slug)
    cheese.refresh_from_db()
    assert cheese.description=='Something new'