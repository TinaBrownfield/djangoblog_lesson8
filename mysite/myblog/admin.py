from django.contrib import admin

# Register your models here.
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    fields = ('category',)

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'author', 'published_date']
    inlines = [CategoryInline,]
    
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts',]


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)