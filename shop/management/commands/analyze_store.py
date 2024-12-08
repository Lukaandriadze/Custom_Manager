from django.core.management.base import BaseCommand
from django.db.models import Count, Sum, Avg, Max, Min
from shop.models import Item, Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        category = Category.objects.first()
        if category:
            item_count = category.items.count()
            print(f"{category.name}: {item_count}")
        prices = Item.objects.aggregate(
            max_price=Max('price'),
            min_price=Min('price'),
            avg_price=Avg('price')
        )
        print(f"Max Price: {prices['max_price']}, Min Price: {prices['min_price']}, Avg Price: {prices['avg_price']}")
        categories = Category.objects.annotate(
            items_count=Count('items'),
            total_price=Sum('items__price')
        )
        for cat in categories:
            print(f"Category {cat.name}: Count {cat.items_count}, Price {cat.total_price}")
        items = Item.objects.select_related('category').all()
        for item in items:
            print(f"{item.name}: {item.category.name}")
        items_with_tags = Item.objects.prefetch_related('tags').all()
        for item in items_with_tags:
            tags = ", ".join(tag.name for tag in item.tags.all())
            print(f"Item {item.name} tags: {tags}")
