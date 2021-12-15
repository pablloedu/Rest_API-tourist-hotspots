from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username