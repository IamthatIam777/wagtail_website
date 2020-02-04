# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('snippets', '0026_auto_20170227_1401'),
        ('wagtailcore', '0040_page_draft_title'),
        ('images', '0009_ietfimage_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='IESGStatementIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'IESG Statements Index Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='IESGStatementPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, help_text='Description of this page as it should appear when shared on social networks, or in Google results', max_length=255)),
                ('date_published', models.DateTimeField(blank=True, help_text='Use this field to override the date that the blog post appears to have been published.', null=True)),
                ('introduction', models.CharField(help_text='The page introduction text.', max_length=511)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}))])),
                ('prepared_body', models.TextField(blank=True, help_text='The prepared body content after bibliography styling has been applied. Auto-generated on each save.', null=True)),
                ('feed_image', models.ForeignKey(blank=True, help_text='This image will be used in listings and indexes across the site, if no feed image is added, the social image will be used.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.IETFImage')),
                ('social_image', models.ForeignKey(blank=True, help_text="Image to appear alongside 'social text', particularly for sharing on social networks", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.IETFImage')),
            ],
            options={
                'verbose_name': 'IESG Statement Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='IESGStatementTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='iesg_statement.IESGStatementPage')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.Topic')),
            ],
        ),
    ]
