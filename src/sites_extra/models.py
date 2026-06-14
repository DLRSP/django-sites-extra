from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Background(models.Model):
    name = models.CharField(
        verbose_name=_("Background"), max_length=50, null=True
    )
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
