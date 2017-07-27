# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def create_member_roles(apps, schema_editor):
    MemberRole = apps.get_model("ggit_platform", "MemberRole")

    MemberRole.objects.create(name='Ambasadoare Coordonatoare')
    MemberRole.objects.create(name='Ambasadoare Comunicare')
    MemberRole.objects.create(name='Ambasadoare Logistică')
    MemberRole.objects.create(name='Ambasadoare Învățare')
    MemberRole.objects.create(name='Ambasadoare')
    MemberRole.objects.create(name='Voluntar')

def set_default_member_role(apps, schema_editor):
    MemberRole = apps.get_model("ggit_platform", "MemberRole")
    Member = apps.get_model("ggit_platform", "Member")

    volunteer_role = MemberRole.objects.get(name='Voluntar')
    Member.objects.update(role=volunteer_role)

class Migration(migrations.Migration):

    dependencies = [
        ('ggit_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ggit_platform.MemberRole'),
        ),

        migrations.RunPython(create_member_roles),
        migrations.RunPython(set_default_member_role),

        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ggit_platform.MemberRole'),
        ),
    ]
