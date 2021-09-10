from django.contrib import admin
from .models import Comment

admin.site.register(Comment)
admin.site.site_header = "Lungelo Software"
admin.site.site_title = "Lungelo Software"
admin.site.index_title = "Lungelo Software"