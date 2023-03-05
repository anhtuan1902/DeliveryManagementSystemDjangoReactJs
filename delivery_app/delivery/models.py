from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.safestring import mark_safe


class AdminUser(AbstractUser):
    updated_date = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar/admin/%Y/%m', default='avatar/avatar-default.png')

    def user_img(self):
        return mark_safe('<img src="{}" width="100" alt="avatar"/>'.format(self.avatar.url))


class Customer(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, null=False)
    avatar = models.ImageField(upload_to='avatar/customers/%Y/%m', null=False)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=254, unique=True, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def user_img(self):
        return mark_safe('<img src="{}" width="100" alt="avatar"/>'.format(self.avatar.url))


class Shipper(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, null=False)
    avatar = models.ImageField(upload_to='avatar/%Y/%m', null=False)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=254, unique=True, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    CMND = models.CharField(max_length=50, null=False)
    already_verify = models.BooleanField(default=False)

    def user_img(self):
        return mark_safe('<img src="{}" width="100" alt="avatar"/>'.format(self.avatar.url))


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        # Sắp xếp theo thứ tự giảm dần theo id
        ordering = ['-id']


class Discount(BaseModel):
    discount_title = models.CharField(max_length=50, null=False)
    discount_percent = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    admin = models.ForeignKey(AdminUser, related_name='discounts', on_delete=models.CASCADE)

    def __str__(self):
        return self.discount_title


class Order(BaseModel):
    STATUS = (
        ("CONFIRM", "CONFIRM"),
        ("DELIVERING", 'Delivering'),
        ('RECEIVED', 'Received')
    )

    status_order = models.CharField(max_length=12, choices=STATUS, default='CONFIRM')
    post = models.ForeignKey('Post', related_name='order_post', on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, related_name='order_shipper', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Post(BaseModel):
    title = models.CharField(max_length=100, null=False)
    product_name = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=False)
    product_img = models.ImageField(upload_to='products/%Y/%m', null=False)
    from_address = models.CharField(max_length=150, null=False)
    to_address = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=255, null=True)
    discount = models.ForeignKey(Discount, related_name='order_discount', on_delete=models.SET_DEFAULT, default=0)
    customer = models.ForeignKey(Customer, related_name='posts_customer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Auction(BaseModel):
    content = models.CharField(max_length=150)
    delivery = models.ForeignKey(Shipper, related_name='auctions_delivery', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='auctions_post', on_delete=models.CASCADE)
    had_accept = models.BooleanField(default=False)


class Comment(BaseModel):
    content = models.TextField(max_length=525)
    shipper = models.ForeignKey(Shipper, related_name="comments_shipper", on_delete=models.CASCADE)
    creator = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="comments_creator")

    def __str__(self):
        return self.content


class Rating(BaseModel):
    rate = models.PositiveSmallIntegerField(default=0)
    shipper = models.ForeignKey(Shipper, related_name="rating", on_delete=models.CASCADE)
    creator = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="rating_creator")

    def __str__(self):
        return self.rate
