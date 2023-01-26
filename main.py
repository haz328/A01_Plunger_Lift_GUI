# -*- coding: utf-8 -*-
"""
The TUALP plunger lift simulator graphic user interface (GUI)
@author: jiz172

Version history:
Jianjun Zhu     Jul 23 2019     Started version 1.0
"""

import sys
import os
path_abs = os.path.dirname(os.path.abspath(__file__))   # current path
path = os.path.join(path_abs, 'C:\\Users\\haz328\\Desktop\\Github') # join path
sys.path.append(path)  # add to current py

from TUALP_Models import *
import numpy as np
import pandas as pd
import sqlite3
import matplotlib as mpl
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import xml.etree.ElementTree as ET
from Public_variables import *
import time
import threading
from queue import Queue

from mainWindow import Ui_MainWindow
from about import Ui_Dialog as aboutUI
from case_db import Ui_Dialog as caseUI

sys.path.append("..")
# from Funcs import *     #import plunger lift model

mpl.use('Qt5Agg')
plt.style.use('seaborn-ticks')
mpl.rcParams['figure.figsize'] = (4, 3)
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['markers.fillstyle'] = 'none'
mpl.rcParams['lines.markersize'] = 5



"""global constants"""
psi_to_pa = 1.013e5 / 14.7
psi_to_ft = 2.3066587368787
bbl_to_m3 = 0.15897
colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
symbols = ['o', 's', '^', '*', 'd', 'p', 'v', 'D', 'x', '+']
T_Final=0

PI = np.pi                  # 3.1415926
G = 9.81                    # gravitational acceleration m/s/s
R = 8.314                   # J/mol/K
M_air = 28.97e-3            # air molecular weight in kg/mol
UiMPa = 10e6                # MPa to Pa




