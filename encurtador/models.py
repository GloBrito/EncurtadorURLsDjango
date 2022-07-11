from django.db import models


class Links(models.Model):
    link_redirecionado = models.URLField
    link_personalizado = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.link_personalizado
