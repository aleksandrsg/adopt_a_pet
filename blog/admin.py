from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date',
        'body',
    )

admin.site.register(Comment, CommentAdmin)