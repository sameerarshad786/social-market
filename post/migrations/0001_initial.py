# Generated by Django 3.2.5 on 2022-10-28 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models.post_model
import post.models.remarks_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('text', models.TextField()),
                ('files', models.FileField(upload_to=post.models.post_model.post_uploaded_files, verbose_name='file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.uuid',),
        ),
        migrations.CreateModel(
            name='PostRemarks',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('popularity', models.CharField(choices=[('like', 'LIKE'), ('heart', 'HEART'), ('funny', 'FUNNY'), ('insightful', 'INSIGHTFUL'), ('disappoint', 'DISAPPOINT')], max_length=11)),
                ('on_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.uuid',),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('comment', models.TextField(blank=True)),
                ('files', models.FileField(blank=True, upload_to=post.models.remarks_model.comment_media_path, verbose_name='file')),
                ('on_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.uuid',),
        ),
        migrations.CreateModel(
            name='CommentRemarks',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('popularity', models.CharField(choices=[('like', 'LIKE'), ('heart', 'HEART'), ('funny', 'FUNNY'), ('insightful', 'INSIGHTFUL'), ('disappoint', 'DISAPPOINT')], max_length=11)),
                ('on_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comments')),
                ('on_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.uuid',),
        ),
    ]