# main window
class plungerLiftGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(plungerLiftGUI, self).__init__(parent)
        self.setupGUI()
        self.setConnection()
        self.inputs = {"Well_name": 'Well_1', "Well_depth":10000 * 0.3048 , "Tubing_ID":1.995 * 0.0254 ,
        "Tubing_OD":2.125 * 0.0254, "Casing_ID":4.85 * 0.0254,"Vertical_roughness":2.5e-4, "Horizontal_length":1500 * 0.3048,
        "Inclination_angle":1, "Inner_diameter":4.85 * 0.0254, "Horizontal_roughness":2.5e-4, 
        "Plunger_weight":5, "Plunger_length":0.4, "Plunger_diameter":1.9 * 0.0254, 
        "Plunger_drag_coefficient":0.1019, "Plunger_rise":0.0457,
        "Line_pressure": 1.1e6, "Valve_Cv":0.5e-7, "Surface_T": 288,
        "Relative_density_L":0.85, "Relative_density_G":0.7, "Liquid_viscosity":4e-4,
        "Reservoir_C": 2.58e-15, "Reservoir_n":1, "Reservoir_P":6e6,
        "GLR": 10, "Geothermal_gradient": 0.03, "Gas_solubility":0.1,
        "Casing_pressure":1.6e6, "Tubing_pressure": 1.57e6, "L_above_plunger": 5.,
        "L_below_plunger": 0., "Time_step_horizontal":0.5, "Time_step_upward":5.,
        "Time_step_downward": 10., "Plunger_cycle": 1., "Plunger_period": 30,
        "Valve_open_T": 12., "Fluid_type":1}
        self.z_f = [0.13,0.18,61.92,14.08,8.35,0.97,3.41,0.84,1.48,1.79,6.85]
        self.Pc_f = [493,1070.6,667.8,707.8,616.3,529.1,550.7,490.4,488.6,436.9,350]
        self.w_f = [0.04,0.23,0.01,0.1,0.15,0.18,0.19,0.23,0.25,0.3,0.38]
        self.Tc_f = [-232.4,87.9,-116.6,90.1,206,275,305.7,369.1,385.7,453.7,650]
        self.M_f = [28.02,44.01,16.04,30.07,44.1,58.12,58.12,72.15,72.15,86.18,143]
        self.dfcompositional = pd.DataFrame({"z_f": self.z_f,  "Pc_f": self.Pc_f,       "w_f": self.w_f, "Tc_f": self.Tc_f,
                    "M_f": self.M_f})



        self.uploadGUI()
        self.init()
        self.dfoutput = pd.DataFrame()
        # set the tab page index
        self.tabWidget_simulation.setCurrentIndex(0)

        # ToolButton in Configuration
        self.btnWell.clicked.connect(self.btnWell_clicked)
        self.btnSurface.clicked.connect(self.btnSurface_clicked)
        self.btnFluid.clicked.connect(self.btnFluid_clicked)
        self.btnReservoir.clicked.connect(self.btnReservoir_clicked)

        # Toolbutton in Simulation
        self.btnRun.clicked.connect(self.btnRun_clicked)
        self.btnStop.clicked.connect(self.btnStop_clicked)
        self.Thread_icon=0          # Thread #
        self.r=[]                   # Thread list
        self.btnReset.clicked.connect(self.btnReset_clicked)
        self.btnResults.clicked.connect(self.btnResults_clicked)
        self.btnOutput.clicked.connect(self.btnOutput_clicked)      # pass for now 

        # ToolButton in Analyze
        self.btnPlot.clicked.connect(self.btnPlot_clicked)
        self.btnData.clicked.connect(self.btnData_clicked)
        self.btn_reset_analyzePlot.clicked.connect(self.btn_reset_analyzePlot_clicked)
        self.btn_save_analyzePlot.clicked.connect(self.btn_save_analyzePlot_clicked)      # pass for now 
        self.btn_reset_analyzeData.clicked.connect(self.btn_reset_analyzeData_clicked)
        self.btn_save_analyzeData.clicked.connect(self.btn_save_analyzeData_clicked)      # pass for now         
        

        # Toolbox and tabWidget connection
        self.tabWidget_main.currentChanged.connect(self.tabWidget_main_currentChanged)
        self.toolBox.currentChanged.connect(self.toolBox_currentChanged)

    
        # plot1 initialize (simulation plot 1)
        self.figure1 = plt.figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.toolbar1.setMaximumHeight(20)
        self.ax1 = self.figure1.add_subplot(111)
        plot_layout1 = QtWidgets.QVBoxLayout()
        plot_layout1.addWidget(self.toolbar1)
        plot_layout1.addWidget(self.canvas1)
        self.widget_simulationPlot1.setLayout(plot_layout1)

        # plot2 initialize (simulation plot 2)
        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.toolbar2.setMaximumHeight(20)
        self.ax2 = self.figure2.add_subplot(111)
        plot_layout2 = QtWidgets.QVBoxLayout()
        plot_layout2.addWidget(self.toolbar2)
        plot_layout2.addWidget(self.canvas2)
        self.widget_simulationPlot2.setLayout(plot_layout2)

        # plot3 initialize (Analyze plot)
        self.figure3 = plt.figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        self.toolbar3.setMaximumHeight(20)
        self.ax3 = self.figure3.add_subplot(111)
        plot_layout3 = QtWidgets.QVBoxLayout()
        plot_layout3.addWidget(self.toolbar3)
        plot_layout3.addWidget(self.canvas3)
        self.widget_analyzePlot.setLayout(plot_layout3)

        # ComboBox
        self.comboBox_analyzePlot.addItems(["Plunger acceleration", "Plunger velocity", "Production rate", "Pressure", "Liquid column"])
        self.comboBox_analyzePlot.currentIndexChanged.connect(self.comboBox_analyzePlot_index_changed)

        # Output data
        self.tableWidget_analyzeData.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)


    def runUI(self,n,q):
        
        global Pc, Pt, Pl, Ltt, Ltb, mga, mla, mgtt, mltt, mgtb, mltb, Xp, Vp, Ar, v, La, Pcb, Ptb, Pwf, Fgout, Ppb, Ppt, \
           Acc, Flout, Fgtub, Fltub, Fgres, Flres, Fgann, Flann, t, dt, Ltt0
        global Thread_Run

        initialize(self.inputs)
        # initialize(self.inputs, self.dfcompositional)
        # print(Xp, La)
        starttime=time.time()
        self.time = []
        self.XP = []
        self.VP = []
        self.ACC = []
        self.Fout = []
        self.PC = []
        self.PL = []
        self.PT = []
        self.PWF = []
        self.LT = []
        self.LA = []
        self.LTT = []
        self.LTB = []
        self.MGA = []
        self.MGTT = []
        self.MGTB = []

        self.icon = 0



        Thread_Run=True
        counter = 0

        
        Xp, Vp, Acc, Pc, Pt, Pwf, Ppt, Ptb, La, Ltt, Ltb, mga, mgtt, mgtb, Flout, Fgout=updateUI(t,dt,Xp,Vp,Ltt0,False)
        self.ax1.tick_params(direction='in', labelsize=6)
        self.ax1.plot(t, Pc / 1e6, 'k-', label='Pc')
        self.ax1.plot(t, Pt / 1e6, 'b--', label='Pt')
        self.ax1.plot(t, Pwf / 1e6, 'r-.', label='Pwf')
        self.ax1.plot(t, Pl / 1e6, 'y-.', label='Pl')
        self.ax1.legend(frameon=False)
        self.canvas1.draw()

        self.ax2.tick_params(direction='in', labelsize=6)
        self.ax2.plot(t, Vp, 'r-.', label='Vp')
        self.ax2.legend(frameon=False)
        self.canvas2.draw()

 
        try:
            while counter < cycles:

                Xp = 0
                Vp = 0
                Ltt0 = Ltt
                # print("{} cycle starts at {} s".format(counter+1, t), '\n')
                _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, =updateUI(t, dt, Xp, Vp, Ltt0, True)
                # print_io()
                while Thread_Run and t < Period * (counter + 1):
                    if t < T_open + Period * counter:
                        if Xp != H_well:
                            dt = dt_H
                        else:
                            dt = dt_U
                    else:
                        dt = dt_D
                    Xp, Vp, Acc, Pc, Pt, Pwf, Ppt, Ptb, La, Ltt, Ltb, mga, mgtt, mgtb, Flout, Fgout=updateUI(t,dt,Xp,Vp,Ltt0,False)
                    self.time.append(t)
                    self.XP.append(Xp)
                    self.LA.append(La)
                    self.LT.append(Ltt + Ltb)
                    self.VP.append(Vp)
                    self.ACC.append(Acc)
                    qprod = Fgout / gas_density_std(den_gas_relative, 273.15, 1e5) + Flout / denl
                    self.Fout.append(1000 * qprod)
                    self.PC.append(Pc / 1e6)
                    self.PL.append(Pl / 1e6)
                    self.PT.append(Pt / 1e6)
                    self.PWF.append(Pwf / 1e6)
                    self.LTT.append(Ltt)
                    self.LTB.append(Ltb)
                    self.MGA.append(mga)
                    self.MGTT.append(mgtt)
                    self.MGTB.append(mgtb)

                    if t < T_open + Period * counter:
                        if Xp != H_well:
                            dt = dt_H
                        else:
                            dt = dt_U
                        upward()
                    else:
                        dt = dt_D
                        downward()
                    t += dt

                    if self.icon==4:
                        self.ax1.tick_params(direction='in', labelsize=6)
                        self.ax1.plot(self.time[-5:], self.PC[-5:], 'k-', label='Pc')
                        self.ax1.plot(self.time[-5:], self.PT[-5:], 'b--', label='Pt')
                        self.ax1.plot(self.time[-5:], self.PWF[-5:], 'r-.', label='Pwf')
                        self.ax1.plot(self.time[-5:], self.PL[-5:], 'y:', label='Pl')
                        self.canvas1.draw()

                        self.ax2.tick_params(direction='in', labelsize=6)
                        self.ax2.plot(self.time[-5:], self.VP[-5:], 'r-', label='Vp')
                        self.canvas2.draw()
                        self.icon = 1
                    else:
                        self.icon +=1

                # next cycle
                counter += 1
                if Ppt>50000000.0:
                    try:
                        pass
                    except expression as identifier:
                        pass
        except:
            pass

            self.dfoutput = pd.DataFrame({"time": self.time,  "Xp": self.XP,       "Acc": self.ACC, "Vp": self.VP,
                                "Pc": self.PC,      "Pt": self.PT,       "Pwf": self.PWF, "PL": self.PL,
                                "La": self.LA,      "Ltt": self.LTT,     "Ltb": self.LTB, "Fout": self.Fout,
                                "mga": self.MGA,    "mgtt": self.MGTT,   "mgtb": self.MGTB})
            q.put(self.dfoutput)



        self.dfoutput = pd.DataFrame({"time": self.time,  "Xp": self.XP,       "Acc": self.ACC, "Vp": self.VP,
                    "Pc": self.PC,      "Pt": self.PT,       "Pwf": self.PWF, "PL": self.PL,
                    "La": self.LA,      "Ltt": self.LTT,     "Ltb": self.LTB, "Fout": self.Fout,
                    "mga": self.MGA,    "mgtt": self.MGTT,   "mgtb": self.MGTB})
        # q.put(self.dfoutput)


        self.tableWidget_analyzeData.setRowCount(self.dfoutput.shape[0])
        self.tableWidget_analyzeData.setColumnCount(self.dfoutput.shape[1])
        header=list(self.dfoutput)
        self.tableWidget_analyzeData.setHorizontalHeaderLabels(header) 
        for i in range(self.dfoutput.shape[0]):
            for j in range(self.dfoutput.shape[1]):
                self.tableWidget_analyzeData.setItem(i, j, QtWidgets.QTableWidgetItem(str(np.around(self.dfoutput.iloc[i, j], decimals=4))))

        endtime=time.time()
        print(starttime-endtime)

        # self.msg = QtWidgets.QMessageBox()
        # self.msg.setIcon(QtWidgets.QMessageBox.Information)
        # self.msg.setText("Calculation Complete!")
        # self.msg.setWindowTitle("Finish")
        # self.msg.exec_()
        
        # msg = QtWidgets.QMessageBox()
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setText("Calculation Complete!")
        # msg.setWindowTitle("Finish")
        # msg.exec_()

    def Threadupdate(self):
        # pass
        self.ax1.plot(t, Pc / 1e6, 'k-', label='Pc')
        self.ax1.plot(t, Pt / 1e6, 'b--', label='Pt')
        self.ax1.plot(t, Pwf / 1e6, 'r-.', label='Pwf')
        self.ax1.plot(t, Pl / 1e6, 'y-.', label='Pl')
        self.canvas1.draw()

        self.ax2.plot(t, Vp, 'r-.', label='Vp')
        self.canvas2.draw()

        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.tick_params(direction='in', labelsize=6)
        self.ax1.plot(self.r[self.Thread_icon-1].time, self.r[self.Thread_icon-1].PC, 'k-', label='Pc')
        self.ax1.plot(self.r[self.Thread_icon-1].time, self.r[self.Thread_icon-1].PT, 'b--', label='Pt')
        self.ax1.plot(self.r[self.Thread_icon-1].time, self.r[self.Thread_icon-1].PWF, 'r-.', label='Pwf')
        self.ax1.plot(self.r[self.Thread_icon-1].time, self.r[self.Thread_icon-1].PL, 'y-.', label='Pl')
        self.ax1.set_title('Puressure', fontsize=6)
        self.ax1.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax1.set_ylabel(r'$P$ (MPa)', fontsize=6)
        self.canvas1.draw()

        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.tick_params(direction='in', labelsize=6)
        self.ax2.plot(self.r[self.Thread_icon-1].time, self.r[self.Thread_icon-1].VP, 'r-.', label='Vp')
        self.ax2.set_title('Plunger velocity', fontsize=6)
        self.ax2.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax2.set_ylabel(r'$V_{p}$ (m/s)', fontsize=6)
        self.canvas2.draw()

    def Threadfinish(self):
        
        # self.dfoutput=self.q.get()        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("The calculation is finished!")
        msg.setWindowTitle("Finish")
        msg.exec_()

            # data = pd.DataFrame({"time": time,  "Xp": XP,       "Acc": ACC, "Vp": VP,
            #                     "Pc": PC,      "Pt": PT,       "Pwf": PWF, "PL": PL,
            #                     "La": LA,      "Ltt": LTT,     "Ltb": LTB, "Fout": Fout,
            #                     "mga": MGA,    "mgtt": MGTT,   "mgtb": MGTB})
        self.figure1.clear()
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.tick_params(direction='in', labelsize=6)
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pc"], 'k-', label='Pc')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pt"], 'b--', label='Pt')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pwf"], 'r-.', label='Pwf')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["PL"], 'y-.', label='Pl')
        self.ax1.set_title('Puressure', fontsize=6)
        self.ax1.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax1.set_ylabel(r'$P$ (MPa)', fontsize=6)
        self.canvas1.draw()


        self.figure2.clear()
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.tick_params(direction='in', labelsize=6)
        self.ax2.plot(self.dfoutput["time"], self.dfoutput["Vp"], 'r-.', label='Vp')
        self.ax2.set_title('Plunger velocity', fontsize=6)
        self.ax2.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax2.set_ylabel(r'$V_{p}$ (m/s)', fontsize=6)
        self.canvas2.draw()

    def btnRun_clicked(self):
        self.load_Inputs()
        self.init()
        self.tabWidget_simulation.setCurrentIndex(1)
        self.q=Queue()
        t=threading.Thread(target=self.runUI,args=(0,self.q))
        # t.finished.connect(self.Threadfinish)

        # self.r.append(btnRunThread(self.inputs))
        self.r.append(t)
        # self.r[self.Thread_icon].update.connect(self.Threadupdate)
        # self.r[self.Thread_icon].finished.connect(self.Threadfinish)
        # self.threads.append(self.r)
        self.figure1.clear()
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.tick_params(direction='in', labelsize=6)
        self.ax1.set_title('Puressure', fontsize=6)
        self.ax1.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax1.set_ylabel(r'$P$ (MPa)', fontsize=6)
        self.canvas1.draw()

        self.figure2.clear()
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.tick_params(direction='in', labelsize=6)
        self.ax2.set_title('Plunger velocity', fontsize=6)
        self.ax2.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax2.set_ylabel(r'$V_{p}$ (m/s)', fontsize=6)
        self.ax2.tick_params(direction='in', labelsize=6)
        self.canvas2.draw()

        self.r[self.Thread_icon].start()
        # self.r[self.Thread_icon].join()
        # results=[]
        # results.append(self.q.get())
        # self.dfoutput=results[0].copy()     
        self.Thread_icon+=1

    def btnStop_clicked(self):
        try:
            global Thread_Run
            Thread_Run=False
            # self.dfoutput=self.q.get()      
            # self.dfoutput = self.r[self.Thread_icon-1].data
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Calculation Complete!")
            self.msg.setWindowTitle("Finish")
            self.msg.exec_()
        except:
            pass

    def btnReset_clicked(self):
        self.resetCalculation()
        self.figure1.clear()
        self.canvas1.draw()

        self.figure2.clear()
        self.canvas2.draw()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Case resetted!")
        msg.setWindowTitle("Reset Case")
        msg.exec_()

    def resetCalculation(self):
        updateUIinitial(self.inputs["L_above_plunger"])
        global mla, mgtt, mltt, mgtb, mltb, Xp, Vp, Ar, v, La, Pcb, Ptb, Pwf, PwfB, Fgout, Flout, t, dt, PGT, \
            Ppb, Ppt, Acc, Fgres, Flres, FgresB, FlresB, Fgtub, Fltub, Fgann, Flann, Ltt0, HLB
        mga =0.                    # mass of gas in annulus (kg)
        mla = 0.                    # mass of liquid in annulus (kg)
        mgtt = 0.                   # mass of gas in tubing top (kg)
        mltt = 0.                   # mass of liquid in tubing top (kg)
        mgtb = 0.                   # mass of gas in tubing bottom (kg)
        mltb = 0.                   # mass of liquid in tubing bottom (kg)
        Xp = 0.                     # plunger position from tubing shoe (m), initially at the bottom
        Vp = 0.                     # plunger velocity (m/s)
        Ar = 0.                     # plunger arrival time (s)
        v = 0                       # motor valve open or close: 0 - close, 1 - open
        # intermediate variables
        La = 0.                     # ASSUME initial liquid column length in annulus (m)
        Pcb = Pc                    # annular pressure right above liquid level
        Ptb = Pt                    # tubing gas pressure right above plunger
        Pwf = 0                     # bottom pressure at tubing shoe
        PwfB = 0.                   # bottom pressure at wellbore
        Fgout = 0.                  # surface gas mass flow rate (kg/s)
        Flout = 0.                  # surface liquid mass flow rate (kg/s)
        t = 0.                      # calculation time
        dt = 0.01                   # delta t in s
        PGT = 0.                    # total pressure gradient in horizontal well (pa/m)
        Ppb = 0.                    # pressure on the bottom of plunger
        Ppt = 0.                    # pressure on top of the plunger
        Acc = -1                    # plunger acceleration in m/s2
        Fgres = 0.                  # gas flow from horizontal well kg/s
        Flres = 0.                  # liquid flow from horizontal well kg/s
        FgresB = 0.                 # gas flow from reservoir kg/s
        FlresB = 0.                 # liquid flow from reservoir kg/s
        Fgtub = 0.                  # gas flow into tubing kg/s
        Fltub = 0.                  # liquid flow into tubing kg/s
        Fgann = 0.                  # gas flow into annulus kg/s
        Flann = 0.                  # liquid flow into annulus kg/s
        Ltt0 = self.inputs["L_above_plunger"]                # initial liquid height in tubing for each plunger cycle
        HLB = 1                     # liquid holdup in the inclined or horizontal section of wellbore`
        
    def btnResults_clicked(self):
        # self.dfoutput=self.q.get()        
        # msg = QtWidgets.QMessageBox()
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setText("The calculation is finished!")
        # msg.setWindowTitle("Finish")
        # msg.exec_()

        self.figure1.clear()
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1.tick_params(direction='in', labelsize=6)
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pc"], 'k-', label='Pc')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pt"], 'b--', label='Pt')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["Pwf"], 'r-.', label='Pwf')
        self.ax1.plot(self.dfoutput["time"], self.dfoutput["PL"], 'y:', label='Pl')
        self.ax1.set_title('Puressure', fontsize=6)
        self.ax1.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax1.set_ylabel(r'$P$ (MPa)', fontsize=6)
        self.ax1.legend(frameon=False)
        self.canvas1.draw()

        self.figure2.clear()
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.tick_params(direction='in', labelsize=6)
        self.ax2.plot(self.dfoutput["time"], self.dfoutput["Vp"], 'r-', label='Vp')
        self.ax2.set_title('Plunger velocity', fontsize=6)
        self.ax2.set_xlabel(r'$t$ (s)', fontsize=6)
        self.ax2.set_ylabel(r'$V_{p}$ (m/s)', fontsize=6)
        self.ax2.legend(frameon=False)
        self.canvas2.draw()

    def btnOutput_clicked(self):
        pass
    
    def btnWell_clicked(self):
        self.tabWidget_configure.setCurrentIndex(0)
        if self.btnSurface.isChecked() == True:
            self.btnSurface.toggle()
        elif self.btnFluid.isChecked() == True:
            self.btnFluid.toggle()
        elif self.btnReservoir.isChecked() == True:
            self.btnReservoir.toggle()

    def btnSurface_clicked(self):
        self.tabWidget_configure.setCurrentIndex(1)
        if self.btnWell.isChecked() == True:
            self.btnWell.toggle()
        elif self.btnFluid.isChecked() == True:
            self.btnFluid.toggle()
        elif self.btnReservoir.isChecked() == True:
            self.btnReservoir.toggle()

    def btnFluid_clicked(self):
        self.tabWidget_configure.setCurrentIndex(2)
        if self.btnWell.isChecked() == True:
            self.btnWell.toggle()
        elif self.btnSurface.isChecked() == True:
            self.btnSurface.toggle()
        elif self.btnReservoir.isChecked() == True:
            self.btnReservoir.toggle()

    def btnReservoir_clicked(self):
        self.tabWidget_configure.setCurrentIndex(3)
        if self.btnWell.isChecked() == True:
            self.btnWell.toggle()
        elif self.btnSurface.isChecked() == True:
            self.btnSurface.toggle()
        elif self.btnFluid.isChecked() == True:
            self.btnFluid.toggle()

    def btnPlot_clicked(self):
        self.tabWidget_analyze.setCurrentIndex(0)
        if self.btnData.isChecked() == True:
            self.btnData.toggle()

    def comboBox_analyzePlot_index_changed(self):
        try:
            if self.comboBox_analyzePlot.currentIndex() == 0:
                self.figure3.clear()
                self.ax3 = self.figure3.add_subplot(111)
                self.ax3.tick_params(direction='in', labelsize=6)
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Acc"], 'r-', label='Plunger acceleration')
                self.ax3.set_title('Plunger acceleration', fontsize=6)
                self.ax3.set_xlabel(r'$t$ (s)', fontsize=6)
                self.ax3.set_ylabel(r'$a_{p}$ $(m/s^2)$', fontsize=6)
                self.ax3.legend(frameon=False)
                self.canvas3.draw()
            elif self.comboBox_analyzePlot.currentIndex() == 1:
                self.figure3.clear()
                self.ax3 = self.figure3.add_subplot(111)
                self.ax3.tick_params(direction='in', labelsize=6)
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Vp"], 'r-', label='Vp')
                self.ax3.set_title('Plunger velocity', fontsize=6)
                self.ax3.set_xlabel(r'$t$ (s)', fontsize=6)
                self.ax3.set_ylabel(r'$V_{p}$ (m/s)', fontsize=6)
                self.ax3.legend(frameon=False)
                self.canvas3.draw()
            elif self.comboBox_analyzePlot.currentIndex() == 2:
                self.figure3.clear()
                self.ax3 = self.figure3.add_subplot(111)
                self.ax3.tick_params(direction='in', labelsize=6)
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Fout"], 'r-', label='Production rate')
                self.ax3.set_title('Production rate', fontsize=6)
                self.ax3.set_xlabel(r'$t$ (s)', fontsize=6)
                self.ax3.set_ylabel(r'$Q_{prod}$ $dm^3/s$', fontsize=6)
                self.ax3.legend(frameon=False)
                self.canvas3.draw()
            elif self.comboBox_analyzePlot.currentIndex() == 3:
                self.figure3.clear()
                self.ax3 = self.figure3.add_subplot(111)
                self.ax3.tick_params(direction='in', labelsize=6)
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Pc"], 'k-', label='Pc')
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Pt"], 'b--', label='Pt')
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Pwf"], 'r-.', label='Pwf')
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["PL"], 'y:', label='Pl')
                self.ax3.set_title('Puressure', fontsize=6)
                self.ax3.set_xlabel(r'$t$ (s)', fontsize=6)
                self.ax3.set_ylabel(r'$P$ (MPa)', fontsize=6)
                self.ax3.legend(frameon=False)
                self.canvas3.draw()
            elif self.comboBox_analyzePlot.currentIndex() == 4:
                self.figure3.clear()
                self.ax3 = self.figure3.add_subplot(111)
                self.ax3.tick_params(direction='in', labelsize=6)
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["La"], 'k-', label='Anuulus')
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Ltt"], 'b--', label='Above plunger')
                self.ax3.plot(self.dfoutput["time"], self.dfoutput["Ltb"], 'r-.', label='Below plunger')
                self.ax3.set_title('Liquid column', fontsize=6)
                self.ax3.set_xlabel(r'$t$ (s)', fontsize=6)
                self.ax3.set_ylabel(r'$H$ (m)', fontsize=6)
                self.ax3.legend(frameon=False)
                self.canvas3.draw()
        except:
            pass

    def btn_reset_analyzePlot_clicked(self):
        self.resetCalculation()
        self.dfoutput=[]
        self.figure3.clear()
        self.canvas3.draw()

    def btn_save_analyzePlot_clicked(self):
        try:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Save Data File', "Do you want to overwrite current plot?",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                        QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                # self.table_input.clearContents()
                options = QtWidgets.QFileDialog.Options()
                options |= QtWidgets.QFileDialog.DontUseNativeDialog
                filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Data File", "",
                                                                    "Images (*.jpg)",
                                                                    options=options)
            # Write XML file
            self.figure3.savefig(filename)
            
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error in save plot!")
            msg.setWindowTitle("Save File Error")
            msg.exec_()

    def btn_reset_analyzeData_clicked(self):
        self.resetCalculation()
        self.tableWidget_analyzeData.clearContents()


    def btn_save_analyzeData_clicked(self):
        try:
            # self.table_input.clearContents()
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filename, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Data File", "",
                                                                "xlsx Files (*.xlsx);;txt Files (*.txt);;XML files (*.xml)",
                                                                options=options)

            df_data = pd.DataFrame()
            if filetype == 'txt Files (*.txt)':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                msg.setText("txt file save, program not ready yet")
                msg.setWindowTitle("Save File")
                msg.exec_()
                df_data = pd.read_table(filename)
            elif filetype == 'xlsx Files (*.xlsx)':
                writer = pd.ExcelWriter(filename+'.xlsx', engine='xlsxwriter')
                self.dfoutput.to_excel(writer, sheet_name='Plunger lift simulation')
                writer.save()
            elif filetype == 'XML files (*.xml)':
                pass
                # Create XML file
                root=ET.Element('Inputs')   # Create root element 'Inputs' that contains all parameters in xml
                tree=ET.ElementTree(root)   # Save root to ElementTree, which will be used to write XML file
                
                # Create parameters within the root element
                Well_Geometry=ET.Element('Well_Geometry')
                Surface_Information=ET.Element('Surface_Information')
                Fluid_Property=ET.Element('Fluid_Property')
                Reservoir_Parameter=ET.Element('Reservoir_Parameter')
                root.append(Well_Geometry)
                root.append(Surface_Information)
                root.append(Fluid_Property)
                root.append(Reservoir_Parameter)

                #Create sub-element within the above paremeter elements
                Well_Name=ET.SubElement(Well_Geometry,"Well_Name")
                Well_Name.text="Well_1"

                # Write XML file
                with open(filename,'wb') as f:
                    tree.write(f)
                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)      #icon: Question, Information, Critical, Warning 
                msg.setText("xml file save")
                msg.setWindowTitle("Save File")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("file not saved")
                msg.setWindowTitle("Save File")
                msg.exec_()
            
                    

        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error in save inputs!")
            msg.setWindowTitle("Save File Error")
            msg.exec_()


    def btnData_clicked(self):
        self.tabWidget_analyze.setCurrentIndex(1)
        if self.btnPlot.isChecked() == True:
            self.btnPlot.toggle()

    def toolBox_currentChanged(self):
        index=self.toolBox.currentIndex()
        self.tabWidget_main.setCurrentIndex(index)
        self.comboBox_analyzePlot_index_changed()

    def tabWidget_main_currentChanged(self):
        index=self.tabWidget_main.currentIndex()
        self.toolBox.setCurrentIndex(index)

    # Upload case inputs
    def uploadGUI(self):

        self.lineEdit_wellName.setText(str(self.inputs["Well_name"]))
        self.lineEdit_wellDepth.setValidator(QtGui.QDoubleValidator())    # set input format to be floating-point numbers
        self.lineEdit_wellDepth.setText(str(self.inputs["Well_depth"]))
        self.lineEdit_tubingID.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_tubingID.setText(str(self.inputs["Tubing_ID"]))
        self.lineEdit_tubingOD.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_tubingOD.setText(str(self.inputs["Tubing_OD"]))
        self.lineEdit_casingID.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_casingID.setText(str(self.inputs["Casing_ID"]))
        self.lineEdit_absoluteRoughnessV.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_absoluteRoughnessV.setText(str(self.inputs["Vertical_roughness"]))
        self.lineEdit_horizontalLength.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_horizontalLength.setText(str(self.inputs["Horizontal_length"]))
        self.lineEdit_inclinationAngle.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_inclinationAngle.setText(str(self.inputs["Inclination_angle"]))
        self.lineEdit_innerDiameter.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_innerDiameter.setText(str(self.inputs["Inner_diameter"]))
        self.lineEdit_absoluteRoughnessH.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_absoluteRoughnessH.setText(str(self.inputs["Horizontal_roughness"]))
        self.lineEdit_plungerWeight.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerWeight.setText(str(self.inputs["Plunger_weight"]))
        self.lineEdit_plungerLength.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerLength.setText(str(self.inputs["Plunger_length"]))
        self.lineEdit_plungerRise.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerRise.setText(str(self.inputs["Plunger_rise"]))
        self.lineEdit_plungerDiameter.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerDiameter.setText(str(self.inputs["Plunger_diameter"]))
        self.lineEdit_plungerDrag.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerDrag.setText(str(self.inputs["Plunger_drag_coefficient"]))
        self.lineEdit_linePressure.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_linePressure.setText(str(self.inputs["Line_pressure"]))
        self.lineEdit_valveCoeff.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_valveCoeff.setText(str(self.inputs["Valve_Cv"]))
        self.lineEdit_surfaceT.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_surfaceT.setText(str(self.inputs["Surface_T"]))
        self.lineEdit_denlR.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_denlR.setText(str(self.inputs["Relative_density_L"]))
        self.lineEdit_visL.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_visL.setText(str(self.inputs["Liquid_viscosity"]))
        self.lineEdit_dengR.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_dengR.setText(str(self.inputs["Relative_density_G"]))
        self.lineEdit_C.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_C.setText(str(self.inputs["Reservoir_C"]))
        self.lineEdit_n.setValidator(QtGui.QDoubleValidator())   
        self.lineEdit_n.setText(str(self.inputs["Reservoir_n"]))
        self.lineEdit_Pr_L.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Pr_L.setText(str(self.inputs["Reservoir_P"]))
        self.lineEdit_GLR_L.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_GLR_L.setText(str(self.inputs["GLR"]))
        self.lineEdit_Tgr_L.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Tgr_L.setText(str(self.inputs["Geothermal_gradient"]))
        self.lineEdit_Rsl.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Rsl.setText(str(self.inputs["Gas_solubility"]))
        self.lineEdit_cycles.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_cycles.setText(str(self.inputs["Plunger_cycle"]))
        self.lineEdit_plungerT.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_plungerT.setText(str(self.inputs["Plunger_period"]))
        self.lineEdit_valveT.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_valveT.setText(str(self.inputs["Valve_open_T"]))
        self.lineEdit_Pc.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Pc.setText(str(self.inputs["Casing_pressure"]))
        self.lineEdit_Pt.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Pt.setText(str(self.inputs["Tubing_pressure"]))
        self.lineEdit_Ltt.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Ltt.setText(str(self.inputs["L_above_plunger"]))
        self.lineEdit_Ltb.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_Ltb.setText(str(self.inputs["L_below_plunger"]))
        self.lineEdit_dtH.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_dtH.setText(str(self.inputs["Time_step_horizontal"]))
        self.lineEdit_dtUp.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_dtUp.setText(str(self.inputs["Time_step_upward"]))
        self.lineEdit_dtDown.setValidator(QtGui.QDoubleValidator())    
        self.lineEdit_dtDown.setText(str(self.inputs["Time_step_downward"]))


        for i in range(self.dfcompositional.shape[0]):
            for j in range(self.dfcompositional.shape[1]):
                self.tableWidget_Compositional.setItem(i, j, QtWidgets.QTableWidgetItem(str(np.around(self.dfcompositional.iloc[i, j], decimals=4))))


    # Load inputs from GUI
    def load_Inputs(self):
        self.inputs["Well_name"]=str(self.lineEdit_wellName.text())
        self.inputs["Well_depth"]=float(self.lineEdit_wellDepth.text())
        self.inputs["Tubing_ID"]=float(self.lineEdit_tubingID.text())
        self.inputs["Tubing_OD"]=float(self.lineEdit_tubingOD.text())
        self.inputs["Casing_ID"]=float(self.lineEdit_casingID.text())
        self.inputs["Vertical_roughness"]=float(self.lineEdit_absoluteRoughnessV.text())
        self.inputs["Horizontal_length"]=float(self.lineEdit_horizontalLength.text())
        self.inputs["Inclination_angle"]=float(self.lineEdit_inclinationAngle.text())
        self.inputs["Inner_diameter"]=float(self.lineEdit_innerDiameter.text())
        self.inputs["Horizontal_roughness"]=float(self.lineEdit_absoluteRoughnessH.text())
        self.inputs["Plunger_weight"]=float(self.lineEdit_plungerWeight.text())
        self.inputs["Plunger_length"]=float(self.lineEdit_plungerLength.text())
        self.inputs["Plunger_rise"]=float(self.lineEdit_plungerRise.text())
        self.inputs["Plunger_diameter"]=float(self.lineEdit_plungerDiameter.text())
        self.inputs["Plunger_drag_coefficient"]=float(self.lineEdit_plungerDrag.text())
        self.inputs["Line_pressure"]=float(self.lineEdit_linePressure.text())
        self.inputs["Valve_Cv"]=float(self.lineEdit_valveCoeff.text())
        self.inputs["Surface_T"]=float(self.lineEdit_surfaceT.text())
        self.inputs["Relative_density_L"]=float(self.lineEdit_denlR.text())
        self.inputs["Liquid_viscosity"]=float(self.lineEdit_visL.text())
        self.inputs["Relative_density_G"]=float(self.lineEdit_dengR.text())
        self.inputs["Reservoir_C"]=float(self.lineEdit_C.text())
        self.inputs["Reservoir_n"]=float(self.lineEdit_n.text())
        self.inputs["Reservoir_P"]=float(self.lineEdit_Pr_L.text())
        self.inputs["GLR"]=float(self.lineEdit_GLR_L.text())
        self.inputs["Geothermal_gradient"]=float(self.lineEdit_Tgr_L.text())
        self.inputs["Gas_solubility"]=float(self.lineEdit_Rsl.text())
        self.inputs["Plunger_cycle"]=float(self.lineEdit_cycles.text())
        self.inputs["Plunger_period"]=float(self.lineEdit_plungerT.text())
        self.inputs["Valve_open_T"]=float(self.lineEdit_valveT.text())
        self.inputs["Casing_pressure"]=float(self.lineEdit_Pc.text())
        self.inputs["Tubing_pressure"]=float(self.lineEdit_Pt.text())
        self.inputs["L_above_plunger"]=float(self.lineEdit_Ltt.text())
        self.inputs["L_below_plunger"]=float(self.lineEdit_Ltb.text())
        self.inputs["Time_step_horizontal"]=float(self.lineEdit_dtH.text())
        self.inputs["Time_step_upward"]=float(self.lineEdit_dtUp.text())
        self.inputs["Time_step_downward"]=float(self.lineEdit_dtDown.text())
        if self.radioButton_BlackOil.isChecked()==True:
            self.inputs["Fluid_type"]=1
        else:
            self.inputs["Fluid_type"]=2

        for i in range(self.dfcompositional.shape[0]):
            for j in range(self.dfcompositional.shape[1]):
                self.dfcompositional.iloc[i, j]=float(self.tableWidget_Compositional.item(i,j).text())
        for i in range(self.dfcompositional.shape[0]):
            self.z_f[i]= self.dfcompositional.iloc[i,0]
            self.Pc_f[i]= self.dfcompositional.iloc[i,1]
            self.w_f[i] = self.dfcompositional.iloc[i,2]
            self.Tc_f[i]= self.dfcompositional.iloc[i,3]
            self.M_f[i]= self.dfcompositional.iloc[i,4]


    # initialization inputs
    def init(self):
        global  m_plunger, L_plunger, d_plunger, Cd_plunger, Epsilon_plunger, A_plunger, H_well, ID_tubing, \
                OD_tubing, ID_casing, ED, A_tubing, A_casing, AB, Ann, LB, VB, ANG, DB, Cv, T_wellhead, Pl, \
                den_liquid_relative, den_gas_relative, vis_liquid, denl, M_gas, P_res, C_res, n, GLR, Rsl, \
                Tgrd, Pc, Pt, Ltt, Ltb, dt_H, dt_U, dt_D, cycles, Period, T_open
        self.load_Inputs()
        """Upload global variables for configuration"""
        # plunger parameters
        m_plunger = self.inputs["Plunger_weight"]               # plunger mass in kg
        L_plunger = self.inputs["Plunger_length"]             # plunger length in mD
        d_plunger = self.inputs["Plunger_diameter"]    # plunger diameter in
        Cd_plunger = self.inputs["Plunger_drag_coefficient"]         # plunger fall drag coefficient
        Epsilon_plunger = self.inputs["Plunger_rise"]    # plunger rise 
        A_plunger = 0.25*PI*d_plunger**2   # plunger cross sectional area in m2

        # well parameters
        H_well = self.inputs["Well_depth"]     # well depth in m
        ID_tubing = self.inputs["Tubing_ID"]  # tubing ID in m
        OD_tubing = self.inputs["Tubing_OD"]  # tubing OD in m
        ID_casing = self.inputs["Casing_ID"]   # casing ID in m
        ED = self.inputs["Vertical_roughness"]                 # tubing roughness

        A_tubing = 0.25*PI*(ID_tubing**2)                   # tubing cross sectional area in m2     ########################3
        A_casing = 0.25*PI*(ID_casing**2 - OD_tubing**2)    # annulus cross section area in m2      ########################3
        AB = 0.25*PI*ID_casing**2                           # cross-sectional area of casing        ########################3
        Ann = 0.25*PI*(ID_tubing**2 - d_plunger**2)         # cross section area between plunger and tubing in m2       ########################3

        # wellbore section
        LB = self.inputs["Horizontal_length"]          # deviated section of the wellbore
        VB = AB * LB                # horizontal section volume in m3       ########################3
        ANG = self.inputs["Inclination_angle"]                   # inclination angle of the deviated section
        DB = self.inputs["Inner_diameter"]              # assume inner diameter the same as casing ID

        # surface parameters
        Cv = self.inputs["Valve_Cv"]                 # coefficient of motor valve
        T_wellhead = self.inputs["Surface_T"]            # temperature at well head in K
        Pl = self.inputs["Line_pressure"]                  # production line pressure - fixed if no surface line or separator considered

        # fluid properties
        den_liquid_relative = self.inputs["Relative_density_L"]  # relative density of liquid
        den_gas_relative = self.inputs["Relative_density_G"]      # relative density of gas
        vis_liquid = self.inputs["Liquid_viscosity"]           # liquid viscosity in Pa.s
        denl = den_liquid_relative * 1000
        M_gas = M_air * den_gas_relative

        # reservoir IPR
        P_res = self.inputs["Reservoir_P"]                 # reservoir pressure in Pa
        C_res = self.inputs["Reservoir_C"]            # reservoir coefficient for gas flow rate in Vogel model
        n = self.inputs["Reservoir_n"]                       # reservoir index for gas flow rate in Vogel model
        GLR = self.inputs["GLR"]                    # gas-liquid-ratio 
        Rsl = self.inputs["Gas_solubility"]                   # average gas solubility in liquid at average T and P, m3/m3
        Tgrd = self.inputs["Geothermal_gradient"]                 # formation temperature gradient 30K/km

        """Upload global variables for initial flow conditions"""

        Pc = self.inputs["Casing_pressure"]                  # casing pressure
        Pt = self.inputs["Tubing_pressure"]                 # tubing pressure
        Ltt = self.inputs["L_above_plunger"]                    # initial liquid column length above plunger (m)
        Ltb = self.inputs["L_below_plunger"]                    # initial liquid column length below plunger (m)
        dt_H=self.inputs["Time_step_horizontal"]                    # time step for horizontal section
        dt_U=self.inputs["Time_step_upward"]                     # time step for plunger upward section
        dt_D=self.inputs["Time_step_downward"]                   # time step for plunger downward section
        cycles=self.inputs["Plunger_cycle"]                   # Plunger lift cycles to be computed
        Period=self.inputs["Plunger_period"]*60.              # Plunger lift period (s to min)
        T_open=self.inputs["Valve_open_T"]*60.              # Surface valve open time (s to min)


    # set main window 
    def setupGUI(self):
        self.setupUi(self)
        qtRectangle = self.frameGeometry()      # show on the center of screen
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_main.setCurrentIndex(0)
        self.tabWidget_configure.setCurrentIndex(0)
        self.show()
    
    # connect signals and slots
    def setConnection(self):
        self.actionAbout.triggered.connect(self.actionAbout_triggered)
        self.actionOpen.triggered.connect(self.actionOpen_triggered)
        self.actionSave.triggered.connect(self.actionSave_triggered)

    @QtCore.pyqtSlot()
    def actionAbout_triggered(self):
        class dlgAbout(QtWidgets.QDialog, aboutUI):
            def __init__(self):
                super(dlgAbout, self).__init__()
                self.setupUi(self)

        ui = dlgAbout()
        if ui.exec_():
            ui.show()

    @QtCore.pyqtSlot()
    def actionOpen_triggered(self):
        # Original
        # class dlgOpen(QtWidgets.QDialog, caseUI):
        #     def __init__(self):
        #         super(dlgOpen, self).__init__()
        #         self.setupUi(self)
        #         self.btn_cancel.clicked.connect(self.reject)
        #         self.btn_delete.clicked.connect(self.btn_delete_clicked)
        #         self.btn_open.clicked.connect(plungerLiftGUI.Open_File)

        #     @QtCore.pyqtSlot()
        #     def btn_delete_clicked(self):
        #         #TODO: button delete pressed
        #         pass

        # ui = dlgOpen()
        # if ui.exec_():
        #     ui.show()

        #TODO: button open pressed
                
        # try:
        # self.table_input.clearContents()
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "Save Data File", "",
                                                            "XML files (*.xml);;txt Files (*.txt);;csv Files (*.csv)",
                                                            options=options)

        df_data = pd.DataFrame()
        if filetype == 'txt Files (*.txt)':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
            msg.setText("txt file save, program not ready yet")
            msg.setWindowTitle("Save File")
            msg.exec_()
            df_data = pd.read_table(filename)
        elif filetype == 'csv Files (*.csv)':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
            msg.setText("csv file save, program not ready yet")
            msg.setWindowTitle("Save File")
            msg.exec_()
            df_data = pd.read_csv(filename)
        elif filetype == 'XML files (*.xml)':
            # Create XML file
            tree=ET.parse(filename)      # Get root to ElementTree, which will be used to write XML file
            root=tree.getroot()     # Create root element 'Inputs' that contains all parameters in xml
            
            
            # Well Geometry
            for x in root.findall('Well_Geometry'):
                self.inputs["Well_name"]=x.find('Well_Name').text
                self.inputs["Well_depth"]=float(x.find('Well_depth').text)
                self.inputs["Tubing_ID"]=float(x.find('Tubing_ID').text)
                self.inputs["Tubing_OD"]=float(x.find('Tubing_OD').text)
                self.inputs["Casing_ID"]=float(x.find('Casing_ID').text)
                self.inputs["Vertical_roughness"]=float(x.find('Vertical_roughness').text)
                self.inputs["Horizontal_length"]=float(x.find('Horizontal_length').text)
                self.inputs["Inclination_angle"]=float(x.find('Inclination_angle').text)
                self.inputs["Inner_diameter"]=float(x.find('Inner_diameter').text)
                self.inputs["Plunger_weight"]=float(x.find('Plunger_weight').text)
                self.inputs["Plunger_length"]=float(x.find('Plunger_length').text)
                self.inputs["Plunger_diameter"]=float(x.find('Plunger_diameter').text)
                self.inputs["Plunger_drag_coefficient"]=float(x.find('Plunger_drag_coefficient').text)
                self.inputs["Plunger_rise"]=float(x.find('Plunger_rise').text)

            # Surface information
            for x in root.findall('Surface_Information'):
                self.inputs["Valve_Cv"]=float(x.find('Valve_Cv').text)
                self.inputs["Surface_T"]=float(x.find('Surface_T').text)
                self.inputs["Line_pressure"]=float(x.find('Line_pressure').text)

            #Fluid information
            for x in root.findall('Fluid_Property'):
                self.inputs["Relative_density_L"]=float(x.find('Relative_density_L').text)
                self.inputs["Relative_density_G"]=float(x.find('Relative_density_G').text)
                self.inputs["Liquid_viscosity"]=float(x.find('Liquid_viscosity').text)

            #Fluid compositional property
            for x in root.findall('Fluid_Compositional'):
                for i in range(self.dfcompositional.shape[0]):
                    for j in range(self.dfcompositional.shape[1]):
                        Name_composition='dfcomposition'+str(i)+'_'+str(j)
                        self.dfcompositional.iloc[i, j]=float(x.find(Name_composition).text)
                        # Name_composition='dfcomposition'+str(i)+','+str(j)
                        # composition=ET.SubElement(Fluid_Compositional, Name_composition)
                        # composition.text=str(self.dfcompositional.iloc[i, j])
                # for i in range(self.dfcompositional.shape[0]):
                #     self.z_f[i]= self.dfcompositional.iloc[i,0]
                #     self.Pc_f[i]= self.dfcompositional.iloc[i,1]
                #     self.w_f[i] = self.dfcompositional.iloc[i,2]
                #     self.Tc_f[i]= self.dfcompositional.iloc[i,3]
                #     self.M_f[i]= self.dfcompositional.iloc[i,4]




            # Reservoir information
            for x in root.findall('Reservoir_Parameter'):
                self.inputs["Reservoir_P"]=float(x.find('Reservoir_P').text)
                self.inputs["Reservoir_C"]=float(x.find('Reservoir_C').text)
                self.inputs["Reservoir_n"]=float(x.find('Reservoir_n').text)
                self.inputs["GLR"]=float(x.find('GLR').text)
                self.inputs["Gas_solubility"]=float(x.find('Gas_solubility').text)
                self.inputs["Geothermal_gradient"]=float(x.find('Geothermal_gradient').text)

            # Simulation settings
            for x in root.findall('Simulation_settings'):
                self.inputs["Plunger_cycle"]=float(x.find('Plunger_cycle').text)
                self.inputs["Plunger_period"]=float(x.find('Plunger_period').text)
                self.inputs["Valve_open_T"]=float(x.find('Valve_open_T').text)
                self.inputs["Time_step_horizontal"]=float(x.find('Time_step_horizontal').text)
                self.inputs["Time_step_upward"]=float(x.find('Time_step_upward').text)
                self.inputs["Time_step_downward"]=float(x.find('Time_step_downward').text)
                self.inputs["Casing_pressure"]=float(x.find('Casing_pressure').text)
                self.inputs["Tubing_pressure"]=float(x.find('Tubing_pressure').text)
                self.inputs["L_above_plunger"]=float(x.find('L_above_plunger').text)
                self.inputs["L_below_plunger"]=float(x.find('L_below_plunger').text)
            
            self.uploadGUI()
            self.init()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)      #icon: Question, Information, Critical, Warning 
            msg.setText("xml file read")
            msg.setWindowTitle("Read File")
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("file not read")
            msg.setWindowTitle("Read File")
            msg.exec_()
            
                

        # except:
        #     msg = QtWidgets.QMessageBox()
        #     msg.setIcon(QtWidgets.QMessageBox.Critical)
        #     msg.setText("Error in save inputs!")
        #     msg.setWindowTitle("Save File Error")
        #     msg.exec_()


    @QtCore.pyqtSlot()
    def actionSave_triggered(self):
            #TODO: button open pressed
                
        # try:
            self.load_Inputs()
            # self.table_input.clearContents()
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filename, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save Data File", "",
                                                                "XML files (*.xml)",#;;txt Files (*.txt);;csv Files (*.csv)",
                                                                options=options)

            df_data = pd.DataFrame()
            if filetype == 'txt Files (*.txt)':
                filename=filename+'.txt'
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                msg.setText("txt file save, program not ready yet")
                msg.setWindowTitle("Save File")
                msg.exec_()
                df_data = pd.read_table(filename)
            elif filetype == 'csv Files (*.csv)':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                msg.setText("csv file save, program not ready yet")
                msg.setWindowTitle("Save File")
                msg.exec_()
                df_data = pd.read_csv(filename)
            elif filetype == 'XML files (*.xml)':
                filename=filename+'.xml'
                # Create XML file
                root=ET.Element('Inputs')   # Create root element 'Inputs' that contains all parameters in xml
                tree=ET.ElementTree(root)   # Save root to ElementTree, which will be used to write XML file
                
                # Create parameters within the root element
                Well_Geometry=ET.Element('Well_Geometry')
                Surface_Information=ET.Element('Surface_Information')
                Fluid_Property=ET.Element('Fluid_Property')
                Fluid_Compositional=ET.Element('Fluid_Compositional')
                Reservoir_Parameter=ET.Element('Reservoir_Parameter')
                Simulation_Settings=ET.Element('Simulation_settings')
                root.append(Well_Geometry)
                root.append(Surface_Information)
                root.append(Fluid_Property)
                root.append(Fluid_Compositional)
                root.append(Reservoir_Parameter)
                root.append(Simulation_Settings)

                #Create sub-element within the above paremeter elements
                # Well Geometry
                Well_Name=ET.SubElement(Well_Geometry,"Well_Name")
                Well_depth=ET.SubElement(Well_Geometry,"Well_depth")
                Tubing_ID=ET.SubElement(Well_Geometry,"Tubing_ID")
                Tubing_OD=ET.SubElement(Well_Geometry,"Tubing_OD")
                Casing_ID=ET.SubElement(Well_Geometry,"Casing_ID")
                Vertical_roughness=ET.SubElement(Well_Geometry,"Vertical_roughness")
                Horizontal_length=ET.SubElement(Well_Geometry,"Horizontal_length")
                Inclination_angle=ET.SubElement(Well_Geometry,"Inclination_angle")
                Inner_diameter=ET.SubElement(Well_Geometry,"Inner_diameter")
                Plunger_weight=ET.SubElement(Well_Geometry,"Plunger_weight")
                Plunger_length=ET.SubElement(Well_Geometry,"Plunger_length")
                Plunger_diameter=ET.SubElement(Well_Geometry,"Plunger_diameter")
                Plunger_drag_coefficient=ET.SubElement(Well_Geometry,"Plunger_drag_coefficient")
                Plunger_rise=ET.SubElement(Well_Geometry,"Plunger_rise")
                Well_Name.text=str(self.inputs["Well_name"])
                Well_depth.text=str(self.inputs["Well_depth"])
                Tubing_ID.text=str(self.inputs["Tubing_ID"])
                Tubing_OD.text=str(self.inputs["Tubing_OD"])
                Casing_ID.text=str(self.inputs["Casing_ID"])
                Vertical_roughness.text=str(self.inputs["Vertical_roughness"])
                Horizontal_length.text=str(self.inputs["Horizontal_length"])
                Inclination_angle.text=str(self.inputs["Inclination_angle"])
                Inner_diameter.text=str(self.inputs["Inner_diameter"])
                Plunger_weight.text=str(self.inputs["Plunger_weight"])
                Plunger_length.text=str(self.inputs["Plunger_length"])
                Plunger_diameter.text=str(self.inputs["Plunger_diameter"])
                Plunger_drag_coefficient.text=str(self.inputs["Plunger_drag_coefficient"])
                Plunger_rise.text=str(self.inputs["Plunger_rise"])
                
                # Surface information
                Valve_Cv=ET.SubElement(Surface_Information,"Valve_Cv")
                Surface_T=ET.SubElement(Surface_Information,"Surface_T")
                Line_pressure=ET.SubElement(Surface_Information,"Line_pressure")
                Valve_Cv.text=str(self.inputs["Valve_Cv"])
                Surface_T.text=str(self.inputs["Surface_T"])
                Line_pressure.text=str(self.inputs["Line_pressure"])

                #Fluid information
                Relative_density_L=ET.SubElement(Fluid_Property,"Relative_density_L")
                Relative_density_G=ET.SubElement(Fluid_Property,"Relative_density_G")
                Liquid_viscosity=ET.SubElement(Fluid_Property,"Liquid_viscosity")
                Relative_density_L.text=str(self.inputs["Relative_density_L"])
                Relative_density_G.text=str(self.inputs["Relative_density_G"])
                Liquid_viscosity.text=str(self.inputs["Liquid_viscosity"])

                #Fluid compositional property
                for i in range(self.dfcompositional.shape[0]):
                    for j in range(self.dfcompositional.shape[1]):
                        Name_composition='dfcomposition'+str(i)+'_'+str(j)
                        composition=ET.SubElement(Fluid_Compositional, Name_composition)
                        composition.text=str(self.dfcompositional.iloc[i, j])


                # Reservoir information
                Reservoir_P=ET.SubElement(Reservoir_Parameter,"Reservoir_P")
                Reservoir_C=ET.SubElement(Reservoir_Parameter,"Reservoir_C")
                Reservoir_n=ET.SubElement(Reservoir_Parameter,"Reservoir_n")
                GLR=ET.SubElement(Reservoir_Parameter,"GLR")
                Gas_solubility=ET.SubElement(Reservoir_Parameter,"Gas_solubility")
                Geothermal_gradient=ET.SubElement(Reservoir_Parameter,"Geothermal_gradient")
                Reservoir_P.text=str(self.inputs["Reservoir_P"])
                Reservoir_C.text=str(self.inputs["Reservoir_C"])
                Reservoir_n.text=str(self.inputs["Reservoir_n"])
                GLR.text=str(self.inputs["GLR"])
                Gas_solubility.text=str(self.inputs["Gas_solubility"])
                Geothermal_gradient.text=str(self.inputs["Geothermal_gradient"])
                
                # Simulation settings
                Plunger_cycle=ET.SubElement(Simulation_Settings,"Plunger_cycle")
                Plunger_period=ET.SubElement(Simulation_Settings,"Plunger_period")
                Valve_open_T=ET.SubElement(Simulation_Settings,"Valve_open_T")
                Time_step_horizontal=ET.SubElement(Simulation_Settings,"Time_step_horizontal")
                Time_step_upward=ET.SubElement(Simulation_Settings,"Time_step_upward")
                Time_step_downward=ET.SubElement(Simulation_Settings,"Time_step_downward")
                Casing_pressure=ET.SubElement(Simulation_Settings,"Casing_pressure")
                Tubing_pressure=ET.SubElement(Simulation_Settings,"Tubing_pressure")
                L_above_plunger=ET.SubElement(Simulation_Settings,"L_above_plunger")
                L_below_plunger=ET.SubElement(Simulation_Settings,"L_below_plunger")
                Plunger_cycle.text=str(self.inputs["Plunger_cycle"])
                Plunger_period.text=str(self.inputs["Plunger_period"])
                Valve_open_T.text=str(self.inputs["Valve_open_T"])
                Time_step_horizontal.text=str(self.inputs["Time_step_horizontal"])
                Time_step_upward.text=str(self.inputs["Time_step_upward"])
                Time_step_downward.text=str(self.inputs["Time_step_downward"])
                Casing_pressure.text=str(self.inputs["Casing_pressure"])
                Tubing_pressure.text=str(self.inputs["Tubing_pressure"])
                L_above_plunger.text=str(self.inputs["L_above_plunger"])
                L_below_plunger.text=str(self.inputs["L_below_plunger"])

         
                # Write XML file
                with open(filename,'wb') as f:
                    tree.write(f)
                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)      #icon: Question, Information, Critical, Warning 
                msg.setText("xml file save")
                msg.setWindowTitle("Save File")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("file not saved")
                msg.setWindowTitle("Save File")
                msg.exec_()
                
                    

        # except:
        #     msg = QtWidgets.QMessageBox()
        #     msg.setIcon(QtWidgets.QMessageBox.Critical)
        #     msg.setText("Error in save inputs!")
        #     msg.setWindowTitle("Save File Error")
        #     msg.exec_()


    @QtCore.pyqtSlot()
    def Open_File(self):
            #TODO: button open pressed
                
        try:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Read Data File', "Do you want to overwrite current data?",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                        QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
            # self.table_input.clearContents()
                options = QtWidgets.QFileDialog.Options()
                options |= QtWidgets.QFileDialog.DontUseNativeDialog
                filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Read Data File", "",
                                                                    "All Files (*);;txt Files (*.txt);;csv Files (*.csv);;XML files (*.xml)",
                                                                    options=options)
                # df_data = pd.DataFrame()
                if filename.split('.')[-1] == 'txt':
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                    msg.setText("txt file read, program not ready yet")
                    msg.setWindowTitle("Open File")
                    msg.exec_()
                    df_data = pd.read_table(filename)
                elif filename.split('.')[-1] == 'csv':
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                    msg.setText("csv file read, program not ready yet")
                    msg.setWindowTitle("Open File")
                    msg.exec_()
                    df_data = pd.read_csv(filename)
                elif filename.split('.')[-1] == 'xml':
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                    msg.setText("xml file read, program not ready yet")
                    msg.setWindowTitle("Open File")
                    msg.exec_()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Question)      #icon: Question, Information, Critical, Warning 
                    msg.setText("Please read the correct data file!")
                    msg.setWindowTitle("Open File")
                    msg.exec_()
                # self.table_input.setRowCount(df_data.shape[0])
                # self.table_input.setColumnCount(df_data.shape[1])

                # for i in range(df_data.shape[0]):
                #     for j in range(df_data.shape[1]):
                #         self.table_input.setItem(i, j, QtWidgets.QTableWidgetItem(str(df_data.iloc[i, j])))
        
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Please read the correct data file!")
            msg.setWindowTitle("Open File Error")
            msg.exec_()


