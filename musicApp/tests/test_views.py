from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Song

class MusicAppViewsTestCase(TestCase):

    def setUp(self):
        # Set up a test client
        self.client = Client()
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create sample songs
        self.song_hindi = Song.objects.create(name="Hindi Song", singer="Singer A", tags="Hindi")
        self.song_kannada = Song.objects.create(name="Kannada Song", singer="Singer B", tags="Kannada")
        self.song_english = Song.objects.create(name="English Song", singer="Singer C", tags="English")
        
        # Define URLs for views
        self.index_url = reverse('index')  # Ensure 'index' is defined in your urls.py
        self.hindi_url = reverse('hindi_songs')
        self.kannada_url = reverse('kannada_songs')
        self.english_url = reverse('english_songs')
        self.home_url = reverse('home')  # For the home view

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Music Portal!")

    def test_index_view_requires_login(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_index_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/index.html')
        self.assertContains(response, self.song_hindi.name)
        self.assertContains(response, self.song_kannada.name)
        self.assertContains(response, self.song_english.name)

    def test_hindi_songs_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.hindi_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/hindi.html')
        self.assertContains(response, self.song_hindi.name)
        self.assertNotContains(response, self.song_kannada.name)
        self.assertNotContains(response, self.song_english.name)

    def test_kannada_songs_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.kannada_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/kannada.html')
        self.assertContains(response, self.song_kannada.name)
        self.assertNotContains(response, self.song_hindi.name)
        self.assertNotContains(response, self.song_english.name)

    def test_english_songs_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.english_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/english.html')
        self.assertContains(response, self.song_english.name)
        self.assertNotContains(response, self.song_hindi.name)
        self.assertNotContains(response, self.song_kannada.name)
