#-*- coding: utf-8 -*-
import _winreg

key = _winreg.HKEY_LOCAL_MACHINE
subkey = "HKLM\\SYSTEM\\ControlSet00X\\Control\\ComputerName\\ActiveComputerName"
# 레지스트리 등록 
registry = _winreg.CreateKey(key,subkey)
