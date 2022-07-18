import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
import openpyxl
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment, NamedStyle
import time
import pandas as pd
import tkinter 
from tkinter import *
from tkinter import filedialog
from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection
#import file code 
import mainwindow 
from mainwindow import *
import loginwindow 
from loginwindow import *
import PointDetail 
from PointDetail import *
import klday
from klday import *
#khai bao cac bien
open_path, DA_name , Code_tailieu,AHU_name, save_path = '','','','',''
bientan,VSD,maynen,dientro,SL_TH,SL_loc,SL_DP, AHU_DPT,AHU_DPS,SL_valve = 0,0,0,0,0,0,0,0,0,0
A1, A2, A3, A4, A5, A6 ,A7  = 0,0,0,0,0,0,0
col_list =[]
#cac ham dung chung cho 2 man hinh
def thongbao(string):
    tbao = QMessageBox()
    tbao.setWindowTitle('THÔNG BÁO ')
    tbao.setText(string)
    tbao.setWindowIcon(QIcon('logo.ico'))
    x = tbao.exec_()
def change_win():
    main_win = MainWindow()
    main_win.show()
def begin():
    app = QApplication(sys.argv)
    login_win = LoginWindow()
    login_win.show()
    sys.exit(app.exec())
def replace(string):
    newstring = ''
    if(string!=''):
        extension = string.split('/')
        n=len(extension)
        newstring = extension[0]
        for i in range(1,n):
            newstring = newstring + '\\' + extension[i]
    print(newstring)
    return newstring
