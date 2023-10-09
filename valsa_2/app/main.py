import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)

def click_escolher_arquivo():
  X=2022
  Y=345
  pyautogui.click(X, Y)

def click_selecionar_pasta():
  X=2015
  Y=556
  pyautogui.click(X, Y)

def click_verificar_arquivo():
  X=2683
  Y=575
  pyautogui.click(X, Y)
  ## await 60seconds
  pyautogui.sleep(60)

def click_lower_folder():
  X=3559
  Y=565
  pyautogui.click(X, Y)

def click_first_file_lower_folder():
  X=3284
  Y=630
  pyautogui.click(X, Y)

def click_upper_folder():
  X=3550
  Y=28
  pyautogui.click(X, Y)


def change_tipo_de_arquivo():
  X=2536
  Y=418
  pyautogui.click(X, Y)
  ## wait 3seconds
  pyautogui.sleep(3)
  X=2480
  Y=505
  pyautogui.click(X, Y)

def main():
    # Wait for user to click
    while True:
      # input("Click anywhere on the screen...")


      #   # Get mouse click position
      # click_x, click_y = pyautogui.position()


      # print(f"Mouse clicked at: X={click_x}, Y={click_y}")

      click_escolher_arquivo()
      ## wait 1seconds
      pyautogui.sleep(1)
      click_selecionar_pasta()
      ## wait 1seconds
      pyautogui.sleep(2)
      ## send key enter
      pyautogui.press('enter')
      ## wait 5 seconds
      pyautogui.sleep(3)
      change_tipo_de_arquivo()
      click_verificar_arquivo()

      # press control+X

      click_first_file_lower_folder()
      pyautogui.hotkey('ctrl', 'x')
      # # wait 5 seconds
      pyautogui.sleep(3)
      click_upper_folder()
      pyautogui.hotkey('ctrl', 'v')

      ## wait 7 minutes
      pyautogui.sleep(300)


if __name__ == "__main__":
    main()


