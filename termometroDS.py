class Termometro:
  #__path = '/Users/alessandro/Desktop/Tesi/code/w1_slave'
  __path = '/sys/bus/w1/devices/28-03742e126461/w1_slave'
  maxtemp = 0.0
  mintemp = 100.0

  def dammiMax(self):
      return self.maxtemp

  def dammiMin(self):
      return self.mintemp

  def aggiornaPath(self, nuovoPath):
          self.__path = nuovoPath
#errore tipico: dimenticarsi di usare self (python non da errore, perche lo prende per inizializzazione variabile)
  def dammiTemperatura(self):
      with open(self.__path) as f:
          content = f.readlines()[1]
          temp = float(content[len(content)-6:len(content)-1])
          temp = temp /1000
          #print(temp)
          if (temp > self.maxtemp):
              self.maxtemp = temp
          if (temp < self.mintemp):
              self.mintemp = temp
          return temp
