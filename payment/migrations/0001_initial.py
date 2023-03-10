# Generated by Django 3.2.4 on 2022-12-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('site', models.CharField(choices=[('zoo', 'zoo'), ('fish_pond', 'fish pond'), ('culture', 'culture')], default='zoo', max_length=50)),
                ('amount_paid', models.FloatField(default=0.0)),
                ('date', models.DateField(auto_now_add=True)),
                ('tourist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tourist.tourist')),
            ],
        ),
    ]
