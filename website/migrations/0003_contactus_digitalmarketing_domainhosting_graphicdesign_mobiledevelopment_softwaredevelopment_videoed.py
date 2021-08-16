# Generated by Django 2.2.20 on 2021-07-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_company'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='DigitalMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='Digital Marketing', max_length=100)),
                ('description1', models.CharField(max_length=200)),
                ('description2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DomainHosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Domain & Hosting', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GraphicDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Graphic Design', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MobileDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Mobile App Development', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Software Development', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='VideoEditing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Video Editing', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WebDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Web Development', max_length=50)),
                ('image', models.ImageField(upload_to='static/img/services/')),
                ('topic', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.TextField()),
                ('feature1', models.CharField(max_length=250)),
                ('feature2', models.CharField(max_length=250)),
                ('feature3', models.CharField(max_length=250)),
                ('feature4', models.CharField(max_length=250)),
                ('feature5', models.CharField(max_length=250)),
            ],
        ),
    ]
