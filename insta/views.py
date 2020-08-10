from django.shortcuts import render,redirect
from django.http  import Http404
from .models import Image, Profile,Comment
# Create your views here.
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    # likes = Likes.objects.all
    profile = Profile.objects.all()
    # print(likes)
    return render(request,'home.html',locals())

def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')

    else:
        form = ImageForm()
    
    return render(request,'image.html',locals())

def profile(request):
    current_user = request.user
    # profile_details = Profile.objects.get(owner_id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/new.html', locals())

