from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Animal (models.Model):
    CAT = 'Коты'
    DOG = 'Собаки'
    PARROT = 'Попугаи'
    ANIMAL_TYPE = [
        (CAT,'Коты'),
        (DOG, 'Собаки'),
        (PARROT, 'Попугаи'),
    ]
    type = models.CharField(max_length= 30, choices=ANIMAL_TYPE, verbose_name='Тип животного')
    icon = models.ImageField(upload_to='animal_icons/%Y/%m/%d', blank=True, verbose_name='Иконка животного')
    slug = models.SlugField(default='', unique=True)


    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        type = self.type.lower()
        lower_case_letters = {u'а': u'a',
                            u'б': u'b',
                            u'в': u'v',
                            u'г': u'g',
                            u'д': u'd',
                            u'е': u'e',
                            u'ё': u'e',
                            u'ж': u'zh',
                            u'з': u'z',
                            u'и': u'i',
                            u'й': u'y',
                            u'к': u'k',
                            u'л': u'l',
                            u'м': u'm',
                            u'н': u'n',
                            u'о': u'o',
                            u'п': u'p',
                            u'р': u'r',
                            u'с': u's',
                            u'т': u't',
                            u'у': u'u',
                            u'ф': u'f',
                            u'х': u'h',
                            u'ц': u'ts',
                            u'ч': u'ch',
                            u'ш': u'sh',
                            u'щ': u'sch',
                            u'ъ': u'',
                            u'ы': u'y',
                            u'ь': u'',
                            u'э': u'e',
                            u'ю': u'yu',
                            u'я': u'ya', }

        translit_string = ""

        for index, char in enumerate(type):
            if char in lower_case_letters.keys():
                char = lower_case_letters[char]
            translit_string += char

        if not self.slug:
            self.slug = translit_string
        super(Animal, self).save(*args, **kwargs)


class Breed (models.Model):
    BIG = 'Большого телосложения'
    AVG = 'Среднего телосложения'
    SMALL = 'Маленького телосложения'
    BREED_SIZE = [
        (BIG,'Большого телосложения'),
        (AVG, 'Среднего телосложения'),
        (SMALL, 'Маленького телосложения'),
    ]
    name = models.CharField(max_length=50, verbose_name='Порода')
    size = models.CharField(max_length=100, choices=BREED_SIZE, verbose_name='Размер')
    color = models.CharField(max_length=100, verbose_name='Окрас')
    life = models.SmallIntegerField(verbose_name='Средняя продолжительность жизни')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Тип животного' )

    def __str__(self):
        return self.name

class Pet (models.Model):

    MALE = 'Мальчик'
    FEMALE = 'Девочка'

    PET_SEX = [
        (MALE,'Мальчик'),
        (FEMALE, 'Девочка'),
    ]


    # def get_slug(self, filename):
    #     filename = self.pk
    #     return 'pet_images\{}\{}.png'.format(self.type.type, filename)


    nickname = models.CharField(max_length=80, verbose_name='Кличка питомца')
    sex = models.CharField (max_length = 10, choices= PET_SEX, verbose_name='Пол питомца')
    breed = models.ForeignKey(Breed, on_delete= models.CASCADE, verbose_name='Порода питомца')
    description = models.TextField(verbose_name='Описание')
    date_enter = models.DateField(default=datetime.date.today(), verbose_name='Дата поступления')
    type = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Тип питомца')
    year = models.SmallIntegerField(verbose_name='Возраст питомца')
    photo = models.ImageField(upload_to='pet_images/%Y/%m/%d', blank=True, verbose_name='Фото питомца')
    like = models.SmallIntegerField (default=0, verbose_name='Лайки')
    vetpasport = models.BooleanField(default= False,verbose_name='Наличие ветпаспорта у питомца')

    def __str__(self):
        return '{} - {} лет'.format(self.nickname, self.year)


class Blog (models.Model):
    title = models.CharField(max_length= 200, verbose_name='Дата опубликования')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата опубликования')
    blogpost = models.TextField(verbose_name='Текст сообщения')
    small_decc = models.CharField(max_length = 50, blank=True, verbose_name='Короткий текст сообщения')

    def save(self, *args, **kwargs):
        blogpost = self.blogpost.split()
        short_text =''
        i = 0
        while i <= 30:
            short_text += '{} '.format(blogpost[i])
            i += 1
        short_text += '...'
 
        self.small_decc = short_text
        super(Blog, self).save(*args, **kwargs)






