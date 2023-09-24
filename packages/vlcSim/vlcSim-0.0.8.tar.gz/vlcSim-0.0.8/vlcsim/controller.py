from .scenario import *
from .connection import *
from enum import Enum


class Controller:
    status = Enum("status", "ALLOCATED NOT_ALLOCATED")
    nextStatus = Enum("nextStatus", "PAUSE FINISH RESUME IDLE")

    def __init__(self, x, y, z, nGrids, rho) -> None:
        self.__scenario = Scenario(x, y, z, nGrids, rho)
        vled = VLed(-1.25, -1.25, 2.15, 60, 60, 20, 70)
        vled.sliceTime = 2
        self.__scenario.addVLed(vled)
        vled = VLed(-1.25, 1.25, 2.15, 60, 60, 20, 70)
        vled.sliceTime = 2
        self.__scenario.addVLed(vled)
        vled = VLed(1.25, -1.25, 2.15, 60, 60, 20, 70)
        vled.sliceTime = 2
        self.__scenario.addVLed(vled)
        vled = VLed(1.25, 1.25, 2.15, 60, 60, 20, 70)
        vled.sliceTime = 2
        self.__scenario.addVLed(vled)
        self.__allocator = None
        self.__allocationStatus = None
        # self.__activeConnections = [[]] * len(self.__scenario.vleds)
        self.__activeConnections = []
        for i in range(len(self.__scenario.vleds)):
            self.__activeConnections.append([])
        self.__activeConnection = [0] * len(self.__activeConnections)

    @property
    def scenario(self):
        return self.__scenario

    @property
    def allocationStatus(self):
        return self.__allocationStatus

    @property
    def allocator(self):
        return self.__allocator

    @allocator.setter
    def allocator(self, allocator):
        self.__allocator = allocator

    def assignConnection(self, connection, time):
        # connection = Connection(id_connection, receiver)
        self.__allocationStatus, connection = self.__allocator(
            connection.receiver, connection, self.__scenario
        )
        connection.receiver.timeFirstConnected = time
        if self.__allocationStatus == Controller.status.ALLOCATED:
            if len(self.__activeConnections[connection.AP]) == 0:
                self.__scenario.vleds[connection.AP].setBUSY()
                self.__activeConnections[connection.AP].append(connection)
                return Controller.nextStatus.RESUME, time, connection
            else:
                self.__activeConnections[connection.AP].insert(
                    self.__activeConnection[connection.AP], connection
                )
                self.__activeConnection[connection.AP] += 1
                return Controller.nextStatus.IDLE, time, connection
        else:
            return Controller.nextStatus.IDLE, time, connection

    def pauseConnection(self, connection, time):
        receiver = connection.receiver
        receiver.timeActive += self.__scenario.vleds[connection.AP].sliceTime
        if len(self.__activeConnections[connection.AP]) > 1:
            self.__activeConnection[connection.AP] += 1
            self.__activeConnection[connection.AP] = self.__activeConnection[
                connection.AP
            ] % len(self.__activeConnections[connection.AP])
            connection = self.__activeConnections[connection.AP][
                self.__activeConnection[connection.AP]
            ]
        return Controller.nextStatus.RESUME, time, connection

    def resumeConnection(self, connection, time):
        receiver = connection.receiver
        if (
            receiver.goalTime
            < receiver.timeActive + self.__scenario.vleds[connection.AP].sliceTime
        ):
            return (
                Controller.nextStatus.FINISH,
                time + receiver.goalTime - receiver.timeActive,
                connection,
            )
        else:
            return (
                Controller.nextStatus.PAUSE,
                time + self.__scenario.vleds[connection.AP].sliceTime,
                connection,
            )

    def unassignConnection(self, connection, time):
        receiver = connection.receiver
        receiver.timeActive = receiver.goalTime
        receiver.timeFinished = time
        self.__activeConnections[connection.AP].pop(
            self.__activeConnection[connection.AP]
        )
        if len(self.__activeConnections[connection.AP]) == 0:
            self.__activeConnection[connection.AP] = 0
            self.__scenario.vleds[connection.AP].setIDLE()
            return Controller.nextStatus.IDLE, time, None
        self.__activeConnection[connection.AP] = self.__activeConnection[
            connection.AP
        ] % len(self.__activeConnections[connection.AP])
        if len(self.__activeConnections[connection.AP]) > 0:
            connection = self.__activeConnections[connection.AP][
                self.__activeConnection[connection.AP]
            ]
            return Controller.nextStatus.RESUME, time, connection
        else:
            self.__scenario.vleds[connection.AP].setIDLE()
            return Controller.nextStatus.IDLE, time, None
