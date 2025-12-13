from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=50, default='Developer')
    created_up = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name 