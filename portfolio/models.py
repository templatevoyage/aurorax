from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    category = models.ForeignKey(
        "Category", related_name="portfolios", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    project_date = models.DateField(auto_now=True)
    project_url = models.URLField()
    description = models.TextField()
    downloads = models.PositiveIntegerField(default=1323)

    def get_absolute_url(self):
        return reverse("portfolio-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name='images',null=True)