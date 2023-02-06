from django.db import models

# Create your models here.

def generate_order_id(self, id):
    new_id = "order_"+id
    return new_id

class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    web = models.URLField()
    email = models.EmailField(null=False)
    new_id = generate_order_id(id)


class FoodChoice(models.Model):
    food_type = models.CharField(max_length=25)
    cuisine = models.CharField(max_length=25)
    extra_toppings = models.CharField(max_length=20)


class ClubAttendee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=150, unique=True)
    food_choice = models.ForeignKey(FoodChoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' '+self.last_name


class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    attendee = models.ManyToManyField(ClubAttendee, null=False)

    def __str__(self):
        return self.name


