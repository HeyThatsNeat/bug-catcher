from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Bug(models.Model):
  subject = models.CharField(max_length=100)
  bugged_Code = models.TextField()
  fixed_Code = models.TextField()
  language = models.CharField(max_length=100, verbose_name = "Language(s)")
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.subject
  
  def get_absolute_url(self):
    return reverse('bug-detail', kwargs={'bug_id': self.id})