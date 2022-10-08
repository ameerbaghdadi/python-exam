from django.db import models
from login_app.models import *
import datetime

class TreeManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['species']) < 5:
            errors["species"] = "Species should be at least 5 characters"
        if len(postData['location']) < 2:
            errors["location"] = "Location should be at least 2 characters"
        if len(postData['reason']) > 50:
            errors["reason"] = "Reason should be max 50 characters"
        return errors

class Tree(models.Model):
    species = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    reason = models.TextField(default = "")
    date = models.DateField(default=datetime.date.today())
    planted_by = models.ForeignKey(User, related_name="tree_planted", on_delete = models.CASCADE)
    users_who_viwe = models.ManyToManyField(User, related_name="viewed_trees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TreeManager()