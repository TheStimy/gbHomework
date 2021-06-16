from time import sleep
import os


class TrafficLight:
    def switch_lights(self):
        '''Надо запускать в терминале :)'''
        os.system('clear')
        print('\033[91m' + '⬤' + '\033[0m' + '\n' +
              '\033[30m' + '⬤' + '\033[0m' + '\n' +
              '\033[30m' + '⬤' + '\033[0m')
        sleep(7)
        os.system('clear')
        print('\033[30m' + '⬤' + '\033[0m' + '\n' +
              '\033[93m' + '⬤' + '\033[0m' + '\n' +
              '\033[30m' + '⬤' + '\033[0m')
        sleep(2)
        os.system('clear')
        print('\033[30m' + '⬤' + '\033[0m' + '\n' +
              '\033[30m' + '⬤' + '\033[0m' + '\n' +
              '\033[92m' + '⬤' + '\033[0m')
        sleep(9)
        os.system('clear')


traffic = TrafficLight()
traffic.switch_lights()
