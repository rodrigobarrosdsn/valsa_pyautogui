import pyautogui
# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print(screenWidth, screenHeight)

def click_escolher_arquivo():
  # X=2022
  # Y=345
  X=2092
  Y=374
  pyautogui.click(X, Y)
  pyautogui.sleep(4)

def click_selecionar_pasta():
  # X=2015
  # Y=556
  X=1980
  Y=405
  pyautogui.click(X, Y)

  pyautogui.sleep(3)
  pyautogui.press('enter')



  # X=2243
  # Y=143
  # pyautogui.doubleClick(X, Y)
  # # doubleClick
  # pyautogui.sleep(3)
  # ## send arquivo
  ## select arquivo


  # X=2838
  # Y=36
  # pyautogui.click(X, Y)

def click_verificar_arquivo():
  # X=2683
  # Y=575
  X=2680
  Y=608
  pyautogui.click(X, Y)
  ## await 60seconds
  pyautogui.sleep(15)

def click_lower_folder():
  X=3559
  Y=565
  pyautogui.click(X, Y)

def click_first_file_lower_folder():
  # X=3284
  # Y=630

  X=3489
  Y=657
  pyautogui.click(X, Y)
  pyautogui.sleep(2)

def click_upper_folder():
  # X=3550
  # Y=28
  X=3596
  Y=32
  pyautogui.click(X, Y)
  pyautogui.sleep(2)

def change_tipo_de_arquivo():
  X=2526
  Y=442
  pyautogui.click(X, Y)
  ## wait 3seconds
  pyautogui.sleep(2)
  X=2492
  Y=531

  pyautogui.click(X, Y)
  pyautogui.sleep(2)

def get_mouse_position():
    input("Click anywhere on the screen...")
    #   # Get mouse click position
    click_x, click_y = pyautogui.position()
    print(f"Mouse clicked at: X={click_x}, Y={click_y}")


def main():
    # Wait for user to click
    while True:

      # get_mouse_position()


      click_escolher_arquivo()

      click_selecionar_pasta()

      pyautogui.sleep(2)


      change_tipo_de_arquivo()

      click_verificar_arquivo()

      # # press control+X
      click_first_file_lower_folder()
      pyautogui.hotkey('ctrl', 'x')

      click_upper_folder()
      pyautogui.hotkey('ctrl', 'v')


      # ## wait 4 minutes to upload next file
      # pyautogui.sleep(240)
      pyautogui.sleep(200)


if __name__ == "__main__":
    main()


