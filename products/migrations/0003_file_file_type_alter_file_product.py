# Generated by Django 4.2 on 2024-04-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_text_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=2, verbose_name='file type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.product', verbose_name='product'),
        ),
    ]
