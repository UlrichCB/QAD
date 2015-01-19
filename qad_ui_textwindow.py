# -*- coding: latin1 -*-
"""
/***************************************************************************
 QAD Quantum Aided Design plugin

                              -------------------
        begin                : 2013-05-22
        copyright            : (C) 2013 IREN Acqua Gas SpA
        email                : geosim.dev@gruppoiren.it
        developers           : bbbbb aaaaa ggggg
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from PyQt4 import QtCore, QtGui


import qad_debug
from qad_msg import QadMsg


class Ui_QadTextWindow(object):
    def setupUi(self, QadTextWindow):
        QadTextWindow.setObjectName("QadTextWindow")
        QadTextWindow.setWindowModality(QtCore.Qt.NonModal)
        QadTextWindow.setEnabled(True)
        QadTextWindow.resize(642, 193)
        QadTextWindow.setMinimumSize(100, 20)
        QadTextWindow.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("QadTextWindowDockWidgetContents")
        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("QadTextWindowVBoxLayout")
        QadTextWindow.setWidget(self.dockWidgetContents)

        self.retranslateUi(QadTextWindow)
        QtCore.QMetaObject.connectSlotsByName(QadTextWindow)

    def retranslateUi(self, QadTextWindow):
       QadTextWindow.setWindowTitle(QadMsg.translate("Text_window", "Finestra di testo QAD"))

class Ui_QadCmdSuggestWindow(object):
    def setupUi(self, QadCmdSuggestWindow):
        QadCmdSuggestWindow.setObjectName("QadCmdsListWindow")
        QadCmdSuggestWindow.setWindowModality(QtCore.Qt.NonModal)
        QadCmdSuggestWindow.setEnabled(True)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("QadCmdsListWindowDockWidgetContents")
        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.vboxlayout.setObjectName("QadCmdsListWindowVBoxLayout")
        self.vboxlayout.setMargin(0)
        QadCmdSuggestWindow.setLayout(self.vboxlayout)        
        QtCore.QMetaObject.connectSlotsByName(QadCmdSuggestWindow)


