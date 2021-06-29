from django.test import TestCase
import pytest
from pytest_django.asserts import (
assertContains,
assertRedirects
)
from django.urls import reverse
from django.contrib.sessions.middleware \
import SessionMiddleware




# Create your tests here.
