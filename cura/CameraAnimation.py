# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.


from PyQt5.QtCore import QVariantAnimation, QEasingCurve
from PyQt5.QtGui import QVector3D

from UM.Math.Vector import Vector
from UM.Logger import Logger


class CameraAnimation(QVariantAnimation):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._camera_tool = None
        self.setDuration(500)
        self.setEasingCurve(QEasingCurve.InOutQuad)

    def setCameraTool(self, camera_tool):
        self._camera_tool = camera_tool

    def setStart(self, start):
        Logger.log("d", "Camera start: %s %s %s" % (start.x, start.y, start.z))
        vec = QVector3D()  #QVector3D(start.x, start.y, start.z)
        vec.setX(start.x)
        vec.setY(start.y)
        vec.setZ(start.z)
        Logger.log("d", "setStartValue...")
        self.setStartValue(vec)

    def setTarget(self, target):
        Logger.log("d", "Camera end: %s %s %s" % (target.x, target.y, target.z))
        self.setEndValue(QVector3D(target.x, target.y, target.z))

    def updateCurrentValue(self, value):
        self._camera_tool.setOrigin(Vector(value.x(), value.y(), value.z()))
