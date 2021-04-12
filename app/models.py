from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    PK_Manufacturer = models.AutoField(db_column='PK_Manufacturer', primary_key=True) 
    name = models.CharField(db_column='nameBrand', max_length=100)

    class Meta:
        db_table = 'Manufacturer'

    def __str__(self):
        return self.name

        
class Category(models.Model):
    PK_Category = models.AutoField(db_column='PK_Category', primary_key=True) 
    name = models.CharField(db_column='nameCategory', max_length=100)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name



class Puzzle(models.Model):
    PK_Puzzle = models.AutoField(db_column='PK_Puzzle', primary_key=True)
    name = models.CharField(db_column='name_of_puzzle', max_length=200)
    number_of_details = models.IntegerField(db_column='number_of_details')
    age = models.IntegerField(db_column='age')
    ifalldetails = models.BooleanField(db_column='ifalldetails')
    description = models.TextField(db_column='description', blank=True, null=True)
    imagepath = models.ImageField(db_column='imagepath', upload_to='photos', blank=True, null=True)
    category = models.IntegerField(db_column='category')
    manufacturer = models.IntegerField(db_column='manufacturer')

    def get_url(self):
        return reverse('puzzleinfo',args=[str(self.PK_Puzzle)])

    class Meta:
        db_table = 'Puzzle'
