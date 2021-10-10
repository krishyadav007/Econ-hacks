from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
# Create your views here.
def home(request):
    query = request.GET.get("title")
    allInfras = None
    if query:
        allInfras = Infra.objects.filter(name__icontains=query)
    else:
        allInfras = Infra.objects.all()  # select * from Infra
    
    context = {
        "Infras": allInfras,
    }

    return render(request, 'main/index.html', context)

# detail page
def detail(request, id):
    infrastructure = Infra.objects.get(id=id) # select * from Infra where id=id
    reviews = Review.objects.filter(Infra=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "Infra": infrastructure,
        "reviews": reviews,
        "average": average
    }
    return render(request, 'main/details.html', context)


# add Infras to the database
def add_Infras(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = InfraForm(request.POST or None)

                # check if the form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form = InfraForm()
            return render(request, 'main/addInfras.html', {"form": form, "controller": "Add Infras"})
        
        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login")    


# edit the Infra
def edit_Infras(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the Infras linked with id
            infrastructure = Infra.objects.get(id=id)

            # form check
            if request.method == "POST":
                form = InfraForm(request.POST or None, instance=infrastructure)
                # check if form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = InfraForm(instance=infrastructure)
            return render(request, 'main/addInfras.html', {"form": form, "controller": "Edit Infras"})
        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login") 


# delete Infras
def delete_Infras(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the moveis
            infrastructure = Infra.objects.get(id=id)

            # delte the Infra
            infrastructure.delete()
            return redirect("main:home")
        # if they are not admin
        else:
            return redirect("main:home")

    # if they are not loggedin
    return redirect("accounts:login") 

def add_review(request, id):
    if request.user.is_authenticated:
        infrastructure = Infra.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.Infra = infrastructure
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")


# edit the review
def edit_review(request, Infra_id, review_id):
    if request.user.is_authenticated:
        infrastructure = Infra.objects.get(id=Infra_id)
        # review
        review = Review.objects.get(Infra=infrastructure, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                         error = "Out or range. Please select rating from 0 to 10."
                         return render(request, 'main/editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("main:detail", Infra_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form": form})
        else:
            return redirect("main:detail", Infra_id)
    else:
        return redirect("accounts:login")


# delete reivew
def delete_review(request, Infra_id, review_id):
    if request.user.is_authenticated:
        infrastructure = Infra.objects.get(id=Infra_id)
        # review
        review = Review.objects.get(Infra=infrastructure, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission to delete
            review.delete()

        return redirect("main:detail", Infra_id)
            
    else:
        return redirect("accounts:login")