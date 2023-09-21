from eagleRpaUtility.CustomLogger import CustomLogger

cl = CustomLogger(__name__)
cl.setupLogger()
cl.setupCentralizedLogger("test_log", "client", "developer")
cl.info("Test")
cl.info(cl.central_logger.DEAFULT_STOP)