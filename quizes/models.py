from django.db import models
from training.models import *


class Question(models.Model):
    text = models.TextField(null=True)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.text}'
    
    class Meta:
        verbose_name = 'soraw '
        verbose_name_plural = 'sorawlar'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True)
    is_correct = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.question}'

    class Meta:
        verbose_name = 'test juwabi '
        verbose_name_plural = 'test juwablari'

class TestResult(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_date = models.DateField(auto_now_add=True)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user} - {self.score}'

    class Meta:
        verbose_name = 'test sigariwshini '
        verbose_name_plural = 'test shigariwshilar'


class TestResultDetail(models.Model):
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.test_result}'
    
    class Meta:
        verbose_name = 'toliq test juwabi '
        verbose_name_plural = 'toliq test juwablari'