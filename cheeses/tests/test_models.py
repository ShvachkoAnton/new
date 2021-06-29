from cheeses.models import Cheese
import pytest
from cheeses.tests.factories import CheeseFactory
@pytest.mark.django_db(True)
def test__str__():
    cheese=CheeseFactory()
    assert cheese.__str__()==cheese.name
    assert str(cheese)==cheese.name
@pytest.mark.django_db(True)
def test_get_absolute_url():
    cheese=CheeseFactory()
    url=cheese.get_absolute_url()
    assert url==f'/cheeses/{cheese.slug}/'
