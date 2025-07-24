from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "новости"
        verbose_name = "новость"

