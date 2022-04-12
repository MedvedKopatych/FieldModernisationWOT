from django.db import models


class Tank(models.Model):
    tier = models.PositiveSmallIntegerField('Tier')
    type = models.CharField('Type', max_length=120)
    nation = models.CharField('Nation', max_length=120)
    name = models.CharField('Name', max_length=255)
    small_icon = models.CharField('Small_icon', max_length=400, default=None)
    heroku_flag = models.CharField('Heroku_flag', max_length=400, null=True)
    heroku_type = models.CharField('Heroku_type', max_length=400, null=True)
    modernization_1 = models.CharField('Modernization 1', max_length=255, default=None)
    modernization_2 = models.CharField('Modernization 2', max_length=255, default=None)
    modernization_3 = models.CharField('Modernization 3', max_length=255, default=None)
    modernization_4 = models.CharField('Modernization 4', max_length=255, default='---')
    modernization_5 = models.CharField('Modernization 5', max_length=255, default='---')
    flag = models.ImageField(upload_to='flags/', blank=True)
    type_icon = models.ImageField(upload_to='type_icons/', blank=True)

    class Meta:
        verbose_name = 'Танк'
        verbose_name_plural = 'Танки'

    def __str__(self):
        return f' {self.name}'
