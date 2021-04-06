from django.contrib import admin
from testapp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    list_display=['id','name','description','cost_per_item','stock_quantity','volume']

admin.site.register(Product,ProductAdmin)