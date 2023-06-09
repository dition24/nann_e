# Generated by Django 4.1.7 on 2023-04-26 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_feeding_date_alter_feeding_meal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('A', 'Activity'), ('D', 'Diaper'), ('M', 'Medicine'), ('N', 'Nap'), ('S', 'Sick')], default='A', max_length=1, verbose_name='event type')),
                ('description', models.CharField(max_length=250, verbose_name='event description')),
                ('date', models.DateField(verbose_name='event date')),
                ('time', models.TimeField(verbose_name='event time')),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.kid')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.DeleteModel(
            name='Feeding',
        ),
    ]
