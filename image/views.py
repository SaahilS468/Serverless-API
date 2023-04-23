from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView
import requests
import re

count = 6
# Create your views here.
def home(request):
    template_name = 'home.html'
    return render(request, template_name=template_name)


def getPainting(request):
    template_name = 'arts.html'
    prelink = "https://drive.google.com/uc?export=view&id="
    if request.method == "POST":
        global count
        # request.POST['id']
        imgid = count + 1
        name = request.POST['name']
        link = request.POST['link']
        linkid = re.search(r"\bd\/\w+[^/]([A-Za-z0-9-_])*", link)
        link = prelink + linkid.group()[2:]
        requests.post('https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/image',
                         json = {'imgId':f'{imgid}',
                                 'altText': f'{name}',
                                 'imgUrl': f'{link}'})

    allImages = requests.get("https://kvdvse6qr3.execute-api.ap-south-1.amazonaws.com/img/images")
    
    return render(request, template_name=template_name, context = { 'images': allImages.json()['images'] })

# class getPaintingView(View):
#     template_name = 'arts.html'
#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         print(request)


# class addPaintingView(CreateView):
#     template_name = 'addArt.html'
#     def get(self, request):
#         return render(request, self.template_name)