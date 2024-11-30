from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)  
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"


class Blog(models.Model):
    image = models.ImageField(upload_to='works/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)