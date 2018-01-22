from django.db import models

class Location(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/',blank =True)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =3000)
    location = models.ForeignKey(Location,null = True)
    category = models.ForeignKey(Category, null = True) 

    def __str__(self):
        return self.first_name

    def save_images(self):
        self.save()

    def delete_images(self):
        self.delete()





