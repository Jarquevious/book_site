# Generated by Django 3.0.4 on 2020-04-15 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Author'),
        ),
    ]
