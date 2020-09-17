from django.db import models

# Create your models here.


# to show product type if it machine ( enum == 1 ), if it bods ( enum == 2 )
class ProductType(models.Model):
    product_type_name_en = models.CharField(max_length=200)
    product_type_name_ar = models.CharField(max_length=200)
    product_type_enum    = models.IntegerField()

    def __str__(self):
        return self.product_type_name_en


# model for Coffe machine
class CoffeMachine(models.Model):
    product_type_id       = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    water_line            = models.BooleanField()
    coffe_machine_name_en = models.CharField(max_length=200)
    coffe_machine_name_ar = models.CharField(max_length=200)

    def __str__(self):
        return self.coffe_machine_name_en


class CoffeFlaver(models.Model):
    coffe_flaver_name_en = models.CharField(max_length=200)
    coffe_flaver_name_ar = models.CharField(max_length=200)

    def __str__(self):
       return self.coffe_flaver_name_en



class PackSize(models.Model):
    pack_size_value = models.IntegerField()
    pack_size_name_en = models.CharField(max_length=200)
    pack_size_name_ar = models.CharField(max_length=200)

    def __str__(self):
        return self.pack_size_name_en


# model for Bods
class CoffePods(models.Model):
    product_type_id    = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    coffe_pods_name_en = models.CharField(max_length=200)
    coffe_pods_name_ar = models.CharField(max_length=200)
    coffe_flaver_id    = models.ForeignKey(CoffeFlaver, on_delete=models.CASCADE)
    pack_size_id       = models.ForeignKey(PackSize, on_delete=models.CASCADE)

    def __str__(self):
        return self.coffe_pods_name_en







