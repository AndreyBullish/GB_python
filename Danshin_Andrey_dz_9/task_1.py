import time


class TrafficLight:
    __color: dict = {
        'red': 4,
        'yellow': 2,
        'green': 3
    }

    def running(self):
        cycle = 10
        for k, v in self.__color.items():
            print(f'{k} {v} сек')
            time.sleep(v)

if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()

print('end')