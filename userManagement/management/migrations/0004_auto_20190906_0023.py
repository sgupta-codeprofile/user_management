# Generated by Django 2.0.3 on 2019-09-05 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20190905_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='getallall', to=settings.AUTH_USER_MODEL),
        ),
    ]