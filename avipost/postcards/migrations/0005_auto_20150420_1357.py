# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postcards', '0004_auto_20150420_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcard',
            name='message',
            field=models.CharField(default=b'Hello!', max_length=10, verbose_name=b'Message'),
            preserve_default=True,
        ),
    ]
