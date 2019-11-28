from django.db import models
from datetime import datetime
# Create your models here.

class Complain(models.Model):
    phone = models.IntegerField()
    claim = models.TextField(blank=True,help_text = '건의 사항을 적으십시오')

    def __str__(self):
        return str(self.phone)

class User(models.Model):
    user_id = models.AutoField(primary_key = True)
 
class Bike(models.Model):
    num = models.AutoField(primary_key=True)    # bike_num => num: 좀 더 직관적임
    _type = models.CharField(max_length=10)     ## type => _type: 예약어와 겹침
    price = models.IntegerField()   
    isBorrowed = models.BooleanField(default=False) # is_borrowed => isBorrowed
    isBroken = models.BooleanField(default=False)   # is_broken => isBroken
    password = models.CharField(max_length=4, default="0000")   
    startTime = models.TimeField(null=True, blank=True) # start_time => startTime
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  ## user 외래 키 추가

