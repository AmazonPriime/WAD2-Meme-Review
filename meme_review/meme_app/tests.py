from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from meme_app.models import UserProfile, Category, Meme, Comment, View, MemeRating, CommentRating
from meme_app.forms import UserForm
from datetime import datetime


'''

Views

'''

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

    def test_index_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meme_app/index.html')

    def test_index_view_with_no_top_meme(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Currently no meme of the day.')
        self.assertEquals(response.context['trending_meme'], None)

    def test_index_view_with_top_meme(self):

        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
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

        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 1, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 2, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 3, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 4, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 5, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 6, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 6, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 8, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)
        Meme.objects.create(user = UserProfile.objects.get(user_id = 1), title= 'Test Meme', picture = 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                                   date = datetime.now() , likes = 7, dislikes = 0, views = 10, category = Category.objects.get(name = 'Test Category'), nsfw = False)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.context['popular_memes'].count(), 9)


class test_meme_creator_view(TestCase):

    @classmethod
    def setUp(self):
        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()

        UserProfile.objects.create(user = test_user, picture = 'https://i.pinimg.com/originals/63/4f/c7/634fc7589ecb8b3229528763c2a246a1.jpg', dob = datetime.now() , bio = '') 

        Category.objects.create(name = 'Test Category')
        
        pass

    
    def test_memecreator_redirect_if_not_logged_in(self):
        
        response = self.client.get(reverse('meme_creator'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/meme_creator/')

    def test_memecreator_access_if_logged_in(self):
        login = self.client.login(username='Username', password='password1')
        response = self.client.get(reverse('meme_creator'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_meme_made(self):
        login = self.client.login(username='Username', password='password1')
        meme_details = {'title': 'test meme' , 'category': 'Test Category'}
        
        response = self.client.post(reverse('meme_creator'), data = meme_details)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/meme/')
        

class test_register_view(TestCase):
    
    @classmethod
    def setUp(self):

        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()
        pass
    
    def test_register_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meme_app/register.html')

    def test_register_registers_a_user(self):
        user_details = {'username' : 'Username', 'first_name': 'John', 'last_name': 'Smith',
                    'email' : 'example@test.com', 'password' : 'password1'}
        response = self.client.post(reverse('register'), data=user_details)
        self.assertTrue(User.objects.filter(username= 'Username').exists())


'''

Models

'''


class test_UserProfile_model(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()

        UserProfile.objects.create(user = test_user, picture = 'https://i.pinimg.com/originals/63/4f/c7/634fc7589ecb8b3229528763c2a246a1.jpg', dob = datetime.now() , bio = '')
        
    def test_UserProfile_user_label(self):
        up = UserProfile.objects.get(id=1)
        field_label = up._meta.get_field("user").verbose_name
        self.assertEquals(field_label, "user")

    def test_UserProfile_picture_label(self):
        up = UserProfile.objects.get(id=1)
        field_label = up._meta.get_field("picture").verbose_name
        self.assertEquals(field_label, "picture")

    def test_UserProfile_dob_label(self):
        up = UserProfile.objects.get(id=1)
        field_label = up._meta.get_field("dob").verbose_name
        self.assertEquals(field_label, "dob")

    def test_UserProfile_bio_label(self):
        up = UserProfile.objects.get(id=1)
        field_label = up._meta.get_field("bio").verbose_name
        self.assertEquals(field_label, "bio")
        

class test_Category_model(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name = 'Test Category')

    def test_category_name_label(self):
        cat = Category.objects.get(name = 'Test Category')
        field_label = cat._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_max_length(self):
        cat = Category.objects.get(name = 'Test Category')
        max_length = cat._meta.get_field('name').max_length
        self.assertEquals(max_length, 64)
        


        


