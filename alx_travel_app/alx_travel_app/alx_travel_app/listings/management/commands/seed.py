from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Cozy Apartment in Downtown",
                "description": "A very cozy apartment with all amenities",
                "location": "Cairo",
                "price_per_night": random.randint(20, 100),
                "available": True
            },
            {
                "title": "Beachside Villa",
                "description": "Enjoy the sea view and luxury living",
                "location": "Alexandria",
                "price_per_night": random.randint(80, 200),
                "available": True
            }
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))