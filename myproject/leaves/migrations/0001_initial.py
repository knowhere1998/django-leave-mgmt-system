# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 09:11
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('headofdept', models.BooleanField()),
                ('permanent', models.BooleanField()),
                ('teaching', models.BooleanField()),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(help_text='Please use the following format: <em>+91__________</em>.', max_length=128)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.Department')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('reason', models.CharField(default='Casual leave', max_length=400)),
                ('date', models.DateTimeField(verbose_name='leave date')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeavesRemain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ManyToManyField(to='leaves.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='somevalue', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='leavesremain',
            name='typeofleave',
            field=models.ManyToManyField(to='leaves.LeaveType'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='typeofleave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.LeaveType'),
        ),
    ]
