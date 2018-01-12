from django.db import models

# Create your models here.

class StateLit(models.Model):
	state = models.CharField(max_length = 100,null = True)
	population = models.IntegerField(default = 0)
	pop_increase = models.DecimalField(max_digits = 8,decimal_places = 7,null = True)
	area_km2 = models.IntegerField(default = 0,null = True)
	density = models.IntegerField(default = 0,null = True)
	sex_ratio = models.IntegerField(default = 0)
	literacy_rate = models.DecimalField(max_digits = 4,decimal_places = 2,null = True)
	percent_below_pov_line = models.DecimalField(max_digits = 7 ,decimal_places = 5,null=True)
	def __str__(self):
		return self.state

"""class StatePoverty(models.Model):
	state = models.CharField(max_length = 100)
	percent_below_pov_line = models.DecimalField(max_digits = 7 ,decimal_places = 5)
	#num_lakhs_below_pov_line = models.DecimalField(max_digits = 7,decimal_places = 3)
	def __str__(self):
		return self.state"""