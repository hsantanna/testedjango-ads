from django.db import models

# Create your models here.

class URL(models.Model):
    url = models.CharField(max_length=220,)
    shorturl = models.CharField(max_length=15, unique=True)
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.atualizado)


'''
sempre que alterar o models.py é preciso rodar:
python manage.py makemigrations
python manage.py migrate
'''
