from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 )
    password = models.CharField(max_length=500)


    def register(self):
        self.save() # to save the values which are coming from signup page


    # this fuction is used in views.py for checking if email alreday exists
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    

    # this function is used in views.py for login 
    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
            