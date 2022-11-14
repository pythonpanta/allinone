from django.db import models
import uuid
import datetime

from user.models import User
# Create your models here.


def uuid_generate():
    return uuid.uuid4().hex
# Create your models here


class MyCustomField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp'


class BaseModel(models.Model):
    id = models.CharField(max_length=32, unique=True,
                          primary_key=True, default=uuid_generate)
    creaed_at = MyCustomField(null=True)
    created_by = models.ForeignKey(
        "user.User", on_delete=models.PROTECT, related_name="+", db_column="created_by")
    updated_at = MyCustomField(null=True)
    updated_by = models.CharField(max_length=150)
    is_void = models.BooleanField(default=False)
    void_remarks = models.CharField(max_length=150, null=True)

    class Meta:
        abstract = True


class Customer(BaseModel):

    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.PROTECT, related_name="+")
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.BinaryField()

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.name


class Product(BaseModel):
    STATUS_CHOICES = (
        ("0", "Delivered"),
        ("1", "pending"),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.ForeignKey(
        'clg_api.Category', null=True, on_delete=models.PROTECT, related_name="+")
    sub_category = models.ForeignKey(
        'clg_api.SubCategory', null=True, on_delete=models.PROTECT, related_name="+")
    manufactured_date = models.DateField(
        default=datetime.datetime.now(), null=True)
    photo = models.BinaryField(null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='1')
    description = models.TextField(null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Order(BaseModel):
    STATUS = (('Pending', 'Pending'),
              ('Out for delivery', 'Out for delivery'),
              ('Delivered', 'Delivered'),
              )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.PROTECT, related_name="+")
    product = models.ForeignKey(
        Product, null=True, on_delete=models.PROTECT, related_name="+")
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = "order"

    def __str__(self) -> str:
        return self.product.name


class Province(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'province'

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    province_id = models.ForeignKey(
        Province, on_delete=models.PROTECT, db_column='province_id', related_name="+")

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    province_id = models.ForeignKey(
        Province, on_delete=models.PROTECT, db_column='province_id', related_name="+")
    district_id = models.ForeignKey(
        District, on_delete=models.PROTECT, db_column='district_id', related_name="+")

    class Meta:
        db_table = 'municipality'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(
        Category, related_name="+", on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'sub_category'

    def __str__(self):
        return self.name
