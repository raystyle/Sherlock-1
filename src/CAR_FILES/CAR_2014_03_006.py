# CAR_2014_03_006: RunDLL32.exe monitoring

# Adversaries may find it necessary to use Dyanamic-link Libraries (DLLs) to
# evade defenses. One way these DLLs can be "executed" is through the use of the
# built-in Windows utility RunDLL32, which allows a user to execute code in a
# DLL, providing the name and optional arguments to an exported entry point.
# Windows uses RunDll32 legitimately in its normal operation, but with a proper
# baseline and understanding of the environment, monitoring its usage could be
# fruitful.

# Pseudocode
# When looking for all instances of RunDLL32, it is imperative to also have the
# command line information, which contains the DLL information, including the
# name, entry point, and optional arguments.

# process = search Process:Create
# rundll32 = filter process where (exe == "rundll32.exe")
# output rundll32

TECHNIQUE = ['Rundll32']
TACTICS = ['Defense Evasion', 'Execution']
DURATION_MINS = 30

from pyspark.sql.functions import *

class CAR_2014_03_006():
    def __init__(self):
        self.time = 0
        self.duration = DURATION_MINS
        self.tactics = TACTICS
        self.techniques = TECHNIQUES
        self.df = 0

    def analyze(self):
        sysmon_df = self.df.where(col('log_name') == 'Microsoft-Windows-Sysmon/Operational')
        process_create_events = sysmon_df.where(col('event_id') == 1)
        events = process_create_events.where((col('event_data.Image') == "C:\\Windows\\System32\\rundll32.exe"))
        events = events.where((col('event_data.ParentImage') != "C:\\Windows\\explorer.exe"))
        return events