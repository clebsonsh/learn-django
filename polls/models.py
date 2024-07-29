import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_at = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.text

    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_at <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text

