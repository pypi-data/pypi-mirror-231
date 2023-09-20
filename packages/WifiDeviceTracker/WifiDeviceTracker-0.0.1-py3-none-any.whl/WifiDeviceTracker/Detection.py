import os
import platform
import subprocess
import pandas as pd

class Detection:
    # create a custom exception
    class ScanError(Exception):
        def __init__(self, message: str) -> None:
            super().__init__(message)

    def __init__(self, interface: str="wlan0", stored_scan_depth: int=-1) -> None:
        self.interface = interface
        self.os_name = platform.system()
        self.stored_scan_depth = stored_scan_depth
        self.scan_history = []

        if self.os_name == "Linux":
            if os.geteuid() != 0:
                raise Detection.ScanError("You must have sudo privileges to run this script.")

            self.scan_command = f"sudo arp-scan --interface={self.interface} --localnet".split(" ")
        else:
            self.scan_command = None
    
    def __store_scan(self, scan_details: pd.DataFrame) -> None:
        if self.stored_scan_depth < 0:
            self.scan_history.append(scan_details)
        else:
            # if the scan history is full, remove the oldest scan
            if len(self.scan_history) >= self.stored_scan_depth:
                self.scan_history.pop(0)
            
            self.scan_history.append(scan_details)

    def perform_scan(self) -> str:
        if self.scan_command is None:
            raise Detection.ScanError("This OS is not supported")
        
        scan_result = subprocess.run(self.scan_command, capture_output=True, text=True)
        scan_result = scan_result.stdout.split("\n")

        # parse the scan result into a dataframe
        #scan_result = pd.DataFrame([x.split("\t") for x in scan_result])
        #scan_result.columns = ["ip_address", "mac_address", "manufacturer"]

        #self.__store_scan(scan_result)

        return scan_result