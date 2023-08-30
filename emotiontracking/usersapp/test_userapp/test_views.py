from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
from usersapp.views import home,register
from django.contrib.auth.models import User
from usersapp.forms import RegistrationForm

class HomeViewTestCase(TestCase):
    def test_home_view(self):
        request = HttpRequest()
        response = home(request)
        
        self.assertEqual(response.status_code, 200)  # Vérifie que la réponse est un succès (code 200)
        self.assertTemplateUsed(response, 'usersapp/home.html') 

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)  # Vérifie que la page de formulaire de registration est accessible
        self.assertTemplateUsed(response, 'usersapp/register.html')  # Vérifie que le bon modèle est utilisé

    def test_register_view_post_valid_form(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)  # Vérifie qu'une redirection a eu lieu (code 302)

        # Vérifie que l'utilisateur a été créé dans la base de données
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Vérifie que l'utilisateur a été redirigé vers la page de connexion
        login_url = reverse('login')
        self.assertRedirects(response, login_url)

    def test_register_view_post_invalid_form(self):
        data = {}  # Données vides pour provoquer une validation de formulaire invalide
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)  # Vérifie que la page de formulaire de registration est réaffichée
        self.assertFormError(response, 'form', 'username', 'This field is required.')  # Vérifie les erreurs de formulaire

        # Vérifie qu'aucun utilisateur n'a été créé dans la base de données
        self.assertFalse(User.objects.exists())