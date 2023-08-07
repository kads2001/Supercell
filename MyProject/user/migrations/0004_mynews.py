# Generated by Django 3.2.4 on 2022-09-04 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_city_myblog_ncategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntitle', models.CharField(max_length=500)),
                ('nhead', models.CharField(max_length=500)),
                ('ndes', models.TextField()),
                ('npic', models.ImageField(null=True, upload_to='static/news/')),
                ('ndate', models.DateField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ncategory')),
                ('ncity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.city')),
            ],
        ),
    ]
