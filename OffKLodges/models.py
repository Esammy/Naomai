from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import secrets
from .paystack import PayStack

class Lodge(models.Model):
    name = models.CharField(max_length=200, null=True)
    homeImg = models.ImageField(default='Profile-Photo-Place-Holder.PNG', upload_to='home_img', null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.homeImg.url
        except:
            url = ''
        return url


class LodgeProperties(models.Model):
    lodge = models.OneToOneField(Lodge, on_delete=models.CASCADE)
    sorrounding = models.ImageField(upload_to='home_img', null=True, blank=True)
    lodge_interior = models.ImageField(upload_to='home_img', null=True, blank=True)
    roomFront = models.ImageField(upload_to='home_img', null=True, blank=True)
    roomBack = models.ImageField(upload_to='home_img', null=True, blank=True)
    roomKitchen = models.ImageField(upload_to='home_img', null=True, blank=True)
    roomToiletBath = models.ImageField(upload_to='home_img', null=True, blank=True)
    bedRoom = models.ImageField(upload_to='home_img', null=True, blank=True)

    roomsTotalNum = models.PositiveSmallIntegerField()
    roomsAvailable = models.PositiveSmallIntegerField()
    selfCon = models.BooleanField(default=False)


    def __str__(self):
        return str(self.lodge)

    @property
    def sorroundingImageURL(self):
        try:
            url = self.sorrounding.url
        except:
            url = ''
        return url

    @property
    def lodge_interiorImageURL(self):
        try:
            url = self.lodge_interior.url
        except:
            url = ''
        return url

    @property
    def roomFrontImageURL(self):
        try:
            url = self.roomFront.url
        except:
            url = ''
        return url

    @property
    def roomBackImageURL(self):
        try:
            url = self.roomBack.url
        except:
            url = ''
        return url

    @property
    def roomKitchenImageURL(self):
        try:
            url = self.roomKitchen.url
        except:
            url = ''
        return url

    @property
    def toiletRoomImageURL(self):
        try:
            url = self.bedRoom.url
        except:
            url = ''
        return url           

    @property
    def bedRoomImageURL(self):
        try:
            url = self.bedRoom.url
        except:
            url = ''
        return url      

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='profile_pics')
    email = models.EmailField(default= 'egwusamuel2015@gmail.com')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ('-date_created')

    def __str__(self) -> str:
        return f"payment: {self.amount}"  

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            objects_with_similar_ref = Payment.objects.filter(ref=ref)
            if not objects_with_similar_ref:
                self.ref = ref
            super().save(*args, **kwargs)  

    def amount_value(self) -> int:
        return self.amount * 100   

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

class FindRoomMate(models.Model):
    pass