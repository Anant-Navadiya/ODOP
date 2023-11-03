import uuid

from django.db import models
from argon2 import PasswordHasher
from django.contrib.auth.password_validation import validate_password


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    is_active = models.BooleanField(default=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    email = models.EmailField(max_length=128, unique=True, default='', blank=True)
    mobile_number = models.CharField(max_length=10, unique=True, default='', blank=True)

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    password = models.CharField(max_length=128, validators=[validate_password])

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        ph = PasswordHasher()
        self.password = ph.hash(self.password)
        super().save(*args, **kwargs)
