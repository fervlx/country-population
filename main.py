import sys
sys.path.append('./utils')

from utils.population import load_data, get_population_by_country
from utils.charts import generate_bar_chart

country = input('Please, Type country ==> ')

if not country:
    print('Sorry, You should enter a country name.')
    exit()

countries = load_data()
population, country = get_population_by_country( countries, country.capitalize() )

if population == None:
    print(' Sorry, We have no this country in the database.')
    exit()
print(population);
generate_bar_chart( population.keys(), population.values() )