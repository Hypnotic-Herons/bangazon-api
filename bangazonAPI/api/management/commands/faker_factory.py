from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from api.models import Customer
# , Payment_Type, Product_Type, Product

class Command(BaseCommand):

  def handle(self, *args, **options):
    #seeder.add_entity(Product_Type, 12) # the number argument is the total num of rows you want created
    seeder.add_entity(Customer, 25)
    #seeder.add_entity(Payment_Type, 50, {'acct_number': lambda x: random.randint(11111,99999)})
    # Override the seeder "guess" of what faker provider you want it to use
    #seeder.add_entity(Product, 100, {'name': lambda x: seeder.faker.catch_phrase()})

    inserted_pks = seeder.execute()