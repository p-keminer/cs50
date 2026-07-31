from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Bid, Comments, ListingForm, Listing
from django.db.models import Max

from django.contrib.auth.decorators import login_required

from decimal import Decimal


def get_highest_bid(listing):
    highest_bid = listing.bids.aggregate(Max("bid"))["bid__max"]
    if highest_bid is None:
        highest_bid = listing.starting_bid
    return highest_bid

def is_closed(listing):
    is_closed = 0
    if listing.winner:
        is_closed = 1 
    return is_closed

def index(request):
    listings = Listing.objects.all()
    offers = [];
    for listing in listings:
        if not is_closed(listing):
            highest_bid = get_highest_bid(listing)
            offers.append((listing,highest_bid))
    return render(request, "auctions/index.html", {
        "offers" : offers
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

 

def create(request):

    if request.method == "POST":
        formular = ListingForm(request.POST)
        
        if formular.is_valid():

            title = formular.cleaned_data["title"]
            if Listing.objects.filter(title=title).exists():
                return render(request, "auctions/create.html", {"formular": formular, "title_exists": 1})
            listing = formular.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect("index")
    else:
        formular = ListingForm()
    return render(request, "auctions/create.html", {"formular": formular, "title_exists": 0})



def show(request, title_item , bad_req=None):
    listing = Listing.objects.get(title=title_item)
    comments = listing.comments.all()
    if not comments.exists():
        comments = []
    

    watchlist = listing.watchers.all()
    user = request.user
    on_watchlist = 0
    if user in watchlist:
        on_watchlist = 1 

    return render(request, "auctions/item.html", {
        "listing" : listing,
        "comments" : comments,
        "on_watchlist" : on_watchlist,
        "bid" : get_highest_bid(listing),
        "bad_req" : bad_req,
        "user" : user,
        "is_closed" : is_closed(listing)
        
    })

@login_required
def save(request, title):
    if request.method == "POST":
        listing = Listing.objects.get(title=title)
        user = request.user
        listing.watchers.add(user)
        print(listing.watchers.all())
        return show(request, title)
    else:
        return show(request, title)

@login_required   
def delete(request, title):
    if request.method == "POST":
        listing = Listing.objects.get(title=title)
        user = request.user
        listing.watchers.remove(user)
        print(listing.watchers.all())
        return show(request, title)
    else:
       return show(request, title)

@login_required
def bid(request, title):
    if request.method == "POST":
        listing = Listing.objects.get(title=title)
        bid_raw = request.POST.get("bid")
        if get_highest_bid(listing) > Decimal(bid_raw):
                return show(request, title, bad_req=1)
        listing.bids.create(bid=bid_raw, owner=request.user)
        return show(request, title)
    else:
        return show(request, title)
    
@login_required
def close(request, title):
    if request.method == "POST":
        listing = Listing.objects.get(title=title)
        highest_bid = listing.bids.order_by("-bid").first()
        if highest_bid is None:
            listing.winner = listing.owner.username
        else:
            listing.winner = listing.winner.owner.username
        listing.save()
        return show(request, title)
    else:
        return show(request, title)
    
@login_required
def comment(request, title):
    if request.method == "POST":
        listing = Listing.objects.get(title=title)
        comment_ = request.POST.get("comment")
        print(comment)
        listing.comments.create(comment=comment_,owner=request.user)
        return show(request, title)
    else:
        return show(request, title)

@login_required    
def watchlist(request):
    listings = request.user.watchlist.all()
    offers = [];
    for listing in listings:
        if not is_closed(listing):
            highest_bid = get_highest_bid(listing)
            offers.append((listing,highest_bid))
    return render(request, "auctions/watchlist.html", {
        "offers" : offers
        })

def category(request):
    categories = Listing.objects.values_list("category", flat=True).distinct()
    print(categories)
    return render(request, "auctions/category.html", {
        "categories" : categories
        })


def items_category(request, category):
    listings = request.user.watchlist.all()
    offers = [];
    for listing in listings:
        if listing.category == category:
            highest_bid = get_highest_bid(listing)
            offers.append((listing,highest_bid))
    return render(request, "auctions/items_category.html", {
        "offers" : offers,
        "category" : category
        })
   