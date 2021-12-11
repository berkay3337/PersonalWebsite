from django.contrib import admin
from post.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date','slug']
    list_display_links = ['title']
    list_filter = ['publishing_date']
    search_fields = ['title', 'post_content']
    
    

    class Meta:
        model = Post
admin.site.register(Post,PostAdmin)
