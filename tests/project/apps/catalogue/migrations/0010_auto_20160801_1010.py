# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('catalogue', '0009_slugfield_noop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='category',
            name='path',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='page_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='wagtailcore.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='publish_revision_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Description', blank=True),
        ),
    ]
