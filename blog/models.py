from django.db import models
import uuid
from django.contrib.auth import get_user_model
# Create your models here.


user = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid.uuid4)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username
