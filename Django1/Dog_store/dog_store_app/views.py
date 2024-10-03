from django.shortcuts import render,redirect
from dog_store_app.models import dog_Crud

def index(request):
    return render(request, 'index.html')


def cart(request):
    # if request.method == 'POST':
    #     Product_For=request.POST['Product_For']
    #     Product_name=request.POST['Product_name']
    #     create=dog_Crud.objects.create(Product_For=Product_For,Product_name=Product_name)
    #     create.save()
    #     return redirect('index')
    return render(request, 'cart.html')

def add(request):
    if request.method == 'POST':
        Product_For=request.POST['Product_For']
        Product_name=request.POST['Product_name']
        create=dog_Crud.objects.create(Product_For=Product_For,Product_name=Product_name)
        create.save()
        return redirect('/read/')
    return render(request, 'productadd.html')

def read(request):
    reads=dog_Crud.objects.all().order_by('id')  # F
    return render(request,'dog_read.html',{'reads':reads})

def edit(request,id):
    edit=dog_Crud.objects.get(id=id)
    return render(request,'dog_edit.html',{'edit':edit})

def update(request,id):
    if request.method=="POST":
        Product_For=request.POST['Product_For']
        Product_name=request.POST['Product_name']
        get=dog_Crud.objects.get(id=id)
        get.Product_For=Product_For
        get.Product_name=Product_name     
        get.save()
        return redirect('/read/')
    return redirect("/edit/id/")

def delete(request,id):
    dels=dog_Crud.objects.get(id=id)
    dels.delete()
    return redirect('/read/')