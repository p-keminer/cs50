from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2)
    url = models.URLField(blank=True)
    category = models.CharField(max_length=24, blank=True)
    winner = models.CharField(max_length =64, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    watchers = models.ManyToManyField(User, related_name="watchlist")


class Bid(models.Model):
    bid = models.DecimalField(max_digits=12, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

class Comments(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")







class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "starting_bid", "url", "category"]