# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Post date'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feed_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='stream_field',
            field=wagtail.wagtailcore.fields.StreamField([('heading_h1', home.models.H1Block(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
    ]