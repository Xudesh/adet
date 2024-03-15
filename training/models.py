from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def image_size(file_obj):
    megabyte_limit = 3
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(F'max file razmeri {megabyte_limit}MB')


class Language(models.Model):
    subject = models.CharField('kurs tili', max_length=250)
    subject_slug = models.SlugField('kurs url',max_length=250)
    klass = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 12)])

    class Meta:
        verbose_name = 'kurs tilin '
        verbose_name_plural = 'kurs tilleri'


    def __str__(self) -> str:
        return self.subject
    
    def get_absolute_url(self):
        return reverse(
            'lessons',
            args=[
                self.klass,
                self.subject_slug,
            ]
        )
    


class Lesson(models.Model):
    name = models.CharField('sabaqtin temasi', max_length=250)
    slug = models.SlugField('sabaqtin url', max_length=250)
    image = models.ImageField(null=True, blank=True, upload_to='lesson-image/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), image_size])
    video = models.URLField(max_length=255, null=True, blank=True)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, null=True, verbose_name='sabaq')
    klass = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 12)])
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'lesson_detail',
            args=[
                self.slug
            ]
        )
    
    class Meta:
        verbose_name = 'sabaqti '
        verbose_name_plural = 'sabaqlar'

