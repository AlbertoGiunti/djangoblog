# comunica con la creazione di nuovi utenti e profili

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Per creare la foto profilo
@receiver(post_save, sender=User)  # riceve il segnale post_save quando un utente viene salvato
def create_profile(sender, instance, created,
                   **kwargs):  # sender è il modello che ha inviato il segnale, instance è l'istanza del modello, created è un booleano che indica se l'istanza è stata appena creata, kwargs sono argomenti aggiuntivi
    if created:
        Profile.objects.create(user=instance)  # crea un profilo per ogni utente creato


# Per salvare la foto profilo
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # salva il profilo per ogni utente creato
