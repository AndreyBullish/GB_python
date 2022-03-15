import time


class TrafficLight:
    __color: dict = {
        'red': 4,
        'yellow': 2,
        'green': 3
    }

    def running(self):
        cycle = 3
        while cycle != 0: #сделал нескольков кругов
            for k, v in self.__color.items():
                if (list(self.__color.values())[0]) == 4 and (list(self.__color.values())[1]) == 2 and (list(self.__color.values())[2]) == 3:
                    print(f'{k} {v} сек')
                    time.sleep(v)

                else:
                    print('неверная последовательность светофора')
            cycle -= 1

if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()

print('end')