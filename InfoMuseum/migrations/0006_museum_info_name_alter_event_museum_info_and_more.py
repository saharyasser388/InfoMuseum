# Generated by Django 4.1.7 on 2023-03-04 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InfoMuseum', '0005_alter_event_museum_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum_info',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='museum_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Events', to='InfoMuseum.museum_info'),
        ),
        migrations.AlterField(
            model_name='media',
            name='museum_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InfoMuseum.museum_info'),
        ),
        migrations.AlterField(
            model_name='museum_info',
            name='contact_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='openning_hour',
            name='day',
            field=models.CharField(blank=True, choices=[('FR', 'Friday'), ('ST', 'Saturday'), ('SN', 'Sunday'), ('MN', 'Monday'), ('TU', 'Tuseday'), ('WE', 'Wednesday'), ('TH', 'Thursday')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='openning_hour',
            name='museum_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='openning_Hours', serialize=False, to='InfoMuseum.museum_info'),
        ),
        migrations.AlterField(
            model_name='user',
            name='museum_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='InfoMuseum.museum_info'),
        ),
    ]
