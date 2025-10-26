from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	"""Modelo de usuário customizado.

	Nesse momento herdamos de AbstractUser sem campos adicionais.
	Você pode estender adicionando campos (por exemplo: phone, is_artist, profile_picture).
	"""

	# Exemplo de campo adicional (comente/descomente se quiser usar)
	# phone = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self) -> str:
		return self.username
