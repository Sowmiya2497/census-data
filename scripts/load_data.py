import sys, os, django
sys.path.append("C:/Users/subrafive/census")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "censusdata.settings")
django.setup()

from graphs.models import StateLit
import csv

with open("C:/Users/subrafive/census/graphs/static/states.csv") as f:
	reader = csv.reader(f)
	fields = reader.__next__()
	for row in reader:
		_, created = StateLit.objects.get_or_create(
			state=row[1],
			population=row[2],
			pop_increase = row[3],
			area_km2=row[4],
			density=row[5],
			sex_ratio=row[6],
			literacy_rate=row[7],
			percent_below_pov_line = row[8]
			)

"""with open("C:/Users/subrafive/census/graphs/static/states_poverty.csv") as f:
	reader = csv.reader(f)
	fields = reader.__next__()
	for row in reader:
		_, created = StatePoverty.objects.get_or_create(
			state=row[0],
			percent_below_pov_line=row[3],
			#num_lakhs_below_pov_line = row[6],
			)"""