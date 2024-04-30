from django.db import models
from .validators import validate_file_extension

# Create your models here.

class Author(models.Model):

    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='user_profile_upload/') 
    resume = models.CharField(max_length=200, default = "Default Resume")

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Image(models.Model):
    image = models.ImageField(upload_to='system_image_upload/')
    aditional_info = models.CharField( max_length=20, blank = True, null =  True) 
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return f'Image: {self.aditional_info}'

    def get_absolute_url(self):
        return reverse("Image_detail", kwargs={"pk": self.pk})
class Resource(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField( max_length=100, validators=[validate_file_extension], upload_to='document_upload/')
    description =  models.CharField(max_length=50, null = True, blank = True)
    related_image = models.ForeignKey(Image, on_delete=models.CASCADE, null = True, blank = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  null = True, blank = True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Article Resource"
        verbose_name_plural = "Article Resources"

    def __str__(self):
        return f'Resource: {self.name}'

    def get_absolute_url(self):
        return reverse("Resource_detail", kwargs={"pk": self.pk})

class ArticleType(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "article Type"
        verbose_name_plural = "article Types"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ArticleType_detail", kwargs={"pk": self.pk})


class Article(models.Model):

    name = models.CharField(max_length=200)
    related_image = models.ForeignKey(Image, on_delete=models.CASCADE, blank = True, null = True)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, default=1)
    resources = models.ManyToManyField(Resource, blank =  True, null = True)
    content = models.TextField(default="Default Article Content")
    resume = models.CharField(max_length=200, default = "Default Resume")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  blank =  True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    data = models.CharField(max_length=200)
    article = models.ForeignKey( Article, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    ci = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'Comment: {self.pk}'

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})



