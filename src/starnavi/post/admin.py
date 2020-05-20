from django.contrib import admin

from starnavi.post.models import Post, Like


class LikeAdmin(admin.TabularInline):
    model = Like
    fields = ['user', 'date']
    readonly_fields = ['date']


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'author')}),
        ('Main', {'fields': ('text',)}),
        ('Important dates', {'fields': ('date_created', 'date_modified')})
    )
    readonly_fields = ('id', 'date_created', 'date_modified')

    inlines = (LikeAdmin,)


admin.site.register(Post, PostAdmin)
