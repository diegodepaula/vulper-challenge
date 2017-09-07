from django.db import models

class Professional(models.Model):
	
	login = models.CharField(max_length=255)
	picture = models.TextField()
	classification = models.CharField(max_length=255)