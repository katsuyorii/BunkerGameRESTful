from django.db import models


class Proffesion(models.Model):
    ''' Модель для таблицы профессий персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
    
    def __str__(self):
        return self.name


class HealthStatus(models.Model):
    ''' Модель для таблицы состояния здоровья персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Состояние здоровья'
        verbose_name_plural = 'Состояния здоровья'
    
    def __str__(self):
        return self.name


class Hobbies(models.Model):
    ''' Модель для таблицы хобби и увлечений персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Хобби и увлечение'
        verbose_name_plural = 'Хобби и увлечения'
    
    def __str__(self):
        return self.name


class Phobia(models.Model):
    ''' Модель для таблицы фобий персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Фобия'
        verbose_name_plural = 'Фобии'   
    
    def __str__(self):
        return f'{self.name}'


class CharacterTrait(models.Model):
    ''' Модель для таблицы черты характера персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Черта характера'
        verbose_name_plural = 'Черты характера'   
    
    def __str__(self):
        return self.name


class Physique(models.Model):
    ''' Модель для таблицы телосложения персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Телосложение'
        verbose_name_plural = 'Телосложения'   
    
    def __str__(self):
        return self.name


class Items(models.Model):
    ''' Модель для таблицы предметов инвентаря персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Предмет инвентаря'
        verbose_name_plural = 'Предметы инвентаря'   
    
    def __str__(self):
        return self.name


class SpecialAction(models.Model):
    ''' Модель для таблицы специальных действий персонажа '''
    description = models.CharField(verbose_name='Описание', max_length=500)

    class Meta:
        verbose_name = 'Специальное действие'
        verbose_name_plural = 'Специальные действия'   
    
    def __str__(self):
        return self.description
    

class AdditionalInfo(models.Model):
    ''' Модель для таблицы доп. сведенией персонажа '''
    description = models.CharField(verbose_name='Описание', max_length=500)

    class Meta:
        verbose_name = 'Дополнительное сведение'
        verbose_name_plural = 'Дополнительные сведения'   
    
    def __str__(self):
        return self.description


class BunkerRooms(models.Model):
    ''' Модель для таблицы комнат бункера '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Комната бункера'
        verbose_name_plural = 'Комнаты бункера'
    
    def __str__(self):
        return self.name


class BunkerItems(models.Model):
    ''' Модель для таблицы вещей в бункере '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Вещь в бункере'
        verbose_name_plural = 'Вещи в бункере'
    
    def __str__(self):
        return self.name


class Bunker(models.Model):
    ''' Модель для таблицы описания бункера '''
    title = models.CharField(verbose_name='Наименование бункера', max_length=255)
    description = models.TextField(verbose_name='Описание бункера')

    class Meta:
        verbose_name = 'Описание бункера'
        verbose_name_plural = 'Описания бункера'
    
    def __str__(self):
        return self.description


class Catastrophe(models.Model):
    ''' Модель для таблицы катастрофы '''
    title = models.CharField(verbose_name='Наименование катастрофы', max_length=255)
    description = models.TextField(verbose_name='Описание катастрофы')

    class Meta:
        verbose_name = 'Катастрофа'
        verbose_name_plural = 'Катастрофы'
    
    def __str__(self):
        return f'{self.title} - {self.description}'
