from django.db import models
from django.contrib.auth.models import User
import uuid

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("updated_at"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed"]