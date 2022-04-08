import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fieldmod.settings")
django.setup()


from tanksbase.models import Tank


tanks = Tank.objects.all()
for tank in tanks:
    if tank.type == 'Тяжелый танк':
        tank.type_icon = "type_icons/heavyTank.png"
    elif tank.type == 'Средний танк':
        tank.type_icon = "type_icons/mediumTank.png"
    elif tank.type == 'Легкий танк':
        tank.type_icon = "type_icons/lightTank.png"
    elif tank.type == 'ПТ САУ':
        tank.type_icon = "type_icons/AT-SPG.png"
    elif tank.type == 'САУ':
        tank.type_icon = "type_icons/SPG.png"
Tank.objects.bulk_update(tanks, ['type_icon'])
        