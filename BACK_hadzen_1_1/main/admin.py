from django.contrib import admin
from .models import *
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'create_field', 'update_field','delete_comm', 'red_ch','ch')


admin.site.register(Bl)
admin.site.register(Ch)
admin.site.register(Comm)
admin.site.register(LikeDisComm)
admin.site.register(LikeDisShareBl)
admin.site.register(Manager,MyModelAdmin)
admin.site.register(Subs)
