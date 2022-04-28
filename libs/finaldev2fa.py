import sys
from secrets import choice
sys.path.append("./libs/")
from core import *
from configfile import *
from createmaster import *

class Ui_otpwindow(object): 
   def auth_window(self, ConfigOTP):
      ConfigOTP.setObjectName("ConfigOTP")
      ConfigOTP.resize(480, 260)
      ConfigOTP.setWindowModality(QtCore.Qt.ApplicationModal)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(ConfigOTP.sizePolicy().hasHeightForWidth())
      ConfigOTP.setWindowTitle("2FA Authenticator")
      #Label 1
      self.l1 = QtWidgets.QLabel(ConfigOTP)
      self.l1.setGeometry(QtCore.QRect(75, 20, 351, 31))
      self.l1.setText("2FA Authenticator")
      self.l1.setAlignment(QtCore.Qt.AlignCenter)
      self.l1.setFont(QtGui.QFont('Times',18))
      self.l1.setObjectName("l1")
      
      #Label 2
      self.label_Msg = QtWidgets.QLabel(ConfigOTP)
      self.label_Msg.setGeometry(QtCore.QRect(20, 90, 400, 300))
      self.label_Msg.setText("""
         First Click to generate the Secret here ^

         Instructions to save Secret to Google Authenticator:
         1. Open Google Authenticator on your phone.
         2. Click '+' icon at the right bottom.
         3. Click 'Enter a setup key'.
         4. Enter any account name of your choice, then enter the new secret.
         5. Click 'Add' to generate Time-based OTPs for use while login.
         NOTE - Make sure your phone and the current device are time-synced.
         """)
      self.label_Msg.setAlignment(QtCore.Qt.AlignLeft)
      self.label_Msg.setObjectName("label_Msg")

      #Button
      self.pushOtp = QtWidgets.QPushButton(ConfigOTP)
      self.pushOtp.setGeometry(QtCore.QRect(190, 60, 120, 30))
      self.pushOtp.setFocusPolicy(QtCore.Qt.WheelFocus)
      self.pushOtp.setText("Generate Secret")
      self.pushOtp.setStyleSheet(u"background:rgb(40, 44, 52);color: orange;")
      self.pushOtp.setObjectName("pushOtp")
      self.pushOtp.raise_()
      self.pushOtp.clicked.connect(self.generate_secret)   
      
   def generate_secret(self, ConfigOTP):  # Function to return a random string with length 16.
      self.msg = QtWidgets.QMessageBox()
      self.msg.setWindowTitle("Secret Code")
      new_secret = ''
      while len(new_secret) < 16:
         new_secret += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
      self.msg.setText(new_secret)
      x = self.msg.exec_() 
      #Save secret to configfile
      f = open("./libs/configfile.py","rt") 
      contents = f.read()
      result = [x.strip() for x in contents.split('\n')] 
      set_secret = result[18]; set_secret = [x.strip() for x in set_secret.split('=')]
      set_secretN = '"' + new_secret + '"'
      f.close()
      result[18] = result[18].replace(str(set_secret[1]),str(set_secretN))
      #write
      f = open("./libs/configfile.py","wt")         
      f.write('\n'.join(result))
      f.close()
      return None


