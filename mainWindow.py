# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1205, 675)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plunger/icons/plunger_logo_PFmZvE.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("\n"
"QMainWindow::separator {\n"
"    background: yellow;\n"
"    width: 10px; /* when vertical */\n"
"    height: 10px; /* when horizontal */\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"    background: red;\n"
"}\n"
"\n"
"/***************************************************************/\n"
"QMenuBar {\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"\n"
"/***************************************************************/\n"
"QMenu {\n"
"    background-color: white;\n"
"    margin: 2px; /* some spacing around the menu */\n"
"    font: 14px \"Arial\",\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border-color: darkblue;\n"
"    background: rgba(100, 100, 100, 150);\n"
"}\n"
"\n"
"QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"    background: gray;\n"
"    border: 1px inset gray;\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"/***************************************************************/\n"
"QToolButton { /* all types of tool button */\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(downarrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color: qlineargradient(spread:reflect, x1:0.477, y1:0.778591, x2:1, y2:0, stop:0 rgba(0, 120, 178, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.toolBox = QtWidgets.QToolBox(self.splitter)
        self.toolBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.toolBox.setStyleSheet("QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border-radius: 5px;\n"
"    color: darkgray;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: 14px \"Arial\";\n"
"    color: black;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*border: 2px solid #8f8f91;*/\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    /*border: none;*/\n"
"    border-radius: 10px;\n"
"    background-position: center bottom;\n"
"    background-repeat: no-repeat;\n"
"    background-origin: content;\n"
"    font: 14px \"Arial\",\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"   background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0  #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.pageConfigure = QtWidgets.QWidget()
        self.pageConfigure.setGeometry(QtCore.QRect(0, 0, 170, 485))
        self.pageConfigure.setObjectName("pageConfigure")
        self.btnWell = QtWidgets.QToolButton(self.pageConfigure)
        self.btnWell.setGeometry(QtCore.QRect(20, 10, 140, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWell.sizePolicy().hasHeightForWidth())
        self.btnWell.setSizePolicy(sizePolicy)
        self.btnWell.setMaximumSize(QtCore.QSize(16777215, 120))
        self.btnWell.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnWell.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plunger/icons/well_trajectory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnWell.setIcon(icon1)
        self.btnWell.setIconSize(QtCore.QSize(45, 60))
        self.btnWell.setCheckable(True)
        self.btnWell.setChecked(False)
        self.btnWell.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btnWell.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnWell.setAutoRaise(True)
        self.btnWell.setObjectName("btnWell")
        self.btnSurface = QtWidgets.QToolButton(self.pageConfigure)
        self.btnSurface.setGeometry(QtCore.QRect(18, 111, 140, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSurface.sizePolicy().hasHeightForWidth())
        self.btnSurface.setSizePolicy(sizePolicy)
        self.btnSurface.setMaximumSize(QtCore.QSize(16777215, 120))
        self.btnSurface.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnSurface.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plunger/icons/valve.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSurface.setIcon(icon2)
        self.btnSurface.setIconSize(QtCore.QSize(45, 60))
        self.btnSurface.setCheckable(True)
        self.btnSurface.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnSurface.setObjectName("btnSurface")
        self.btnFluid = QtWidgets.QToolButton(self.pageConfigure)
        self.btnFluid.setGeometry(QtCore.QRect(20, 213, 140, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFluid.sizePolicy().hasHeightForWidth())
        self.btnFluid.setSizePolicy(sizePolicy)
        self.btnFluid.setMaximumSize(QtCore.QSize(16777215, 120))
        self.btnFluid.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plunger/icons/oil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFluid.setIcon(icon3)
        self.btnFluid.setIconSize(QtCore.QSize(45, 60))
        self.btnFluid.setCheckable(True)
        self.btnFluid.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnFluid.setObjectName("btnFluid")
        self.btnReservoir = QtWidgets.QToolButton(self.pageConfigure)
        self.btnReservoir.setGeometry(QtCore.QRect(20, 315, 140, 83))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReservoir.sizePolicy().hasHeightForWidth())
        self.btnReservoir.setSizePolicy(sizePolicy)
        self.btnReservoir.setMaximumSize(QtCore.QSize(16777215, 120))
        self.btnReservoir.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plunger/icons/reservoir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReservoir.setIcon(icon4)
        self.btnReservoir.setIconSize(QtCore.QSize(45, 60))
        self.btnReservoir.setCheckable(True)
        self.btnReservoir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnReservoir.setObjectName("btnReservoir")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plunger/icons/configuration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageConfigure, icon5, "")
        self.pageSimulation = QtWidgets.QWidget()
        self.pageSimulation.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageSimulation.setObjectName("pageSimulation")
        self.btnRun = QtWidgets.QToolButton(self.pageSimulation)
        self.btnRun.setGeometry(QtCore.QRect(60, 10, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnRun.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnRun.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/plunger/icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRun.setIcon(icon6)
        self.btnRun.setIconSize(QtCore.QSize(45, 60))
        self.btnRun.setCheckable(False)
        self.btnRun.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnRun.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnRun.setAutoRaise(False)
        self.btnRun.setObjectName("btnRun")
        self.btnStop = QtWidgets.QToolButton(self.pageSimulation)
        self.btnStop.setGeometry(QtCore.QRect(60, 100, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy)
        self.btnStop.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnStop.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnStop.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/plunger/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon7)
        self.btnStop.setIconSize(QtCore.QSize(45, 60))
        self.btnStop.setCheckable(False)
        self.btnStop.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btnStop.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnStop.setAutoRaise(False)
        self.btnStop.setObjectName("btnStop")
        self.btnReset = QtWidgets.QToolButton(self.pageSimulation)
        self.btnReset.setGeometry(QtCore.QRect(60, 190, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReset.sizePolicy().hasHeightForWidth())
        self.btnReset.setSizePolicy(sizePolicy)
        self.btnReset.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnReset.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnReset.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/plunger/icons/Reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReset.setIcon(icon8)
        self.btnReset.setIconSize(QtCore.QSize(45, 60))
        self.btnReset.setCheckable(False)
        self.btnReset.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnReset.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnReset.setAutoRaise(False)
        self.btnReset.setArrowType(QtCore.Qt.NoArrow)
        self.btnReset.setObjectName("btnReset")
        self.btnResults = QtWidgets.QToolButton(self.pageSimulation)
        self.btnResults.setGeometry(QtCore.QRect(60, 280, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnResults.sizePolicy().hasHeightForWidth())
        self.btnResults.setSizePolicy(sizePolicy)
        self.btnResults.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnResults.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/plunger/icons/results.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnResults.setIcon(icon9)
        self.btnResults.setIconSize(QtCore.QSize(45, 60))
        self.btnResults.setCheckable(False)
        self.btnResults.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnResults.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnResults.setAutoRaise(False)
        self.btnResults.setObjectName("btnResults")
        self.btnOutput = QtWidgets.QToolButton(self.pageSimulation)
        self.btnOutput.setGeometry(QtCore.QRect(60, 370, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOutput.sizePolicy().hasHeightForWidth())
        self.btnOutput.setSizePolicy(sizePolicy)
        self.btnOutput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnOutput.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/plunger/icons/output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOutput.setIcon(icon10)
        self.btnOutput.setIconSize(QtCore.QSize(45, 60))
        self.btnOutput.setCheckable(False)
        self.btnOutput.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnOutput.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnOutput.setAutoRaise(False)
        self.btnOutput.setObjectName("btnOutput")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/plunger/icons/simulation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageSimulation, icon11, "")
        self.pageAnalyze = QtWidgets.QWidget()
        self.pageAnalyze.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageAnalyze.setObjectName("pageAnalyze")
        self.btnPlot = QtWidgets.QToolButton(self.pageAnalyze)
        self.btnPlot.setGeometry(QtCore.QRect(60, 10, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPlot.sizePolicy().hasHeightForWidth())
        self.btnPlot.setSizePolicy(sizePolicy)
        self.btnPlot.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnPlot.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/plunger/icons/plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlot.setIcon(icon12)
        self.btnPlot.setIconSize(QtCore.QSize(80, 80))
        self.btnPlot.setCheckable(True)
        self.btnPlot.setChecked(False)
        self.btnPlot.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnPlot.setObjectName("btnPlot")
        self.btnData = QtWidgets.QToolButton(self.pageAnalyze)
        self.btnData.setGeometry(QtCore.QRect(60, 100, 61, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnData.sizePolicy().hasHeightForWidth())
        self.btnData.setSizePolicy(sizePolicy)
        self.btnData.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnData.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/plunger/icons/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnData.setIcon(icon13)
        self.btnData.setIconSize(QtCore.QSize(45, 60))
        self.btnData.setCheckable(True)
        self.btnData.setChecked(False)
        self.btnData.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnData.setObjectName("btnData")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/plunger/icons/analyze.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageAnalyze, icon14, "")
        self.tabWidget_main = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_main.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_main.setFont(font)
        self.tabWidget_main.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    top:-1px; \n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"   /* background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); */\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    border: 1px solid #C4C4C3;\n"
"    border: 1px solid lightgray;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    min-width: 25ex;\n"
"    padding: 4px;\n"
"    font: 14px  \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0,0,255);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -0px;\n"
"    margin-right: -0px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}\n"
"")
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tabConfigure = QtWidgets.QWidget()
        self.tabConfigure.setObjectName("tabConfigure")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabConfigure)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_configure = QtWidgets.QTabWidget(self.tabConfigure)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_configure.setFont(font)
        self.tabWidget_configure.setStyleSheet("/**********************************/\n"
"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"/*********************************/\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"    font: 12px \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 30ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"\n"
"/********************************************/\n"
"QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 10pt;\n"
"}")
        self.tabWidget_configure.setObjectName("tabWidget_configure")
        self.tabWell = QtWidgets.QWidget()
        self.tabWell.setObjectName("tabWell")
        self.label_wellGeometry = QtWidgets.QLabel(self.tabWell)
        self.label_wellGeometry.setGeometry(QtCore.QRect(10, 10, 451, 481))
        self.label_wellGeometry.setStyleSheet("border: 2px solid gray;")
        self.label_wellGeometry.setText("")
        self.label_wellGeometry.setPixmap(QtGui.QPixmap(":/plunger/icons/plunger_system.png"))
        self.label_wellGeometry.setScaledContents(True)
        self.label_wellGeometry.setObjectName("label_wellGeometry")
        self.layoutWidget = QtWidgets.QWidget(self.tabWell)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 10, 511, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_vertical = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical.setFont(font)
        self.groupBox_vertical.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical.setObjectName("groupBox_vertical")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_vertical)
        self.formLayoutWidget.setGeometry(QtCore.QRect(12, 20, 231, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_wellName = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_wellName.setObjectName("label_wellName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_wellName)
        self.lineEdit_wellName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_wellName.setMaxLength(8)
        self.lineEdit_wellName.setObjectName("lineEdit_wellName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_wellName)
        self.label_wellDepth = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_wellDepth.setObjectName("label_wellDepth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_wellDepth)
        self.lineEdit_wellDepth = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_wellDepth.setMaxLength(8)
        self.lineEdit_wellDepth.setObjectName("lineEdit_wellDepth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_wellDepth)
        self.label_absoluteRoughness = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_absoluteRoughness.setObjectName("label_absoluteRoughness")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_absoluteRoughness)
        self.lineEdit_absoluteRoughnessV = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_absoluteRoughnessV.setMaxLength(8)
        self.lineEdit_absoluteRoughnessV.setObjectName("lineEdit_absoluteRoughnessV")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_absoluteRoughnessV)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_vertical)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(260, 20, 231, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_tubingID = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_tubingID.setObjectName("label_tubingID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tubingID)
        self.lineEdit_tubingID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_tubingID.setMaxLength(8)
        self.lineEdit_tubingID.setObjectName("lineEdit_tubingID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tubingID)
        self.label_tubingOD = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_tubingOD.setObjectName("label_tubingOD")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_tubingOD)
        self.lineEdit_tubingOD = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_tubingOD.setMaxLength(8)
        self.lineEdit_tubingOD.setObjectName("lineEdit_tubingOD")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tubingOD)
        self.label_casingID = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_casingID.setObjectName("label_casingID")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_casingID)
        self.lineEdit_casingID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_casingID.setMaxLength(8)
        self.lineEdit_casingID.setObjectName("lineEdit_casingID")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_casingID)
        self.verticalLayout.addWidget(self.groupBox_vertical)
        self.groupBox_horizontal = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_horizontal.setFont(font)
        self.groupBox_horizontal.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_horizontal.setObjectName("groupBox_horizontal")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_horizontal)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(11, 30, 231, 71))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_horizontalLength = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_horizontalLength.setObjectName("label_horizontalLength")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_horizontalLength)
        self.lineEdit_horizontalLength = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_horizontalLength.setMaxLength(8)
        self.lineEdit_horizontalLength.setObjectName("lineEdit_horizontalLength")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_horizontalLength)
        self.label_inclinationAngle = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_inclinationAngle.setObjectName("label_inclinationAngle")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_inclinationAngle)
        self.lineEdit_inclinationAngle = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_inclinationAngle.setMaxLength(8)
        self.lineEdit_inclinationAngle.setObjectName("lineEdit_inclinationAngle")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inclinationAngle)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_horizontal)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(260, 30, 231, 71))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setSpacing(5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_horizontalAngle = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_horizontalAngle.setObjectName("label_horizontalAngle")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_horizontalAngle)
        self.lineEdit_innerDiameter = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_innerDiameter.setMaxLength(8)
        self.lineEdit_innerDiameter.setObjectName("lineEdit_innerDiameter")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_innerDiameter)
        self.label_innerDiameter = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_innerDiameter.setObjectName("label_innerDiameter")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_innerDiameter)
        self.lineEdit_absoluteRoughnessH = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_absoluteRoughnessH.setMaxLength(8)
        self.lineEdit_absoluteRoughnessH.setObjectName("lineEdit_absoluteRoughnessH")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_absoluteRoughnessH)
        self.verticalLayout.addWidget(self.groupBox_horizontal)
        self.groupBox_plunger = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_plunger.setFont(font)
        self.groupBox_plunger.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_plunger.setObjectName("groupBox_plunger")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_plunger)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(13, 30, 231, 72))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setSpacing(5)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_plungerWeight = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_plungerWeight.setObjectName("label_plungerWeight")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_plungerWeight)
        self.lineEdit_plungerWeight = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_plungerWeight.setMaxLength(8)
        self.lineEdit_plungerWeight.setObjectName("lineEdit_plungerWeight")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plungerWeight)
        self.label_plungerLength = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_plungerLength.setObjectName("label_plungerLength")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_plungerLength)
        self.label_plungerRise = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_plungerRise.setObjectName("label_plungerRise")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_plungerRise)
        self.lineEdit_plungerLength = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_plungerLength.setMaxLength(8)
        self.lineEdit_plungerLength.setObjectName("lineEdit_plungerLength")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plungerLength)
        self.lineEdit_plungerRise = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_plungerRise.setMaxLength(8)
        self.lineEdit_plungerRise.setObjectName("lineEdit_plungerRise")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plungerRise)
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_plunger)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(260, 30, 231, 71))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setSpacing(5)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_plungerDiameter = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.label_plungerDiameter.setObjectName("label_plungerDiameter")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_plungerDiameter)
        self.lineEdit_plungerDiameter = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.lineEdit_plungerDiameter.setMaxLength(8)
        self.lineEdit_plungerDiameter.setObjectName("lineEdit_plungerDiameter")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plungerDiameter)
        self.label_plungerDrag = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.label_plungerDrag.setObjectName("label_plungerDrag")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_plungerDrag)
        self.lineEdit_plungerDrag = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.lineEdit_plungerDrag.setMaxLength(8)
        self.lineEdit_plungerDrag.setObjectName("lineEdit_plungerDrag")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_plungerDrag)
        self.verticalLayout.addWidget(self.groupBox_plunger)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.tabWell)
        self.layoutWidget1.setGeometry(QtCore.QRect(580, 410, 311, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_reset_WG = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_reset_WG.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_WG.setIcon(icon8)
        self.btn_reset_WG.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_WG.setObjectName("btn_reset_WG")
        self.horizontalLayout_6.addWidget(self.btn_reset_WG)
        self.btn_save_WG = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_save_WG.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/plunger/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_WG.setIcon(icon15)
        self.btn_save_WG.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_WG.setObjectName("btn_save_WG")
        self.horizontalLayout_6.addWidget(self.btn_save_WG)
        self.btn_cancel_WG = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_cancel_WG.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_cancel_WG.setIcon(icon7)
        self.btn_cancel_WG.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel_WG.setObjectName("btn_cancel_WG")
        self.horizontalLayout_6.addWidget(self.btn_cancel_WG)
        self.tabWidget_configure.addTab(self.tabWell, "")
        self.tabSurface = QtWidgets.QWidget()
        self.tabSurface.setObjectName("tabSurface")
        self.groupBox_valve = QtWidgets.QGroupBox(self.tabSurface)
        self.groupBox_valve.setGeometry(QtCore.QRect(390, 10, 471, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_valve.setFont(font)
        self.groupBox_valve.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_valve.setObjectName("groupBox_valve")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_valve)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 171, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_valveCv = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_valveCv.setStyleSheet("font: 10pt;")
        self.radioButton_valveCv.setChecked(True)
        self.radioButton_valveCv.setObjectName("radioButton_valveCv")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_valveCv)
        self.verticalLayout_3.addWidget(self.radioButton_valveCv)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setSpacing(5)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_valveCoeff = QtWidgets.QLabel(self.layoutWidget2)
        self.label_valveCoeff.setObjectName("label_valveCoeff")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_valveCoeff)
        self.lineEdit_valveCoeff = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_valveCoeff.setMaxLength(10)
        self.lineEdit_valveCoeff.setObjectName("lineEdit_valveCoeff")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_valveCoeff)
        self.verticalLayout_3.addLayout(self.formLayout_8)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_valve)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 120, 123, 184))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_valveFunc = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_valveFunc.setStyleSheet("font: 10pt;")
        self.radioButton_valveFunc.setObjectName("radioButton_valveFunc")
        self.buttonGroup_2.addButton(self.radioButton_valveFunc)
        self.verticalLayout_4.addWidget(self.radioButton_valveFunc)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setSpacing(5)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_tubingID_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_tubingID_2.setObjectName("label_tubingID_2")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tubingID_2)
        self.lineEdit_tubingID_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_tubingID_2.setMaxLength(8)
        self.lineEdit_tubingID_2.setObjectName("lineEdit_tubingID_2")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tubingID_2)
        self.label_tubingOD_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_tubingOD_2.setObjectName("label_tubingOD_2")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_tubingOD_2)
        self.lineEdit_tubingOD_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_tubingOD_2.setMaxLength(8)
        self.lineEdit_tubingOD_2.setObjectName("lineEdit_tubingOD_2")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tubingOD_2)
        self.label_casingID_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_casingID_2.setObjectName("label_casingID_2")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_casingID_2)
        self.lineEdit_casingID_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_casingID_2.setMaxLength(8)
        self.lineEdit_casingID_2.setObjectName("lineEdit_casingID_2")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_casingID_2)
        self.label_tubingOD_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_tubingOD_4.setObjectName("label_tubingOD_4")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_tubingOD_4)
        self.lineEdit_casingID_4 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_casingID_4.setMaxLength(8)
        self.lineEdit_casingID_4.setObjectName("lineEdit_casingID_4")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_casingID_4)
        self.label_tubingOD_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_tubingOD_5.setObjectName("label_tubingOD_5")
        self.formLayout_9.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_tubingOD_5)
        self.label_tubingOD_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_tubingOD_6.setObjectName("label_tubingOD_6")
        self.formLayout_9.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_tubingOD_6)
        self.lineEdit_casingID_5 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_casingID_5.setMaxLength(8)
        self.lineEdit_casingID_5.setObjectName("lineEdit_casingID_5")
        self.formLayout_9.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_casingID_5)
        self.lineEdit_casingID_6 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_casingID_6.setMaxLength(8)
        self.lineEdit_casingID_6.setObjectName("lineEdit_casingID_6")
        self.formLayout_9.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_casingID_6)
        self.verticalLayout_4.addLayout(self.formLayout_9)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_valve)
        self.layoutWidget4.setGeometry(QtCore.QRect(220, 30, 221, 23))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.formLayout_10 = QtWidgets.QFormLayout(self.layoutWidget4)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_surfaceT = QtWidgets.QLabel(self.layoutWidget4)
        self.label_surfaceT.setObjectName("label_surfaceT")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_surfaceT)
        self.lineEdit_surfaceT = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_surfaceT.setMaxLength(8)
        self.lineEdit_surfaceT.setObjectName("lineEdit_surfaceT")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_surfaceT)
        self.label_4 = QtWidgets.QLabel(self.groupBox_valve)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 321, 231))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/plunger/icons/valve_equation.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.groupBox_linePressure = QtWidgets.QGroupBox(self.tabSurface)
        self.groupBox_linePressure.setGeometry(QtCore.QRect(10, 10, 331, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_linePressure.setFont(font)
        self.groupBox_linePressure.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_linePressure.setObjectName("groupBox_linePressure")
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_linePressure)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 30, 245, 425))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setObjectName("formLayout_12")
        self.verticalLayout_7.addLayout(self.formLayout_12)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_constantPL = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_constantPL.setStyleSheet("font: 10pt;")
        self.radioButton_constantPL.setChecked(True)
        self.radioButton_constantPL.setObjectName("radioButton_constantPL")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_constantPL)
        self.verticalLayout_5.addWidget(self.radioButton_constantPL)
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_linePressure = QtWidgets.QLabel(self.layoutWidget5)
        self.label_linePressure.setObjectName("label_linePressure")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_linePressure)
        self.lineEdit_linePressure = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_linePressure.setMaxLength(10)
        self.lineEdit_linePressure.setObjectName("lineEdit_linePressure")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_linePressure)
        self.verticalLayout_5.addLayout(self.formLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_varyingPL = QtWidgets.QVBoxLayout()
        self.verticalLayout_varyingPL.setObjectName("verticalLayout_varyingPL")
        self.radioButton_varyingT = QtWidgets.QRadioButton(self.layoutWidget5)
        self.radioButton_varyingT.setStyleSheet("font: 10pt;")
        self.radioButton_varyingT.setChecked(False)
        self.radioButton_varyingT.setObjectName("radioButton_varyingT")
        self.buttonGroup.addButton(self.radioButton_varyingT)
        self.verticalLayout_varyingPL.addWidget(self.radioButton_varyingT)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_addRow = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_addRow.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 10pt \"Arial\";")
        self.btn_addRow.setObjectName("btn_addRow")
        self.horizontalLayout_5.addWidget(self.btn_addRow)
        self.btn_readData = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_readData.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 10pt \"Arial\";")
        self.btn_readData.setObjectName("btn_readData")
        self.horizontalLayout_5.addWidget(self.btn_readData)
        self.btn_plotLinepressure = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_plotLinepressure.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 10pt \"Arial\";")
        self.btn_plotLinepressure.setObjectName("btn_plotLinepressure")
        self.horizontalLayout_5.addWidget(self.btn_plotLinepressure)
        self.verticalLayout_varyingPL.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_varyingPL)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.table_linePressure = QtWidgets.QTableWidget(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_linePressure.sizePolicy().hasHeightForWidth())
        self.table_linePressure.setSizePolicy(sizePolicy)
        self.table_linePressure.setSizeIncrement(QtCore.QSize(0, 0))
        self.table_linePressure.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.table_linePressure.setFont(font)
        self.table_linePressure.setStyleSheet("QHeaderView::section {\n"
"    background-color: lightgrey;\n"
"    padding: 2px;\n"
"    font: 10pt \"Arial\";\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.table_linePressure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_linePressure.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_linePressure.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_linePressure.setAlternatingRowColors(True)
        self.table_linePressure.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_linePressure.setShowGrid(True)
        self.table_linePressure.setGridStyle(QtCore.Qt.SolidLine)
        self.table_linePressure.setWordWrap(True)
        self.table_linePressure.setCornerButtonEnabled(False)
        self.table_linePressure.setObjectName("table_linePressure")
        self.table_linePressure.setColumnCount(2)
        self.table_linePressure.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_linePressure.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_linePressure.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_linePressure.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_linePressure.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_linePressure.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_linePressure.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_linePressure.setItem(0, 1, item)
        self.table_linePressure.horizontalHeader().setCascadingSectionResizes(True)
        self.table_linePressure.horizontalHeader().setDefaultSectionSize(70)
        self.table_linePressure.horizontalHeader().setMinimumSectionSize(39)
        self.table_linePressure.verticalHeader().setDefaultSectionSize(21)
        self.verticalLayout_7.addWidget(self.table_linePressure)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabSurface)
        self.layoutWidget_2.setGeometry(QtCore.QRect(550, 390, 311, 34))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_reset_SI = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_reset_SI.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_SI.setIcon(icon8)
        self.btn_reset_SI.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_SI.setObjectName("btn_reset_SI")
        self.horizontalLayout_7.addWidget(self.btn_reset_SI)
        self.btn_save_SI = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_save_SI.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_SI.setIcon(icon15)
        self.btn_save_SI.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_SI.setObjectName("btn_save_SI")
        self.horizontalLayout_7.addWidget(self.btn_save_SI)
        self.btn_cancel_SI = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_cancel_SI.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_cancel_SI.setIcon(icon7)
        self.btn_cancel_SI.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel_SI.setObjectName("btn_cancel_SI")
        self.horizontalLayout_7.addWidget(self.btn_cancel_SI)
        self.tabWidget_configure.addTab(self.tabSurface, "")
        self.tabFluid = QtWidgets.QWidget()
        self.tabFluid.setObjectName("tabFluid")
        self.groupBox_vertical_2 = QtWidgets.QGroupBox(self.tabFluid)
        self.groupBox_vertical_2.setGeometry(QtCore.QRect(10, 50, 301, 114))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_2.setFont(font)
        self.groupBox_vertical_2.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_2.setObjectName("groupBox_vertical_2")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_vertical_2)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 20, 281, 47))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_13 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.formLayout_13.setSpacing(5)
        self.formLayout_13.setObjectName("formLayout_13")
        self.lineEdit_denlR = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        self.lineEdit_denlR.setMaxLength(8)
        self.lineEdit_denlR.setObjectName("lineEdit_denlR")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_denlR)
        self.label_denlR = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.label_denlR.setObjectName("label_denlR")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_denlR)
        self.label_visL = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.label_visL.setObjectName("label_visL")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_visL)
        self.lineEdit_visL = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        self.lineEdit_visL.setMaxLength(8)
        self.lineEdit_visL.setObjectName("lineEdit_visL")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_visL)
        self.groupBox_vertical_3 = QtWidgets.QGroupBox(self.tabFluid)
        self.groupBox_vertical_3.setGeometry(QtCore.QRect(10, 170, 301, 114))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_3.setFont(font)
        self.groupBox_vertical_3.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_3.setObjectName("groupBox_vertical_3")
        self.formLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_vertical_3)
        self.formLayoutWidget_11.setGeometry(QtCore.QRect(11, 20, 281, 81))
        self.formLayoutWidget_11.setObjectName("formLayoutWidget_11")
        self.formLayout_16 = QtWidgets.QFormLayout(self.formLayoutWidget_11)
        self.formLayout_16.setContentsMargins(0, 0, 0, 0)
        self.formLayout_16.setSpacing(5)
        self.formLayout_16.setObjectName("formLayout_16")
        self.label_dengR = QtWidgets.QLabel(self.formLayoutWidget_11)
        self.label_dengR.setObjectName("label_dengR")
        self.formLayout_16.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_dengR)
        self.lineEdit_dengR = QtWidgets.QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_dengR.setMaxLength(8)
        self.lineEdit_dengR.setObjectName("lineEdit_dengR")
        self.formLayout_16.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dengR)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tabFluid)
        self.layoutWidget_3.setGeometry(QtCore.QRect(150, 450, 311, 34))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_reset_FP = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_reset_FP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_FP.setIcon(icon8)
        self.btn_reset_FP.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_FP.setObjectName("btn_reset_FP")
        self.horizontalLayout_8.addWidget(self.btn_reset_FP)
        self.btn_save_FP = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_save_FP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_FP.setIcon(icon15)
        self.btn_save_FP.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_FP.setObjectName("btn_save_FP")
        self.horizontalLayout_8.addWidget(self.btn_save_FP)
        self.btn_cancel_FP = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_cancel_FP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_cancel_FP.setIcon(icon7)
        self.btn_cancel_FP.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel_FP.setObjectName("btn_cancel_FP")
        self.horizontalLayout_8.addWidget(self.btn_cancel_FP)
        self.radioButton_BlackOil = QtWidgets.QRadioButton(self.tabFluid)
        self.radioButton_BlackOil.setGeometry(QtCore.QRect(12, 20, 171, 20))
        self.radioButton_BlackOil.setStyleSheet("font: 10pt;")
        self.radioButton_BlackOil.setCheckable(True)
        self.radioButton_BlackOil.setChecked(True)
        self.radioButton_BlackOil.setObjectName("radioButton_BlackOil")
        self.radioButton_Compositional = QtWidgets.QRadioButton(self.tabFluid)
        self.radioButton_Compositional.setGeometry(QtCore.QRect(450, 20, 221, 20))
        self.radioButton_Compositional.setStyleSheet("font: 10pt;")
        self.radioButton_Compositional.setCheckable(True)
        self.radioButton_Compositional.setChecked(False)
        self.radioButton_Compositional.setObjectName("radioButton_Compositional")
        self.groupBox_vertical_8 = QtWidgets.QGroupBox(self.tabFluid)
        self.groupBox_vertical_8.setGeometry(QtCore.QRect(340, 50, 621, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_8.setFont(font)
        self.groupBox_vertical_8.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_8.setObjectName("groupBox_vertical_8")
        self.tableWidget_Compositional = QtWidgets.QTableWidget(self.groupBox_vertical_8)
        self.tableWidget_Compositional.setGeometry(QtCore.QRect(30, 20, 541, 311))
        self.tableWidget_Compositional.setObjectName("tableWidget_Compositional")
        self.tableWidget_Compositional.setColumnCount(5)
        self.tableWidget_Compositional.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Compositional.setHorizontalHeaderItem(4, item)
        self.tableWidget_Compositional.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Compositional.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Compositional.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_Compositional.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Compositional.verticalHeader().setDefaultSectionSize(25)
        self.tabWidget_configure.addTab(self.tabFluid, "")
        self.tabReservoir = QtWidgets.QWidget()
        self.tabReservoir.setObjectName("tabReservoir")
        self.groupBox_vertical_4 = QtWidgets.QGroupBox(self.tabReservoir)
        self.groupBox_vertical_4.setGeometry(QtCore.QRect(12, 48, 281, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_4.setFont(font)
        self.groupBox_vertical_4.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_4.setTitle("")
        self.groupBox_vertical_4.setObjectName("groupBox_vertical_4")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_vertical_4)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 261, 181))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_14 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_14.setContentsMargins(0, 0, 0, 0)
        self.formLayout_14.setSpacing(5)
        self.formLayout_14.setObjectName("formLayout_14")
        self.label_C = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_C.setObjectName("label_C")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_C)
        self.lineEdit_C = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_C.setMaxLength(8)
        self.lineEdit_C.setObjectName("lineEdit_C")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_C)
        self.label_n = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_n.setObjectName("label_n")
        self.formLayout_14.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_n)
        self.lineEdit_n = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_n.setMaxLength(8)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.formLayout_14.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_n)
        self.label_Pr_L = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_Pr_L.setObjectName("label_Pr_L")
        self.formLayout_14.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Pr_L)
        self.lineEdit_Pr_L = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_Pr_L.setMaxLength(8)
        self.lineEdit_Pr_L.setObjectName("lineEdit_Pr_L")
        self.formLayout_14.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Pr_L)
        self.label_GLR_L = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_GLR_L.setObjectName("label_GLR_L")
        self.formLayout_14.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_GLR_L)
        self.lineEdit_GLR_L = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_GLR_L.setMaxLength(8)
        self.lineEdit_GLR_L.setObjectName("lineEdit_GLR_L")
        self.formLayout_14.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GLR_L)
        self.label_Tgr_L = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_Tgr_L.setObjectName("label_Tgr_L")
        self.formLayout_14.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_Tgr_L)
        self.lineEdit_Tgr_L = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_Tgr_L.setMaxLength(8)
        self.lineEdit_Tgr_L.setObjectName("lineEdit_Tgr_L")
        self.formLayout_14.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Tgr_L)
        self.label_Tgr_L_2 = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_Tgr_L_2.setObjectName("label_Tgr_L_2")
        self.formLayout_14.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_Tgr_L_2)
        self.lineEdit_Rsl = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.lineEdit_Rsl.setMaxLength(8)
        self.lineEdit_Rsl.setObjectName("lineEdit_Rsl")
        self.formLayout_14.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Rsl)
        self.radioButton_backPressure = QtWidgets.QRadioButton(self.tabReservoir)
        self.radioButton_backPressure.setGeometry(QtCore.QRect(12, 22, 171, 20))
        self.radioButton_backPressure.setStyleSheet("font: 10pt;")
        self.radioButton_backPressure.setCheckable(True)
        self.radioButton_backPressure.setChecked(True)
        self.radioButton_backPressure.setObjectName("radioButton_backPressure")
        self.radioButton_reservoirDetails = QtWidgets.QRadioButton(self.tabReservoir)
        self.radioButton_reservoirDetails.setGeometry(QtCore.QRect(340, 22, 221, 20))
        self.radioButton_reservoirDetails.setStyleSheet("font: 10pt;")
        self.radioButton_reservoirDetails.setCheckable(True)
        self.radioButton_reservoirDetails.setChecked(False)
        self.radioButton_reservoirDetails.setObjectName("radioButton_reservoirDetails")
        self.groupBox_vertical_5 = QtWidgets.QGroupBox(self.tabReservoir)
        self.groupBox_vertical_5.setGeometry(QtCore.QRect(340, 48, 281, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_5.setFont(font)
        self.groupBox_vertical_5.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_5.setTitle("")
        self.groupBox_vertical_5.setObjectName("groupBox_vertical_5")
        self.formLayoutWidget_10 = QtWidgets.QWidget(self.groupBox_vertical_5)
        self.formLayoutWidget_10.setGeometry(QtCore.QRect(10, 20, 261, 181))
        self.formLayoutWidget_10.setObjectName("formLayoutWidget_10")
        self.formLayout_15 = QtWidgets.QFormLayout(self.formLayoutWidget_10)
        self.formLayout_15.setContentsMargins(0, 0, 0, 0)
        self.formLayout_15.setSpacing(5)
        self.formLayout_15.setObjectName("formLayout_15")
        self.label_Pr_R = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_Pr_R.setObjectName("label_Pr_R")
        self.formLayout_15.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Pr_R)
        self.lineEdit_Pr_R = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_Pr_R.setMaxLength(8)
        self.lineEdit_Pr_R.setObjectName("lineEdit_Pr_R")
        self.formLayout_15.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Pr_R)
        self.label_mD = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_mD.setObjectName("label_mD")
        self.formLayout_15.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_mD)
        self.lineEdit_mD = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_mD.setMaxLength(8)
        self.lineEdit_mD.setObjectName("lineEdit_mD")
        self.formLayout_15.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_mD)
        self.label_Hr = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_Hr.setObjectName("label_Hr")
        self.formLayout_15.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Hr)
        self.lineEdit_Hr = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_Hr.setMaxLength(8)
        self.lineEdit_Hr.setObjectName("lineEdit_Hr")
        self.formLayout_15.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Hr)
        self.label_Rdrain = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_Rdrain.setObjectName("label_Rdrain")
        self.formLayout_15.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_Rdrain)
        self.lineEdit_Rdrain = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_Rdrain.setMaxLength(8)
        self.lineEdit_Rdrain.setObjectName("lineEdit_Rdrain")
        self.formLayout_15.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Rdrain)
        self.label_Rwell = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_Rwell.setObjectName("label_Rwell")
        self.formLayout_15.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_Rwell)
        self.lineEdit_Rwell = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_Rwell.setMaxLength(8)
        self.lineEdit_Rwell.setObjectName("lineEdit_Rwell")
        self.formLayout_15.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Rwell)
        self.label_Tgr_R = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_Tgr_R.setObjectName("label_Tgr_R")
        self.formLayout_15.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_Tgr_R)
        self.lineEdit_Tgr_R = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_Tgr_R.setMaxLength(8)
        self.lineEdit_Tgr_R.setObjectName("lineEdit_Tgr_R")
        self.formLayout_15.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Tgr_R)
        self.label_GLR_R = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.label_GLR_R.setObjectName("label_GLR_R")
        self.formLayout_15.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_GLR_R)
        self.lineEdit_GLR_R = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_GLR_R.setMaxLength(8)
        self.lineEdit_GLR_R.setObjectName("lineEdit_GLR_R")
        self.formLayout_15.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GLR_R)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tabReservoir)
        self.layoutWidget_4.setGeometry(QtCore.QRect(160, 270, 311, 34))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_reset_RP = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_reset_RP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_RP.setIcon(icon8)
        self.btn_reset_RP.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_RP.setObjectName("btn_reset_RP")
        self.horizontalLayout_9.addWidget(self.btn_reset_RP)
        self.btn_save_RP = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_save_RP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_RP.setIcon(icon15)
        self.btn_save_RP.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_RP.setObjectName("btn_save_RP")
        self.horizontalLayout_9.addWidget(self.btn_save_RP)
        self.btn_cancel_RP = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_cancel_RP.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_cancel_RP.setIcon(icon7)
        self.btn_cancel_RP.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel_RP.setObjectName("btn_cancel_RP")
        self.horizontalLayout_9.addWidget(self.btn_cancel_RP)
        self.tabWidget_configure.addTab(self.tabReservoir, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_configure)
        self.tabWidget_main.addTab(self.tabConfigure, "")
        self.tabSimulation = QtWidgets.QWidget()
        self.tabSimulation.setObjectName("tabSimulation")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabSimulation)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget_simulation = QtWidgets.QTabWidget(self.tabSimulation)
        self.tabWidget_simulation.setStyleSheet("/**********************************/\n"
"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"/*********************************/\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"    font: 12px \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 30ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"\n"
"/********************************************/\n"
"QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 10pt;\n"
"}")
        self.tabWidget_simulation.setObjectName("tabWidget_simulation")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.splitter_2 = QtWidgets.QSplitter(self.tabSettings)
        self.splitter_2.setGeometry(QtCore.QRect(10, 10, 691, 321))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox_vertical_7 = QtWidgets.QGroupBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_7.setFont(font)
        self.groupBox_vertical_7.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_7.setObjectName("groupBox_vertical_7")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_vertical_7)
        self.splitter_3.setGeometry(QtCore.QRect(12, 30, 666, 74))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_cycles = QtWidgets.QLabel(self.layoutWidget6)
        self.label_cycles.setObjectName("label_cycles")
        self.gridLayout.addWidget(self.label_cycles, 0, 0, 1, 1)
        self.lineEdit_cycles = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_cycles.setObjectName("lineEdit_cycles")
        self.gridLayout.addWidget(self.lineEdit_cycles, 0, 1, 1, 1)
        self.label_plungerT = QtWidgets.QLabel(self.layoutWidget6)
        self.label_plungerT.setObjectName("label_plungerT")
        self.gridLayout.addWidget(self.label_plungerT, 1, 0, 1, 1)
        self.lineEdit_plungerT = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_plungerT.setObjectName("lineEdit_plungerT")
        self.gridLayout.addWidget(self.lineEdit_plungerT, 1, 1, 1, 1)
        self.label_valveT = QtWidgets.QLabel(self.layoutWidget6)
        self.label_valveT.setObjectName("label_valveT")
        self.gridLayout.addWidget(self.label_valveT, 2, 0, 1, 1)
        self.lineEdit_valveT = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_valveT.setObjectName("lineEdit_valveT")
        self.gridLayout.addWidget(self.lineEdit_valveT, 2, 1, 1, 1)
        self.layoutWidget7 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_dtDown = QtWidgets.QLabel(self.layoutWidget7)
        self.label_dtDown.setObjectName("label_dtDown")
        self.gridLayout_2.addWidget(self.label_dtDown, 2, 0, 1, 1)
        self.lineEdit_dtDown = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_dtDown.setObjectName("lineEdit_dtDown")
        self.gridLayout_2.addWidget(self.lineEdit_dtDown, 2, 1, 1, 1)
        self.lineEdit_dtUp = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_dtUp.setObjectName("lineEdit_dtUp")
        self.gridLayout_2.addWidget(self.lineEdit_dtUp, 1, 1, 1, 1)
        self.label_dtUp = QtWidgets.QLabel(self.layoutWidget7)
        self.label_dtUp.setObjectName("label_dtUp")
        self.gridLayout_2.addWidget(self.label_dtUp, 1, 0, 1, 1)
        self.label_dtH = QtWidgets.QLabel(self.layoutWidget7)
        self.label_dtH.setObjectName("label_dtH")
        self.gridLayout_2.addWidget(self.label_dtH, 0, 0, 1, 1)
        self.lineEdit_dtH = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_dtH.setObjectName("lineEdit_dtH")
        self.gridLayout_2.addWidget(self.lineEdit_dtH, 0, 1, 1, 1)
        self.groupBox_vertical_6 = QtWidgets.QGroupBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_vertical_6.setFont(font)
        self.groupBox_vertical_6.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox_vertical_6.setObjectName("groupBox_vertical_6")
        self.formLayoutWidget_12 = QtWidgets.QWidget(self.groupBox_vertical_6)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(10, 20, 331, 101))
        self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
        self.formLayout_17 = QtWidgets.QFormLayout(self.formLayoutWidget_12)
        self.formLayout_17.setContentsMargins(0, 0, 0, 0)
        self.formLayout_17.setSpacing(5)
        self.formLayout_17.setObjectName("formLayout_17")
        self.label_Pc = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_Pc.setObjectName("label_Pc")
        self.formLayout_17.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Pc)
        self.lineEdit_Pc = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_Pc.setObjectName("lineEdit_Pc")
        self.formLayout_17.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Pc)
        self.label_Pt = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_Pt.setObjectName("label_Pt")
        self.formLayout_17.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Pt)
        self.lineEdit_Pt = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_Pt.setObjectName("lineEdit_Pt")
        self.formLayout_17.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Pt)
        self.label_Ltt = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_Ltt.setObjectName("label_Ltt")
        self.formLayout_17.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Ltt)
        self.lineEdit_Ltt = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_Ltt.setObjectName("lineEdit_Ltt")
        self.formLayout_17.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Ltt)
        self.label_Ltb = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_Ltb.setObjectName("label_Ltb")
        self.formLayout_17.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_Ltb)
        self.lineEdit_Ltb = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_Ltb.setObjectName("lineEdit_Ltb")
        self.formLayout_17.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Ltb)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tabSettings)
        self.layoutWidget_5.setGeometry(QtCore.QRect(200, 340, 311, 34))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_reset_setting = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_reset_setting.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_setting.setIcon(icon8)
        self.btn_reset_setting.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_setting.setObjectName("btn_reset_setting")
        self.horizontalLayout_10.addWidget(self.btn_reset_setting)
        self.btn_save_setting = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_save_setting.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_setting.setIcon(icon15)
        self.btn_save_setting.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_setting.setObjectName("btn_save_setting")
        self.horizontalLayout_10.addWidget(self.btn_save_setting)
        self.btn_cancel_setting = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_cancel_setting.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_cancel_setting.setIcon(icon7)
        self.btn_cancel_setting.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancel_setting.setObjectName("btn_cancel_setting")
        self.horizontalLayout_10.addWidget(self.btn_cancel_setting)
        self.tabWidget_simulation.addTab(self.tabSettings, "")
        self.tabCalculation = QtWidgets.QWidget()
        self.tabCalculation.setObjectName("tabCalculation")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tabCalculation)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.graphicsView = QtWidgets.QGraphicsView(self.tabCalculation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.graphicsView.setBaseSize(QtCore.QSize(250, 0))
        self.graphicsView.setLineWidth(1)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_11.addWidget(self.graphicsView)
        self.splitter_4 = QtWidgets.QSplitter(self.tabCalculation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.widget_simulationPlot1 = QtWidgets.QWidget(self.splitter_4)
        self.widget_simulationPlot1.setObjectName("widget_simulationPlot1")
        self.widget_simulationPlot2 = QtWidgets.QWidget(self.splitter_4)
        self.widget_simulationPlot2.setObjectName("widget_simulationPlot2")
        self.horizontalLayout_11.addWidget(self.splitter_4)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.tabWidget_simulation.addTab(self.tabCalculation, "")
        self.horizontalLayout_3.addWidget(self.tabWidget_simulation)
        self.tabWidget_main.addTab(self.tabSimulation, "")
        self.tabAnalyze = QtWidgets.QWidget()
        self.tabAnalyze.setObjectName("tabAnalyze")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabAnalyze)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget_analyze = QtWidgets.QTabWidget(self.tabAnalyze)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_analyze.setFont(font)
        self.tabWidget_analyze.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"    font: 12px \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 30ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget_analyze.setObjectName("tabWidget_analyze")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.widget_analyzePlot = QtWidgets.QWidget(self.tabPlot)
        self.widget_analyzePlot.setGeometry(QtCore.QRect(182, 20, 791, 461))
        self.widget_analyzePlot.setObjectName("widget_analyzePlot")
        self.layoutWidget8 = QtWidgets.QWidget(self.tabPlot)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 20, 162, 151))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFDD00, stop: 1 #FBB034);\n"
