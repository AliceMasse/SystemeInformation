from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class TempDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print(f'Update temperature {temperature}')

class HumidityDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print(f'Update humidity {humidity}')

class PressureDisplay(Display):
    def update(self, temperature, humidity, pressure):
        print(f'Update pressure {pressure}')


class WeatherData:

    def __init__(self):
        self.__display  = []

    def register_display(self, display : Display):
        self.__display.append(display)

    def get_temperature(self):
        # get data from sensor and return collected value
        return 12

    def get_pressure(self):
        # get data from sensor and return collected value
        return 900

    def get_humidity(self):
        # get data from sensor and return collected value
        return 70

    def measurements_changed(self):
        latest_temperature = self.get_temperature()
        latest_pressure = self.get_pressure()
        latest_humidity = self.get_humidity()

        for display in self.__display:
            display.update(latest_temperature, latest_humidity, latest_pressure)

if __name__ == '__main__':
    weatherData = WeatherData()
    weatherData.register_display(TempDisplay())
#    weatherData.register_display(HumidityDisplay())
    weatherData.register_display(PressureDisplay())
    for _ in range(2):
        weatherData.measurements_changed()