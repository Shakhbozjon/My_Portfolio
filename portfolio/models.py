from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv', blank=True, null=True)

    def __str__(self):
        return self.full_name



class AboutMe(models.Model):
    profession = models.CharField(max_length=200, null=True, blank=True)
    full_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=500, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.full_name



class Education(models.Model):
    edu_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    from_time = models.DateField(null=True, blank=True)
    to_time = models.DateField(null=True, blank=True, default='Current')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.edu_name


class Experience(models.Model):
    company = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    from_time = models.DateField(null=True, blank=True)
    to_time = models.DateField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.company


class ContactMe(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email


class Skill(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=80)

    def __str__(self):
        return self.name