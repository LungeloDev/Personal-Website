from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name