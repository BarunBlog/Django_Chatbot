# Generated by Django 3.2 on 2021-05-02 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_chatbot', '0003_auto_20210501_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessageInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1024, verbose_name='message')),
                ('status', models.BooleanField(blank=True, help_text='Message evaluation right or wrong?', null=True, verbose_name='Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('correct_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usermessageinput_corrected', to='simple_chatbot.tag', verbose_name='correct tag')),
                ('identified_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usermessageinput_identified', to='simple_chatbot.tag', verbose_name='identified tag')),
            ],
        ),
    ]