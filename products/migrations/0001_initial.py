# Generated by Django 4.0.3 on 2022-03-21 21:14

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('properties', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]
