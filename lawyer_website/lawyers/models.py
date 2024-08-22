from django.db import models


class Lawyer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='lawyer_photos/', blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

