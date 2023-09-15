from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
# class RegisterTestCase(TestCase):
#     def setUp(self):
#         self.client= Client()
#         self.url = reverse('register')

#     def test_register_new_user(self):
#         form_data={
#             'username':'testuser',
#             'email':'testgmailcom',
#             'password':'password1',
#             'password2':'password1',
#         }

#         response = self.client.post(self.url,data=form_data)
#         print(response)
#         self.assertIn(response.status_code, [200, 302])
#         print("assertIn", self.assertIn(response.status_code, [200, 302]))

#         # Assert that the user is created in the database
#         self.assertTrue(User.objects.filter(username='testuser').exists())

#     def invalid_password(self):
#         form_data1 ={
#             'username':'invalid',
#             'email':'test@gmail.com',
#             'password':'password',
#             'password2':'password1',
#         }
#         response = self.client.post(self.url, data=form_data1)
#         self.assertIn(response.status_code, [200,302])
#         self.assertFalse(User.objects.filter(username='invalid').exists())

#     def invalid_email(self):
#         form_data2 ={
#             'username':'invalidemail',
#             'email':'testgmailcom',
#             'password':'password1',
#             'password2':'password1',
#         }
#         response = self.client.post(self.url, data=form_data2)
#         self.assertIn(response.status_code, [200, 302])
#         self.assertFalse(User.objects.filter(email='testgmailcom').exists())





class LoginTestCase(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(response, reverse('home'))  # Expect redirect to home page
        self.client.get(reverse('home'))  # Get home page after login
        self.assertContains(response, self.username)  # Expect username on the home page
        self.assertContains(response, 'Logout')  # Expect logout button on the home page

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Expect HTTP 200 OK
        self.assertContains(response, 'Invalid username or password.')  # Expect error message
        self.assertContains(response, 'Login')  # Expect login button on the login page

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)  # Log in user
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(response, reverse('login'))  # Expect redirect to login page
        self.client.get(reverse('login'))  # Get login page after logout
        self.assertContains(response, 'Login')  # Expect login button on the login page
