import uuid
from django.db import models
from argon2 import PasswordHasher


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    time_stamp = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    is_active = models.BooleanField(default=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    email = models.EmailField(max_length=128, unique=True,blank=True,default = None)
    email_verified_at = models.DateTimeField(auto_now_add=True, blank=True)

    mobile_number = models.IntegerField(unique=True, blank=True,default = None)
    mobile_number_verified_at = models.DateTimeField(auto_now_add=True, blank=True)

    avatar = models.CharField(max_length=128, blank=True)

    password = models.CharField(max_length=128)

    class Meta:
        ordering = ["-time_stamp"]
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        ph = PasswordHasher()
        self.password = ph.hash(self.password)
        super().save(*args, **kwargs)
