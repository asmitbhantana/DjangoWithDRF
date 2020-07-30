from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Create your views here.
def manage_media(request):
    if request.method == 'POST':
        print("post data", request.POST)
        print("Files ", request.FILES)
        file_object = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(file_object.name, file_object)

    return render(request, 'media.html')


def manage_static(request):
    return render(request, 'static.html')
