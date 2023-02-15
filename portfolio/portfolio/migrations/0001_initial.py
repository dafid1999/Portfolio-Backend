# Generated by Django 4.1.5 on 2023-02-12 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolioName', models.CharField(error_messages={'unique': 'A portfolio is already created with this name'}, max_length=255, unique=True)),
                ('dataZalozenia', models.DateField(auto_now_add=True)),
                ('wyswietlenia', models.IntegerField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Dostepny'), (2, 'Edytowany'), (3, 'Wygasly')], default=2)),
                ('wlasciciel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wlasciciel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zdjecia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolio_zdjecia', to='portfolio.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Tresc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.CharField(max_length=255)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolio_tresc', to='portfolio.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Filmy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolio_filmy', to='portfolio.portfolio')),
            ],
        ),
    ]