from django.db import models

class Regi(models.Model):
    First_Name=models.CharField(max_length=70)
    Last_name=models.CharField(max_length=70)
    Email_Id = models.EmailField(max_length=70)
    Phone_Number=models.IntegerField()
    username=models.CharField(max_length=70)
    password=models.CharField(max_length=70)


    def __str__(self):
        return self.username

    class Meta:
        db_table="Regi"

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_username(username):
        try:
            return Regi.objects.get(username=username)
        except:
            return False

    def isExists(self):
        if Regi.objects.filter(username=self.username):
            return True
        return False


class productlist(models.Model):
    category=models.CharField(max_length=70)
    item=models.CharField(max_length=70)
    quantity= models.CharField(max_length=70)
    image=models.ImageField('media/')
    price=models.FloatField()

    def __str__(self):
        return self.item

    class Meta:
        db_table = "productlist"

    @staticmethod
    def get_item_by_name(item):
        try:
            return productlist.objects.get(item=item)
        except:
            return False

    def isExists(self):
        if productlist.objects.filter(item=self.item):
            return True
        return False

class cartlist(models.Model):
    category=models.CharField(max_length=70)
    item=models.CharField(max_length=70)
    quantity= models.CharField(max_length=70)
    image=models.ImageField('cartimg/')
    price=models.FloatField()

    def __str__(self):
        return self.item

    class Meta:
        db_table = "cartlist"

    @staticmethod
    def get_item_to_delete(item):
        try:
            return cartlist.objects.get(item=item)
        except:
            return False

    def isExists(self):
        if cartlist.objects.filter(item=self.item):
            return True
        return False

