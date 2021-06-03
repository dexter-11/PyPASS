#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
from createmaster import *
from mainmenu import *
#######################################################
class Ui_loginmenu(object):       
    def setupUi(self, loginmenu):
        loginmenu.setObjectName("loginmenu")
        loginmenu.resize(480, 260)
        loginmenu.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginmenu.sizePolicy().hasHeightForWidth())
        loginmenu.setSizePolicy(sizePolicy)
        loginmenu.setMaximumSize(QtCore.QSize(480, 260))    # Resize - Increase
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
        self.pushButton_ok.setGeometry(QtCore.QRect(200, 150, 101, 41))
        self.pushButton_ok.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_ok.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.msgdialog = QtWidgets.QLabel(loginmenu)
        self.msgdialog.setGeometry(QtCore.QRect(90, 210, 321, 16))
        self.msgdialog.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog.setObjectName("msgdialog")
        self.msgdialog_2 = QtWidgets.QLabel(loginmenu)
        self.msgdialog_2.setGeometry(QtCore.QRect(75, 25, 351, 31))     # 25, 10, 321, 31
        font = QtGui.QFont()
        font.setPointSize(18)
        self.msgdialog_2.setFont(font)
        self.msgdialog_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdialog_2.setObjectName("msgdialog_2")
        self.retranslateUi(loginmenu)
        QtCore.QMetaObject.connectSlotsByName(loginmenu)
        
        ### Action Buttons
        self.pushButton_ok.clicked.connect(self.checkLogin)        
    def retranslateUi(self, loginmenu):
        _translate = QtCore.QCoreApplication.translate
        loginmenu.setWindowTitle(_translate("loginmenu", LWTE))
        self.label.setText(_translate("loginmenu", LUSR))
        self.label_2.setText(_translate("loginmenu", LPWD))
        self.pushButton_ok.setText(_translate("loginmenu", LBOK))
        self.msgdialog.setText(_translate("loginmenu", LFUP))
        self.msgdialog_2.setText(_translate("loginmenu", LMSG))
        
    def closeEvent(self, event):        
        try:            
            f = open(sessiontmp,"r")
            pass
        except:
            core.exit_now('','')

    ### Check Login function    
    def checkLogin(self, loginmenu):
        username = self.username.text()
        password = self.password.text()        
        if not username:
            self.msgdialog.setText(LUCE)
            self.repaint()
            return False
        if not password:
            self.msgdialog.setText(LPCE)
            self.repaint()
            return False        
        try:
            ### DECRYPT FILE
            keyfile = core.decrypt(password)        
            pyAesCrypt.decryptFile(filename, filetemp, keyfile, bufferSize)
            df = pd.read_csv(filetemp, index_col=0, header=0, nrows=1)
            ### Check if username exist
            if username in df['Username'][0]:
                if not password:
                    self.msgdialog.setText(LPCE)
                    self.repaint()
                    return False
                ### Check password
                check = core.verify_password(df['Password'][0], password)            
                if check is True and username in df['Username'][0]:
                    self.msgdialog.setText(LOMM)
                    self.repaint()
                    session = core.session()
                    token = session[0]
                    timestamp = session[1]
                    self.switch_window.emit()
                else:
                    self.msgdialog.setText(LMPW)
                    self.repaint()
                    return False
            else:
                self.msgdialog.setText(LMPW)       
                self.repaint()
                return False
        except:
            self.msgdialog.setText(LMPW)
            self.repaint()
            return False
        return None