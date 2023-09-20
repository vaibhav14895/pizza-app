from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import pizza_add





def home(request):
    pizzas =pizza.objects.all()
    context={'pizzz':pizzas}
    return render(request,'home.html',context)

def login_page(request):   # sourcery skip: extract-method, last-if-guard, use-named-expression
 if request.method == 'POST':
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_objects = User.objects.filter(username=username)
        if not user_objects.exists:
            messages.warning(request, 'username does not exist')
            return redirect('login')
        user_objects = authenticate(username=username,password=password)
        if user_objects:
            login(request,user_objects)
            return redirect('/')
        messages.success(request, 'wrong password')
        return redirect('login')
    except Exception as e:
        messages.error(request, 'wrong credentials')
        return redirect(request, 'register')
    
 return render(request,'login.html')
    
    
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check if the username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken.')
                return redirect('register')

            # Create a new user
            user_object = User.objects.create(username=username)
            user_object.set_password(password)
            user_object.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')
        except Exception as e:
            messages.error(
                request, 'Something went wrong during registration.')

        return redirect('register')

    return render(request, 'register.html')



def logout_page(request):
    logout(request)
    return redirect('home')


@login_required   # used for those functions which should active when user is logged in
def addcart(request,pizza_uid):
    user = request.user
    pizza_obj=pizza.objects.get(uid=pizza_uid)
    # By using the underscore (, _) as a variable name, you're essentially discarding the boolean value returned by the get_or_create method. This way, you only store the cart object in the Cart variable, which can then be assigned to the "cart" field in the creation of the "cartitems" object.
    Cart, _ = cart.objects.get_or_create(user=user, is_paid=False)
    cart_obj = cartitems.objects.create(
        cart =Cart,
        pizza=pizza_obj
    )
    return redirect('/')
    

def orderpage(request):
    cartpay=cart.objects.get(is_paid=False,user=request.user)
    context={}
    if request.method == 'POST':
        price=request.POST.get('price')
        user=request.user
        context={'price':price,'user':user} 
        return render(request,'payment.html',context)
    context={'carts':cartpay}
    return render (request,'cart.html',context)

def removeitem(request,item_uid):
    try:
     cartitems.objects.get(uid=item_uid).delete()
     return redirect('cart')
    except Exception as e:
        print(e)
        
def payment(request):
    return render(request,'payment.html')



#CRUD operation for production
def production(request):
    all_pizza=pizza.objects.all()
    return render(request ,'production.html',{'all_pizza':all_pizza})


def edit_pizza(request, uid):
    instance_object = get_object_or_404(pizza, uid=uid)

    if request.method == 'POST':
        edit = pizza_add(request.POST, request.FILES, instance=instance_object)
        if edit.is_valid():
            x = edit.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('production')  # Redirect to a pizza list view after editing
    else:
        edit = pizza_add(instance=instance_object)

    return render(request, 'pizza_add.html', {'pizza_form': edit, 'pizza_instance': instance_object})


def delete_pizza(request,uid):
    x=pizza.objects.filter(uid=uid)
    x.delete()
    return redirect('production')

def add_pizza(request):
    if request.method == 'POST':
        d = pizza_add(request.POST, request.FILES)
        if d.is_valid():
            pizza_instance = d.save(commit=False)
            pizza_instance.user = request.user  # Assign the user who added the pizza
            pizza_instance.save()
            return redirect('home')
        else:
            print(d.errors)  # Print form errors for debugging
    else:
        d = pizza_add()
    
    return render(request, 'pizza_add.html', {'pizza_form': d})



