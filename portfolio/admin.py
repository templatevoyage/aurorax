from django.contrib import admin
from .models import Portfolio, Category, Image


class ImageInline(admin.StackedInline):
    model = Image


class PortfolioAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    model = Portfolio
    fields = ("title", "description", "downloads")


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category)
admin.site.register(Image)
