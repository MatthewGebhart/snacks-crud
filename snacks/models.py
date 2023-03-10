from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Snack(models.Model):
    title = models.CharField(max_length=256)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")
    image_url = models.URLField(default="https://arborpointe.com/wp-content/uploads/2018/06/comingsoon.jpg")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])

