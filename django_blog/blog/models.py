from django.db import models


class User(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="blog", on_delete=models.CASCADE)
  

    def __str__(self):
        return self.title
