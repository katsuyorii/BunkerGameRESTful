from django.db import models
from accounts.models import User


class Profession(models.Model):
    ''' Модель для таблицы профессий персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
    
    def __str__(self):
        return self.name


class Health(models.Model):
    ''' Модель для таблицы состояния здоровья персонажа '''
    name = models.CharField(verbose_name='Наименование', max_length=255)

    class Meta:
        verbose_name = 'Состояние здоровья'
        verbose_name_plural = 'Состояния здоровья'
    
    def __str__(self):
        return self.name


class Hobby(models.Model):
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


class Trait(models.Model):
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


class Baggage(models.Model):
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


class UserGenerationCharacter(models.Model):
    ''' Модель для таблицы списка хранения генераций персонажей пользователя '''
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    gender = models.CharField(verbose_name='Пол персонажа', max_length=255)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст персонажа')
    fertility = models.CharField('Способность к оплодотворению', max_length=255)
    profession = models.CharField('Профессия', max_length=255)
    health = models.CharField('Состояние здоровья', max_length=255)
    physique = models.CharField('Телосложение', max_length=255)
    trait = models.CharField('Черта характера', max_length=255)
    hobby = models.CharField('Хобби', max_length=255)
    phobia = models.CharField('Фобия', max_length=255)
    baggage = models.CharField('Багаж', max_length=255)
    additional_info = models.CharField('Доп. информация', max_length=255)
    special_action_one = models.CharField('Спец. умение №1', max_length=255)
    special_action_two = models.CharField('Спец. умение №1', max_length=255)

    class Meta:
        verbose_name = 'Генерация персонажа пользователя'
        verbose_name_plural = 'Генерации персонажей пользователей'
    
    def __str__(self):
        return {self.user.email}
    

class UserBunker(models.Model):
    ''' Модель для таблицы хранения генераций бункера пользователя '''
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    bunker = models.ForeignKey(verbose_name='Бункер', to=Bunker, on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='Дата и время генерации', auto_now_add=True)

    class Meta:
        verbose_name = 'Cписок генерация бункера пользователя'
        verbose_name_plural = 'Список генерации бункера пользователями'

    def __str__(self):
        return f'{self.user.email} | {self.bunker.title}'


class UserCatastrophe(models.Model):
    ''' Модель для таблицы хранения генераций катастроф пользователя '''
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    catastrophe = models.ForeignKey(verbose_name='Бункер', to=Catastrophe, on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='Дата и время генерации', auto_now_add=True)

    class Meta:
        verbose_name = 'Генерация катастрофы пользователя'
        verbose_name_plural = 'Генерации катастроф пользователями'

    def __str__(self):
        return f'{self.user.email} | {self.catastrophe.title}'
    

class UserCharacter(models.Model):
    ''' Модель для таблицы хранения генераций персонажа пользователя '''
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    character = models.ForeignKey(verbose_name='Персонаж', to=UserGenerationCharacter, on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='Дата и время генерации', auto_now_add=True)

    class Meta:
        verbose_name = 'Генерация бункера пользователя'
        verbose_name_plural = 'Генерации бункера пользователями'

    def __str__(self):
        return f'{self.user.email} | {self.bunker.title}'