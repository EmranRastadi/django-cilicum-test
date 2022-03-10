from django.contrib import admin
from .models import Articles


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
        'createdAt',
        'status',
    )
    list_filter = (
        'status',
        'createdAt'
    )
    search_fields = (
        'title',
        'slug',
        'description'
    )
    ordering = ['status', '-publish']


admin.site.register(Articles, ArticleAdmin)
