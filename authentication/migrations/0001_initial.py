# Generated by Django 3.2.1 on 2021-05-14 19:27

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.user')),
                ('company_name', models.CharField(default='Missing', max_length=60, verbose_name='company name')),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.user')),
                ('first_name', models.CharField(default='Missing', max_length=60, verbose_name='first name')),
                ('last_name', models.CharField(default='Missing', max_length=60, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('funds', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='funds')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.company')),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='buy price')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='sell price')),
            ],
        ),
        migrations.CreateModel(
            name='AcquiredStock',
            fields=[
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.stock', verbose_name='stock')),
                ('investors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.investor')),
            ],
        ),
    ]
