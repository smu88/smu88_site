from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


def project_image_directory_path(instance, filename):
    """Create path for save photo """
    return f'{instance.project.name}/{filename}'


class AboutInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = RichTextUploadingField()

    class Meta:
        verbose_name = 'текст на главной'
        verbose_name_plural = 'текст на главной'

    def __str__(self):
        return f'{self.title}'


class Project(models.Model):
    """Строительный объект(ЖК)"""

    name = models.CharField(max_length=255, verbose_name='название объекта')
    slug = models.SlugField(max_length=255, verbose_name='slug объекта')

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проект'

    def __str__(self):
        return f'{self.name}'


class ProjectPhoto(models.Model):
    """Фото для проекта(объектов строительства)"""

    image = models.ImageField(upload_to=project_image_directory_path, verbose_name='фото проекта')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='image', verbose_name='проект')

    class Meta:
        verbose_name = 'фото проекта'
        verbose_name_plural = 'фото проекта'

    def __str__(self):
        return f'{self.project}'


class Innovation(models.Model):
    """Раздел инноваций на сайте"""

    title = models.CharField(max_length=255, verbose_name='заголовок инновации')
    slug = models.SlugField(max_length=255, verbose_name='slug инновации')
    text = RichTextUploadingField()
    image = models.ImageField(upload_to='innovations_image', verbose_name='картинка')

    class Meta:
        verbose_name = 'инновация'
        verbose_name_plural = 'инновации'

    def __str__(self):
        return f'{self.title}'


class Iframe(models.Model):
    title = models.CharField(max_length=255, verbose_name='название формы')
    iframe = models.TextField(verbose_name='iframe форма')

    class Meta:
        verbose_name = 'форма iframe'
        verbose_name_plural = 'формы iframe'

    def __str__(self):
        return f'{self.title}'



