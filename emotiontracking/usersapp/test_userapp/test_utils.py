from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
from usersapp.views import home

class HomeViewTestCase(TestCase):
    def test_home_view(self):
        request = HttpRequest()
        response = home(request)
        
        self.assertEqual(response.status_code, 200)  # Vérifie que la réponse est un succès (code 200)
        self.assertTemplateUsed(response, 'usersapp/home.html') 