from django.db import models

# Create your models here.



class children(models.Model):
    b_id=models.IntegerField(default=0)
    b_name=models.CharField(max_length=40)
    b_auth=models.CharField(max_length=15)
    b_review = models.CharField(max_length=15)
    b_image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return str(self.b_id)


class political(models.Model):
    b_id=models.IntegerField(default=0)
    b_name=models.CharField(max_length=40)
    b_auth=models.CharField(max_length=15)
    b_review = models.CharField(max_length=15)
    b_image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.b_id)

class poetry(models.Model):
    b_id=models.IntegerField(default=0)
    b_name=models.CharField(max_length=40)
    b_auth=models.CharField(max_length=15)
    b_review = models.CharField(max_length=15)
    b_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.b_id)

class artdesign(models.Model):
    b_id=models.IntegerField(default=0)
    b_name=models.CharField(max_length=40)
    b_auth=models.CharField(max_length=15)
    b_review = models.CharField(max_length=15)
    b_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.b_id)

class programing(models.Model):
    b_id=models.IntegerField(default=0)
    b_name=models.CharField(max_length=40)
    b_auth=models.CharField(max_length=15)
    b_review = models.CharField(max_length=15)
    b_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.b_id)


