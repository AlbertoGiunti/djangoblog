from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one to one relationship, un profilo per ogni utente
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # upload_to è la directory dove verranno salvate le immagini, profile_pics è la cartella che verrà creata all'interno di media

    def __str__(self):
        return f'{self.user.username} Profile'

    # override del metodo save per ridimensionare l'immagine del profilo
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # resize immagine profilo
        img = Image.open(self.image.path)  # apre l'immagine del profilo
        if img.height > 300 or img.width > 300:  # se l'immagine è più grande di 300x300
            output_size = (300, 300)  # dimensioni dell'immagine
            img.thumbnail(output_size)  # ridimensiona l'immagine
            img.save(self.image.path)  # salva l'immagine
