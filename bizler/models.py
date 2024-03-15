from django.db import models
from django.core.validators import FileExtensionValidator


class Parents(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True)
    image_url = models.URLField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='parents/files/', null=True, blank=True)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.public_date}'
    
    class Meta:
        verbose_name = 'Ata-analar ushin '
        verbose_name_plural = 'Ata-analar'


