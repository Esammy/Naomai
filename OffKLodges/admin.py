from django.contrib import admin
from .models import Profile, LodgeProperties, Lodge, Payment, FindRoomMate

admin.site.register(Profile)
admin.site.register(LodgeProperties)
admin.site.register(Lodge)
admin.site.register(Payment)
admin.site.register(FindRoomMate)