from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('barber', 'Barber'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Foydalanuvchilar'
        verbose_name = 'Foydalanuvchi'


class Barber(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    bio = models.TextField(max_length=500)
    experience = models.IntegerField()
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sartaroshlar'
        verbose_name = 'Sartarosh'


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Servis Hizmatlari'
        verbose_name = 'Servis Hizmati'


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Servislar'
        verbose_name = 'Servis'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