#Man hinh login
class LoginWindow:
    def __init__(self):
        self.login_win = QMainWindow()
        self.uic = Ui_Loginwindow()
        self.main = Ui_MainWindow()
        self.KLday = Ui_KLday()
        self.uic.setupUi(self.login_win)    
        #button_push
        self.uic.exit_button.clicked.connect(self.exit_push)
        self.uic.path_button.clicked.connect(self.path_push)
        self.uic.next_button.clicked.connect(self.next_push)
        self.uic.save_button.clicked.connect(self.save_push)
    def show(self):
        self.login_win.show()
        root = Tk()
        root.withdraw()
    def begin(self):
        self.login_win = QMainWindow()
        self.uic = Ui_Loginwindow()
        self.uic.setupUi(self.login_win)   
        self.login_win.show()
        #button_push
        self.uic.exit_button.clicked.connect(self.exit_push)
        self.uic.path_button.clicked.connect(self.path_push)
        self.uic.next_button.clicked.connect(self.next_push)
        self.uic.save_button.clicked.connect(self.save_push)
    def next_push(self):
        global DA_name, Code_tailieu,open_path,save_path
        DA_name = self.uic.DA_name.text()
        Code_tailieu = self.uic.code.text()
        print(DA_name)
        print(Code_tailieu)
        if(DA_name!="" and open_path!="" and save_path!=""):
            if (self.uic.bocKLday.isChecked()==True):
                print("BOC KL")     
                self.bocKLday()
            else:
                print("FINISH")
                self.finish()
        elif(DA_name==""):
            thongbao("CHƯA ĐẶT TÊN DỰ ÁN")
        elif(save_path==""):
            thongbao("CHƯA CHỌN FILE LƯU")
        elif(open_path==""):
            thongbao("CHƯA CHỌN FILE CƠ SỞ DỮ LIỆU ")
            
    def bocKLday(self):
        self.KLday.setupUi(self.login_win)
        self.login_win.show()
        self.KLday.next_button.clicked.connect(self.KL_next_push)        
    def KL_next_push(self):
        global A1, A2, A3, A4, A5, A6 ,A7 
        dk_next = True
        if(self.KLday.A1.text()!=''):
            try:
                A1 = float(self.KLday.A1.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A1=0
        print("KL day A1: ",A1)
        if(self.KLday.A2.text()!=''):
            try:
                A2 = float(self.KLday.A2.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A2=0
        print("KL day A2: ",A2)
        if(self.KLday.A3.text()!=''):
            try:
                A3 = float(self.KLday.A3.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A3=0
        print("KL day A3: ",A3)
        if(self.KLday.A4.text()!=''):
            try:
                A4 = float(self.KLday.A4.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A4=0
        print("KL day A4: ",A4)
        if(self.KLday.A5.text()!=''):
            try:
                A5 = float(self.KLday.A5.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A5=0
        print("KL day A5: ",A5)
        if(self.KLday.A6.text()!=''):
            try:
                A6 = float(self.KLday.A6.text())
                
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A6=0
        print("KL day A6: ",A6)
        if(self.KLday.A7.text()!=''):
            try:
                A7 = float(self.KLday.A7.text())
            except:
                thongbao("HÃY NHẬP SỐ NGUYÊN")
                dk_next = False
        else:
            A7=0
        print("KL day A7: ",A7)
        #Di den man hinh chinh 
        if(dk_next):
            self.finish()
            change_value(A1, A2, A3, A4, A5, A6 ,A7)
    def exit_push(self):
        WireSheet()
        self.login_win.close() 
    def path_push(self):
        global open_path
        open_path = filedialog.askopenfilename()        
        print(open_path)
    def save_push(self):
        global save_path
        save_path = filedialog.askdirectory()        
        print("save_path: "+ save_path)
        save_path = replace(save_path)
        print("save_path: "+ save_path)
    def finish(self):
        global A1, A2, A3, A4, A5, A6 ,A7
        change_value(A1, A2, A3, A4, A5, A6 ,A7)
        dkien =False
        if(open_path!="" and save_path !=""):
            dkien = True
        elif(open_path == ""):
            thongbao("CHƯA CHỌN FILE BIỂU MẪU EXCEL !")
        elif(save_path == ""):
            thongbao("CHƯA CHỌN FOLDER LƯU!")
        if(dkien):
            global col_list
            self.main.setupUi(self.login_win)
            self.login_win.show()
            self.main.finish_button.clicked.connect(self.finish_push)
            self.main.back_button.clicked.connect(self.begin)
            self.main.again_button.clicked.connect(self.again_push)
            self.main.quit_button.clicked.connect(self.exit_push)
            count = 0
            #tạo file excel mới để ghi 
            while (count < 2):
                try:
                    col_list = get_col_list(open_path,save_path, DA_name)
                    count+=1
                except:
                    thongbao("HÃY KIỂM TRA LẠI TÊN FILE CÓ BỊ TRÙNG KHÔNG !")
                    self.finish()
    def again_push(self):
        self.main.AHU_name.setText("")
        self.main.bientan.setText("")
        self.main.VSD.setText("")
        self.main.SL_maynen.setText("")
        self.main.SL_dientro.setText("")
        self.main.AHU_DPT.setText("")
        self.main.AHU_DPS.setText("")
        self.main.SL_TH.setText("")
        self.main.SL_loc.setText("")
        self.main.SL_DP.setText("")
    def finish_push(self):
        global col_list
        dkien_nhap = True
        #lay cac gia tri bien nguoi dung nhap
        AHU_name = self.main.AHU_name.text()
        print(AHU_name)
        if(self.main.bientan.text()!=''):
            try:
                bientan = int(self.main.bientan.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                bientan = 0
                dkien_nhap = False
        else: 
            bientan = 0
        print("SO LUONG BIEN TAN : " , bientan)
        if(self.main.VSD.text()!=''):    
            try:
                VSD = int(self.main.VSD.text())                
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                VSD = 0
                dkien_nhap = False
        else: 
            VSD = 0
        print("SO LUONG VSD : " , VSD)
        if(self.main.SL_maynen.text()!=''):
            try:
                maynen = int(self.main.SL_maynen.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                maynen = 0
                dkien_nhap = False
        else: 
            maynen = 0
        print("SO LUONG MAY NEN : " , maynen)
        if(self.main.SL_dientro.text()!=""):
            try:
                dientro = int(self.main.SL_dientro.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                dientro = 0
                dkien_nhap = False
        else: 
            dientro = 0
        print("SO LUONG DIEN TRO : " , dientro)
        #SO LUONG AHU_DPT
        if(self.main.AHU_DPT.text()!=""):
            try:
                AHU_DPT = int(self.main.AHU_DPT.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                AHU_DPT = 0
                dkien_nhap = False
        else: 
            AHU_DPT = 0
        print("SO LUONG DPT : ", AHU_DPT)
        #SO LUONG AHU_DPS
        if(self.main.AHU_DPS.text()!=""):
            try:
                AHU_DPS = int(self.main.AHU_DPS.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                AHU_DPS = 0
                dkien_nhap = False
        else: 
            AHU_DPS = 0
        print("SO LUONG DPS : ", AHU_DPT)
        #SO LUONG CAM BIEN NHIET DO - DO AM 
        if(self.main.SL_TH.text()!=""):
            try:
                SL_TH = int(self.main.SL_TH.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                SL_TH = 0
                dkien_nhap = False
        else: 
            SL_TH = 0
        print("SO LUONG CB NHIET, DO AM : " , SL_TH)
        #SO LUONG LOC PHONG
        if(self.main.SL_loc.text()!=""):
            try:
                SL_loc = int(self.main.SL_loc.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                SL_loc = 0
                dkien_nhap = False
        else: 
            SL_loc = 0
        print("SO LUONG LOC : " , SL_loc)
        #SO LUONG CAM BIEN AP SUAT
        if(self.main.SL_DP.text()!=''):
            try:
                SL_DP = int(self.main.SL_DP.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                SL_DP = 0
                dkien_nhap = False
        else: 
            SL_DP = 0
        print("SO LUONG CB DP : ", SL_DP)
        #SO LUONG VALVE
        if(self.main.SL_valve.text()!=""):
            try:
                SL_valve = int(self.main.SL_valve.text())
            except:
                thongbao("Hãy nhập số nguyên dương !!!")
                SL_valve = 0
                dkien_nhap = False
        else: 
            SL_valve = 0
        # Kiem tra cac checkbox
        cool_coil = False
        hot_coil = False
        if(self.main.coil_lanh.isChecked()==True):
            print("coil lanh = true ")
            cool_coil = True
        if(self.main.coil_nong.isChecked()==True):
            print("coil nong = true ")
            hot_coil = True
        if(dkien_nhap):
            #try:
            DataHandling(col_list,AHU_name, bientan, VSD, hot_coil, cool_coil, maynen, dientro, AHU_DPT, AHU_DPS, SL_loc, SL_TH,SL_DP,SL_valve)
            thongbao("ĐÃ ADD!")
            #except:
                #thongbao("LỖI XUẤT !")
    #code chay file main.py
begin()
