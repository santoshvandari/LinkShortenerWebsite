from django.contrib import admin
from main.models import URLTable

# Register your models here.
class URLTableDisp(admin.ModelAdmin):
    list_display = ('id','url', 'short_url')
admin.site.register(URLTable,URLTableDisp)