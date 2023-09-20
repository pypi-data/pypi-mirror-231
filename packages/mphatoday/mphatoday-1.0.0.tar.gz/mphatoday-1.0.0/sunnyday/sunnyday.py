import requests, pprint

class Weather:
    """This app coolctes data from weather app

    Package use exanples

    # Create weather object using city or lat and long
    >>> weather = Weather(city='Madrid', lat=4.1, lon=4.5)

    # get data for next 12 hours
    >>> weather.next_12h()

    # get simplified data for next 12 hours
    >>> weather.next_12h_simplified()
    """

    api_key = '20b20523ec6401d8a72ddbbe09e0ed29'

    def __init__(self, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={self.api_key}"
            r = requests.get(url)
            self.data = r.json()
            #print(self.data)
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={self.api_key}"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide city name or long and lat")

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for time_block in self.data['list'][:4]:
            print(time_block['dt_txt'])
            simple_data.append((time_block['dt_txt'],
                               time_block['main']['temp'],
                               time_block['weather'][0]['description'])
                               )
        return simple_data