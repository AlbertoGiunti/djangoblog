from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one to one relationship, un profilo per ogni utente
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics')  # upload_to è la directory dove verranno salvate le immagini, profile_pics è la cartella che verrà creata all'interno di media

    def __str__(self):
        return f'{self.user.username} Profile'
