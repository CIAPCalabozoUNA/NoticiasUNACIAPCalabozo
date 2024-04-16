from django.db import models

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
    author = models.CharField(max_length=100, null=True)


    class Meta:
        verbose_name = "article Resource"
        verbose_name_plural = "article Resources"

    def __str__(self):
        return self.name

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
    image = models.URLField(max_length=200)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, default=1)
    resources = models.ManyToManyField(Resource)


    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})


