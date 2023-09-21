from eagleRpaUtility.RequestMaker import RequestMaker

rm = RequestMaker("localhost", 5420)
automation_list_info = rm.makeRequest("http","GET", "getAutomationList", params={"client":"RPA"})
print(automation_list_info)