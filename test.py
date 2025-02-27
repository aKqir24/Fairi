
'''
from shutil import move
from os import path, makedirs, listdir

desktop = "D:\\Desktop"
fileTypes = {  "Pdf's":".pdf", "Docx":".docx", "Exe":".exe", "Txt":".txt", "Wav":".wav",
                "Msi":".msi", "Xpf":".xpf", "Zip":[".zip", ".tgz"], "McPack": ".mcpack"}
for filename in listdir(desktop):
    src = (desktop+"\\"+filename)
    ext = path.splitext(filename)[1].lower()
    for folder, extensions in fileTypes.items():
        try:
            if ext in extensions or not extensions:
                dest = path.join(desktop, folder)
                if not path.exists(dest):
                    makedirs(dest, exist_ok = True)
                move(src, dest)
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

UI = Tk()
UI.title("Just Arrange")
UI.config(background=bg)
UI.geometry("870x560")

folder_list_wrapper = Frame( UI, background="#232121", height=413, width=783)
folder_list_wrapper.place(x=45, y=45)

Add = Button( UI, text="ADD", height=3, width=20 )
Start = Button ( UI, text="Start", height=3, width=20 )
Start.place(x=210, y=480)
Add.place(x= 45, y= 480)

UI.mainloop()

'''
