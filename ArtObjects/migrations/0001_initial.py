# Generated by Django 4.1.7 on 2023-03-01 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('epoch', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtStory',
            fields=[
                ('story', models.TextField(blank=True, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ArtS', serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedCollection',
            fields=[
                ('date_borrowed', models.DateTimeField(blank=True, null=True)),
                ('date_returned', models.DateTimeField(blank=True, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Chariot',
            fields=[
                ('object_number', models.IntegerField(blank=True, null=True)),
                ('origin', models.CharField(blank=True, max_length=255, null=True)),
                ('chassis_number', models.CharField(blank=True, max_length=255, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('description', models.TextField(blank=True, default='None', null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('origin', models.CharField(blank=True, max_length=255, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('artist_name', models.CharField(blank=True, max_length=255, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='PermenantCollection',
            fields=[
                ('date_aquired', models.DateTimeField(blank=True, null=True)),
                ('art_object', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ArtObjects.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('art_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ArtObjects.artobject')),
            ],
        ),
        migrations.AddField(
            model_name='artobject',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ArtObjects.hall'),
        ),
    ]
