"""
Pacote de settings para o projeto core.

Por padrão este __init__ importa as configurações de desenvolvimento.
Em produção você pode ajustar para importar .production ou apontar DJANGO_SETTINGS_MODULE
para o módulo desejado.
"""

from .development import *
