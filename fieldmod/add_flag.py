import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fieldmod.settings")
django.setup()


from tanksbase.models import Tank


def add_flag():
    tanks = Tank.objects.all()
    for tank in tanks:
        if tank.nation == 'Германия':
            tank.flag = "flags/filter-germany.png"
        elif tank.nation == 'Чехословакия':
            tank.flag = "flags/filter-czech.png"
        elif tank.nation == 'Франция':
            tank.flag = "flags/filter-france.png"
        elif tank.nation == 'Италия':
            tank.flag = "flags/filter-italy.png"
        elif tank.nation == 'Китай':
            tank.flag = "flags/filter-china.png"
        elif tank.nation == 'Япония':
            tank.flag = "flags/filter-japan.png"
        elif tank.nation == 'Швеция':
            tank.flag = "flags/filter-sweden.png"
        elif tank.nation == 'Великобритания':
            tank.flag = "flags/filter-uk.png"
        elif tank.nation == 'США':
            tank.flag = "flags/filter-usa.png"
        elif tank.nation == 'СССР':
            tank.flag = "flags/filter-ussr.png"
    Tank.objects.bulk_update(tanks, ['flag'])


add_flag()


