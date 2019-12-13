from django.contrib import admin
from .models import Post, Komen, User
# from ckeditor.widgets import CKEditorWidget


# class AdminBlogForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Post
#         fields = '__all__'


# class AdminBlog(admin.ModelAdmin):
#     form = AdminBlogForm

# Register your models here.
admin.site.register(Post)
admin.site.register(Komen)
admin.site.register(User)