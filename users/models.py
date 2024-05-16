from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='user-photos/', 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], 
        blank=True, 
        null=True)
    klass = models.PositiveIntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 12)])

    def __str__(self) -> str:
        return f'{self.user.username} - {self.klass} klass'
    
    class Meta:
        verbose_name = 'Profildi '
        verbose_name_plural = 'Profiller '



class DailyVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_visited = models.DateField()

    class Meta:
        unique_together = ['user', 'date_visited']
