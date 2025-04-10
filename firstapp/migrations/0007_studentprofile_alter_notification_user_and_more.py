# Generated by Django 5.1.6 on 2025-03-25 13:52

import django.db.models.deletion
import firstapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_board_course_post_author_post_board_post_tags_admin_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default=firstapp.models.generate_student_id, max_length=20, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('academic_level', models.CharField(blank=True, max_length=50)),
                ('major', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('courses', models.ManyToManyField(blank=True, to='firstapp.course')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.university')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.studentprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.studentprofile'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.studentprofile'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
