from django.core.management.base import BaseCommand
from shop.models import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = Category.objects.with_item_count()
        for category in categories:
            print(f"{category.name}:{category.item_count}")
        items = Item.objects.with_tag_count()
        for item in items:
            print(f"{item.name}:{item.tags_count}")
        min_items = 2  
        print(f"{min_items}")
        tags = Tag.objects.popular_tags(min_items=min_items)
        for tag in tags:
            print(f"{tag.name}:{tag.item_count}")
