# Generated by Django 4.2.7 on 2023-12-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_rename_kvartira_apartaments_title_apartaments_kv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartaments',
            name='date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
