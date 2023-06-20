from django.contrib import admin
from .models import Food, Users, Message, Rating, Comment

admin.site.register(Food)
admin.site.register(Users)
admin.site.register(Message)
admin.site.register(Rating)
admin.site.register(Comment)

