from playsound import playsound
import os
import wx

if os.path.exists("/Wallet") == False:
    try:
        os.system("mkdir Wallet")
    except:
        print("File found!")
else:
    pass

#Play the Code
app = wx.App()

panel = wx.Panel()
while 1:
   
    Sound = wx.TextEntryDialog(panel, 'type mp3 name(must add extension): ','mp3')
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
