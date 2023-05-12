import csv

def read_csv( path, mode='r', delimiter=',' ):
    try:
        with open( path, mode ) as csvfile:
            reader = csv.reader( csvfile, delimiter = delimiter )
            header = next( reader )
            data = []
            for row in reader:
                iterable = zip( header, row )
                country_dict = { key: value for key, value in iterable }
                data.append( country_dict )
            return data
    except FileNotFoundError as error:
       print(error)
       return None

if __name__ == '__main__':
    data = read_csv('./data/world_population.csv')
    if data == None:
        print('File not fount')
    else:
        print( data[0] )