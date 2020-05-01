from django.contrib import admin

from blog.models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'last_modified', 'is_draft')
    list_filter = ('is_draft',)
    search_fields = ('title__exact',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 18
    actions = ('set_blogs_to_publish',)
    date_hierarchy = 'date_created'
    fields = ('title', 'body', 'slug', 'is_draft')

    def get_ordering(self, request):
        if request.user.is_superuser:
            return 'title', '-date_created',
        return ('title',)

    def set_blogs_to_publish(self, request, queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request, '{} blog telah berhasil dipublikasi'.format(count))

    set_blogs_to_publish.short_description = 'Tandai blog terpilih sebagai publik'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
