from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Daniel de Almeida
# Developed Full Stack


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='cat_child', on_delete=models.CASCADE)
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Product, self).save()
            self.slug = '%s-%i' % (slugify(self.name), self.id)
        super(Product, self).save(*args, **kwargs)


class ProductQuestion(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    product = models.ForeignKey('Product',  on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Product Questions'

    def __str__(self):
        return self.question


class ProductAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_question = models.ForeignKey(ProductQuestion, on_delete=models.CASCADE)
    answer = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer
