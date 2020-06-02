# Generated by Django 2.2.5 on 2020-06-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech_to_text', '0003_auto_20200602_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='result',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='resulted_on',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='uploaded_on',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
