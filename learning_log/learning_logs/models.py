from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length =200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma String do model"""