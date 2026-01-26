from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Food_category(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name
    



class Online_menu(models.Model):
    
    category = models.ForeignKey(Food_category, on_delete=models.CASCADE)
    food_image = models.ImageField(upload_to='menu/online_menu')
    food_name = models.CharField( max_length=50)
    food_details = models.TextField(null=False)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    rating = models.FloatField()

    is_special = models.BooleanField(default=False)
    is_offer = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.food_name
    





class Offline_menu(models.Model):

    table_no = models.CharField( max_length=3)
    category = models.ForeignKey(Food_category,  on_delete=models.CASCADE, related_name="food")
    food_name = models.CharField(max_length=50)
    food_price = models.DecimalField( max_digits=5, decimal_places=2)
    food_image = models.ImageField( upload_to='Offline_menu/', )
    food_descriprion = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.food_name


    def discounted_price(self):

        if self.discount_percentage > 0:
            return self.food_price - (self.food_price * self.discount_percentage/100)

        return self.food_price
    
