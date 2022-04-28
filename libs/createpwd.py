#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
from mainmenu import *
import random, string
######################################################
class Ui_createpwd(object):
    def setupUi(self, createpwd):
        createpwd.setObjectName("createpwd")
        createpwd.resize(640, 480)
        createpwd.setWindowModality(QtCore.Qt.ApplicationModal)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createpwd.sizePolicy().hasHeightForWidth())
        createpwd.setSizePolicy(sizePolicy)
        createpwd.setMaximumSize(QtCore.QSize(640, 480))
        self.label = QtWidgets.QLabel(createpwd)
        self.label.setGeometry(QtCore.QRect(90, 40, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter) 
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createpwd)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setStyleSheet(u"color:rgb(40, 44, 52);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(createpwd)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setStyleSheet(u"color:rgb(40, 44, 52);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createpwd)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setStyleSheet(u"color:rgb(40, 44, 52);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(createpwd)
        self.label_5.setGeometry(QtCore.QRect(90, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setStyleSheet(u"color:rgb(40, 44, 52);")
        self.label_5.setObjectName("label_5")        
        self.lineProject = QtWidgets.QLineEdit(createpwd)
        self.lineProject.setGeometry(QtCore.QRect(260, 115, 201, 30))
        self.lineProject.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineProject.setObjectName("lineProject")
        self.lineUsername = QtWidgets.QLineEdit(createpwd)
        self.lineUsername.setGeometry(QtCore.QRect(260, 155, 201, 30)) 
        self.lineUsername.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineUsername.setObjectName("lineUsername")
        self.linePassword = QtWidgets.QLineEdit(createpwd)
        self.linePassword.setGeometry(QtCore.QRect(260, 195, 201, 30))
        self.linePassword.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.linePassword.setObjectName("linePassword")
        self.lineNotes = QtWidgets.QLineEdit(createpwd)
        self.lineNotes.setGeometry(QtCore.QRect(260, 265, 201, 40))
        self.lineNotes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineNotes.setObjectName("lineNotes")
        self.pushCheck = QtWidgets.QPushButton(createpwd)
        self.pushCheck.setGeometry(QtCore.QRect(470, 195, 91, 30))
        self.pushCheck.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushCheck.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushCheck.setObjectName("pushCheck")
        self.pushSave = QtWidgets.QPushButton(createpwd)
        self.pushSave.setGeometry(QtCore.QRect(165, 340, 98, 51))
        self.pushSave.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushSave.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushSave.setObjectName("pushSave")
        self.pushClear = QtWidgets.QPushButton(createpwd)
        self.pushClear.setGeometry(QtCore.QRect(275, 340, 98, 51))
        self.pushClear.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushClear.setStyleSheet(u"background:rgb(254, 254, 254);color: black;")
        self.pushClear.setObjectName("pushClear")
        self.pushClose = QtWidgets.QPushButton(createpwd)
        self.pushClose.setGeometry(QtCore.QRect(385, 340, 98, 51))
        self.pushClose.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushClose.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.pushClose.setObjectName("pushClose")
        self.label_Msg = QtWidgets.QLabel(createpwd)
        self.label_Msg.setGeometry(QtCore.QRect(165, 410, 320, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Msg.setFont(font)
        self.label_Msg.setText("")
        self.label_Msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") # Red
        self.label_Msg.setObjectName("label_Msg")
        
        self.toolButtonGenerate = QtWidgets.QToolButton(createpwd)
        self.toolButtonGenerate.setGeometry(QtCore.QRect(295, 230, 120, 25))
        self.toolButtonGenerate.setStyleSheet(u"background:rgb(230,230,250);color: black;")
        self.toolButtonGenerate.setObjectName("toolButtonGenerate")

        self.retranslateUi(createpwd)
        QtCore.QMetaObject.connectSlotsByName(createpwd)
        ### Action Buttons
        self.pushSave.clicked.connect(self.newpassword)
        self.pushClear.clicked.connect(self.clearall)
        self.pushCheck.clicked.connect(self.checkpassword) 
        self.pushClose.clicked.connect(self.reject) 
        self.toolButtonGenerate.clicked.connect(self.generate) 
        
    def retranslateUi(self, createpwd):
        _translate = QtCore.QCoreApplication.translate
        createpwd.setWindowTitle(_translate("createpwd", CPWT))
        self.label.setText(_translate("createpwd", CPNP))
        self.label_2.setText(_translate("createpwd", CPPN))
        self.label_3.setText(_translate("createpwd", LUSR))
        self.label_4.setText(_translate("createpwd", LPWD))
        self.label_5.setText(_translate("createpwd", CPNO))
        self.pushSave.setText(_translate("createpwd", CPSP))
        self.pushClear.setText(_translate("createpwd", CPCA))
        self.pushCheck.setText(_translate("createpwd", CPCP))
        self.pushClose.setText(_translate("createpwd", CPCD))
        self.toolButtonGenerate.setText(_translate("createpwd", "Generate Password"))
    
    ### CLOSE DIALOG
    def reject(self):
        core.sessioncheck()
        self.close()
        return False
    
    ### CLEAR FIELDS
    def clearall(self):
        self.lineProject.setText("")
        self.lineUsername.setText("")
        self.linePassword.setText("")
        self.lineNotes.setText("")
        core.sessioncheck()
        self.repaint()
        return None
    
    ### GENERATE RANDOM PASSWORD
    def generate(self):
        # function
        advance = string.ascii_uppercase + string.ascii_lowercase + string.digits + """`~!@#$%^&*()_-+={}[]\|:;<>?/"""
        data = "".join(random.sample(advance,25))

        encodedBytes = data.encode("utf-8")
        encodedStr = str(encodedBytes, "utf-8")
        encodedStr = encodedStr[10:23]
        self.linePassword.setText(encodedStr)
        self.repaint()
        return True

    ### Check passsword strength
    def checkpassword(self):        
        try:            
            password = self.linePassword.text()
            n = len(password)
            # Checking chars in string
            hasLower = False
            hasUpper = False
            hasDigit = False
            specialChar = False
            normalChars = "abcdefghijklmnopqrstu"
            "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
            
            for i in range(n):
                if password[i].islower():
                    hasLower = True
                if password[i].isupper():
                    hasUpper = True
                if password[i].isdigit():
                    hasDigit = True
                if password[i] not in normalChars:
                    specialChar = True
            # Check empty
            if password == '':
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
        
    ### CREATE NEW PASSWOD
    def newpassword(self):
        core.sessioncheck()        
        project = self.lineProject.text()        
        username = self.lineUsername.text()
        password = self.linePassword.text()
        notes = self.lineNotes.text()
        if project == '':
            self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") # Red
            self.label_Msg.setText(CPPE)
            self.repaint()
            return None
        if username == '':
            self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") # Red
            self.label_Msg.setText(LUCE)
            self.repaint()
            return None
        if password == '':
            self.label_Msg.setStyleSheet(u"color:rgb(192,64,0);") # Red
            self.label_Msg.setText(LPCE)
            self.repaint()
            return None

        ### Hash password
        p = core.hash_password(password)
        
        ### Check duplicates IDs
        date = core.now()
        df = pd.read_csv(filetemp, header=0)
        did = df['ID']
        nid = len(df)              
        for idd in did:
            if idd == nid:
                nid = 1+nid
            else:
                nid = nid

        ### Create date
        ndate = "{}-{}-{}".format(date[3],date[2], date[1])
        df.loc[nid] = [nid, project, username, p, notes, ndate]
        ### Save the changes
        try:
            with open(filetemp, 'w') as f:
                df.to_csv(f,sep=',', encoding=encoding,index=False, mode='a')
                f.close()
                ### CREATE ENC KEY for FILE AND HASH                               
                admpwd = df['Password'][0]
                password = core.detemppwd(admpwd)
                keyfile = core.decrypt(password)        
                pyAesCrypt.encryptFile(filetemp, filename, keyfile, bufferSize) 
                
                self.label_Msg.setText(CPPS)
                self.lineProject.setText("")
                self.lineUsername.setText("")
                self.linePassword.setText("")
                self.lineNotes.setText("")
                core.sessioncheck()
                self.repaint()
        except:            
            self.label_Msg.setText(CPCS)
            self.repaint()
            core.sessioncheck()
        return None
