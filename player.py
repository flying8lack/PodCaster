from playsound import playsound
import os
import wx

if os.path.exists("/Wallet") == False:
    try:
        os.mkdir("Wallet")
    except:
        print("Error!")
        exit(1)
else:
    print("File found!")

#Play the Code
app = wx.App()

panel = wx.Panel()
while 1:
   
    Sound = wx.TextEntryDialog(panel, 'type file name(must add extension): ','the file')
    Sound.ShowModal()
    name = Sound.GetValue()
    Sound.Destroy()
    try:
        if name == "EXIT":
            exit()
        else:
            playsound("Wallet/"+name, False)
    except Exception as e:
        print(str(e))
    
    
app.MainLoop()
