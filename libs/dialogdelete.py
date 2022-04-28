#FINAL

####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from core import *
from mainmenu import *
#######################################################
class Ui_DialogDelete(object):
    def setupUi(self, DialogDelete):
        DialogDelete.setObjectName("DialogDelete")
        DialogDelete.resize(391, 160)
        DialogDelete.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogDelete.sizePolicy().hasHeightForWidth())
        DialogDelete.setSizePolicy(sizePolicy)
        DialogDelete.setMinimumSize(QtCore.QSize(391, 160))
        DialogDelete.setMaximumSize(QtCore.QSize(391, 160))
        DialogDelete.setStyleSheet(u"background:rgb(40, 44, 52);color: white;")
        self.label = QtWidgets.QLabel(DialogDelete)
        self.label.setGeometry(QtCore.QRect(10, 0, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(220,20,60);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tablemsg = QtWidgets.QLabel(DialogDelete)
        self.tablemsg.setGeometry(QtCore.QRect(10, 40, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablemsg.setFont(font)
        self.tablemsg.setText("")
        self.tablemsg.setObjectName("tablemsg")
        self.label_2 = QtWidgets.QLabel(DialogDelete)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 291, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.label_id = QtWidgets.QLabel(DialogDelete)
        self.label_id.setGeometry(QtCore.QRect(310, 40, 61, 31))
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.pushButtonOk = QtWidgets.QPushButton(DialogDelete)
        self.pushButtonOk.setGeometry(QtCore.QRect(300, 110, 81, 32))
        self.pushButtonOk.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonOk.setStyleSheet(u"background:rgb(248,248,255);color: black;")
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCancel = QtWidgets.QPushButton(DialogDelete)
        self.pushButtonCancel.setGeometry(QtCore.QRect(300, 80, 81, 32))
        self.pushButtonCancel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButtonCancel.setStyleSheet(u"background:rgb(50, 54, 62);color: white;")
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.label_id.raise_()
        self.label.raise_()
        self.tablemsg.raise_()
        self.label_2.raise_()
        self.pushButtonOk.raise_()
        self.pushButtonCancel.raise_()

        self.retranslateUi(DialogDelete)
        QtCore.QMetaObject.connectSlotsByName(DialogDelete)
        
        self.pushButtonOk.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)

        core.sessioncheck()

    def retranslateUi(self, DialogDelete):
        _translate = QtCore.QCoreApplication.translate
        DialogDelete.setWindowTitle(_translate("DialogDelete", DWTE))
        self.label.setText(_translate("DialogDelete", DQDR))
        self.label_2.setText(_translate("DialogDelete", DMDS))
        self.pushButtonOk.setText(_translate("DialogDelete", LBOK))
        self.pushButtonCancel.setText(_translate("DialogDelete", DBCC))

    ### Close dialog window
    def reject(self):
        self.close()
        return False      
    
    ### Delete the record
    def accept(self):
        delete = self.label_id.text()
        delete = int(delete)

        if delete == '0':
            self.tablemsg.setText(DADM)
            MainMenu.msg_label.setText(DADM)
            self.repaint()
            self.close()
            core.sessioncheck()
            return False
        else:
            df = pd.read_csv(filetemp)
            df.drop(df.loc[df['ID']==delete].index, inplace=True)
            with open(filetemp, 'w') as f:
                df.to_csv(f,sep=',', encoding=encoding,index=False, mode='a')
                f.close()
                df = pd.read_csv(filetemp,index_col='ID')
                ### CREATE ENC KEY for FILE AND HASH                               
                admpwd = df['Password'][0]
                password = core.detemppwd(admpwd)
                keyfile = core.decrypt(password)        
                pyAesCrypt.encryptFile(filetemp, filename, keyfile, bufferSize) 
                self.pushButtonOk.hide()
                self.pushButtonCancel.setText(DEBT)
                self.label.setText(DRDL)
                self.repaint()
                core.sessioncheck()
            return True
        return None
