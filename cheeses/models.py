import autoslug
from django.db import models
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings


class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField(
        "Cheese Adress", unique=True, always_update=False, populate_from="name"
    )

    description = models.TextField("Description", blank=True)
    country_of_origin = CountryField("Country of origin", blank=True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    firmness = models.CharField(
        "Firmness",
        max_length=25,
        choices=Firmness.choices,
        default=Firmness.UNSPECIFIED,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('detail', kwargs={"slug": self.slug})

    
    