import time
import pyautogui

class ImageManager:
    def waitLoading(self,path,timeout=240,loading=False):
        count= 0
        while True:
            loading_image = pyautogui.locateCenterOnScreen(path)       
            if loading_image == None:
                time.sleep(timeout)
                count=count+1
            if loading == False:    
                if count >= 5:
                    loading_image = pyautogui.locateCenterOnScreen(path)
                    return loading_image
            if loading_image != None:
                return loading_image

    def switchClick(self,path_original,path_secondary):
        time.sleep(5)
        loading_image = pyautogui.locateCenterOnScreen(path_original)
        if loading_image != None:
            try:
                x_img, y_img = pyautogui.locateCenterOnScreen(path_original)
                pyautogui.moveTo(x_img,y_img)
                pyautogui.click()
            except TypeError:
                    print("Errore: non ho trovato l'elemento a schermo. Riprovare o cambiare immagine")       
        if loading_image == None:
            loading_image = pyautogui.locateCenterOnScreen(path_secondary)
            if loading_image != None:
                try:
                    x_img, y_img = pyautogui.locateCenterOnScreen(path_secondary)
                    pyautogui.moveTo(x_img,y_img)
                    pyautogui.click()
                except TypeError:
                    print("Errore: non ho trovato l'elemento a schermo. Riprovare o cambiare immagine")
        return loading_image

    def clickCustom(self,path,x=0,y=0,click_right=False,clicks_number=1):
        count = 0
        while True:
            if count == 10:
                break
            try:
                time.sleep(3)
                x_img, y_img = pyautogui.locateCenterOnScreen(path)
                pyautogui.moveTo(x_img+x,y_img+y,1)
                if click_right == False:
                    if clicks_number > 1:
                        pyautogui.click(clicks=clicks_number)
                        break
                    else:
                        pyautogui.click()
                        break
                else:
                    pyautogui.click("right")
                    break       
            except:
                count = count+1