from django.db import models

# Create your models here.

class project(models.Model):
	label = models.CharField(blank=False, max_length=100)
	description = models.TextField(blank=True)

class datacenter(models.Model):
	"""Les infos sur le datacenter"""
	label = models.CharField(blank=False, max_length=100)
	description = models.TextField(blank=True)

	class Admin:
		list_display = ('label',)
		search_fields = ('label',)

	def __unicode__(self):
		return self.label


class hall(models.Model):
	"""On peut avoir plusieurs salles dans un datacenter"""
	label = models.CharField(blank=False, max_length=100)
	datecenter = models.ForeignKey(datacenter)

	class Admin:
		list_display = ('hall',)
		search_fields = ('hall',)

	def __unicode__(self):
		return self.label


class component(models.Model):
	label = models.CharField(blank=False, max_length=100)
	hall = models.ForeignKey(hall,blank=True, null=True)
	iscabinet = models.BooleanField(default=False)
	Usize = models.IntegerField(blank=True, null=True)
	rackedin = models.ManyToManyField("self",symmetrical=False,blank=True, null=True)

	class Admin:
		list_display = ('component',)
		search_fields = ('component',)

	def __unicode__(self):
		return self.label

