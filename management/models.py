from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Django recommends setting a custom User model on project creation, as
# migrating to one after launch is difficult to do.
class User(AbstractUser):
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)
