from django.contrib import admin
from .models import AssetRequest
# Register your models here.


@admin.register(AssetRequest)
class Requests(admin.ModelAdmin):
    class Meta:
        model = AssetRequest