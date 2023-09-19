# -*- coding: utf-8 -*-
# Generated by Django 4.1.5 on 2023-09-02 04:51

import time

import drf_misc.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "created_at",
                    drf_misc.core.fields.EpochField(blank=True, default=time.time, max_length=20, null=True),
                ),
                ("updated_at", drf_misc.core.fields.EpochField(blank=True, max_length=20, null=True)),
                ("id", models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ("name", models.CharField(max_length=200)),
                ("identifiers", models.JSONField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("running", "Running"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                            ("retrying", "Retrying"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("args", models.JSONField(blank=True, null=True)),
                ("kwargs", models.JSONField(blank=True, null=True)),
                ("return_value", models.JSONField(blank=True, null=True)),
                ("failed_reason", models.JSONField(blank=True, null=True)),
                ("counter", models.IntegerField(default=1)),
                ("retries", models.CharField(blank=True, max_length=20, null=True)),
                ("expires", models.CharField(blank=True, max_length=20, null=True)),
                ("root_id", models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                "db_table": "background_task",
            },
        ),
    ]
