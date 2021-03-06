from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from my_awesome_project.users.tests.factories import UserFactory
from cheeses.models import Cheese
import pytest


@pytest.fixture
def cheese():
    return CheeseFactory()

class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    class Meta:
        model = Cheese
    creator = factory.SubFactory(UserFactory)

    

    