import files

def find_country( countries, country ):
    for data in countries:
        if data['Country/Territory'] == country:
            return data
    return None

def get_population( country_dict, years = [ '2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970' ]):
    values = [ int( y ) for x, y in country_dict.items() if x[:4] in years]
    sorted_list = sorted( zip( years, values ), key=lambda x: x[0] )
    population = { x:y for x , y in sorted_list }
    return population

def get_population_by_country( countries, country ):
    country_dict = find_country( countries= countries, country= country )
    if country_dict == None:
        return None, None
    population = get_population( country_dict )
    return population, country_dict

def load_data():
    countries = files.read_csv('./data/world_population.csv')
    return countries

if __name__ == '__main__':
    #import files
#else: 
    #from . import files
    countries = files.read_csv('./data/world_population.csv')
    population, _ = get_population_by_country( countries,'Curacao' )
    print(population)