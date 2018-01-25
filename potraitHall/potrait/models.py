from django.db import models

class Location(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name
    
    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

    def save_categories(self):
        self.save()

    def delete_categories(self): 
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =3000)
    location = models.ForeignKey(Location,null = True)
    category = models.ForeignKey(Category, null = True)  

    def __str__(self):
        return self.image_name

    def save_images(self):
        self.save()

    def delete_images(self):
        self.delete()

    @classmethod
    def get_images(cls):
        retrieved_images= Image.objects.all()
        return retrieved_images

    @classmethod
    def get_images_categories(cls):
        retrieved_images_category = cls.objects.filter(location = 'Nairobi').all()
        return retrieved_images_category

    @classmethod
    def get_requested_images(cls,search_name):
        requested_image = cls.objects.filter(image_name = search_name).all()
        return requested_image
 




