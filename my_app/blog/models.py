from django.db import models
from django.shortcuts import reverse, get_object_or_404
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.


class UserDb(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=200)
    Message = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.Message)


class item(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.IntegerField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)


class LatestProduct(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


class LatestProductOne(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


class TopProduct(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


class TopProductOne(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


class ReviewProduct(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


class ReviewProductOne(models.Model):
    items_name = models.CharField(max_length=300)
    price = models.FloatField()
    Description = models.TextField(max_length=600, blank=True)
    Image = models.ImageField()
    slug = models.SlugField()

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.items_name)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })


PRODUCT_CHOICE = {
    'Jordan': 'Jordan',
    'nike': 'Nike',
    'man': 'Man',
}


class ShopMain(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)


class Shoes(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Shoes'


class Watches(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Watches'


class Slippers(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Slippers'


class Shorts(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Shorts'


class Pants(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Pants'


class Shirts(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(max_length=3000)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("shop-details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })

    class Meta:
        verbose_name_plural = 'Shirts'


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    objects = models.Manager()

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    objects = models.Manager()
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def get_sub_total(self):
        subtotal = 0
        for order_item in self.items.all():
            subtotal += order_item.item.price
        return subtotal


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Country = CountryField(multiple=True)
    street_address = models.CharField(max_length=100)
    Apartment_address = models.CharField(max_length=100)
    Town_or_City = models.CharField(max_length=100)
    Zip = models.CharField(max_length=100)
    Phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.TextField(max_length=800)
    slug = models.SlugField(blank=True)


class PostForm(models.Model):
    title = models.TextField(max_length=800)
    answers = models.TextField(max_length=800)
    slug = models.SlugField(blank=True)