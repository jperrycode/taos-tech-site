# Generated by Django 5.0.6 on 2024-05-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0003_reviews_review_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating_message_dj',
            field=models.TextField(blank=True, null=True, verbose_name='Comment for the DJs eyes only'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='rating_message_front',
            field=models.TextField(blank=True, null=True, verbose_name='How did we Do?'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date_of_event',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Event'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='event_city',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Where?'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_event_type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='What Event?'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='reviewer_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Your Name'),
        ),
    ]