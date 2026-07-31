from django.contrib import admin
from .models import Listing, Bid, Comments, User




admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comments)