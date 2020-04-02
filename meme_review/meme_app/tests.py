from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from meme_app.models import UserProfile, Category, Meme, Comment, View, MemeRating, CommentRating
from meme_app.forms import UserForm
from datetime import datetime

def add_meme(title, picture, likes, dislikes, views, category, user,
             date = datetime.now(), nsfw = False):

    meme = Meme.objects.create()[0]
    meme.user = user
    meme.title = title
    meme.picture = picture
    meme.date = date
    meme.likes = likes
    meme.dislikes = dislikes
    meme.views = views
    meme.category = UserObject.objects(name = category)
    meme.nsfw = nsfw
    meme.save()
    return meme

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

    '''def test_index_view_with_popular_memes(self):

        test_user = UserProfile.objects.get_or_create(user_id = 1)[0]
        test_cat = Category.objects.get_or_create('Test Category')[0]

        for i in range(9):
            add_meme(str(i), 'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                     i, 0, 100, test_cat, test_user)

        
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.context['popular_memes'].count(), 9)
        self.assertTrue(response.context['popular_memes'].sorted(iterable, key=likes))'''


class test_meme_creator_view(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()

        UserProfile.objects.create(user = test_user, picture = 'https://i.pinimg.com/originals/63/4f/c7/634fc7589ecb8b3229528763c2a246a1.jpg', dob = datetime.now() , bio = '') 
        
        pass

    
    def test_memecreator_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('meme_creator'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

    def test_memecreator_access_if_logged_in(self):
        login = self.client.login(username='Username', password='password1')
        response = self.client.get(reverse('meme_creator'))


class test_register_view(TestCase):
    @classmethod
    def setUp(self):
        test_user = User.objects.create_user(username = 'Username', first_name = 'John', last_name = 'Smith',
                                      email = 'example@test.com', password = 'password1')
        test_user.save()

    def test_register_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meme_app/register.html')

    def test_register_registers_a_user(self):
        user_details = {'username' : 'Username', 'first_name': 'John', 'last_name': 'Smith',
                    'email' : 'example@test.com', 'password' : 'password1'}
        response = self.client.post(reverse('register'), data=user_details)
        self.assertTrue(User.objects.filter(username= 'Username').exists())

    '''def test_register_age_under_13(self):
        user_birthday = {datetime(2015, 1, 1)}

        response = self.client.post(reverse('register'), data= user_birthday)
        self.assertFalse(User.objects.filter(dob = datetime(2015, 1, 1)).exists())'''


'''

MODELS

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
        


        


