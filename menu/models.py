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
    

class Order(models.Model):

    ORDER_TYPE =(
        ('online','Online'),
        ('offline','Offline'),  
    )

    ORDEWR_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Order Item
    order_type = models.CharField( max_length=10, choices=ORDER_TYPE)
    status = models.CharField(max_length=50, choices=ORDEWR_STATUS)

     # Customer details for offline orders (optional)
    customer_name = models.CharField(max_length=150, blank=True, null=True)
    table_number = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=11, blank=False, null=True)
   

    # Pricing fields
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    # Extra info
    special_instructions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f"{self.get_order_type_display()} Order #{self.id}"


    def calculate_total(self):

        self.total = self.subtotal + self.vat + self.service_charge - self.discount

        return self.total
    

class Order_food(models.Model):

    order = models.ForeignKey(Order,  on_delete=models.CASCADE, related_name='food')
    foods = models.ForeignKey(Offline_menu,  on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField( max_digits=10, decimal_places=2)


    def __str__(self):
        return f'(self.quantity) * (self.foods.food_name)'


    def save(self, *args, **kwargs):

        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)
    