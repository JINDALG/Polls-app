from __future__ import unicode_literals

from django.db import models

class Questions(models.Model):
	"""docstring for Questions"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
		


class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeignKey(Questions)
	choice_text = models.CharField(max_length=200)
	votes  = models.IntegerField(default=0)
		
