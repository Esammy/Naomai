from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import secrets
from .paystack import PayStack
import numpy as np
import datetime

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



class FindRoomMates(models.Model):

        
    sex_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ("I don't care","I don't care")
    )
    state_choice = (
        ("abuja", "Abuja"), ("abia","Abia"),
        ("adamawa","Adamawa"),("anambra","Anambra"),
        ("akwa Ibom","Akwa Ibom"),("bauchi","Bauchi"),
        ("bayelsa","Bayelsa"),("benue","Benue"),("borno","Borno"),
        ("cross River","cross River"),("delta","Delta"),
        ("ebonyi","Ebonyi"),("edo","Edo"),("ekiti","Ekiti"),
        ("enugu","Enugu"),("gombe","Gombe"),("imo","Imo"),
        ("jigawa","Jigawa"),("kaduna","Kaduna"),("kano","Kano"),
        ("katsina","Katsina"),("kebbi","kebbi"),
        ("kogi","Kogi"),("kwara","Kwara"),("lagos","Lagos"),
        ("nassarawa","Nassarawa"),("niger","Niger"),("ogun","Ogun"),
        ("ondo","Ondo"),("osun","Osun"),("oyo","Oyo"),
        ("plateau","Plateau"),("rivers","Rivers"),
        ("sokoto","Sokoto"),("taraba","Taraba"),
        ("yobe","Yobe"), ("zamfara","Zamfara"),
        ("I don't care","I don't care")
    )

    sleep_late = (
        ('early','Early'),
        ('late','Late'),
        ("I don't care","I don't care")
    )
    study_silence = (
        ('silence','Silence'),
        ('background noise','Background noise'),
        ("I don't care","I don't care")
    )
    space_organized = (
        ('yes','Yes'),
        ('no','No'),
        ("I don't care","I don't care")
    )
    share_foodstuffs = (
        ('yes','Yes'),
        ('no','No'),
        ("I don't care","I don't care")
    )
    qualityTimeWithRoommate = (
        ('spend time with my roomate','Spend time with my roomate'),
        ('have my own space and time','Have my own space and time'),
        ("I don't care","I don't care")
    )
    allergies_disabilities_others = (
        ('allergies','Allergies'),
        ('disabilities','Disabilities'),
        ("I don't care","I don't care"),
        
    )
    level_choice = (
        ('100L','100L'),
        ('200L','200L'),
        ('300L','300L'),
        ('400L','400L'),
        ('500L','500L'),
        ("I don't care","I don't care"),
    )



    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    state = models.CharField(max_length=200, choices = state_choice, default = state_choice[-1][1])
    sex = models.CharField(max_length=200, choices = sex_choice, default = sex_choice[-1][1])
    level = models.CharField(max_length=200, choices = level_choice, default = level_choice[-1][1])

    earlywake = models.CharField(
        #labels = 'Do you prefer to go to bed early or stay up late?', 
        max_length=200, choices = sleep_late, 
        default = sleep_late[-1][1])
    noise = models.CharField(
        #label = 'Do you like to study in silent or with background noise?', 
        max_length=200, 
        choices = study_silence, 
        default = study_silence[-1][1])
    organizedSpace = models.CharField(
        #label = 'Do you like to keep your living space clean and organized?', 
        max_length=200,
        choices = space_organized, 
        default = space_organized[-1][1])
    grocries = models.CharField(
        #label = 'Do you expect to share groceries and household items?', 
        max_length=200, 
        choices = share_foodstuffs, 
        default = share_foodstuffs[-1][1])
    personalSpace = models.CharField(
        #label = 'Do you prefer to spend a lot of time with your roommte, or do you prefer to have your own space and time?', 
        max_length=200, 
        choices = qualityTimeWithRoommate, 
        default = qualityTimeWithRoommate[-1][1])
    disabilites = models.CharField(
        #label = 'Do you have any allergies, disabilities, or others?', 
        max_length=200, 
        choices = allergies_disabilities_others, 
        default = allergies_disabilities_others[-1][1])
    date_created = models.DateField(default = datetime.date.today)

    match_score = models.IntegerField()

    def __str__(self):
        return str(self.fname)


    def save(self, *args, **kwargs):
        attri_ = [self.sex, self.earlywake, 
                self.noise, self.organizedSpace, self.grocries, 
                self.personalSpace, self.disabilites]
        
        choice_att_ = [self.sex_choice, self.sleep_late, 
                    self.study_silence, self.space_organized, self.share_foodstuffs, 
                    self.qualityTimeWithRoommate, self.allergies_disabilities_others]
        print('the value for sex is:', self.sex)
        print('the value for sex choice is:', choice_att_[2][1][1])

        total_scores = []
        for i in range(len(attri_)):
            if attri_[i] == choice_att_[i][0][1]:
                total_scores.append(1)
            if attri_[i] == choice_att_[i][1][1]:
                total_scores.append(3)
            if attri_[i] == choice_att_[i][2][1]:
                total_scores.append(5)
        
        x = np.sum(total_scores) + 45
    
        if x:
            self.match_score = x
        super().save(*args, **kwargs)
        
    