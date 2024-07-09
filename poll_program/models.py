from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    poll_question = models.CharField(max_length=255)
    creating_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll_question

class Option(models.Model):
    poll = models.ForeignKey(Poll, related_name='option', on_delete=models.CASCADE)
    option_name = models.CharField(max_length=255)

    def __str__(self):
        return self.option_name

class Select(models.Model):
    user = models.ForeignKey(User, related_name='select', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    selecting_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'option')
