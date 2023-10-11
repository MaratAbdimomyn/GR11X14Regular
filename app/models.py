from django.db import models

class Action(models.Model):
    action = models.CharField(max_length=40)
    about = models.CharField(max_length=40)
    deadline = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.action