# class btnRunThread(QtCore.QThread):
    # # class variables for signals
    # total = QtCore.pyqtSignal(object)
    # update = QtCore.pyqtSignal()

class btnRunThread(QtCore.QThread):
    
    update = QtCore.pyqtSignal()
    def __init__(self, inputs):
        super(btnRunThread, self).__init__()
        self.inputs=inputs
        self.n=n
        self.Run=True
        self.data=pd.DataFrame()
    def Thread_stop(self):
        self.Thread_Run=False
    def Thread_start(self):
        self.Thread_Run=True

    def run(self):
        

        global Pc, Pt, Pl, Ltt, Ltb, mga, mla, mgtt, mltt, mgtb, mltb, Xp, Vp, Ar, v, La, Pcb, Ptb, Pwf, Fgout, Ppb, Ppt, \
           Acc, Flout, Fgtub, Fltub, Fgres, Flres, Fgann, Flann, t, dt, Ltt0

        initialize(self.inputs)
        # print(Xp, La)

        self.time = []
        self.XP = []
        self.VP = []
        self.ACC = []
        self.Fout = []
        self.PC = []
        self.PL = []
        self.PT = []
        self.PWF = []
        self.LT = []
        self.LA = []
        self.LTT = []
        self.LTB = []
        self.MGA = []
        self.MGTT = []
        self.MGTB = []

        counter = 0


        try:
            while counter < cycles:
                Xp = 0
                Vp = 0
                Ltt0 = Ltt
                print("{} cycle starts at {} s".format(counter+1, t), '\n')
                # print_io()
                if self.Thread_Run == True:
                    while t < Period * (counter + 1):
                        Xp, Vp, Acc, Pc, Pt, Pwf, Ppt, Ptb, La, Ltt, Ltb, mga, mgtt, mgtb, Flout, Fgout=print_io(t)
                        self.time.append(t)
                        self.XP.append(Xp)
                        self.LA.append(La)
                        self.LT.append(Ltt + Ltb)
                        self.VP.append(Vp)
                        self.ACC.append(Acc)
                        qprod = Fgout / gas_density_std(den_gas_relative, 273.15, 1e5) + Flout / denl
                        self.Fout.append(1000 * qprod)
                        self.PC.append(Pc / 1e6)
                        self.PL.append(Pl / 1e6)
                        self.PT.append(Pt / 1e6)
                        self.PWF.append(Pwf / 1e6)
                        self.LTT.append(Ltt)
                        self.LTB.append(Ltb)
                        self.MGA.append(mga)
                        self.MGTT.append(mgtt)
                        self.MGTB.append(mgtb)

                        if t < T_open + Period * counter:
                            if Xp != H_well:
                                dt = dt_H
                            else:
                                dt = dt_U
                            upward()
                        else:
                            dt = dt_D
                            downward()
                        t += dt
                        self.update.emit()

                    # next cycle
                    counter += 1
                    if Ppt>50000000.0:
                        try:
                            pass
                        except expression as identifier:
                            pass
        except:
            pass
            # msg = QtWidgets.QMessageBox()
            # msg.setIcon(QtWidgets.QMessageBox.Critical)
            # msg.setText("Calculation failed at t = " + str(t/60) + "min\n"
            #         + "cycle = " + str(counter))
            # msg.setWindowTitle("Finish")
            # msg.exec_()
            self.data = pd.DataFrame({"time": self.time,  "Xp": self.XP,       "Acc": self.ACC, "Vp": self.VP,
                                "Pc": self.PC,      "Pt": self.PT,       "Pwf": self.PWF, "PL": self.PL,
                                "La": self.LA,      "Ltt": self.LTT,     "Ltb": self.LTB, "Fout": self.Fout,
                                "mga": self.MGA,    "mgtt": self.MGTT,   "mgtb": self.MGTB})
            self.data.to_excel("output.xlsx")



        #     fig1 = plt.figure()
        #     ax1 = fig1.add_subplot(111)
        #     ax1.plot(time, ACC, label="Plunger acceleration")
        #     ax1.set_xlabel(r'$t$ (s)')
        #     ax1.set_ylabel(r'$a_{p}$ $(m/s^2)$')
        #     ax1.set_ylim(-1)
        #     ax1.legend(frameon=False)
        #     fig1.show()





        
        # #Final result
        # self.data = pd.DataFrame({"time": time,  "Xp": XP,       "Acc": ACC, "Vp": VP,
        #                     "Pc": PC,      "Pt": PT,       "Pwf": PWF, "PL": PL,
        #                     "La": LA,      "Ltt": LTT,     "Ltb": LTB, "Fout": Fout,
        #                     "mga": MGA,    "mgtt": MGTT,   "mgtb": MGTB})
        self.data = pd.DataFrame({"time": self.time,  "Xp": self.XP,       "Acc": self.ACC, "Vp": self.VP,
                    "Pc": self.PC,      "Pt": self.PT,       "Pwf": self.PWF, "PL": self.PL,
                    "La": self.LA,      "Ltt": self.LTT,     "Ltb": self.LTB, "Fout": self.Fout,
                    "mga": self.MGA,    "mgtt": self.MGTT,   "mgtb": self.MGTB})
        self.data.to_excel("output.xlsx")

        # fig1 = plt.figure()
        # ax1 = fig1.add_subplot(111)
        # ax1.plot(time, ACC, label="Plunger acceleration")
        # ax1.set_xlabel(r'$t$ (s)')
        # ax1.set_ylabel(r'$a_{p}$ $(m/s^2)$')
        # ax1.set_ylim(-1)
        # ax1.legend(frameon=False)
        # fig1.show()
        # msg = QtWidgets.QMessageBox()
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setText("Calculation complete!")
        # msg.setWindowTitle("Finish")
        # msg.exec_()




