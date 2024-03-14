# Generated by Django 4.2.6 on 2024-03-13 13:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_alter_profile_profile_image'),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='saved_posts', to='Profile.profile'),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('associated_posts', models.ManyToManyField(blank=True, related_name='hashtags', to='Post.post')),
                ('followed_by', models.ManyToManyField(related_name='followed_hastags', to='Profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='commentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.comment')),
                ('reply_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='replied_by',
            field=models.ManyToManyField(related_name='replied_comments', through='Post.commentReply', to='Profile.profile'),
        ),
    ]