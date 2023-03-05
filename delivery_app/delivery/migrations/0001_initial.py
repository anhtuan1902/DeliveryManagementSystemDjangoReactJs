# Generated by Django 4.1.7 on 2023-03-05 15:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(default='avatar/avatar-default.png', upload_to='avatar/admin/%Y/%m')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('avatar', models.ImageField(upload_to='avatar/customers/%Y/%m')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('discount_title', models.CharField(max_length=50)),
                ('discount_percent', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('avatar', models.ImageField(upload_to='avatar/%Y/%m')),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('CMND', models.CharField(max_length=50)),
                ('already_verify', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('rate', models.PositiveSmallIntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_creator', to='delivery.customer')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='delivery.shipper')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('product_img', models.ImageField(upload_to='products/%Y/%m')),
                ('from_address', models.CharField(max_length=150)),
                ('to_address', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_customer', to='delivery.customer')),
                ('discount', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='order_discount', to='delivery.discount')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('status_order', models.CharField(choices=[('CONFIRM', 'CONFIRM'), ('DELIVERING', 'Delivering'), ('RECEIVED', 'Received')], default='CONFIRM', max_length=12)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_post', to='delivery.post')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_shipper', to='delivery.shipper')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.TextField(max_length=525)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_creator', to='delivery.customer')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_shipper', to='delivery.shipper')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=150)),
                ('had_accept', models.BooleanField(default=False)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions_delivery', to='delivery.shipper')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions_post', to='delivery.post')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
