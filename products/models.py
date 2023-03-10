from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(verbose_name=_('Avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(verbose_name=_('Is Enable'), default=True)
    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = _('categories')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)

    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, _('Audio')),
        (FILE_VIDEO, _('Video')),
        (FILE_PDF, _('PDF')),
    )

    product = models.ForeignKey('Product', related_name='files', verbose_name=_('Product'), on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    file_type = models.IntegerField(_('file type'), choices=FILE_TYPES,default=2)
    file = models.FileField(_('File'), upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
