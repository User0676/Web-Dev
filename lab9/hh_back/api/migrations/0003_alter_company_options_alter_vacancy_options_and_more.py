# Generated by Django 4.2 on 2023-04-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_vacancy_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={},
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(),
        ),
    ]
