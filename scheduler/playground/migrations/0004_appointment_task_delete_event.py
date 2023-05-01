# Generated by Django 4.2 on 2023-05-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_alter_event_event_type_delete_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('repetition', models.CharField(choices=[('Never', 'Never'), ('Every Day', 'Every Day'), ('Every Week', 'Every Week'), ('Every Month', 'Every Month'), ('Every Year', 'Every Year')], default='Never', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('expected_time', models.IntegerField()),
                ('date', models.DateField()),
                ('importancy_level', models.CharField(choices=[('Low', 'Low'), ('Middle', 'Middle'), ('High', 'High')], default='Low', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
