from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# not sure if I need to specifically use the auth_user model, regular old User passes the tests and is
# more in line with how we've done things, well leave the code commented out for future reference.

# from django.conf import settings

# USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User,
        null=True,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
