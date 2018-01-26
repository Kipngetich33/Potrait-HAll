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
    name = models.CharField(max_length =30,null= True)
    image_description = models.CharField(max_length =3000)
    location = models.ForeignKey(Location,null = True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


    def save_images(self):
        self.save()

    def delete_images(self):
        self.delete()

    def update_image(self,new_name):
        self.name= new_name
        self.save()

    @classmethod
    def get_images(cls):
        retrieved_images= Image.objects.all()
        return retrieved_images

    @classmethod
    def get_images_categories(cls,id):
        retrieved_images_category = cls.objects.filter(categories = id).all()
        return retrieved_images_category 

    @classmethod
    def get_requested_images(cls,search_name):
        requested_image = cls.objects.filter(image_name = search_name).all()
        return requested_image

    @classmethod
    def search_image_name(cls,search_term):
        search_result=cls.objects.filter(name__icontains = search_term)
        return search_result
        
 




