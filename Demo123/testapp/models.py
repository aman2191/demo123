from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost_per_item = models.DecimalField(max_digits=13, decimal_places=2)
    stock_quantity = models.IntegerField(default=None)
    volume = models.FloatField(editable=False,null=True)

def save(self,*args,**Kwargs):
    self.volume = self.calculate_sum()
    super(Product,self).save(*args,**kwargs)

def calculate_sum(self):
    a = (self.cost_per_item)
    b = (self.stock_quantity)
    r = a*b
    return r


    

    

    #def save(self):
        #v = Product.objects.annotate(volume=('cost_per_item') * ('stock_quantity'))
        #c=Product.objects.all().only('cost_per_item')
        #self.volume = 90
        #super(Product, self).save

    
    
    def __str__(self):
        return '{}'.format(self.name)

