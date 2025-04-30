import pyautogui
import time
from PIL import Image
import os
from datetime import datetime

screen = pyautogui.size()
print(f'Screen size:{screen}')

# 待機（この間に画面を手動で変える？）
time.sleep(2)

def capture_and_click(num_loops):
    screenshots = []
    for i in range(num_loops):

        print(f'Page:{i}')
        # ※全画面を撮ってからクロップすると解像度が落ちない．
        # 全画面を撮る（Macのディスプレイ）
        screenshot = pyautogui.screenshot()
        # print(pyautogui.locateOnScreen(screenshot))

        # クロップする
        # 新書1ページ
        croped = screenshot.crop((820, 0, 2060, 1800))

        screenshots.append(croped)
  
        # ページ送り（右の「次へ」ボタン）
        pyautogui.click(x=1400, y=450, button="left", interval=0.5)

    #ファイル名のための日時取得
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    print(f'保存中...{now}')
    # スクリーンショットをPDFとして保存
    if screenshots:
        screenshots[0].save(now + "_screenshots.pdf", save_all=True, append_images=screenshots[1:])
    
    print(f"{num_loops}回のスクリーンショットとクリックが完了しました。PDFが保存されました。")

# 使用例
capture_and_click(num_loops=330)