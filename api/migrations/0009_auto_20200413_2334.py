# Generated by Django 3.0.3 on 2020-04-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200413_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledactivity',
            name='precip_probability',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='scheduledactivity',
            name='temp_hi',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='scheduledactivity',
            name='temp_low',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='scheduledactivity',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
