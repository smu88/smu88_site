from django import forms
from django.contrib import admin

from .models import Project, ProjectPhoto, AboutInfo, Innovation, Iframe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutInfoAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutInfo
        fields = '__all__'


class InnovationAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Innovation
        fields = '__all__'


class AboutInfoAdmin(admin.ModelAdmin):
    form = AboutInfoAdminForm


class InnovationAdmin(admin.ModelAdmin):
    form = InnovationAdminForm
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    max_num = 10
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)


class IframeAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Iframe, IframeAdmin)
admin.site.register(ProjectPhoto)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(Innovation, InnovationAdmin)
