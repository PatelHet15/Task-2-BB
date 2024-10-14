from django.db import models

# Create your models here.

class Car(models.Model):
    company = models.CharField(max_length=100) 
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.company} {self.model} ({self.year}) - ${self.price}"
    
class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.company} purchased on {self.purchase_date}"

