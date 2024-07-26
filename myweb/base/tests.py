from django.test import TestCase
from .models import Animal
# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='Dog', sound="woof")
        Animal.objects.create(name='Wolf', sound="owoooo")

    def test_animal_can_speak(self):
        wolf = Animal.objects.get(name='Wolf')
        dog = Animal.objects.get(name='Dog')
        self.assertEqual(wolf.speak(), 'The Wolf says "owoooo"')
        self.assertEqual(dog.speak(), 'The Dog says "woof"')


