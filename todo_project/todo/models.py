from django.db import models
from django.utils.translation import gettext_lazy as _



class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    completed = models.BooleanField(default=False, verbose_name=_("Completed"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.title