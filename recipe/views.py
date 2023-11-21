from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_decription = data.get('recipe_decription')
        recipe_image = request.FILES.get("recipe_image")

        # print(recipe_name)
        # print(recipe_decription )
        # print(recipe_image)

        Recipe.objects.create(

            recipe_image = recipe_image ,
            recipe_name = recipe_name ,
            recipe_decription = recipe_decription ,
           

        )
        

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
        
    context= { 'recipes' : queryset }
    return render(request , "recipe/form.html" ,  context)

def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_decription = data.get('recipe_decription')
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_decription = recipe_decription

        if recipe_image:
           queryset.recipe_image = recipe_image


        queryset.save()
        return redirect('/recipes/')


    context = {'recipe' : queryset}
    return render(request , "recipe/update.html" ,  context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')
    
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request , "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request , "Invalid Password")
            return redirect('/login/')
        else:
            login(request ,user)
            return redirect('/recipes/')
        
    return render(request,'recipe/login.html') 


def logout_page(request):
    logout(request)

    return redirect('/login/')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "User already exist")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username =  username,
                 
            
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Successfully! Account created.")
        return redirect('/register')
    return render (request,'recipe/register.html')