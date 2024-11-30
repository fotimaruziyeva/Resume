from django.contrib import admin
from .models import Contact, Blog

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
      list_display = ("name", "email", "subject", "budget")  
      search_fields = ("name", "email")  
      list_filter = ("budget",) 

admin.site.register((Blog))

