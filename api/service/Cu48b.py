#!/usr/bin/python3

from serial.tools.list_ports import comports
from service.KerongCommProtocol import KerongCommProtocol


class Cu48b:

    port_name = "COM3"
    baudrate = 19200
    lockers = []
    sensors = []

    def onResponse(self, lockers, sensors):
        self.lockers = lockers
        self.sensors = sensors

    def getStatus(self):
        comm = KerongCommProtocol(self.port_name, self.baudrate, self.onResponse)
        comm.open()
        comm.send(0, KerongCommProtocol.LOCKER_ALL, KerongCommProtocol.GET_STATUS)
        comm.read()
        comm.close()

    def unlock(self, board_number, lock_number):
        comm = KerongCommProtocol(self.port_name, self.baudrate, None)
        comm.open()
        comm.send(board_number, lock_number, KerongCommProtocol.LOCKER_UNLOCK)
        comm.close()

    def unlockAll(self):
        comm = KerongCommProtocol(self.port_name, self.baudrate, None)
        comm.open()
        comm.send(0, KerongCommProtocol.LOCKER_ALL, KerongCommProtocol.LOCKER_UNLOCK)
        comm.close()

    @staticmethod
    def getAvailablePorts():
        ports = []
        for port, desc, hwid in sorted(comports()):
            ports.append(port)
        return ports


if __name__ == "__main__":
    cu48b = Cu48b()
    cu48b.getStatus()

# try:
#     main()
# except Exception as exception:
#     print(exception)