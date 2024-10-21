from django.shortcuts import render




posts=[
    {
        'post_id': 1,
        'course_id':1,
        'sender':'Jaydeep',
        'content':'Welcome to the course C++ Programming!',
        'parent_post_id':0,
        'date_posted':'August 27, 2024',

    },
    {
        'post_id': 1,
        'course_id':1,
        'sender':'Shourya',
        'content':'Sir, how do pointers work?',
        'parent_post_id':0,
        'date_posted':'August 28, 2024',

    },
]

def home(request):
     return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
     return render(request,'register.html')

def courses(request):
     return render(request,'courses.html')

def profile(request):
     return render(request,'profile.html')

def admin_view(request):
     return render(request,'admin_view.html')

def course_details(request):
     return render(request,'course_details.html')
     
def home_unregistered(request):
     return render(request,'home_unregistered.html')

def discussion(request):
    context = {
        'posts': posts
    }
    return render(request,'discussion.html',context)