from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.EmailField(blank=True, null= True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile')
    about_image = models.ImageField(upload_to='about')
    skill_image = models.ImageField(upload_to='skill')
    personal_info = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=15)
    cv = models.FileField()
    num_of_clients = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Profile'



class Projects(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural = 'Projects'
        
        
    
class Skills(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} : {self.email}'