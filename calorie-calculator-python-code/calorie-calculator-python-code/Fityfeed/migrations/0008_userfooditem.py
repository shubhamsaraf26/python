# Generated by Django 3.0.6 on 2020-07-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0007_fooditem_calorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFooditem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem', models.ManyToManyField(to='Fityfeed.Fooditem')),
            ],
        ),
    ]