# class SurgingProgressBar(QtWidgets.QDialog, Ui_progressDialog):
#     def __init__(self, inputValues, QBEM, parent=None):
#         super(SurgingProgressBar, self).__init__(parent)
#         self.setupUi(self)
#         self.inputValues = inputValues
#         self.QBEM = QBEM
        
#         self.surgingThread = SurgingThread(self.n, self.inputValues, self.QBEM, self.QG)
#         self.surgingThread.total.connect(self.progressBar.setMaximum)
#         self.surgingThread.update.connect(self.update)
#         self.surgingThread.finished.connect(self.finished)
#         self.btn_OK.clicked.connect(self.accept)

#         self.icon = 0
#         self.surgingThread.start()

#     @QtCore.pyqtSlot()
#     def finished(self):
#         self.df = pd.DataFrame({'GVF': self.surgingThread.GF, 'GV': self.surgingThread.GV,
#                                 'P_single-phase': self.surgingThread.PP_sgl, 'P_homogeneous': self.surgingThread.PP_homo,
#                                 'P_model': self.surgingThread.PP, 'Flow_pattern': self.surgingThread.FGL})
#         self.progressBar.setValue(self.n)
#         msg = QtWidgets.QMessageBox()
#         msg.setIcon(QtWidgets.QMessageBox.Information)
#         msg.setText("The calculation is finished!")
#         msg.setWindowTitle("Finish")
#         msg.exec_()

