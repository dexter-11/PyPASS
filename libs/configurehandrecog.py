#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
from createmaster import *
from hand_gesture_recog.hand_gesture_detection import *
#######################################################
class Ui_ConfigGestures(object):
    def setupUi(self, ConfigGestures):
        ConfigGestures.setObjectName("ConfigGestures")
        ConfigGestures.resize(480, 360)
        ConfigGestures.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigGestures.sizePolicy().hasHeightForWidth())
        ConfigGestures.setSizePolicy(sizePolicy)
        ConfigGestures.setMinimumSize(QtCore.QSize(480, 360))
        ConfigGestures.setMaximumSize(QtCore.QSize(480, 360))
        ConfigGestures.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.label = QtWidgets.QLabel(ConfigGestures)
        self.label.setGeometry(QtCore.QRect(60, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(189,147,249);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_msg = QtWidgets.QLabel(ConfigGestures)
        self.label_msg.setGeometry(QtCore.QRect(40, 250, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_msg.setFont(font)
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")
        self.label_question = QtWidgets.QLabel(ConfigGestures)
        self.label_question.setGeometry(QtCore.QRect(101, 60, 291, 16))
        self.label_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question.setObjectName("label_question")
        # Radio button for yes
        self.radioButton_yes = QtWidgets.QRadioButton(ConfigGestures)
        self.radioButton_yes.setGeometry(QtCore.QRect(200, 80, 55, 20))   
        # Radio button for no
        self.radioButton_no = QtWidgets.QRadioButton(ConfigGestures)
        self.radioButton_no.setGeometry(QtCore.QRect(260, 80, 55, 20))

        self.label_g1 = QtWidgets.QLabel(ConfigGestures)
        self.label_g1.setGeometry(QtCore.QRect(60, 130, 71, 21))
        font.setPointSize(12)
        self.label_g1.setFont(font)
        self.label_g1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_g1.setObjectName("label_g1")
        self.comboGesture1 = QtWidgets.QComboBox(ConfigGestures)
        self.comboGesture1.setGeometry(QtCore.QRect(150, 125, 111, 31))
        self.comboGesture1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboGesture1.setObjectName("comboGesture1")
        self.label_g2 = QtWidgets.QLabel(ConfigGestures)
        self.label_g2.setGeometry(QtCore.QRect(60, 170, 71, 21))
        self.label_g2.setFont(font)
        self.label_g2.setObjectName("label_g2")
        self.comboGesture2 = QtWidgets.QComboBox(ConfigGestures)
        self.comboGesture2.setGeometry(QtCore.QRect(150, 165, 111, 31))
        self.comboGesture2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboGesture2.setObjectName("comboGesture2")
        self.label_g3 = QtWidgets.QLabel(ConfigGestures)
        self.label_g3.setGeometry(QtCore.QRect(60, 210, 71, 21))
        self.label_g3.setFont(font)
        self.label_g3.setObjectName("label_g3")
        self.comboGesture3 = QtWidgets.QComboBox(ConfigGestures)
        self.comboGesture3.setGeometry(QtCore.QRect(150, 205, 111, 31))
        self.comboGesture3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboGesture3.setObjectName("comboGesture3")
        self.label_trycam = QtWidgets.QLabel(ConfigGestures)
        self.label_trycam.setGeometry(QtCore.QRect(332, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_trycam.setFont(font)
        self.label_trycam.setObjectName("label_trycam")
        self.pushButtonTry = QtWidgets.QPushButton(ConfigGestures)
        self.pushButtonTry.setGeometry(QtCore.QRect(320, 170, 101, 21))
        font.setPointSize(8)
        self.pushButtonTry.setFont(font)
        self.pushButtonTry.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonTry.setStyleSheet(u"background:rgb(50, 54, 62);color: white;")
        self.pushButtonTry.setObjectName("pushButtonTry")
        self.label_trycam_quit = QtWidgets.QLabel(ConfigGestures)
        self.label_trycam_quit.setGeometry(QtCore.QRect(310, 195, 135, 31))
        font.setPointSize(7)
        self.label_trycam_quit.setFont(font)
        self.label_trycam_quit.setStyleSheet("font-weight: bold")
        self.label_trycam_quit.setObjectName("label_trycam_quit")
        self.pushButtonOk = QtWidgets.QPushButton(ConfigGestures)
        self.pushButtonOk.setGeometry(QtCore.QRect(360, 300, 81, 32))
        self.pushButtonOk.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonOk.setStyleSheet(u"background:rgb(248,248,255);color: black;")
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.label_msg.raise_()
        self.pushButtonOk.raise_()
        self.pushButtonTry.raise_()

        self.retranslateUi(ConfigGestures)
        QtCore.QMetaObject.connectSlotsByName(ConfigGestures)
        
        self.pushButtonOk.clicked.connect(self.accept)
        self.pushButtonTry.clicked.connect(self.trygestures)
        self.radioButton_yes.toggled.connect(self.option_yes)
        self.radioButton_no.toggled.connect(self.option_no)

        ### SET GESTURE OPTIONS
        self.comboGesture1.addItems(optgest)
        self.comboGesture2.addItems(optgest)   
        self.comboGesture3.addItems(optgest)
        
        ### START 
        self.runconfig_gestures()

    def retranslateUi(self, ConfigGestures):
        _translate = QtCore.QCoreApplication.translate
        ConfigGestures.setWindowTitle(_translate("ConfigGestures", "PyPASS - Gesture Configuration"))
        self.label.setText(_translate("ConfigGestures", CGWT))
        self.label_question.setText(_translate("ConfigGestures", CGRQ))
        self.radioButton_yes.setText(_translate("MainWindow", "Yes"))
        self.radioButton_no.setText(_translate("MainWindow", "No"))
        self.label_g1.setText(_translate("ConfigGestures", CGGF))
        self.label_g2.setText(_translate("ConfigGestures", CGGS))
        self.label_g3.setText(_translate("ConfigGestures", CGGT))
        self.label_trycam.setText(_translate("ConfigGestures", CGTC))
        self.label_trycam_quit.setText(_translate("ConfigGestures", CGCM))
        self.pushButtonTry.setText(_translate("ConfigGestures", CGOC))
        self.pushButtonOk.setText(_translate("ConfigGestures", CGSV))

    def option_yes(self, selected):
        global ConfigGestures_loginoption_selected
        if selected:
            ConfigGestures_loginoption_selected = True
            return None
             
    def option_no(self, selected):
        global ConfigGestures_loginoption_selected
        if selected:
            ConfigGestures_loginoption_selected = False
            return None

    def trygestures(self):
        only_try_handGesture()
 
    ### Load Config vars
    def runconfig_gestures(self):
        #core.sessioncheck()
        f = open("./libs/configfile.py","r")     
        gestureshere1 = f.read()
        result = [x.strip() for x in gestureshere1.split('\n')]
        #set_gesture1 = result[12]; set_gesture1 = set_gesture1.replace('"', '', 2); set_gesture1 = [x.strip() for x in set_gesture1.split('=')]
        set_gesture1 = result[13]; set_gesture1 = set_gesture1.replace('"', '', 2); set_gesture1 = [x.strip() for x in set_gesture1.split('=')]
        set_gesture2 = result[14]; set_gesture2 = set_gesture2.replace('"', '', 2); set_gesture2 = [x.strip() for x in set_gesture2.split('=')]
        set_gesture3 = result[15]; set_gesture3 = set_gesture3.replace('"', '', 2); set_gesture3 = [x.strip() for x in set_gesture3.split('=')]
        
        #self.usegest.setCurrentText(encoding[12])
        self.comboGesture1.setCurrentText(set_gesture1[1])
        self.comboGesture2.setCurrentText(set_gesture2[1])
        self.comboGesture3.setCurrentText(set_gesture3[1])
        f.close()
        return None
        
    ### LOAD THE FILE AND THE CONFIG GESTURE VARS
    def accept(self):

        f = open("./libs/configfile.py","rt")        
        gestureshere = f.read()
        result = [x.strip() for x in gestureshere.split('\n')]
        #usegest = result[13]; usegest = [x.strip() for x in usegest.split('=')]
        set_gesture1 = result[13]; set_gesture1 = [x.strip() for x in set_gesture1.split('=')]
        set_gesture2 = result[14]; set_gesture2 = [x.strip() for x in set_gesture2.split('=')]
        set_gesture3 = result[15]; set_gesture3 = [x.strip() for x in set_gesture3.split('=')]
        set_option = result[12]; set_option = [x.strip() for x in set_option.split('=')]

        #usegestN = self.lineTimeout.text()
        set_gesture1N = '"' + self.comboGesture1.currentText() + '"'
        set_gesture2N = '"' + self.comboGesture2.currentText() + '"'
        set_gesture3N = '"' + self.comboGesture3.currentText() + '"'
        set_optionN = ConfigGestures_loginoption_selected
        f.close()
        #options = options.replace(bool(usegest[1]),bool(usegestN))
        result[12] = result[12].replace(str(set_option[1]),str(set_optionN))
        result[13] = result[13].replace(str(set_gesture1[1]),str(set_gesture1N))
        result[14] = result[14].replace(str(set_gesture2[1]),str(set_gesture2N))
        result[15] = result[15].replace(str(set_gesture3[1]),str(set_gesture3N))
        
        f = open("./libs/configfile.py","wt")         
        f.write('\n'.join(result))
        f.close()
        return None
