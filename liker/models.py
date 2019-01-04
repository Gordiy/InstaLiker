from django.db import models


class UserData(models.Model):
	login = models.CharField(max_length=36, blank=True, null=True, default=None)
	password = models.CharField(max_length=58, blank=True, null=True, default=None)

	def __str__(self):
		return "{}".format(self.login)

	class Meta:
		verbose_name = "User data"
		verbose_name_plural = "User's data"
