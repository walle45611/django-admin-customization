from django.shortcuts import render

def home(request):
    context = {
        'slides': [
            {'image_url': 'https://fakeimg.pl/250x100/', 'caption': 'Caption for image 1'},
            {'image_url': 'https://fakeimg.pl/250x100/', 'caption': 'Caption for image 2'},
            {'image_url': 'https://fakeimg.pl/250x100/', 'caption': 'Caption for image 3'},
        ]
    }
    return render(request, 'home/home.html', context)
