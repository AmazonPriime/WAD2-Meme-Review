from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from meme_app.models import UserProfile, Category, Meme, Comment, View, MemeRating, CommentRating
from meme_app.forms import UserForm
from datetime import datetime

class test_index_view(TestCase):
    
    @classmethod
    def setUp(self):
        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()

        UserProfile.objects.create(user = test_user, picture = 'https://i.pinimg.com/originals/63/4f/c7/634fc7589ecb8b3229528763c2a246a1.jpg', dob = datetime.now() , bio = '') 

        Category.objects.create(name = 'Test Category')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meme_app/index.html')

    def test_index_view_with_no_top_meme(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Currently no meme of the day.')
        self.assertEquals(response.context['trending_meme'], None)

    def test_index_view_with_top_meme(self):

        Meme.objects.create(user = UserProfile.objects.get(user = test_user), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 100, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEquals(response.context['trending_meme'], None)

    
    def test_index_view_with_no_popular_memes(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Currently no popular memes.')
        self.assertEquals(response.context['popular_memes'].count(), 0)

    def test_index_view_with_popular_memes(self):
        



