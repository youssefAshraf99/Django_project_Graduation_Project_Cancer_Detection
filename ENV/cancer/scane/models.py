from __future__ import unicode_literals
from django.db import migrations, models
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AnonymousUser, User
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M'), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    def __str__(self):
        return  self.user + " say :- " + self.value

class Doctors(models.Model):
    name = models.CharField(max_length=150)
    depart = models.CharField( max_length=150, choices=[("psychiatrist", "psychiatrist"), ("cardiologist", "cardiologist"), ("neurologist", "neurologist")], default="psychiatrist")
    photo = models.ImageField(upload_to='doctors/')
    def __str__(self):
        return self.name
class Nurses(models.Model):
    name = models.CharField(max_length=150)
    depart = models.CharField(max_length=150,
                              choices=[("Children", "Children"), ("Men", "Men"),
                                       ("Ladies", "Ladies")], default="Men")
    photo = models.ImageField(upload_to='Nurses/')
    def __str__(self):
        return self.name

class Feedback(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    def __str__(self):
        return "question from "+ self.f_name +" "+ self.l_name

class Post(models.Model):
    image = models.ImageField(
        default ="default_foo.png", upload_to ="post_picture")
    caption = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
 
    def __str__(self):
        return f'{self.author.username}\'s Post- {self.title}'

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)





class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DNASeq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('sequence', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='PeptideSeq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('sequence', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='RNASeq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('sequence', models.CharField(max_length=2000)),
            ],
        ),
    ]

class DNASeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)


# RNA Sequence model class

class RNASeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)


# Peptide Sequence model class

class PeptideSeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)
