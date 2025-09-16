from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class MiniProject(models.Model):
    PRIORITY_CHOICES = [('low','Low'), ('medium','Medium'), ('high','High')]
    STATUS_CHOICES = [('todo','To Do'), ('inprogress','In Progress'), ('complete','Complete')]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