#     @QtCore.pyqtSlot()
#     def update(self):
#         self.icon += 1
#         self.progressBar.setValue(self.icon)

# class SurgingThread(QtCore.QThread):
#     # class variables for signals
#     total = QtCore.pyqtSignal(object)
#     update = QtCore.pyqtSignal()

#     def __init__(self, n, inputValues, QBEM, QG):
#         super(SurgingThread, self).__init__()
#         self.n = n                          # maximum run times
#         self.inputValues = inputValues      # input dictionary
#         self.QBEM = QBEM
#         self.QG = QG                        # QG array for surging calculation
#         self.ql = self.inputValues['QL']
#         self.PP_homo = []                   # homogeneous model for comparison
#         self.PP_sgl = []                    # single-phase performance
#         self.GF = []
#         self.GV = []
#         self.PP = []
#         self.FGL = []

#         HP_sgl, HE_sgl, HEE_sgl, HF_sgl, HT_sgl, HRE_sgl, QLK_sgl = \
#             MainProgram.single_phase_calculation(self.inputValues, self.QBEM, self.ql)

#         self.HP_sgl = HP_sgl

#     def run(self):
#         self.total.emit(self.n)

#         i = 0
#         while i <= self.n:
#             self.msleep(1)          # A necessary pause to show the progress
#             qg = self.QG[i]
#             gf, gv, pp, fgl = MainProgram.two_phase_calculation(self.inputValues, self.QBEM, self.ql, qg)
#             if gf <= 0.3:   # GVF is high enough to make the plot
#                 self.PP_sgl.append(self.HP_sgl)
#                 self.GF.append(gf * 100)
#                 self.GV.append(gv * 100)
#                 self.FGL.append(fgl)
#                 c_h = (1 - gf) + gf * self.inputValues['DENG'] / self.inputValues['DENL']
#                 c_m = (1 - gv) + gv * self.inputValues['DENG'] / self.inputValues['DENL']
#                 self.PP_homo.append(c_h * self.HP_sgl)
#                 self.PP.append(c_m * self.HP_sgl)
#             else:
#                 break
#             i += 1
#             self.update.emit()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = plungerLiftGUI()
    sys.exit(app.exec_())