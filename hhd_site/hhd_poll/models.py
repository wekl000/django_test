import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text + ' <pub in> ' + str(self.pub_date)

	def Was_Publish_Recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	vote = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text + ' <vote num is> ' + str(self.vote)
	
class HHD_db(models.Model):
	name = models.CharField(max_length=20)
	birthday = models.DateTimeField()
	gender = models.TextField(max_length=2)

	def __str__(self):
		return self.name + ' is birthed in ' + str(self.birthday)

