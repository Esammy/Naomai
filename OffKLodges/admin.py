from django.contrib import admin
from .models import Profile, LodgeProperties, Lodge, NewPayment, Payment, FindRoomMate, AgentPersonalInfo, AgentProperties

admin.site.register(Profile)
admin.site.register(LodgeProperties)
admin.site.register(Lodge)
admin.site.register(Payment)
admin.site.register(FindRoomMate)
admin.site.register(AgentPersonalInfo)
admin.site.register(AgentProperties)
admin.site.register(NewPayment)