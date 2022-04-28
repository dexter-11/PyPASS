#FINAL

####### PyPASS Version 1.0.0 ####
import sys
from onetimepass import valid_totp
sys.path.append("./libs/")
from core import *
from createmaster import *
from mainmenu import *
from hand_gesture_recog.hand_gesture_detection import *
from configfile import *
from finaldev2fa import *

#######################################################
def checkOTP(data):
    global secret
    is_valid = valid_totp(token=data, secret=secret)
    if is_valid: return True
#######################################################
class Ui_loginmenu(object):       
    def setupUi2(self, loginmenu):
        loginmenu.setObjectName("loginmenu")
        loginmenu.resize(480, 260)
        loginmenu.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginmenu.sizePolicy().hasHeightForWidth())
        loginmenu.setSizePolicy(sizePolicy)
        loginmenu.setMaximumSize(QtCore.QSize(480, 320))    # Resize - Increase
        loginmenu.setAcceptDrops(True)
        self.username = QtWidgets.QLineEdit(loginmenu)
        self.username.setGeometry(QtCore.QRect(200, 80, 141, 21))
        self.username.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(loginmenu)
        self.password.setGeometry(QtCore.QRect(200, 110, 141, 21))
        self.password.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(loginmenu)
        self.label.setGeometry(QtCore.QRect(120, 80, 71, 21))        # 60, 50, 71, 21
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginmenu)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_ok = QtWidgets.QPushButton(loginmenu)
        self.pushButton_ok.setGeometry(QtCore.QRect(200, 180, 101, 41))
        self.pushButton_ok.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_ok.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.msgdialog = QtWidgets.QLabel(loginmenu)
        self.msgdialog.setGeometry(QtCore.QRect(90, 150, 321, 16))
        self.msgdialog.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog.setStyleSheet(u"color:rgb(192,64,0);")
        self.msgdialog.setObjectName("msgdialog")
        self.msgdialog_2 = QtWidgets.QLabel(loginmenu)
        self.msgdialog_2.setGeometry(QtCore.QRect(75, 25, 351, 31))     # 25, 10, 321, 31
        font = QtGui.QFont()
        font.setPointSize(18)
        self.msgdialog_2.setFont(font)
        self.msgdialog_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog_2.setObjectName("msgdialog_2")

        self.label_2fa = QtWidgets.QPushButton(loginmenu)
        self.label_2fa.setGeometry(QtCore.QRect(200, 230, 101, 21))
        self.label_2fa.setFocusPolicy(QtCore.Qt.WheelFocus)
        font.setPointSize(8)
        self.label_2fa.setFont(font)
        self.label_2fa.setCheckable(True)
        self.label_2fa.setStyleSheet(u"text-decoration: underline;")
        self.label_2fa.setObjectName("label_2fa")
        self.otp_auth = QtWidgets.QLineEdit(loginmenu)
        self.otp_auth.setGeometry(QtCore.QRect(230, 265, 111, 21))
        self.otp_auth.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.otp_auth.setStyleSheet("border: 0.5px solid black;")
        self.otp_auth.setObjectName("otp_auth")
        self.label_enterOtp = QtWidgets.QLabel(loginmenu)
        self.label_enterOtp.setGeometry(QtCore.QRect(120, 265, 101, 21))        # 60, 50, 71, 21
        self.label_enterOtp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enterOtp.setObjectName("label_enterOtp")

        self.retranslateUi2(loginmenu)
        QtCore.QMetaObject.connectSlotsByName(loginmenu)
        
        ### Action Buttons
        self.pushButton_ok.clicked.connect(self.checkLogin)
        self.label_2fa.clicked.connect(self._expandWindow)    

    def setupUi(self, loginmenu):
        loginmenu.setObjectName("loginmenu")
        loginmenu.resize(480, 360)
        loginmenu.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginmenu.sizePolicy().hasHeightForWidth())
        loginmenu.setSizePolicy(sizePolicy)
        loginmenu.setMaximumSize(QtCore.QSize(480, 560))    # Resize - Increase
        loginmenu.setAcceptDrops(True)
        self.username = QtWidgets.QLineEdit(loginmenu)
        self.username.setGeometry(QtCore.QRect(201, 90, 135, 21))
        self.username.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(loginmenu)
        self.password.setGeometry(QtCore.QRect(201, 120, 135, 21))
        self.password.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(loginmenu)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(loginmenu)
        self.label.setGeometry(QtCore.QRect(120, 90, 71, 21))        # 60, 50, 71, 21
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_g = QtWidgets.QLabel(loginmenu)
        self.label_g.setGeometry(QtCore.QRect(121, 155, 231, 31))
        font.setPointSize(10)
        self.label_g.setFont(font)
        self.label_g.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_g.setStyleSheet("background-color:rgb(189,147,249);")  #border: 0.5px solid black;
        self.label_g.setObjectName("label_2")
        self.label_click = QtWidgets.QLabel(loginmenu)
        self.label_click.setGeometry(QtCore.QRect(134, 190, 131, 31))
        font.setPointSize(9)
        self.label_click.setFont(font)
        self.label_click.setObjectName("label_2")
        #Authtication 3 buttons
        self.pushButton_clickg1 = QtWidgets.QPushButton(loginmenu)
        self.pushButton_clickg1.setGeometry(QtCore.QRect(260, 199, 15, 15))
        self.pushButton_clickg1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_clickg1.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_clickg1.setText("")
        self.pushButton_clickg1.setObjectName("pushButton_clickg1")
        self.pushButton_clickg2 = QtWidgets.QPushButton(loginmenu)
        self.pushButton_clickg2.setGeometry(QtCore.QRect(290, 199, 15, 15))
        self.pushButton_clickg2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_clickg2.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_clickg2.setText("")
        self.pushButton_clickg2.setObjectName("pushButton_clickg2")
        self.pushButton_clickg3 = QtWidgets.QPushButton(loginmenu)
        self.pushButton_clickg3.setGeometry(QtCore.QRect(320, 199, 15, 15))
        self.pushButton_clickg3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_clickg3.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_clickg3.setText("")
        self.pushButton_clickg3.setObjectName("pushButton_clickg3")

        self.pushButton_ok = QtWidgets.QPushButton(loginmenu)
        self.pushButton_ok.setGeometry(QtCore.QRect(195, 285, 101, 41))
        self.pushButton_ok.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_ok.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.msgdialog = QtWidgets.QLabel(loginmenu)
        self.msgdialog.setGeometry(QtCore.QRect(85, 255, 321, 16))
        self.msgdialog.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog.setObjectName("msgdialog")
        self.msgdialog.setStyleSheet(u"color:rgb(192,64,0);")

        self.msgdialog_2 = QtWidgets.QLabel(loginmenu)
        self.msgdialog_2.setGeometry(QtCore.QRect(75, 25, 351, 31))     # 25, 10, 321, 31
        font = QtGui.QFont()
        font.setPointSize(20)
        self.msgdialog_2.setFont(font)
        self.msgdialog_2.setStyleSheet("font-weight: bold")
        self.msgdialog_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog_2.setObjectName("msgdialog_2")
        self.label_camquit = QtWidgets.QLabel(loginmenu)
        self.label_camquit.setGeometry(QtCore.QRect(130, 225, 321, 16))        # 60, 50, 71, 21
        font.setPointSize(8)
        self.label_camquit.setFont(font)
        self.label_camquit.setStyleSheet(u"color:rgb(255,140,0);")  #font-weight: bold;
        self.label_camquit.setObjectName("label_camquit")  

        self.retranslateUi(loginmenu)
        QtCore.QMetaObject.connectSlotsByName(loginmenu)
        
        ### Action Buttons
        self.pushButton_ok.clicked.connect(self.checkLogin)
        self.pushButton_clickg1.clicked.connect(self.checkGesture1)
        self.pushButton_clickg2.clicked.connect(self.checkGesture2)
        self.pushButton_clickg3.clicked.connect(self.checkGesture3)

    def retranslateUi2(self, loginmenu):
        _translate = QtCore.QCoreApplication.translate
        loginmenu.setWindowTitle(_translate("loginmenu", LWTE))
        self.label.setText(_translate("loginmenu", LUSR))
        self.label_2.setText(_translate("loginmenu", LPWD))
        self.pushButton_ok.setText(_translate("loginmenu", LBOK))
        self.msgdialog.setText(_translate("loginmenu", LFUP))
        self.msgdialog_2.setText(_translate("loginmenu", LMSG))
        self.label_2fa.setText(_translate("loginmenu", LM2F))
        self.label_enterOtp.setText(_translate("loginmenu", LMEO))

    def retranslateUi(self, loginmenu):
        _translate = QtCore.QCoreApplication.translate
        loginmenu.setWindowTitle(_translate("loginmenu", LWTE))
        self.label.setText(_translate("loginmenu", LUSR))
        self.label_2.setText(_translate("loginmenu", LPWD))
        self.label_g.setText(_translate("loginmenu", LMGE))
        self.pushButton_ok.setText(_translate("loginmenu", LBOK))
        self.label_click.setText(_translate("loginmenu", LMCA))
        self.label_camquit.setText(_translate("loginmenu", LMQC))
        self.msgdialog_2.setText(_translate("loginmenu", LMSG))
        
    def closeEvent(self, event):        
        try:            
            f = open(sessiontmp,"r")
            pass
        except:
            core.exit_now('','')

    # Expand/Contract on-click
    def _expandWindow(self, loginmenu):
        if self.label_2fa.isChecked():
            self.resize(480,300)
        else:
            self.resize(480,260)
            
    ### Check first gesture    
    def checkGesture1(self, loginmenu):
        global correctGest_count
        temp_gest1 = detect_handGesture()
        if temp_gest1.lower() == set_gesture1.lower():
            self.pushButton_clickg1.setStyleSheet(u"background:rgb(34,139,34);color: white;")
            correctGest_count = correctGest_count+1
        else:
            self.msgdialog.setText(LMGF)
            self.repaint()
        return None

    ### Check second gesture    
    def checkGesture2(self, loginmenu):
        global correctGest_count
        temp_gest2 = detect_handGesture()
        if temp_gest2.lower() == set_gesture2.lower():
            self.pushButton_clickg2.setStyleSheet(u"background:rgb(34,139,34);color: white;")
            correctGest_count = correctGest_count+1
        else:
            self.msgdialog.setText(LMGS)
            self.repaint()
        return None

    ### Check third gesture    
    def checkGesture3(self, loginmenu):
        global correctGest_count
        temp_gest3 = detect_handGesture()
        if temp_gest3.lower() == set_gesture3.lower():
            self.pushButton_clickg3.setStyleSheet(u"background:rgb(34,139,34);color: white;")
            correctGest_count = correctGest_count+1
        else:
            self.msgdialog.setText(LMGT)
            self.repaint()
        return None

    ### Check Login function    
    def checkLogin(self, loginmenu):
        global correctGest_count
        global otp
        username = self.username.text()
        password = self.password.text()     
        if not username:
            self.msgdialog.setText(LUCE)
            self.repaint()
            return False
        if useGesture_for_login == False:
            otp = self.otp_auth.text()
            if not password:
                self.msgdialog.setText(LPCE)
                self.repaint()
                return False  
            if not otp:
                self.msgdialog.setText(LPOT)
                self.repaint()
                return False 
        try:
            ### DECRYPT FILE
            keyfile = core.decrypt(password)        
            pyAesCrypt.decryptFile(filename, filetemp, keyfile, bufferSize)
            df = pd.read_csv(filetemp, index_col=0, header=0, nrows=1)
            # Here, User+Pass+Gesture
            if useGesture_for_login == True:
                ### Check if username exist
                if username in df['Username'][0]:
                    ### Check password
                    check = core.verify_password(df['Password'][0], password)            
                    if ((check is True) and (correctGest_count == 3)):  
                        if (username in df['Username'][0]):
                            self.msgdialog.setText(LOMM)
                            self.repaint()
                            correctGest_count = 0
                            session = core.session()
                            token = session[0]
                            timestamp = session[1]
                            self.switch_window.emit()
                else:
                    self.msgdialog.setText(LMAF)
                    self.repaint()
                    return False
            # Here, User+Pass+2FA
            if useGesture_for_login == False: 
                    ### Check password
                    check = core.verify_password(df['Password'][0], password)            
                    if (len(otp) == 6) and (checkOTP(otp) == True):
                        if (check is True) and username in df['Username'][0]:  
                            self.msgdialog.setText(LOMM)
                            self.repaint()
                            session = core.session()
                            token = session[0]
                            timestamp = session[1]
                            self.switch_window.emit()
                        else:
                            self.msgdialog.setText(LMAF)
                            self.repaint()
                            return False
                    else:
                        msg1 = QtWidgets.QMessageBox()
                        msg1.setWindowTitle("Not Verified")
                        msg1.setIcon(QMessageBox.Information)
                        msg1.setStyleSheet(u"QLabel{min-width: 110 px; min-height: 50px; font-size: 16px; font-weight: bold; color:rgb(192,64,0);}")
                        msg1.setText("Wrong OTP")
                        msg1.setDefaultButton(QMessageBox.Close)
                        x = msg1.exec_()
            else:
                self.msgdialog.setText(LMSI)       
                self.repaint()
                return False
        except:
            self.msgdialog.setText(LMAF)
            self.repaint()
            return False
        return None