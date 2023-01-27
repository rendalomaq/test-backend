from django.db.models import Avg
from .models import Product


def get_average_product_price() -> float:
    return Product.objects.aggregate(Avg('price'))['price__avg']


def get_products_filtered_by_category(category_id: int) -> list:
    return list(Product.objects.filter(category=category_id))
