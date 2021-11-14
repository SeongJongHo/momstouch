from django.db import models


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)

    class Meta:
        db_table="menu"

    def __str__(self):
         return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)
    menu_id = models.ForeignKey("Menu",on_delete=models.CASCADE,db_constraint="menu_id")

    class Meta:          
        db_table="category"  

    def __str__(self):
         return self.name

class Momsset(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)

    class Meta:          
        db_table="momsset"  

    def __str__(self):
         return self.name

class Momsset_Products(models.Model):
    id = models.AutoField(primary_key=True)
    momsset_id=models.ForeignKey("Momsset",on_delete=models.CASCADE,db_constraint="momsset_id")
    products_id=models.ForeignKey("Products",on_delete=models.CASCADE,db_constraint="products_id")

    class Meta:          
        db_table="momsset_Products"  


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)
    description=models.TextField()
    new=models.BooleanField(default=False)
    best=models.BooleanField(default=False)
    category_id=models.ForeignKey("Category",on_delete=models.CASCADE,db_constraint="category_id")

    class Meta:          
        db_table="Products"  

    def __str__(self):
         return self.name

class Allergy_products(models.Model):
    id = models.AutoField(primary_key=True)
    products_id=models.ForeignKey("Products",on_delete=models.CASCADE,db_constraint="products_id")
    allergy_id=models.ForeignKey("Allergy",on_delete=models.CASCADE,db_constraint="allergy_id")

    class Meta:          
        db_table="allergy_products"  


class Allergy(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)

    class Meta:          
        db_table="allergy"  

    def __str__(self):
         return self.name

# Create your models here.
