# Generated by Django 4.0.1 on 2022-01-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DressingUp', '0007_alter_jacket_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jacket',
            name='photo',
            field=models.ImageField(default='images/jacket.jpeg', upload_to='images/Jackets/%Y-%m-%d/'),
        ),
    ]
