import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fieldmod.settings.dev")
django.setup()

from tanksbase.models import Tank

tanks = Tank.objects.all()
for tank in tanks:
    if tank.type == 'Тяжелый танк':
        tank.heroku_type = "static/img/heavyTank.png"
    elif tank.type == 'Средний танк':
        tank.heroku_type = "static/img/mediumTank.png"
    elif tank.type == 'Легкий танк':
        tank.heroku_type = "static/img/lightTank.png"
    elif tank.type == 'ПТ САУ':
        tank.heroku_type = "static/img/AT-SPG.png"
    elif tank.type == 'САУ':
        tank.heroku_type = "static/img/SPG.png"
Tank.objects.bulk_update(tanks, ['heroku_type'])
