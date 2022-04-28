#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
from configurehandrecog import Ui_ConfigGestures
from finaldev2fa import Ui_otpwindow
#######################################################
class Ui_createmaster(object):
    def setupUi(self, createmaster):
        createmaster.setObjectName("createmaster")
        createmaster.resize(640, 480)       #RESIZED - Increase
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createmaster.sizePolicy().hasHeightForWidth())
        createmaster.setSizePolicy(sizePolicy)
        createmaster.setMaximumSize(QtCore.QSize(640, 480))
        createmaster.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label = QtWidgets.QLabel(createmaster)
        self.label.setStyleSheet("font-weight: bold")
        self.label.setGeometry(QtCore.QRect(90, 60, 451, 51))    #50, 0, 251, 41
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(createmaster)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 151, 41))      #20, 120, 81, 41
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createmaster)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 151, 41))    
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(createmaster)
        self.label_5.setGeometry(QtCore.QRect(70, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_Msg = QtWidgets.QLabel(createmaster)
        self.label_Msg.setGeometry(QtCore.QRect(0, 400, 351, 41))
        self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Msg.setFont(font)
        self.label_Msg.setText("")
        self.label_Msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Msg.setObjectName("label_Msg")
        self.lineUsername = QtWidgets.QLineEdit(createmaster)
        self.lineUsername.setGeometry(QtCore.QRect(230, 145, 261, 30))      # (Left_Indent, Top_Indent, Length, Width)
        self.lineUsername.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineUsername.setFrame(False)
        self.lineUsername.setObjectName("lineUsername")
        self.linePassword = QtWidgets.QLineEdit(createmaster)
        self.linePassword.setGeometry(QtCore.QRect(230, 185, 261, 30))
        self.linePassword.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.linePassword.setFrame(False)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePassword.setObjectName("linePassword")
        self.lineRePass = QtWidgets.QLineEdit(createmaster)
        self.lineRePass.setGeometry(QtCore.QRect(230, 225, 261, 30))
        self.lineRePass.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineRePass.setFrame(False)
        self.lineRePass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineRePass.setObjectName("lineRePass")
        
        #New button - Save Gestures
        self.pushRecog = QtWidgets.QPushButton(createmaster, clicked = lambda: self.gestures())
        self.pushRecog.setGeometry(QtCore.QRect(230, 275, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushRecog.setFont(font)
        self.pushRecog.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushRecog.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushRecog.setObjectName("pushRecog")
        self.pushRecog.raise_()
        #New button - OTP
        self.pushOtp = QtWidgets.QPushButton(createmaster, clicked = lambda: self.otp_window())
        self.pushOtp.setGeometry(QtCore.QRect(230, 320, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushOtp.setFont(font)
        self.pushOtp.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushOtp.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushOtp.setObjectName("pushOtp")
        self.pushOtp.raise_()

        #New button - Check password strength
        self.pushCheck = QtWidgets.QPushButton(createmaster)
        self.pushCheck.setGeometry(QtCore.QRect(500, 185, 91, 30)) 
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushCheck.setFont(font)
        self.pushCheck.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushCheck.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushCheck.setObjectName("pushCheck")
        self.pushCheck.raise_()

        self.pushSave = QtWidgets.QPushButton(createmaster)
        self.pushSave.setGeometry(QtCore.QRect(480, 400, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushSave.setFont(font)
        self.pushSave.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushSave.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushSave.setObjectName("pushSave")
        self.pushSave.raise_()

        self.retranslateUi(createmaster)
        QtCore.QMetaObject.connectSlotsByName(createmaster)
 
        ### Action Buttons
        self.pushSave.clicked.connect(self.masterpassword)
        #self.pushRecog.clicked.connect(self.gestures)
        self.pushCheck.clicked.connect(self.checkpassword)
        
    def retranslateUi(self, createmaster):
        _translate = QtCore.QCoreApplication.translate
        createmaster.setWindowTitle(_translate("createmaster", CWTE))
        self.label.setText(_translate("createmaster", CCMP))
        self.label_3.setText(_translate("createmaster", LUSR))
        self.label_4.setText(_translate("createmaster", LPWD))
        self.label_5.setText(_translate("createmaster", CMRB))
        self.pushSave.setText(_translate("createmaster", CMSP))
        self.pushRecog.setText(_translate("createmaster", CMRH))
        self.pushCheck.setText(_translate("createmaster", CPCP))
        self.pushOtp.setText(_translate("createmaster", CPOT))

    ### Prevent Segment error 11
    def closeEvent(self, event):        
        try:            
            f = open(sessiontmp,"r")
            pass
        except:
            core.exit_now('','')

    ### Check passsword strength
    def checkpassword(self):        
        try:            
            check_password = self.linePassword.text()
            n = len(check_password)
            # Checking chars in string
            hasLower = False
            hasUpper = False
            hasDigit = False
            specialChar = False
            normalChars = "abcdefghijklmnopqrstu"
            "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
            
            for i in range(n):
                if check_password[i].islower():
                    hasLower = True
                if check_password[i].isupper():
                    hasUpper = True
                if check_password[i].isdigit():
                    hasDigit = True
                if check_password[i] not in normalChars:
                    specialChar = True
            # Check empty
            if check_password == '':
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(CPIE)
                self.repaint()
                return False
            # Strength of password
            if (hasLower and hasUpper and
                hasDigit and specialChar and n >= 8):
                self.label_Msg.setStyleSheet(u"color:rgb(34,139,34);") #Green
                self.label_Msg.setText(CPIS)
                self.repaint()
                return False
            elif ((hasLower or hasUpper) and
                specialChar and n >= 6):
                self.label_Msg.setStyleSheet(u"color:rgb(255,140,0);") #Yellow
                self.label_Msg.setText(CPIM)
                self.repaint()
                return False
            else:
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(CPIW)
                self.repaint()
                return False
        except:
            return None
            
    ### Create the first username and password to encrypt the file
    def masterpassword(self):
        df = pd.DataFrame()
        if (df.empty):
            date = core.now()
            ndate = "{}-{}-{}".format(date[3],date[2], date[1])
            username = self.lineUsername.text()
            password = self.linePassword.text()
            repass = self.lineRePass.text()
            if username == '':
                #self.label_Msg.setText(test_call6699())  CHECKING Code import
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(LUCE)
                self.repaint()
                return False
            if password == '':
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(LPCE)
                self.repaint()
                return False
            if repass == '':
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(CRPE)
                self.repaint()
                return False                
            if repass != password:
                self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") #Red
                self.label_Msg.setText(CPNS)
                self.repaint()
                return False  
            ### CREATE ENC KEY for FILE AND HASH
            encMaster = core.encryptMaster(password)
            keyfile = encMaster[0]
            p = encMaster[1]
            ### Create the dataframe to save
            df = pd.DataFrame(columns=['ID', 'Project', 'Username', 'Password','Notes', 'Date'])
            df.loc[0] = ['0', 'master', username, p, 'MASTER KEY', ndate]
            try:
                with open(filetemp, 'w') as f:
                    df.to_csv(f,sep=',', encoding=encoding,index=False)
                    f.close()
            except:
                with open(filetemp, 'x') as f:
                    df.to_csv(f,sep=',', encoding=encoding,index=False)
                    f.close()
            ### Save Encrypted file           
            pyAesCrypt.encryptFile(filetemp, filename, keyfile, bufferSize)
            self.switch_window.emit()
            return None
        else:
            return core.exit_now('','')
        return None

    ### Open the Configure gesture authentication dialogbox
    def gestures(self):
        self.sub_window = QtWidgets.QMainWindow()
        self.ui = Ui_ConfigGestures()
        self.ui.setupUi(self.sub_window)
        self.sub_window.show()

    def otp_window(self):
        self.sub_OTPwindow = QtWidgets.QMainWindow()
        self.ui_otp = Ui_otpwindow()
        self.ui_otp.auth_window(self.sub_OTPwindow)
        self.sub_OTPwindow.show()