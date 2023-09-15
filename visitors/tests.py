from audioop import reverse
from django.test import Client, TestCase
from .forms import VisitorForm
from .models import Purpose
from django.contrib.auth.models import User

class FormTestCase(TestCase):

    #run before every function runs.
    def setUp(self):
        self.p = Purpose.objects.create(name='Guest', description="guest desc.")


    def test_visitor_form_valid(self):
        # Create valid form data
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoeexamplecom',
            'address': '123 Test St',
            'purpose': self.p,
        }

        form = VisitorForm(data=form_data)

        if form.is_valid():
            print("Form is valid")
        else:
            print("Form errors:", form.errors.as_data())

        self.assertTrue(form.is_valid())

       
    
    def test_visitor_purpose_valid(self):
         
        form_data_2 = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'janesmith@example.com',
            'address': '456 Example Ave',
            'purpose': Purpose.objects.get(id=6),
        }
         
        form_2 = VisitorForm(data=form_data_2)

        if form_2.is_valid():
            print("Form 2 is valid")
        else:
            print("Form 2 errors:", form_2.errors.as_data())

        self.assertTrue(form_2.is_valid())




