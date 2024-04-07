from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField



class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Advert (models.Model):
    user= models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
    verbose_name='Author of the ad', related_name='adverts',
    )
    category = models.CharField(*args:('Category'), max_length=20,
    title=models.CharField(*args('Title'), max_length=100)
    content = models.CharField(_('Description'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=)
    file = models.FileField(verbose_name="File", upload_to="files/")

    def __str__(self):
        return f'{self.title}, {self.category}, {self.created}'

    def get_absolute_url(self):
        return reverse(viewname: 'advert_detail', kwargs={'pk': self})

    def reply(self):
        return Response.objects.filter(pk=self.pk)

    class Meta:
        verbose_name = ('Advert')
        verbose_name_plural = ('Advert')
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Заголовок')
    text = RichTextUploadingField()
    datetime_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class Response(models.Model):
    text = models.TextField()
    datetime_response = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    accept = models.BooleanField(default=False)
    advert = models.ForeignKey(
        Advert,
        on_delete=models.CASCADE,
        verbose_name=('Advert'),
        related_name='responses'
    )
     user = models.ForeignKey(
         User,
         on_delete=models.CASCADE(
             User,
             on_delete=models.CASCADE(),
             verbose_name='Author of the ad',
             related_name='responces'
    ))
    accept = models.BooleanField(default=False, verbose_name='Accept')

    def __str__(self):
        return f'{self.text[:20]}...'

    def get_absolute_url(self):
        return f'/response/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)