# Generated by Django 4.0.5 on 2022-08-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0076_modellogentry_revision"),
        ("breads", "0005_breadtype_latest_revision"),
    ]

    operations = [
        migrations.AddField(
            model_name="breadingredient",
            name="expire_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="expiry date/time"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="expired",
            field=models.BooleanField(
                default=False, editable=False, verbose_name="expired"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="first_published_at",
            field=models.DateTimeField(
                blank=True, db_index=True, null=True, verbose_name="first published at"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="go_live_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="go live date/time"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="has_unpublished_changes",
            field=models.BooleanField(
                default=False, editable=False, verbose_name="has unpublished changes"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="last_published_at",
            field=models.DateTimeField(
                editable=False, null=True, verbose_name="last published at"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="latest_revision",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.revision",
                verbose_name="latest revision",
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="live",
            field=models.BooleanField(
                default=True, editable=False, verbose_name="live"
            ),
        ),
        migrations.AddField(
            model_name="breadingredient",
            name="live_revision",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.revision",
                verbose_name="live revision",
            ),
        ),
    ]
