import pyautogui
import time
from PIL import Image
import os
from datetime import datetime

def capture_and_click(num_loops):
    screenshots = []
    for i in range(num_loops):


        # 座標(Mac)
        # left_up=[0,56]
        # left_down=[0,900]
        # right_up=[1440,56]
        # right_down=[1440,900]

        # スクリーンショットを撮影
        screenshot = pyautogui.screenshot(region=[0,56,1440,900])
        screenshots.append(screenshot)
  
        # pyautogui.click(x=32, y=475, button="left", clicks=num_loops, interval=0.5)
        pyautogui.click(x=32, y=475, button="left")

        # 待機
        time.sleep(0.5)
    
    #ファイル名のための日時取得
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    # スクリーンショットをPDFとして保存
    if screenshots:
        screenshots[0].save(now + "_screenshots.pdf", save_all=True, append_images=screenshots[1:])
    
    print(f"{num_loops}回のスクリーンショットとクリックが完了しました。PDFが保存されました。")

# 使用例
capture_and_click(num_loops=165)