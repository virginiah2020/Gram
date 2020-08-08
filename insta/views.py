from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

# Create your views here.
def home(request):
    current_user = request.user
    # all_images = Image.objects.all()
    # comments = Comment.objects.all()
    # likes = Likes.objects.all
    # profile = Profile.objects.all()
    # print(likes)
    # return render(request,'home.html',locals())
