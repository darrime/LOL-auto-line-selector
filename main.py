from tkinter import *
import pyautogui
import keyboard


window = Tk()
window.title("롤 포지션 선택기")
window.geometry('640x400+100+100')
wantPos = Label(window, text="1.원하는 포지션을 입력하세요")
wantPos.pack()



location = (0,0)
dc = 0

def want():
    dc = 1
    wa = Entry.get(in1)
    window.destroy()

    while dc > 0:
        if keyboard.is_pressed('-'):
            location = pyautogui.position()
            print(location)
        if keyboard.is_pressed('='):
            for i in range(10):
                pyautogui.click(location)
                keyboard.write(wa)
                keyboard.press('enter')
                print(wa)
            break;


in1 = Entry(window)
in1.pack()

e1 = Label(window, text="2.채팅창에 마우스를 대고'-'를 누르세요(위치지정)")
e1.pack()

e2 = Label(window, text="3.게임이 잡히면 '='를 누르세요")
e2.pack()

button1 = Button(window, text="확인", width=10, command= want)
button1.pack()

window.mainloop()