from django.contrib.auth.models import User
from django.db import models


# No need to redefine the User model if you're using Django's built-in User
# The Blog model can reference the built-in User model

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

