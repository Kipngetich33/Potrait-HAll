from django.http  import HttpResponse,Http404
from django.shortcuts import render
from .models import Image

# Views will be created here
def index(request):
    all_images = Image.get_images()
    return render(request, 'all-pics/all_pics.html',{"all_images":all_images}) 
    
def home(request):
    return render(request ,'all-pics/home.html')

def categories(request,category):
    category_images = Image.get_images_categories(category)

    def determinine_category(category):
        if category == '1':
            return 'Animals'
        elif category == '2':
            return 'Science'
        elif category == '3':
            return 'Celebrities'
        elif category == '4':
            return 'Scenary'
        else:
            return 'All'

    message =determinine_category(category)

    return render(request,'all-pics/category.html',{"images":category_images,"message":message})

def details(request,photo_id):
    requested_image = Image.objects.get(id= photo_id)
    return render(request,'all-pics/details.html',{"requested_image" :requested_image})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get("image")
        searched_images = Image.search_image_name(search_term)
        message=f"{search_term}"
        return render(request,'all-pics/search.html', {"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

