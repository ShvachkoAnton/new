import pytest
from django.urls import reverse,resolve
from cheeses.tests.factories import CheeseFactory
pytestmark = pytest.mark.django_db




@pytest.fixture
def test_list_reverse(cheese):
    url=reverse('detail', kwargs={'slug':cheese.slug})
    assert url==f'/cheeses/{cheese.slug}/'


@pytest.fixture
def test_list_resolve(cheese):
    url=f'/cheeses/{cheese.slug}/'
    assert resolve(url).view_name=='detail'