from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.contenttypes.models import ContentType
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
from djmoney.models.fields import MoneyField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэги')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('title',)

    def __str__(self):
        return self.title


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset()\
                                         .filter(publish__lte=timezone.now())


class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='post_category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, verbose_name='Тэг', related_name='post_tag')
    title = models.CharField(max_length=200, verbose_name='Название')
    content = RichTextUploadingField(verbose_name='Контент')
    image = models.ImageField(upload_to='post/%Y/%m', verbose_name='фото')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)
    slug = AutoSlugField(verbose_name='url', populate_from='title')
    objects = PublicManager()  # Our custom manager.

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk,

                                              })


    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comments.objects.filter_by_instance(instance)
    #     return qs
    #
    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

    def __str__(self):
        return self.title


class PostCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'publish'
    moderate_after = 365


moderator.register(Post, PostCommentModerator)


class Sale(models.Model):
    product = models.CharField(max_length=128, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание')
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT')
    category = models.ForeignKey(Category,  verbose_name='Категория', related_name='sale_category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, verbose_name='Тэг', related_name='sale_tag')
    slug = AutoSlugField(populate_from='product')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sales/%Y/%m', verbose_name='фото')
    objects = PublicManager()  # Our custom manager.

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('sale-detail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.product

