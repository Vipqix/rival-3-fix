# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import hid
import os
from time import sleep
ELM_5_VID = 4152
ELM_5_PID = 6192

def get_ss_device_path_from_vid_pid(vid, pid):
    SS_DEVICE_USAGE = 1
    SS_DEVICE_USAGE_PAGE = 65472
    for d in hid.enumerate():
        if d['vendor_id'] == vid and d['product_id'] == pid and (d['usage'] == SS_DEVICE_USAGE) and (d['usage_page'] == SS_DEVICE_USAGE_PAGE):
            return d
    else:
        return None

class SsDevice:
    DEVICE_REPORT_ID = 0
    DEVICE_RESET_CMD = 1
    DEVICE_APP_MODE = 0
    DEVICE_BOOTLOADER_MODE = 1

    def __init__(self, vid, pid):
        self.vid = vid
        self.pid = pid
        self.opened = False

    def open(self):
        if self.opened:
            return
        d = get_ss_device_path_from_vid_pid(self.vid, self.pid)
        if d == None:
            raise RuntimeError('Error: Device not found')
        self.device = hid.device()
        self.device.open_path(d['path'])
        self.opened = True

    def close(self):
        self.device.close()
        self.opened = False

    def is_in_bootloader(self):
        return self.is_in_boot

    def write(self, data):
        if self.opened == False:
            raise RuntimeError('Error: Writing to device before opening')
        actual_data = [self.DEVICE_REPORT_ID] + data
        return self.device.write(actual_data)

    def write_data(self, data):
        if self.opened == False:
            raise RuntimeError('Error: Writing to device before opening')
        actual_data = [self.DEVICE_REPORT_ID] + data
        if self.use_feature_reports_for_write == False:
            return self.device.write(actual_data)
        return self.device.send_feature_report(actual_data)

    def read(self, read_size):
        if self.opened == False:
            raise RuntimeError('Error: Reading from device before opening')
        return self.device.read(read_size)

def main():
    device = SsDevice(ELM_5_VID, ELM_5_PID)
    device.open()
    device.write([102])
    device.close()
    print('Success! Please open GG and go to the Engine tab to perform the critical update for your device.')
    print("Press any key to exit")
    os.system('pause')
if __name__ == '__main__':
    try:
        main()
        
    except RuntimeError as err:
        print(f"plug in mouse: {err}")
        sleep(10)
        main()
