from django.db import models

# Create your models here.

class Poll(models.Model):
  states = (
    (0, "Draft"),
    (1, "Published"),
   )

  title = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  active_untill = models.DateTimeField(auto_now=True)
  status = models.IntegerField(Choices=STATUS, default=0)

Class Option(models.Model):
  title = models.CharField(max_length=100)
  has = models.ForeignKey('Poll', on_delete=models.CASCADE)

Class Response(models.Model):
  name = models.CharField(max_length=100)
  response_time - model.DateTimeField(auto_now_add=True)
  has = models.ForeignKey('Option',  on_delete=models.CASCADE)