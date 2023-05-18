import pandas as pd
laptop = pd.read_csv('dataset/ryans.csv', encoding='cp1252', on_bad_lines='skip', usecols=['Brand', 'Model', 'Processor Brand'])
print(laptop)
# Features to choose - Price, Brand,Processor Brand, Processor Type, Processor Generation, Processor Core, RAM size, RAM Type, Total RAM Slot, Max RAM size, Storage(HDD, SSD), Graphics Chipset, Graphics Memory(Shared/Dedicated), Screen size, Display Resolution, USB Ports, LAN supported, WiFi, Bluetooth, WebCam, Keyboard Layout, Color, Weight (Kg), Battery Capacity, Battery Type, Backup Time, Power Adapter, Warranty, Made in