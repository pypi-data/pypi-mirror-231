"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import linuxcnc

class Status:

    def __init__(self):
        self.linuxcnc = linuxcnc
        self.api = self.linuxcnc.stat()
        self.data = None

    def status_work(self):
        pass

    def poll(self):
        self.api.poll()
