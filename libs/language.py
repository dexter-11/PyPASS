####### PyPASS Version 1.0.0 ####
import sys
sys.path.append("./libs/")
from configfile import *
#######################################################

### Define Language List
optlang = ['English']

### Define Encoding List
optenco = ['UTF-8','ISO-8859-1','UTF-16','UTF-32']

### Check language config
if language == 'English':
    ### LOGIN PAGE
    LWTE = "PyPASS {} - Login".format(ver)
    LUSR = "Username"
    LPWD = "Password"
    LBOK = "OK"
    LMSG = "Welcome to < PyPASS >"
    LFUP = "Please fill the Username and password to LOGIN"
    LUCE = "The Username cannot be empty"
    LPCE = "The Passwords cannot be empty"
    LOMM = "Opening the Menu"
    LMPW = "Wrong Username or Password!"
    LMUW = "The MASTER Username is wrong"    
    ### DELETE DIALOG BOX
    DWTE = "PyPASS - Delete Password"
    DQDR = "Are you sure to delete the record ?"
    DMDS = "After deleting, You cannot recover the record !"
    DBCC = "Cancel"
    DADM = "You cannot delete this record. Error !"
    DEBT = "Exit"
    DRDL = "Record deleted !"
    ### CREATE MASTER DIALOG
    CCMP = "Create the Master Pasword"
    CWTE = "PyPASS -  Create Master"
    CMRB = "Repeat Pass"
    CMSP = "Save"
    CRPE = "The repeat password cannot be empty!"
    CPNS = "The passwords are not the same!"
    ### CREATE PASSWORD DIALOG
    CPPE = "The Project name cannot be empty"
    CPWT = "PyPASS - Create new"
    CPNP = "Create a new Record Pasword"
    CPPN = "Project"
    CPNO = "Notes"
    CPSP = "Save"
    CPCA = "Clear All"
    CPCD = "Close"
    CPPS = "Password saved !"
    CPCS = "I cannot save this record !"
    ### OPTIONS DIALOG BOX
    OWTE = "PyPASS - Configuration"
    OSTO = "Set Timeout"
    OSEN = "Set Encoding"
    OSSL = "Set Language"
    OSEB = "Export for Backup"
    OSCB = "Export Cleaned in Excel"
    ORRD = "Reset/Remove Database"
    OSID = "Import Database"
    OOOP = "Old Password"
    OONP = "New Password"
    ORMP = "Reset the Master password"
    OROF = "Reset"
    OFEE = "Excel Exported"
    OBED = "BACKUP Exported"
    OBEP = "I Cannot export the backup"
    OOFD = "PyPASS - Files Box"
    OPED = "Export Excel"
    OPEB = "Export Backup"
    OPIB = "Import Backup"
    ORAP = "Reset admin password done, RESTART!"
    OIDB = "Imported, RESTART!"
    OAPR = "All saved password removed!"
    ODMD = "Are you sure to remove all Passwords ?"
    OAPN = "You cancelled the Reset"
    ODMT = "Confirm delete"
    OIDF = "Failed to import the backup"
    OAPP = "I Cannot save the settings"
    OWEA = "Warning!!!"
    ### MAINMANU OPT
    MWTE = "PyPASS - Main Menu"
    MMCR = "Create"
    MMSP = "Search"
    MMDP = "Delete"
    MMSA = "Show All"
    MMCM = "Config"
    MMSO = "Select your Option:"
    MMRD = "Record Deleted"
    MMPC = "Record Copied to the Clipboard"
    MMRR = "Reading all saved Records..."
    MMPN = "Searching in Projects and Notes..."
    MMMM = "Please select the row to delete"
    MMSE = "No search string detected, type something!"
    MMNF = "No record found, try again..."
    MMFR = "Records Found"
    MMTP = "There is a system problem..." 
    TMOT = "The Session has expired, closing the app! Please Login again :)"
    
else:
    ### Default Language
    language = 'English'
