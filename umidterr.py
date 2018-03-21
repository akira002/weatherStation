class UmidometroTerreno:
  import serial
  __path = '/dev/ttyACM0'
  __baud = 9600
  ser = serial.Serial(__path,__baud)
  maxumid = 0.0
  minumid = 100.0

  def dammiMax(self):
      return self.maxumid

  def dammiMin(self):
      return self.minumid

  def aggiornaPath(self, nuovoPath):
          self.__path = nuovoPath
          self.ser = serial.Serial(__path,__baud)
#errore tipico: dimenticarsi di usare self (python non da errore, perche lo prende per inizializzazione variabile)
  def dammiUmidita(self):
        read_serial=self.ser.readline()
        msg = read_serial.decode('ascii')
        msg = msg[0:len(msg)-1]
        umid = int(msg)
        percumid = (1024-umid)/1024*100
        if (percumid > self.maxumid):
            self.maxumid = percumid
        if (percumid < self.minumid):
            self.minumid = percumid
        return percumid
