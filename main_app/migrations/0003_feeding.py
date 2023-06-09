# Generated by Django 4.1.7 on 2023-04-25 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_kid_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('meal', models.CharField(choices=[('M', 'Milk/Formula'), ('BF', 'Baby Food/Puree'), ('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snack')], default=5, max_length=2)),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.kid')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
