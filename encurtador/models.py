from django.db import models


class Links(models.Model):
    linkredirecionado = models.URLField()
    link_personalizado = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return self.link_personalizado
