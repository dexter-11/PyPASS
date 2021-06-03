#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
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
        self.label.setGeometry(QtCore.QRect(90, 60, 451, 51))    #50, 0, 251, 41
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(createmaster)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 151, 41))      #20, 120, 81, 41
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createmaster)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 151, 41))    
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(createmaster)
        self.label_5.setGeometry(QtCore.QRect(90, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_Msg = QtWidgets.QLabel(createmaster)
        self.label_Msg.setGeometry(QtCore.QRect(0, 40, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Msg.setFont(font)
        self.label_Msg.setText("")
        self.label_Msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Msg.setObjectName("label_Msg")
        self.lineUsername = QtWidgets.QLineEdit(createmaster)
        self.lineUsername.setGeometry(QtCore.QRect(250, 145, 261, 30))      # (Left_Indent, Top_Indent, Length, Width)
        self.lineUsername.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineUsername.setFrame(False)
        self.lineUsername.setObjectName("lineUsername")
        self.linePassword = QtWidgets.QLineEdit(createmaster)
        self.linePassword.setGeometry(QtCore.QRect(250, 185, 261, 30))
        self.linePassword.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.linePassword.setFrame(False)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePassword.setObjectName("linePassword")
        self.lineNotes = QtWidgets.QLineEdit(createmaster)
        self.lineNotes.setGeometry(QtCore.QRect(250, 225, 261, 30))
        self.lineNotes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineNotes.setFrame(False)
        self.lineNotes.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineNotes.setObjectName("lineNotes")
        self.pushSave = QtWidgets.QPushButton(createmaster)
        self.pushSave.setGeometry(QtCore.QRect(280, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushSave.setFont(font)
        self.pushSave.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushSave.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushSave.setObjectName("pushSave")

        self.retranslateUi(createmaster)
        QtCore.QMetaObject.connectSlotsByName(createmaster)
        
        ### Action Buttons
        self.pushSave.clicked.connect(self.masterpassword)
        
    def retranslateUi(self, createmaster):
        _translate = QtCore.QCoreApplication.translate
        createmaster.setWindowTitle(_translate("createmaster", CWTE))
        self.label.setText(_translate("createmaster", CCMP))
        self.label_3.setText(_translate("createmaster", LUSR))
        self.label_4.setText(_translate("createmaster", LPWD))
        self.label_5.setText(_translate("createmaster", CMRB))
        self.pushSave.setText(_translate("createmaster", CMSP))

    ### Prevent Segment error 11
    def closeEvent(self, event):        
        try:            
            f = open(sessiontmp,"r")
            pass
        except:
            core.exit_now('','')
            
    ### Create the first username and password to encrypt the file
    def masterpassword(self):
        df = pd.DataFrame()
        if (df.empty):
            date = core.now()
            ndate = "{}-{}-{}".format(date[3],date[2], date[1])
            username = self.lineUsername.text()
            password = self.linePassword.text()
            checkpass = self.lineNotes.text()
            if username == '':
                self.label_Msg.setText(LUCE)
                self.repaint()
                return False
            if password == '':
                self.label_Msg.setText(LPCE)
                self.repaint()
                return False
            if checkpass == '':
                self.label_Msg.setText(CRPE)
                self.repaint()
                return False                
            if checkpass != password:
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