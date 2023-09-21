import os
from eagleRpaUtility import Logger

def test_Logger():
    test_path = "./log"
    Logger.setup(test_path)
    assert os.path.isdir(test_path), "No folder log created!"
    assert len(os.listdir(test_path))<1, "No file .log created in log folder!"