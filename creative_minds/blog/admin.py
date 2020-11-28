from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post
# Register your models here.


class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'publish_date')
    fields = ['title', 'author', 'create_date']  # after opening the post

    # when using foreign key as the search parameter we should specific which foreignKey__fieldName
    # as author is the FK in Post model we cannot use author to search the row/entry because it is the object
    # so we have to use field/column from the author model
    # that is username or any such field.
    # so here it is author__name
    search_fields = ['title', 'author__username']
    readonly_fields = ('create_date', 'author')

    list_filter = ('create_date', 'publish_date')
    filter_horizontal = ()
    fieldsets = ()
    # now title can be edited from the list
    # list_editable = ['publish_date']


admin.site.register(Post, PostAdmin)
