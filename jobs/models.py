from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    salary = models.IntegerField()

    skills = models.CharField(max_length=200)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title