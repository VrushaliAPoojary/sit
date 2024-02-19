from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    img=models.ImageField(upload_to='Event',blank=True, null=True)


class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption