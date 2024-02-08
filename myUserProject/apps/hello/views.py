from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<center><h1 style='margin:75px 0px 45px'>Django User Registration Shell</h1><h2>Hello Edwardo from Django!</h2></center>")

def home(request):
    return render(request, "hello/hello.html")

# def about(request):
#     return render(request, "hello/about.html")

# def contact(request):
#     return render(request, "hello/contact.html")


# def hello_there(request, name="Buddy"):
#         now = datetime.now()
#         formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
#         # Filter the name argument to letters only using regular expressions. URL arguments
#         # can contain arbitrary text, so we restrict to safe characters only.
#         match_object = re.match("[a-zA-Z]+", name)
    
#         if match_object:
#             clean_name = match_object.group(0)
#         else:
#             clean_name = "Friend"
    
#         content = "Hello there, " + clean_name + "! It's " + formatted_now
#         return HttpResponse(content)

def hello_there(request, name="joe"):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "hello/about.html")
    
def contact(request):
    return render(request, "hello/contact.html")