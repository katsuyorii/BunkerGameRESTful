# Generated by Django 5.1.2 on 2024-10-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BunkerItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вещь в бункере',
                'verbose_name_plural': 'Вещи в бункере',
            },
        ),
        migrations.CreateModel(
            name='BunkerRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Комната бункера',
                'verbose_name_plural': 'Комнаты бункера',
            },
        ),
        migrations.CreateModel(
            name='Catastrophe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание бункера')),
            ],
            options={
                'verbose_name': 'Катастрофа',
                'verbose_name_plural': 'Катастрофы',
            },
        ),
        migrations.CreateModel(
            name='CharacterTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Фобия',
                'verbose_name_plural': 'Фобии',
            },
        ),
        migrations.CreateModel(
            name='HealthStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('status', models.CharField(blank=True, help_text='Необязательно', max_length=255, null=True, verbose_name='Статус заболевания')),
            ],
            options={
                'verbose_name': 'Состояние здоровья',
                'verbose_name_plural': 'Состояния здоровья',
            },
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Хобби и увлечение',
                'verbose_name_plural': 'Хобби и увлечения',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Предмет инвентаря',
                'verbose_name_plural': 'Предметы инвентаря',
            },
        ),
        migrations.CreateModel(
            name='Phobia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.CharField(max_length=255, verbose_name='Описание фобии')),
            ],
            options={
                'verbose_name': 'Фобия',
                'verbose_name_plural': 'Фобии',
            },
        ),
        migrations.CreateModel(
            name='Physique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Телосложение',
                'verbose_name_plural': 'Телосложения',
            },
        ),
        migrations.CreateModel(
            name='Proffesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='SpecialAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Специальное действие',
                'verbose_name_plural': 'Специальные действия',
            },
        ),
        migrations.CreateModel(
            name='Bunker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание бункера')),
                ('items', models.ManyToManyField(to='game.bunkeritems', verbose_name='Вещи в бункере')),
                ('rooms', models.ManyToManyField(to='game.bunkerrooms', verbose_name='Комнаты бункера')),
            ],
            options={
                'verbose_name': 'Описание бункера',
                'verbose_name_plural': 'Описания бункера',
            },
        ),
    ]
