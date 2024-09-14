# from datetime import datetime
#
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
#
# from apps.models import ProductHistory, Product
#
#
# @receiver(post_delete, sender=Product)
# def save_history(instance: Product, **kwargs):
#     ProductHistory.objects.create(
#         action="ochirildi",
#         name=instance.name,
#         price=instance.price,
#         deleted_at=datetime.now()
#     )