"    border-radius:2px;\n"
"    color:blue;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_analyzePlot = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_analyzePlot.setFont(font)
        self.comboBox_analyzePlot.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.comboBox_analyzePlot.setObjectName("comboBox_analyzePlot")
        self.verticalLayout_8.addWidget(self.comboBox_analyzePlot)
        self.verticalLayout_10.addWidget(self.groupBox)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_reset_analyzePlot = QtWidgets.QPushButton(self.layoutWidget8)
        self.btn_reset_analyzePlot.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_analyzePlot.setIcon(icon8)
        self.btn_reset_analyzePlot.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_analyzePlot.setObjectName("btn_reset_analyzePlot")
        self.verticalLayout_9.addWidget(self.btn_reset_analyzePlot)
        self.btn_save_analyzePlot = QtWidgets.QPushButton(self.layoutWidget8)
        self.btn_save_analyzePlot.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_analyzePlot.setIcon(icon15)
        self.btn_save_analyzePlot.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_analyzePlot.setObjectName("btn_save_analyzePlot")
        self.verticalLayout_9.addWidget(self.btn_save_analyzePlot)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget_analyze.addTab(self.tabPlot, "")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.gbx_output = QtWidgets.QGroupBox(self.tabData)
        self.gbx_output.setGeometry(QtCore.QRect(10, 20, 961, 391))
        self.gbx_output.setMinimumSize(QtCore.QSize(0, 0))
        self.gbx_output.setMaximumSize(QtCore.QSize(16777215, 450))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gbx_output.setFont(font)
        self.gbx_output.setObjectName("gbx_output")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbx_output)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hbx_data = QtWidgets.QHBoxLayout()
        self.hbx_data.setObjectName("hbx_data")
        self.tableWidget_analyzeData = QtWidgets.QTableWidget(self.gbx_output)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_analyzeData.setFont(font)
        self.tableWidget_analyzeData.setObjectName("tableWidget_analyzeData")
        self.tableWidget_analyzeData.setColumnCount(0)
        self.tableWidget_analyzeData.setRowCount(0)
        self.hbx_data.addWidget(self.tableWidget_analyzeData)
        self.gridLayout_3.addLayout(self.hbx_data, 0, 0, 1, 1)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tabData)
        self.layoutWidget_6.setGeometry(QtCore.QRect(330, 430, 311, 34))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_reset_analyzeData = QtWidgets.QPushButton(self.layoutWidget_6)
        self.btn_reset_analyzeData.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_reset_analyzeData.setIcon(icon8)
        self.btn_reset_analyzeData.setIconSize(QtCore.QSize(24, 24))
        self.btn_reset_analyzeData.setObjectName("btn_reset_analyzeData")
        self.horizontalLayout_13.addWidget(self.btn_reset_analyzeData)
        self.btn_save_analyzeData = QtWidgets.QPushButton(self.layoutWidget_6)
        self.btn_save_analyzeData.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"font: 12pt bold \"Arial\";")
        self.btn_save_analyzeData.setIcon(icon15)
        self.btn_save_analyzeData.setIconSize(QtCore.QSize(24, 24))
        self.btn_save_analyzeData.setObjectName("btn_save_analyzeData")
        self.horizontalLayout_13.addWidget(self.btn_save_analyzeData)
        self.tabWidget_analyze.addTab(self.tabData, "")
        self.horizontalLayout_4.addWidget(self.tabWidget_analyze)
        self.tabWidget_main.addTab(self.tabAnalyze, "")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 22))
        self.menubar.setStyleSheet("font: 75 10pt \"Arial\";")
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuFiles.setFont(font)
        self.menuFiles.setObjectName("menuFiles")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuConfiguration.setFont(font)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuSimulation = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuSimulation.setFont(font)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("font: 75 10pt \"Arial\";")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_Files = QtWidgets.QToolBar(MainWindow)
        self.toolBar_Files.setStyleSheet("")
        self.toolBar_Files.setObjectName("toolBar_Files")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_Files)
        self.toolBar_Input = QtWidgets.QToolBar(MainWindow)
        self.toolBar_Input.setObjectName("toolBar_Input")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_Input)
        self.toolBar_Simulation = QtWidgets.QToolBar(MainWindow)
        self.toolBar_Simulation.setObjectName("toolBar_Simulation")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_Simulation)
        self.toolBar_Analyze = QtWidgets.QToolBar(MainWindow)
        self.toolBar_Analyze.setObjectName("toolBar_Analyze")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_Analyze)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/plunger/icons/add-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon16)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/plunger/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon17)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/plunger/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon18)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon15)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/plunger/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon19)
        self.actionExit.setObjectName("actionExit")
        self.actionWell_Geometry = QtWidgets.QAction(MainWindow)
        self.actionWell_Geometry.setCheckable(False)
        self.actionWell_Geometry.setIcon(icon1)
        self.actionWell_Geometry.setObjectName("actionWell_Geometry")
        self.actionSurface = QtWidgets.QAction(MainWindow)
        self.actionSurface.setIcon(icon2)
        self.actionSurface.setObjectName("actionSurface")
        self.actionFluid_Property = QtWidgets.QAction(MainWindow)
        self.actionFluid_Property.setIcon(icon3)
        self.actionFluid_Property.setObjectName("actionFluid_Property")
        self.actionReservoir_Parameters = QtWidgets.QAction(MainWindow)
        self.actionReservoir_Parameters.setIcon(icon4)
        self.actionReservoir_Parameters.setObjectName("actionReservoir_Parameters")
        self.actionHorizontal_Well_Geometry = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/plunger/icons/icon_unconventional.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHorizontal_Well_Geometry.setIcon(icon20)
        self.actionHorizontal_Well_Geometry.setObjectName("actionHorizontal_Well_Geometry")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setIcon(icon6)
        self.actionRun.setObjectName("actionRun")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName("actionStop")
        self.actionTerminate = QtWidgets.QAction(MainWindow)
        self.actionTerminate.setIcon(icon8)
        self.actionTerminate.setObjectName("actionTerminate")
        self.actionResults = QtWidgets.QAction(MainWindow)
        self.actionResults.setIcon(icon9)
        self.actionResults.setObjectName("actionResults")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setIcon(icon10)
        self.actionOutput.setObjectName("actionOutput")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setIcon(icon13)
        self.actionData.setObjectName("actionData")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        self.actionPlot.setIcon(icon12)
        self.actionPlot.setObjectName("actionPlot")
        self.actionSimulation = QtWidgets.QAction(MainWindow)
        self.actionSimulation.setCheckable(True)
        self.actionSimulation.setChecked(True)
        self.actionSimulation.setObjectName("actionSimulation")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setCheckable(True)
        self.actionInput.setChecked(True)
        self.actionInput.setObjectName("actionInput")
        self.actionFiles = QtWidgets.QAction(MainWindow)
        self.actionFiles.setCheckable(True)
        self.actionFiles.setChecked(True)
        self.actionFiles.setObjectName("actionFiles")
        self.actionAnalyze = QtWidgets.QAction(MainWindow)
        self.actionAnalyze.setCheckable(True)
        self.actionAnalyze.setChecked(True)
        self.actionAnalyze.setObjectName("actionAnalyze")
        self.menuFiles.addAction(self.actionNew)
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.actionDelete)
        self.menuFiles.addAction(self.actionSave)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionExit)
        self.menuConfiguration.addAction(self.actionWell_Geometry)
        self.menuConfiguration.addAction(self.actionSurface)
        self.menuConfiguration.addAction(self.actionFluid_Property)
        self.menuConfiguration.addAction(self.actionReservoir_Parameters)
        self.menuSimulation.addAction(self.actionRun)
        self.menuSimulation.addAction(self.actionStop)
        self.menuSimulation.addAction(self.actionTerminate)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.actionResults)
        self.menuSimulation.addAction(self.actionOutput)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuView.addAction(self.actionFiles)
        self.menuView.addAction(self.actionInput)
        self.menuView.addAction(self.actionSimulation)
        self.menuView.addAction(self.actionAnalyze)
        self.menuAnalyze.addAction(self.actionPlot)
        self.menuAnalyze.addAction(self.actionData)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar_Files.addAction(self.actionNew)
        self.toolBar_Files.addAction(self.actionOpen)
        self.toolBar_Files.addAction(self.actionDelete)
        self.toolBar_Files.addAction(self.actionSave)
        self.toolBar_Files.addAction(self.actionExit)
        self.toolBar_Input.addAction(self.actionWell_Geometry)
        self.toolBar_Input.addAction(self.actionSurface)
        self.toolBar_Input.addAction(self.actionFluid_Property)
        self.toolBar_Input.addAction(self.actionReservoir_Parameters)
        self.toolBar_Simulation.addAction(self.actionRun)
        self.toolBar_Simulation.addAction(self.actionStop)
        self.toolBar_Simulation.addAction(self.actionTerminate)
        self.toolBar_Simulation.addAction(self.actionResults)
        self.toolBar_Simulation.addAction(self.actionOutput)
        self.toolBar_Analyze.addAction(self.actionData)
        self.toolBar_Analyze.addAction(self.actionPlot)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_main.setCurrentIndex(0)
        self.tabWidget_configure.setCurrentIndex(2)
        self.tabWidget_simulation.setCurrentIndex(1)
        self.tabWidget_analyze.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TUALP Transient Plunger Lift Simulator"))
        MainWindow.setStatusTip(_translate("MainWindow", "Tulsa University Artificial Lift Projects Plunger Lift Simulator. Copyright Reserved."))
        self.btnWell.setText(_translate("MainWindow", "Well Geometry"))
        self.btnSurface.setText(_translate("MainWindow", "Surface Information"))
        self.btnFluid.setText(_translate("MainWindow", "Fluid Property"))
        self.btnReservoir.setText(_translate("MainWindow", "Reservoir Parameter"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageConfigure), _translate("MainWindow", "Configuration"))
        self.btnRun.setText(_translate("MainWindow", "Run"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnResults.setText(_translate("MainWindow", "Results"))
        self.btnOutput.setText(_translate("MainWindow", "Output"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageSimulation), _translate("MainWindow", "Simulation"))
        self.btnPlot.setText(_translate("MainWindow", "Plot"))
        self.btnData.setText(_translate("MainWindow", "Data"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageAnalyze), _translate("MainWindow", "Analyze"))
        self.groupBox_vertical.setTitle(_translate("MainWindow", "Vertical Section"))
        self.label_wellName.setText(_translate("MainWindow", "Well name"))
        self.label_wellDepth.setText(_translate("MainWindow", "Well depth (m)"))
        self.label_absoluteRoughness.setText(_translate("MainWindow", "Absolute roughness (m) "))
        self.label_tubingID.setText(_translate("MainWindow", "Tubing ID (m)"))
        self.label_tubingOD.setText(_translate("MainWindow", "Tubing OD (m)"))
        self.label_casingID.setText(_translate("MainWindow", "Casing ID (m)         "))
        self.groupBox_horizontal.setTitle(_translate("MainWindow", "Horizontal Section"))
        self.label_horizontalLength.setText(_translate("MainWindow", "Horizontal length (m)"))
        self.label_inclinationAngle.setText(_translate("MainWindow", "Inclination angle (deg)"))
        self.label_horizontalAngle.setText(_translate("MainWindow", "Inner diameter (m)"))
        self.label_innerDiameter.setText(_translate("MainWindow", "Absolute roughness (m)"))
        self.groupBox_plunger.setTitle(_translate("MainWindow", "Plunger"))
        self.label_plungerWeight.setText(_translate("MainWindow", "Plunger weight (kg)    "))
        self.label_plungerLength.setText(_translate("MainWindow", "Plunger length (m)"))
        self.label_plungerRise.setText(_translate("MainWindow", "Plunger rise [-]"))
        self.label_plungerDiameter.setText(_translate("MainWindow", "Plunger diameter (m)  "))
        self.label_plungerDrag.setText(_translate("MainWindow", "Drag coefficient"))
        self.btn_reset_WG.setText(_translate("MainWindow", "Reset"))
        self.btn_save_WG.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_WG.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget_configure.setTabText(self.tabWidget_configure.indexOf(self.tabWell), _translate("MainWindow", "Well Geometry"))
        self.groupBox_valve.setTitle(_translate("MainWindow", "Motor Valve"))
        self.radioButton_valveCv.setText(_translate("MainWindow", "Valve coefficient"))
        self.label_valveCoeff.setText(_translate("MainWindow", "Valve coefficient (Cv)"))
        self.radioButton_valveFunc.setText(_translate("MainWindow", "Valve function"))
        self.label_tubingID_2.setText(_translate("MainWindow", "Cd"))
        self.label_tubingOD_2.setText(_translate("MainWindow", "Ac"))
        self.label_casingID_2.setText(_translate("MainWindow", "k"))
        self.label_tubingOD_4.setText(_translate("MainWindow", "P1"))
        self.label_tubingOD_5.setText(_translate("MainWindow", "v1"))
        self.label_tubingOD_6.setText(_translate("MainWindow", "gc"))
        self.label_surfaceT.setText(_translate("MainWindow", "Surface temperature (K)"))
        self.groupBox_linePressure.setTitle(_translate("MainWindow", "Line Pressure"))
        self.radioButton_constantPL.setText(_translate("MainWindow", "Constant line pressure"))
        self.label_linePressure.setText(_translate("MainWindow", "Line pressure (Pa)"))
        self.radioButton_varyingT.setText(_translate("MainWindow", "Varying line pressure"))
        self.btn_addRow.setText(_translate("MainWindow", "Add"))
        self.btn_readData.setText(_translate("MainWindow", "Read"))
        self.btn_plotLinepressure.setText(_translate("MainWindow", "Plot"))
        self.table_linePressure.setSortingEnabled(True)
        item = self.table_linePressure.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_linePressure.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_linePressure.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_linePressure.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_linePressure.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_linePressure.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.table_linePressure.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.table_linePressure.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.table_linePressure.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.table_linePressure.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.table_linePressure.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t (s)"))
        item = self.table_linePressure.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pl (Pa)"))
        __sortingEnabled = self.table_linePressure.isSortingEnabled()
        self.table_linePressure.setSortingEnabled(False)
        self.table_linePressure.setSortingEnabled(__sortingEnabled)
        self.btn_reset_SI.setText(_translate("MainWindow", "Reset"))
        self.btn_save_SI.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_SI.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget_configure.setTabText(self.tabWidget_configure.indexOf(self.tabSurface), _translate("MainWindow", "Surface Information"))
        self.groupBox_vertical_2.setTitle(_translate("MainWindow", "Liquid"))
        self.label_denlR.setText(_translate("MainWindow", "Relative density of liquid"))
        self.label_visL.setText(_translate("MainWindow", "Liquid viscosity (Pa.s)"))
        self.groupBox_vertical_3.setTitle(_translate("MainWindow", "Gas"))
        self.label_dengR.setText(_translate("MainWindow", "Relative density of gas"))
        self.btn_reset_FP.setText(_translate("MainWindow", "Reset"))
        self.btn_save_FP.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_FP.setText(_translate("MainWindow", "Cancel"))
        self.radioButton_BlackOil.setText(_translate("MainWindow", "Black oil model"))
        self.radioButton_Compositional.setText(_translate("MainWindow", "Compositional model"))
        self.groupBox_vertical_8.setTitle(_translate("MainWindow", "Mole weight percentage (Mol %)"))
        item = self.tableWidget_Compositional.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "N2"))
        item = self.tableWidget_Compositional.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CO2"))
        item = self.tableWidget_Compositional.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "C1"))
        item = self.tableWidget_Compositional.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "C2"))
        item = self.tableWidget_Compositional.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "C3"))
        item = self.tableWidget_Compositional.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "C4i"))
        item = self.tableWidget_Compositional.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "C4n"))
        item = self.tableWidget_Compositional.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "C5i"))
        item = self.tableWidget_Compositional.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "C5n"))
        item = self.tableWidget_Compositional.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "C6"))
        item = self.tableWidget_Compositional.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "C7plus"))
        item = self.tableWidget_Compositional.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mol %"))
        item = self.tableWidget_Compositional.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pc psia"))
        item = self.tableWidget_Compositional.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tc F"))
        item = self.tableWidget_Compositional.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_Compositional.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mole weight"))
        self.tabWidget_configure.setTabText(self.tabWidget_configure.indexOf(self.tabFluid), _translate("MainWindow", "Fluid Property"))
        self.label_C.setText(_translate("MainWindow", "Cofficient C"))
        self.label_n.setText(_translate("MainWindow", "Exponent n"))
        self.label_Pr_L.setText(_translate("MainWindow", "Reservoir pressure (MPa)"))
        self.label_GLR_L.setText(_translate("MainWindow", "Gas liquid ratio"))
        self.label_Tgr_L.setText(_translate("MainWindow", "Geothermal gradient (K/m)"))
        self.label_Tgr_L_2.setText(_translate("MainWindow", "Gas solubility m3/m3"))
        self.radioButton_backPressure.setText(_translate("MainWindow", "Exponential equation"))
        self.radioButton_reservoirDetails.setText(_translate("MainWindow", "Reservoir model from geometries"))
        self.label_Pr_R.setText(_translate("MainWindow", "Reservoir pressure (MPa)"))
        self.label_mD.setText(_translate("MainWindow", "Gas permeability (mD)"))
        self.label_Hr.setText(_translate("MainWindow", "Reservoir thickness (m)"))
        self.label_Rdrain.setText(_translate("MainWindow", "Drainage radius (m)"))
        self.label_Rwell.setText(_translate("MainWindow", "Well diameter (m)"))
        self.label_Tgr_R.setText(_translate("MainWindow", "Geothermal gradiaent (K/m)"))
        self.label_GLR_R.setText(_translate("MainWindow", "Gas liquid ratio"))
        self.btn_reset_RP.setText(_translate("MainWindow", "Reset"))
        self.btn_save_RP.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_RP.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget_configure.setTabText(self.tabWidget_configure.indexOf(self.tabReservoir), _translate("MainWindow", "Reservoir Parameter"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabConfigure), _translate("MainWindow", "Configuration"))
        self.groupBox_vertical_7.setTitle(_translate("MainWindow", "Iteration"))
        self.label_cycles.setText(_translate("MainWindow", "Plunger lift cycles to be computed"))
        self.label_plungerT.setText(_translate("MainWindow", "Plunger lift period (min)"))
        self.label_valveT.setText(_translate("MainWindow", "Surface valve open time (min)"))
        self.label_dtDown.setText(_translate("MainWindow", "Time step for downward movement (s)"))
        self.label_dtUp.setText(_translate("MainWindow", "Time step for upward movement (s)"))
        self.label_dtH.setText(_translate("MainWindow", "Time step for horizontal section (s)"))
        self.groupBox_vertical_6.setTitle(_translate("MainWindow", "Initialization"))
        self.label_Pc.setText(_translate("MainWindow", "Casing pressure (Pa)"))
        self.label_Pt.setText(_translate("MainWindow", "Tubing pressure (Pa)"))
        self.label_Ltt.setText(_translate("MainWindow", "Liquid height above plunger (m)   "))
        self.label_Ltb.setText(_translate("MainWindow", "Liquid height below plunger (m)   "))
        self.btn_reset_setting.setText(_translate("MainWindow", "Reset"))
        self.btn_save_setting.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_setting.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget_simulation.setTabText(self.tabWidget_simulation.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))
        self.tabWidget_simulation.setTabText(self.tabWidget_simulation.indexOf(self.tabCalculation), _translate("MainWindow", "Calculation"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabSimulation), _translate("MainWindow", "Simulation"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot Selection"))
        self.btn_reset_analyzePlot.setText(_translate("MainWindow", "Reset Calculation"))
        self.btn_save_analyzePlot.setText(_translate("MainWindow", "Save Plot"))
        self.tabWidget_analyze.setTabText(self.tabWidget_analyze.indexOf(self.tabPlot), _translate("MainWindow", "Plot"))
        self.gbx_output.setToolTip(_translate("MainWindow", "Display the calculation data in tables"))
        self.gbx_output.setStatusTip(_translate("MainWindow", "Display the calculation data in tables"))
        self.gbx_output.setTitle(_translate("MainWindow", "Data Output"))
        self.btn_reset_analyzeData.setText(_translate("MainWindow", "Reset Calculation"))
        self.btn_save_analyzeData.setText(_translate("MainWindow", "Save Data"))
        self.tabWidget_analyze.setTabText(self.tabWidget_analyze.indexOf(self.tabData), _translate("MainWindow", "Data"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tabAnalyze), _translate("MainWindow", "Analyze"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.menuSimulation.setTitle(_translate("MainWindow", "Simulation"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.toolBar_Files.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_Input.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_Simulation.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar_Analyze.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New case"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open an existing case"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete an existing case"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save the current case"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit the simulator"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionWell_Geometry.setText(_translate("MainWindow", "Well Geometry"))
        self.actionWell_Geometry.setToolTip(_translate("MainWindow", "Well Geometry Input"))
        self.actionWell_Geometry.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSurface.setText(_translate("MainWindow", "Surface Information"))
        self.actionSurface.setToolTip(_translate("MainWindow", "Surface Information Input"))
        self.actionSurface.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionFluid_Property.setText(_translate("MainWindow", "Fluid Property"))
        self.actionFluid_Property.setToolTip(_translate("MainWindow", "Fluid Property Input"))
        self.actionFluid_Property.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionReservoir_Parameters.setText(_translate("MainWindow", "Reservoir Parameters"))
        self.actionReservoir_Parameters.setToolTip(_translate("MainWindow", "Reservoir Parameters Input"))
        self.actionReservoir_Parameters.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHorizontal_Well_Geometry.setText(_translate("MainWindow", "Horizontal Well Geometry"))
        self.actionHorizontal_Well_Geometry.setToolTip(_translate("MainWindow", "Horizontal Well Geometry Input"))
        self.actionHorizontal_Well_Geometry.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop current simulation"))
        self.actionStop.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionTerminate.setText(_translate("MainWindow", "Reset"))
        self.actionTerminate.setToolTip(_translate("MainWindow", "Reset everything for a new simulation"))
        self.actionResults.setText(_translate("MainWindow", "Results"))
        self.actionResults.setToolTip(_translate("MainWindow", "Show results"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionOutput.setToolTip(_translate("MainWindow", "Output the simulation results"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionPlot.setText(_translate("MainWindow", "Plot"))
        self.actionSimulation.setText(_translate("MainWindow", "Simulation"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionFiles.setText(_translate("MainWindow", "Files"))
        self.actionFiles.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionAnalyze.setText(_translate("MainWindow", "Analyze"))
import plunger_ico_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
