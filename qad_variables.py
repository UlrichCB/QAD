# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QAD Quantum Aided Design plugin

 classe per gestire le variabili di ambiente
 
                              -------------------
        begin                : 2013-05-22
        copyright            : iiiii
        email                : hhhhh
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


from PyQt4.QtCore import *
import os.path
from qgis.core import *


import qad_utils
from qad_msg import QadMsg


#===============================================================================
# Qad variable class.
#===============================================================================
class QadVariableTypeEnum():
   UNKNOWN = 0 # sconosciuto (non gestito da QAD)
   STRING  = 1 # caratteri
   COLOR   = 2 # colore espresso in caratteri (es. rosso = "#FF0000")
   INT     = 3 # numero intero
   FLOAT   = 4 # nmer con decimali
   BOOL    = 5 # booleano (True o False)


#===============================================================================
# Qad variable class.
#===============================================================================
class QadVariable():
   """
   Classe che gestisce le variabili di ambiente di Qad
   """

   def __init__(self, name, value, typeValue, minNum = None, maxNum = None, descr = ""):
      self.name = name
      self.value = value
      self.typeValue = typeValue
      self.default = value
      self.minNum = minNum
      self.maxNum = maxNum
      self.descr = descr


#===============================================================================
# Qad variables class.
#===============================================================================
class QadVariablesClass():
   """
   Classe che gestisce le variabuili di ambiente di Qad
   """    
    
   def __init__(self):
      """
      Inizializza un dizionario con le variabili e i loro valori di default 
      """
      self.__VariableValuesDict = dict() # variabile privata <nome variabile>-<valore variabile>
      
      # ARCMINSEGMENTQTY (int): numero minimo di segmenti perché venga riconosciuto un arco
      VariableName = QadMsg.translate("Environment variables", "ARCMINSEGMENTQTY") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Minimum number of segments to approximate an arc.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(12), \
                                                            QadVariableTypeEnum.INT, \
                                                            4, 999, \
                                                            VariableDescr)
      
      # AUTOSNAP (int): attiva il puntamento polare (somma di bit):
      # 8 = Attiva il puntamento polare
      VariableName = QadMsg.translate("Environment variables", "AUTOSNAP")
      VariableDescr = QadMsg.translate("Environment variables", "Controls the display of the AutoSnap marker, tooltip, and magnet." + \
                                       "\nAlso turns on polar and object snap tracking, and controls the display of polar tracking, object snap tracking, and Ortho mode tooltips." + \
                                       "\nThe setting is stored as a bitcode using the sum of the following values:" + \
                                       "\n0 = Turns off the AutoSnap marker, tooltips, and magnet. Also turns off polar tracking, object snap tracking, and tooltips for polar tracking, object snap tracking, and Ortho mode." + \
                                       "\n1 = Turns on the AutoSnap mark." + \
                                       "\n2 = Turns on the AutoSnap tooltips." + \
                                       "\n4 = Turns on the AutoSnap magnet." + \
                                       "\n8 = Turns on polar tracking." + \
                                       "\n16 = Turns on object snap tracking." + \
                                       "\n32 = Turns on tooltips for polar tracking, object snap tracking, and Ortho mode.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(63), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 64, \
                                                            VariableDescr)
      
      # CIRCLEMINSEGMENTQTY (int): numero minimo di segmenti perché venga riconosciuto un cerchio
      VariableName = QadMsg.translate("Environment variables", "CIRCLEMINSEGMENTQTY") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Minimum number of segments to approximate a circle.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(12), \
                                                            QadVariableTypeEnum.INT, \
                                                            6, 999, \
                                                            VariableDescr)
      
      # CMDINPUTHISTORYMAX (int): Imposta il numero massimo di comandi nella lista di storicizzazione
      VariableName = QadMsg.translate("Environment variables", "CMDINPUTHISTORYMAX") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets the maximum number of previous input values that are stored for a prompt in a command.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(20), \
                                                            QadVariableTypeEnum.INT, \
                                                            1, 999, \
                                                            VariableDescr)
      
      # COPYMODE (int):
      # 0 = Imposta il comando COPIA in modo che venga ripetuto automaticamente
      # 1 = Imposta il comando COPIA in modo da creare una singola copia
      VariableName = QadMsg.translate("Environment variables", "COPYMODE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls whether the COPY command repeats automatically:" + \
                                       "\n0 = Sets the COPY command to repeat automatically." + \
                                       "\n1 = Sets the COPY command to create a single copy.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 1, \
                                                            VariableDescr)
      
      # CROSSINGAREACOLOR (str): Imposta il colore (RGB) dell'area di selezione degli oggetti nel modo intersezione
      VariableName = QadMsg.translate("Environment variables", "CROSSINGAREACOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the color of the transparent selection area during crossing selection (RGB, #33A02C = green)." + \
                                       "\nThe SELECTIONAREA system variable must be on.") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#33A02C"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # green 
      
      # CURSORCOLOR (str): Imposta il colore (RGB) del cursore (la croce)
      VariableName = QadMsg.translate("Environment variables", "CURSORCOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Cross pointer color (RGB, #FF0000 = red).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#FF0000"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # red 
      
      # CURSORSIZE (int): Imposta la dimensione in pixel del cursore (la croce)
      VariableName = QadMsg.translate("Environment variables", "CURSORSIZE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Determines the size of the crosshairs as a percentage of the screen size.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(5), \
                                                            QadVariableTypeEnum.INT, \
                                                            1, 100, \
                                                            VariableDescr)
      
      # DIMSTYLE (str): Imposta il nome dello stile di quotatura corrente
      VariableName = QadMsg.translate("Environment variables", "DIMSTYLE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Stores the name of the current dimension style.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode(""), \
                                                            QadVariableTypeEnum.STRING, \
                                                            None, None, \
                                                            VariableDescr)
      
      # EDGEMODE (int): Controlla i comandi ESTENDI e TAGLIA.
      # O = Vengono usate le dimensioni reali degli oggetti di riferimento
      # 1 = Vengono usate le estensioni  degli oggetti di riferimento (es. un arco viene considerato cerchio)
      VariableName = QadMsg.translate("Environment variables", "EDGEMODE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls how the TRIM and EXTEND commands determine cutting and boundary edges:" + \
                                       "\n0 = Uses the selected edge without an extensions." + \
                                       "\n1 = Extends or trims the selected object to an imaginary extension of the cutting or boundary edge.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 1, \
                                                            VariableDescr)
      
      # FILLETRAD (float): raggio applicato per raccordare (gradi)
      VariableName = QadMsg.translate("Environment variables", "FILLETRAD") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Stores the current fillet radius.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Real type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, float(0.0), \
                                                            QadVariableTypeEnum.FLOAT, \
                                                            0.000001, None, \
                                                            VariableDescr)

      # GRIPCOLOR (str): Imposta il colore (RGB) dei grip non selezionati
      VariableName = QadMsg.translate("Environment variables", "GRIPCOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the color of unselected grips (RGB, #100DD6 = blue).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#100DD6"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # blu 

      # GRIPCONTOUR (str): Imposta il colore (RGB) del bordo dei grip
      VariableName = QadMsg.translate("Environment variables", "GRIPCONTOUR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the color of the grip contour (RGB, #939393 = gray).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#939393"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # gray 

      # GRIPHOT(str): Imposta il colore (RGB) dei grip selezionati
      VariableName = QadMsg.translate("Environment variables", "GRIPHOT") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the color of selected grips (RGB, #FF0000 = red).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#FF0000"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # red 

      # GRIPHOVER(str): Imposta il colore (RGB) dei grip non selezionati quando il cursore si ferma su di essi
      VariableName = QadMsg.translate("Environment variables", "GRIPHOVER") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the fill color of an unselected grip when the cursor pauses over it (RGB, #FF7F7F = orange).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#FF7F7F"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # orange 

      # GRIPS (int): Controlla la visualizzazione dei grip sugli oggetti selezionati
      VariableName = QadMsg.translate("Environment variables", "GRIPS") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the use of selection set grips for the Stretch, Move, Rotate, Scale, and Mirror Grip modes." + \
                                       "\n0 = Hides grips." + \
                                       "\n1 = Displays grips." + \
                                       "\n2 = Displays additional midpoint grips on polyline segments.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(2), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 2, \
                                                            VariableDescr)

      # GRIPSIZE (int): Imposta la dimensione in pixel dei simboli di grip
      VariableName = QadMsg.translate("Environment variables", "GRIPSIZE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Grip symbol size in pixel.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(10), \
                                                            QadVariableTypeEnum.INT, \
                                                            1, 999, \
                                                            VariableDescr)

      # INPUTSEARCHDELAY  (int): Controlla il tempo trascorso prima che le funzionalità di tastiera vengano visualizzate sulla riga di comando
      VariableName = QadMsg.translate("Environment variables", "INPUTSEARCHDELAY") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the amount of time that elapses before automated keyboard features display at the Command prompt." + \
                                       "\nValid values are real numbers from 100 to 10,000, which represent milliseconds." + \
                                       "\nThe time delay setting in the INPUTSEARCHOPTIONS system variable must be turned on for INPUTSEARCHDELAY to have an effect.") # x lupdate      
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(300), \
                                                            QadVariableTypeEnum.INT, \
                                                            100, 10000, \
                                                            VariableDescr)

      # INPUTSEARCHOPTIONS (int): Controlla i tipi di funzioni automatiche della tastiera disponibili dalla riga di comando
      VariableName = QadMsg.translate("Environment variables", "INPUTSEARCHOPTIONS") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls what types of automated keyboard features are available at the Command prompt." + \
                                       "\nThe setting is stored as a bitcode using the sum of the following values:" + \
                                       "\n 0 = Turns off all automated keyboard features when typing at the Command prompt." + \
                                       "\n 1 = Turns on any automated keyboard features when typing at the Command prompt." + \
                                       "\n 2 = Automatically appends suggestions as each keystroke is entered after the second keystroke." + \
                                       "\n 4 = Displays a list of suggestions as keystrokes are entered." + \
                                       "\n 8 = Displays the icon of the command or system variable, if available." + \
                                       "\n16 = Excludes the display of system variables.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(15), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 31, \
                                                            VariableDescr)

      # OFFSETDIST(float): Setta la distanza di default per l'offset
      # < 0  offset di un oggetto attraverso un punto
      # >= 0 offset di un oggetto attraverso la distanza
      VariableName = QadMsg.translate("Environment variables", "OFFSETDIST") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets the default offset distance:" + \
                                       "\n<0 = Offsets an object through a specified point." + \
                                       "\n>=0 =  Sets the default offset distance.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Real type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, float(-1.0), \
                                                            QadVariableTypeEnum.FLOAT, \
                                                            None, None, \
                                                            VariableDescr)

      # OFFSETGAPTYPE (int):
      # 0 = Estende i segmenti di linea alle relative intersezioni proiettate
      # 1 = Raccorda i segmenti di linea in corrispondenza delle relative intersezioni proiettate.
      #     Il raggio di ciascun segmento di arco é uguale alla distanza di offset
      # 2 = Cima i segmenti di linea in corrispondenza delle intersezioni proiettate.
      #     La distanza perpendicolare da ciascuna cima al rispettivo vertice
      #     sull'oggetto originale é uguale alla distanza di offset.
      VariableName = QadMsg.translate("Environment variables", "OFFSETGAPTYPE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls how potential gaps between segments are treated when polylines are offset:" + \
                                       "\n0 = Extends line segments to their projected intersections." + \
                                       "\n1 = Fillets line segments at their projected intersections. The radius of each arc segment is equal to the offset distance." + \
                                       "\n2 = Chamfers line segments at their projected intersections. The perpendicular distance from each chamfer to its corresponding vertex on the original object is equal to the offset distance.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 2, \
                                                            VariableDescr)     
      
      # ORTHOMODE (int):
      # 0 = modalità di movimento ortogonale cursore disabilitata
      # 1 = modalità di movimento ortogonale cursore abilitata
      VariableName = QadMsg.translate("Environment variables", "ORTHOMODE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Constrains cursor movement to the perpendicular." + \
                                       "\nWhen ORTHOMODE is turned on, the cursor can move only horizontally or vertically:" + \
                                       "\n0 = Turns off Ortho mode." + \
                                       "\n1 = Turns on Ortho mode.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 1, \
                                                            VariableDescr)     
      
      # OSCOLOR (str): Imposta il colore (RGB) dei simboli di osnap
      VariableName = QadMsg.translate("Environment variables", "OSCOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Osnap symbols color (RGB, #FF0000 = red).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#FF0000"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # red
      
      # OSMODE (int): Imposta lo snap ad oggetto (somma di bit):
      # 0 = (NON) nessuno
      # 1 = (FIN) punti finali di ogni segmento
      # 2 = (MED) punto medio   
      # 4 = (CEN) centroide di un poligono   
      # 8 = (NOD) ad oggetto punto
      # 16 = (QUA) punto quadrante di un poligono
      # 32 = (INT) intersezione di un oggetto (anche i vertici intermedi di una linestring o polygon)
      # 64 = (INS) punto di inserimento di oggetti (come 8)
      # 128 = (PER) punto perpendicolare a un oggetto
      # 256 = (TAN) tangente di un arco, di un cerchio, di un'ellisse, di un arco ellittico o di una spline
      # 512 = (NEA) punto più vicino di un oggetto
      # 1024 = (C) Cancella tutti gli snap ad oggetto
      # 2048 = (APP) intersezione apparente di due oggetti che non si intersecano nello spazio 3D 
      #        ma che possono apparire intersecanti nella vista corrente
      # 4096 = (EST) Estensione : Visualizza una linea o un arco di estensione temporaneo quando si sposta il cursore sul punto finale degli oggetti, 
      #        in modo che sia possibile specificare punti sull'estensione
      # 8192 = (PAR) Parallelo: Vincola un segmento di linea, un segmento di polilinea, un raggio o una xlinea ad essere parallela ad un altro oggetto lineare
      # 16384 = osnap off
      # 65536 = (PR) Distanza progressiva
      # 131072 = intersezione sull'estensione
      # 262144 = perpendicolare differita
      # 524288 = tangente differita
      # 1048576 = puntamento polare
      # 2097152 = punti finali dell'intera polilinea
      VariableName = QadMsg.translate("Environment variables", "OSMODE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets running object snaps." + \
                                       "\nThe setting is stored as a bitcode using the sum of the following values:" + \
                                       "\n0 = NONe." + \
                                       "\n1 = ENDpoint." + \
                                       "\n2 = MIDpoint." + \
                                       "\n4 = CENter." + \
                                       "\n8 = NODe." + \
                                       "\n16 = QUAdrant." + \
                                       "\n32 = INTersection." + \
                                       "\n64 = INSertion." + \
                                       "\n128 = PERpendicular." + \
                                       "\n256 = TANgent." + \
                                       "\n512 = NEArest." + \
                                       "\n1024 = QUIck." + \
                                       "\n2048 = APParent Intersection." + \
                                       "\n4096 = EXTension." + \
                                       "\n8192 = PARallel." + \
                                       "\n65536 = PRogressive distance (PR[dist])." + \
                                       "\n131072 = Intersection on extension (EXT_INT)." + \
                                       "\n2097152 = Final points on polyline (FIN_PL).") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, None, \
                                                            VariableDescr)
      
      # OSPROGRDISTANCE (float): Distanza progressiva per snap PR
      VariableName = QadMsg.translate("Environment variables", "OSPROGRDISTANCE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Progressive distance for <Progressive distance> snap mode.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Real type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, float(0.0), \
                                                            QadVariableTypeEnum.FLOAT, \
                                                            None, None, \
                                                            VariableDescr)
      
      # OSSIZE (int): Imposta la dimensione in pixel dei simboli di osnap
      VariableName = QadMsg.translate("Environment variables", "OSSIZE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Osnap symbol size in pixel.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(13), \
                                                            QadVariableTypeEnum.INT, \
                                                            1, 999, \
                                                            VariableDescr)
      
      # PICKADD (int): Controlla se le selezioni successive sostituiscono il gruppo di selezione corrente o vengono aggiunte ad esso.
      VariableName = QadMsg.translate("Environment variables", "PICKADD") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls whether subsequent selections replace the current selection set or add to it." + \
                                       "\n0 = Turns off PICKADD. The objects most recently selected become the selection set. Previously selected objects are removed from the selection set. Add more objects to the selection set by pressing SHIFT while selecting." + \
                                       "\n1 = Turns on PICKADD. Each object selected, either individually or by windowing, is added to the current selection set. To remove objects from the set, press SHIFT while selecting." + \
                                       "\n2 = Turns on PICKADD. Each object selected, either individually or by windowing, is added to the current selection set. To remove objects from the set, press SHIFT while selecting. Keeps objects selected after the SELECT command ends. ") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 2, \
                                                            VariableDescr)
      
      # PICKBOX (int): Imposta la dimensione in pixel della distanza di selezione degli oggetti
      # dalla posizione corrente del puntatore
      VariableName = QadMsg.translate("Environment variables", "PICKBOX") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets the object selection target height, in pixels.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(5), \
                                                            QadVariableTypeEnum.INT, \
                                                            1, 999, \
                                                            VariableDescr)
      
      # PICKBOXCOLOR (str): Imposta il colore (RGB) del quadratino di selezione degli oggetti
      VariableName = QadMsg.translate("Environment variables", "PICKBOXCOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets the object selection target color (RGB, #FF0000 = red).") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#FF0000"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # red 

      # PICKFIRST (int): Controlla se è possibile selezionare gli oggetti prima di eseguire un comando.
      VariableName = QadMsg.translate("Environment variables", "PICKFIRST") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls whether you can select objects before you start a command." + \
                                       "\n0 = Off. You can select objects only after you start a command." + \
                                       "\n1 = On. You can also select objects before you start a command") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(1), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 1, \
                                                            VariableDescr)

      # POLARANG (float): incremento dell'angolo polare per il puntamento polare (gradi)
      VariableName = QadMsg.translate("Environment variables", "POLARANG") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Sets the polar angle increment (degree).") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Real type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, float(90.0), \
                                                            QadVariableTypeEnum.INT, \
                                                            0.000001, 359.999999, \
                                                            VariableDescr)
      
      # SELECTIONAREA (int): Controlla gli effetti della visualizzazione della selezione di aree.
      # dalla posizione corrente del puntatore
      VariableName = QadMsg.translate("Environment variables", "SELECTIONAREA") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the display of effects for selection areas." + \
                                       "\nSelection areas are created by the Window, Crossing, WPolygon, CPolygon, WCircle, CCircle, WObjects, CObjects, WBuffer and CBuffer options of SELECT." + \
                                       "\n0 = Off" + \
                                       "\n1 = On") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(1), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 1, \
                                                            VariableDescr)
      
      # SELECTIONAREAOPACITY (int): Controlla gli effetti della visualizzazione della selezione di aree.
      # dalla posizione corrente del puntatore
      VariableName = QadMsg.translate("Environment variables", "SELECTIONAREAOPACITY") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the transparency of the selection area during window and crossing selection." + \
                                       "\nThe valid range is 0 to 100. The lower the setting, the more transparent the area. A value of 100 makes the area opaque. The SELECTIONAREA system variable must be on.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Integer type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, int(25), \
                                                            QadVariableTypeEnum.INT, \
                                                            0, 100, \
                                                            VariableDescr)

      # SUPPORTPATH (str): Path di ricerca per i files di supporto
      default = os.path.abspath(os.path.dirname(__file__) + "\\support")
      VariableName = QadMsg.translate("Environment variables", "SUPPORTPATH") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Searching path for support files.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, default, \
                                                            QadVariableTypeEnum.STRING, \
                                                            None, None, \
                                                            VariableDescr)
      
      # SHOWTEXTWINDOW (bool): Visualizza la finestra di testo all'avvio
      VariableName = QadMsg.translate("Environment variables", "SHOWTEXTWINDOW") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Show the text window at startup.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Boolean type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, True, \
                                                            QadVariableTypeEnum.BOOL, \
                                                            None, None, \
                                                            VariableDescr)
      
      # TOLERANCE2APPROXCURVE (float):
      # massimo errore tollerato tra una vera curva e quella approssimata dai segmenti retti
      # (nel sistema map-coordinate)
      VariableName = QadMsg.translate("Environment variables", "TOLERANCE2APPROXCURVE") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Maximum error approximating a curve to segments.") # x lupdate
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Real type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, float(0.1), \
                                                            QadVariableTypeEnum.FLOAT, \
                                                            0.000001, None, \
                                                            VariableDescr)
      
      # WINDOWAREACOLOR (str): Imposta il colore (RGB) dell'area di selezione degli oggetti nel modo finestra
      VariableName = QadMsg.translate("Environment variables", "WINDOWAREACOLOR") # x lupdate
      VariableDescr = QadMsg.translate("Environment variables", "Controls the color of the transparent selection area during window selection (RGB, #1F78B4 = blu)." + \
                                       "\nThe SELECTIONAREA system variable must be on.") # x lupdate                                       
      VariableDescr = VariableDescr + "\n" + QadMsg.translate("Environment variables", "Character type.")
      self.__VariableValuesDict[VariableName] = QadVariable(VariableName, unicode("#1F78B4"), \
                                                            QadVariableTypeEnum.COLOR, \
                                                            None, None, \
                                                            VariableDescr) # blue 
      

   def getVarNames(self):
      """
      Ritorna la lista dei nomi delle variabili 
      """
      return self.__VariableValuesDict.keys()
          
   def set(self, VarName, VarValue):
      """
      Modifica il valore di una variabile 
      """
      UpperVarName = VarName.upper()
      variable = self.getVariable(UpperVarName)
      
      if variable is None: # se non c'è la variablie
         self.__VariableValuesDict[UpperVarName] = QadVariable(UpperVarName, VarValue, \
                                                               QadVariableTypeEnum.UNKNOWN, \
                                                               None, None, \
                                                               "")
      else:
         if type(variable.value) != type(VarValue):
            if not((type(variable.value) == unicode or type(variable.value) == str) and
                   (type(VarValue) == unicode or type(VarValue) == str)):
               return False
         if variable.typeValue == QadVariableTypeEnum.COLOR:
            if len(VarValue) == 7: # es. "#FF0000"
               if VarValue[0] != "#":
                  return False
            else:
               return False
         elif variable.typeValue == QadVariableTypeEnum.FLOAT or \
              variable.typeValue == QadVariableTypeEnum.INT:
            if variable.minNum is not None:
               if VarValue < variable.minNum:
                  return False 
            if variable.maxNum is not None:
               if VarValue > variable.maxNum:
                  return False 
         
         self.__VariableValuesDict[UpperVarName].value = VarValue

      return True
       
   def get(self, VarName, defaultValue = None):
      """
      Restituisce il valore di una variabile 
      """
      variable = self.getVariable(VarName)
      if variable is None:
         result = defaultValue
      else:
         result = variable.value
      
      return result

   def getVariable(self, VarName):
      UpperVarName = VarName
      return self.__VariableValuesDict.get(UpperVarName.upper())


   def getDefaultQadIniFilePath(self):
      # ottiene il percorso automatico incluso il nome del file dove salvare il file qad.ini
      # se esiste un progetto caricato il percorso è quello del progetto
      prjFileInfo = QFileInfo(QgsProject.instance().fileName())
      path = prjFileInfo.absolutePath()
      if len(path) == 0:
         # se non esiste un progetto caricato uso il percorso di installazione di qad
         path = QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "python/plugins/qad")
      return path + "/" + "qad.ini"
   
            
   def save(self, Path=""):
      """
      Salva il dizionario delle variabili su file 
      """
      if Path == "":
         # Se la path non é indicata uso il file "qad.ini" del progetto o dell'installazione di qad 
         Path = self.getDefaultQadIniFilePath()
      
      dir = QFileInfo(Path).absoluteDir()
      if not dir.exists():
         os.makedirs(dir.absolutePath())
       
      file = open(Path, "w") # apre il file in scrittura
      for VarName in self.__VariableValuesDict.keys():
         VarValue = self.get(VarName)
         # scrivo il valore + il tipo (es var = 5 <type 'int'>)
         VarValue = str(VarValue) + " " + str(type(VarValue))
         Item = "%s = %s\n" % (VarName, VarValue)
         file.write(Item)
          
      file.close()
 
   def load(self, Path=""):
      """
      Carica il dizionario delle variabili da file
      Ritorna True in caso di successo, false in caso di errore
      """
      # svuoto il dizionario e lo reimposto con i valori di default
      self.__VariableValuesDict.clear()
      self.__init__()
      if Path == "":
         # Se la path non é indicata uso il file "qad.ini" del progetto o dell'installazione di qad 
         Path = self.getDefaultQadIniFilePath()

      if not os.path.exists(Path):
         return False
                    
      file = open(Path, "r") # apre il file in lettura
      for line in file:
         # leggo il valore + il tipo (es var = 5 <type 'int'>)
         sep = line.rfind(" = ")
         VarName = line[0:sep]
         VarName = VarName.strip(" ") # rimuovo gli spazi prima e dopo
         VarValue = line[sep+3:]
         sep = VarValue.rfind(" <type '")
         sep2 = VarValue.rfind("'>")
         VarType = VarValue[sep+8:sep2]
         VarValue = VarValue[:sep]
         if VarType == "int":
            VarValue = qad_utils.str2int(VarValue)
            if VarValue is None:
               self.set(VarName, int(0))
            else:
               self.set(VarName, VarValue)
         elif VarType == "long":
            VarValue = qad_utils.str2long(VarValue)
            if VarValue is None:
               self.set(VarName, long(0))
            else:
               self.set(VarName, VarValue)
         elif VarType == "float":
            VarValue = qad_utils.str2float(VarValue)
            if VarValue is None:
               self.set(VarName, float(0))
            else:
               self.set(VarName, VarValue)
         elif VarType == "bool":
            VarValue = qad_utils.str2bool(VarValue)
            if VarValue is None:
               self.set(VarName, False)
            else:
               self.set(VarName, VarValue)
         else:
            self.set(VarName, str(VarValue))
            
      file.close()
      
      return True


#===============================================================================
#  = variabile globale
#===============================================================================

QadVariables = QadVariablesClass()
