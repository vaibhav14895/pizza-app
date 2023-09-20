from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):     #monckey patching   
        from django.contrib.auth.models import User
        from .models import cartitems,cart

        def get_cart_count(self):
            # cart_instance = cart.objects.get(cart_items="omi")
            return cartitems.objects.filter(cart__is_paid=False, cart__user=self).count()

        User.add_to_class("get_cart_count", get_cart_count)
