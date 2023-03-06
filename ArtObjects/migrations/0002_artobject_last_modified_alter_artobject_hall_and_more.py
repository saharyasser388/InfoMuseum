# Generated by Django 4.1.7 on 2023-03-01 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtObjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artobject',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='hall',
            field=models.ForeignKey(default='8', on_delete=django.db.models.deletion.SET_DEFAULT, to='ArtObjects.hall'),
        ),
        migrations.AlterField(
            model_name='artstory',
            name='art_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ArtStory', serialize=False, to='ArtObjects.artobject'),
        ),
        migrations.AlterField(
            model_name='chariot',
            name='art_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject'),
        ),
        migrations.AlterField(
            model_name='holding',
            name='art_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArtObjects.artobject'),
        ),
        migrations.AlterField(
            model_name='other',
            name='art_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='art_object',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject'),
        ),
    ]
