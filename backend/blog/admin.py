from django.contrib import admin
from .models import Comment, Post, PostStatusHistory, PostExcerpt, RelatedPost, Like, ReadTime

# Customizing the admin interface for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'status', 'date_posted')
    list_filter = ('status', 'date_posted')
    search_fields = ('title', 'authors__user__username')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('authors',)  # To display the authors as a multiple-select widget

    def get_authors(self, obj):
        return ", ".join(str(author) for author in obj.authors.all())

    get_authors.short_description = 'Authors'

# Register models with the admin site
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(PostStatusHistory)
admin.site.register(PostExcerpt)
admin.site.register(RelatedPost)
admin.site.register(Like)
admin.site.register(ReadTime)
