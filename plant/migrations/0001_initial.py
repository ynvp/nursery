# Generated by Django 3.1 on 2020-08-10 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nursery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='plant.jpeg', upload_to='plant_pics')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
                ('favorite', models.ManyToManyField(related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('nursery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.nursery')),
            ],
        ),
    ]
