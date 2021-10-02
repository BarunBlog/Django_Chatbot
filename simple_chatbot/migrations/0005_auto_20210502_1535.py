# Generated by Django 3.2 on 2021-05-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_chatbot', '0004_usermessageinput'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pattern',
            options={'verbose_name': 'pattern', 'verbose_name_plural': 'patterns'},
        ),
        migrations.AlterModelOptions(
            name='usermessageinput',
            options={'ordering': ('-timestamp',), 'verbose_name': 'user message input', 'verbose_name_plural': 'user message inputs'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='method',
            field=models.CharField(choices=[], max_length=120, unique=True, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='token',
            name='patterns',
            field=models.ManyToManyField(blank=True, editable=False, related_name='tokens', to='simple_chatbot.Pattern'),
        ),
    ]