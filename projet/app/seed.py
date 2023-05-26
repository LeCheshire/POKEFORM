from django_seed import Seed    
from app.models import Pokemon
import random

def run():
    Pokemon.objects.all().delete()
    seeder = Seed.seeder()
    type=['eau','feu','plante']
    seeder.add_entity(Pokemon,3, {
        'lvl' : lambda x: random.randint(0,100),
        'name' : lambda x: seeder.faker.first_name(),
        'type' : lambda x: type[random.randint(0, 2)],
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)
