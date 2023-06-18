import factory
from ecommerce.apps.catalogue.models import Category
from faker import Faker

fake = Faker()

####
# Catalogue
####

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "django"
    slug = "django"