from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    img = models.ImageField(null=True)


class Accessory(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    img = models.ImageField(null=True)
    name = models.CharField(max_length=40)
    prise = models.CharField(max_length=40)
    comment = models.TextField()

    @property
    def owner_name(self):
        return f'{self.owner.name} {self.owner.surname}'
