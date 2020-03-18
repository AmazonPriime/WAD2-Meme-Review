from django.db import models
class User(models.Model):
    NAME_MAX_LENGTH = 64
    EMAIL_MAX_LENGTH = 64
    PASSWORD_MAX_LENGTH = 32
    name = models.CharField(max_length=NAME_MAX_LENGTH, primary_key=True)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    dob = models.DateTimeField()
    adult = models.BooleanField()
    
    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 64
    TAGS_MAX_LENGTH = 32
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    date = models.DateField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    tags = models.CharField(max_length=TAGS_MAX_LENGTH)

    def __str__(self):
        return self.id

class Comment(models.Model):
    TEXT_MAX_LENGTH = 64 
    TAGS_MAX_LENGTH = 32
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'createduser')
    ratedusername = models.ManyToManyField(User, related_name = 'rateduser')
    text = models.CharField(max_length=TEXT_MAX_LENGTH)
    date = models.DateField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    tags = models.CharField(max_length=TAGS_MAX_LENGTH)

    def __str__(self):
        return self.id


