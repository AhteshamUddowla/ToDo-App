from django.db import models
import uuid

# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=20, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task)
    
    class Meta:
        ordering = ['created']

