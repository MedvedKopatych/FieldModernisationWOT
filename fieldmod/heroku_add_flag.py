import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fieldmod.settings.dev")
django.setup()


from tanksbase.models import Tank


def add_heroku_flag():
    tanks = Tank.objects.all()
    for tank in tanks:
        if tank.nation == 'Германия':
            tank.heroku_flag = "static/img/filter-germany.png"
        elif tank.nation == 'Чехословакия':
            tank.heroku_flag = "static/img/filter-czech.png"
        elif tank.nation == 'Франция':
            tank.heroku_flag = "static/img/filter-france.png"
        elif tank.nation == 'Италия':
            tank.heroku_flag = "static/img/filter-italy.png"
        elif tank.nation == 'Китай':
            tank.heroku_flag = "static/img/filter-china.png"
        elif tank.nation == 'Япония':
            tank.heroku_flag = "static/img/filter-japan.png"
        elif tank.nation == 'Швеция':
            tank.heroku_flag = "static/img/filter-sweden.png"
        elif tank.nation == 'Великобритания':
            tank.heroku_flag = "static/img/filter-uk.png"
        elif tank.nation == 'США':
            tank.heroku_flag = "static/img/filter-usa.png"
        elif tank.nation == 'Польша':
            tank.heroku_flag = "static/img/filter-poland.png"
        elif tank.nation == 'СССР':
            tank.heroku_flag = "static/img/filter-ussr.png"
    Tank.objects.bulk_update(tanks, ['heroku_flag'])


add_heroku_flag()
