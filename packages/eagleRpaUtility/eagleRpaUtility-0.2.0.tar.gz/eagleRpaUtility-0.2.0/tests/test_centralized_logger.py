from eagleRpaUtility.CentralizedLogger import CentralizedLogger
from logging import INFO, DEBUG, WARNING

cl = CentralizedLogger()
cl.setupRun("test_centralized_logger", "RPA", "cpicciafuoco")
cl.addLog("start", INFO)
cl.addLog("test", DEBUG)
cl.addLog("stop", WARNING)