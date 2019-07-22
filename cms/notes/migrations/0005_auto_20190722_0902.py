# Generated by Django 2.2.2 on 2019-07-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.CharField(blank=True, choices=[('calculus', 'Calculus'), ('algebra', 'Algebra'), ('statistics', 'Statistics'), ('economics', 'Economics'), ('astronomy', 'Astronomy'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('comp', 'Computer Science')], default=None, max_length=20),
        ),
    ]
