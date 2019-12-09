# Generated by Django 2.2.6 on 2019-12-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrels',
            fields=[
                ('X', models.FloatField(help_text='Longitude')),
                ('Y', models.FloatField(help_text='Latitude')),
                ('Unique_squirrel_id', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('Shift', models.CharField(blank=True, choices=[('PM', 'PM'), ('AM', 'AM')], max_length=100)),
                ('Date', models.DateField(blank=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=100, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=20, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=20, null=True)),
                ('Specific_location', models.CharField(blank=True, max_length=100, null=True)),
                ('Running', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Chasing', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Climbing', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Eating', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Foraging', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Other_activities', models.CharField(blank=True, max_length=100, null=True)),
                ('Kuks', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Quaas', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Moans', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Tail_flags', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Tail_twitches', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Approaches', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Indifferent', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
                ('Runs_from', models.CharField(blank=True, choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=100)),
            ],
        ),
    ]