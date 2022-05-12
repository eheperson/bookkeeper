from django.db import models
from django import forms
import datetime
# from languages.fields import LanguageField

# Create your models here.

class Genre(models.TextChoices):
        FCTN = '1', "Fiction"
        CLSC = '2', "Classic"
        MYTR = '3', "Mystery"
        FNTS = '4', "Fantasy"
        HSTR = '5', "Historical"
        HRRR = '6', "Horror"
        LTRY = '7', "Literary"
        RMNC = '8', "Romance"
        BGRP = '9', "Biography"
        ABGR = '10', "Autobiography"
        PTRY = '11', "Poetry"
        SCNC = '12', "Scientific"
        DYST = '13', "Dystopian"

class Format(models.TextChoices):
        EBK = '1', "ebook"
        ABK = '2', "audiobook"
        HCP = '3', "hardcover"
        PBK = '4', "paperback"
        EPB = '5', "epub"
        KDL = '6', "kindle"


# class Bookshelf(models.IntegerChoices):    

# class Thing(models.Model):
#     priority = models.IntegerField(default=ThingPriority.LOW, choices=ThingPriority.choices)


class Author(models.Model):
    first_name = models.CharField(max_length=250, blank=False, null=False)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    date_of_birth = models.DateField(default=datetime.date.today, blank=True, null=True)
    date_of_death = models.DateField(default=datetime.date.today, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
         unique_together = ('first_name', 'middle_name', 'last_name')


class Publisher(models.Model):
    name = models.CharField(max_length=250,  blank=False, null=False)
    address = models.CharField(max_length=250,  blank=True)
    phone_no = models.CharField(max_length=250,  blank=True) 

    class Meta:
         unique_together = ('name', 'address', 'phone_no')

    def __str__(self):
        return self.name

class Book(models.Model):
    published_date = models.DateField(default=datetime.date.today, blank=True)
    title = models.CharField(max_length=250, blank=False, unique=True)
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE, blank=False, null=False)
    publisher = models.ForeignKey(Publisher, related_name="publisher", on_delete=models.CASCADE, blank=False, null=False)
    genre = models.CharField(max_length=3, choices=Genre.choices, default=Genre.DYST)
    format = models.CharField(max_length=3, choices=Format.choices, default=Format.EBK)
    isbn = models.CharField(max_length=250, blank=True, null=True)
    # language = LanguageField()
    page_no = models.IntegerField(null=False, blank=False)
    is_readed = models.BooleanField(default=False)
    # to store some notes about book if you want, not required.
    note = models.TextField(blank=False, null=False)  

    def __str__(self):
        return self.title + self.author
        
    class Meta:
        unique_together = ['author', 'title', 'publisher']
