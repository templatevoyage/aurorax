# Generated by Django 4.2.7 on 2023-11-29 16:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('general', 'General'), ('education', 'Education'), ('sports', 'Sports')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('published_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField()),
                ('content', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
