from django.conf import settings
from django.db import models

# Create your models here.
class EntranceExit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entrance_date = models.DateTimeField(auto_now_add=True, blank=False)
    exit_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f"User: {self.user}, entrance_date: {str(self.entrance_date)}, exit_date: {str(self.exit_date)}"
