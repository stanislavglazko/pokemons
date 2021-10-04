from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField('Имя', max_length=200)
    title_en = models.CharField('Имя на английском', max_length=200, default='', blank=True)
    title_jp = models.CharField('Имя на японском', max_length=200, default='', blank=True)
    description = models.TextField('Описание', default='pokemon',  blank=True)
    image = models.ImageField('Изображение', null=True, blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Предок',
        default=None,
        on_delete=models.SET_NULL,
        related_name='evolution',
        null=True,
        blank=True,
        )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        default=None,
        on_delete=models.CASCADE,
        related_name='pokemon_entities',
        )
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Дата появления', default=None, null=True, blank=True)
    disappeared_at = models.DateTimeField('Дата исчезновения', default=None, null=True, blank=True)
    level = models.IntegerField('Уровень', default=None, null=True, blank=True)
    health = models.IntegerField('Здоровье', default=None, null=True, blank=True)
    strength = models.IntegerField('Сила', default=None, null=True, blank=True)
    defence = models.IntegerField('Защита', default=None, null=True, blank=True)
    stamina = models.IntegerField('Выносливость', default=None, null=True, blank=True)
