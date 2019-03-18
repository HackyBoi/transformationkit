import os, urllib.request
from tkinter import *

#Theme item locations
iconsURL = "https://github.com/vinceliuice/Mojave-gtk-theme/raw/images/MacOSX-icon-theme.tar.xz"
themeURL = "https://github.com/B00merang-Project/macOS-Dark/archive/master.zip"
wallpaperURL = "https://media.idownloadblog.com/wp-content/uploads/2016/06/macOS-Sierra-Wallpaper-Macbook-Wallpaper.jpg"

#Theme names
themeName = "macOS-Dark-master"
iconsName = "MacOSX"
wallpaperName = "macOS-Sierra-Wallpaper-Macbook-Wallpaper.jpg"

#Installer window
darkColor = "#333" #Change to alter UI color
sidebarFont = ("Bitstream Vera Sans", 10) #Font for the sidebar items
headerFont = ("Bitstream Vera Sans", 30) #Font for titles
subheaderFont = ("Purisa", 10) #Font for subtitles
headerPadding = 15 #How far in should the titles be?
screenWidth = 800 #How wide should the window be?
screenHeight = 600 #How tall should the window be?
root = Tk() #Used for tkinter
canvas = Canvas(root, width=screenWidth, height=screenHeight) #Makes the window a specified size and lets you do graphics
canvas.pack() #Needed for some reason
canvas.create_rectangle(0, 0, screenWidth, screenHeight, fill="white") #White background

#Top gray area
canvas.create_rectangle(0, 0, screenWidth, 100, fill=darkColor, outline="") #Background
canvas.create_text(headerPadding, headerPadding, text="macOS Theme Installer", font=headerFont, fill="white", anchor=NW) #Title
canvas.create_text(headerPadding, headerPadding + 45, text="By HackyBoi", font=subheaderFont, fill="white", anchor=NW) #Subtitle

#Sidebar
sidebar = canvas.create_rectangle(0, 100, 200, screenHeight, fill=darkColor, outline="") #Background
sidebarHome = canvas.create_rectangle(0, 100, 200, 150, fill="white", outline="") #Home background
sidebarHomeText = canvas.create_text(100, 125, text="Home", fill=darkColor, font=sidebarFont) #Home text
sidebarInstall = canvas.create_rectangle(0, 150, 200, 200, fill=darkColor, outline="") #Install background
sidebarInstallText = canvas.create_text(100, 175, text="Install", fill="white", font=sidebarFont) #Install text
sidebarComplete = canvas.create_rectangle(0, 200, 200, 250, fill=darkColor, outline="") #Complete background
sidebarCompleteText = canvas.create_text(100, 225, text="Complete", fill="white", font=sidebarFont) #Complete text

#Window
screen = []
screenTitleX = (screenWidth / 2) + 100 #Figure out where to put the text
screenTitleY = 150 #Figure out where to put the text
screen.append(canvas.create_text(screenTitleX, screenTitleY, text="Welcome", font=headerFont)) #Title
screen.append(canvas.create_text(screenTitleX, screenTitleY + 100, text="This application will install a macOS-like theme on your computer.")) #Info text
screen.append(canvas.create_rectangle(screenTitleX - 100, screenHeight - 90, screenTitleX + 100, screenHeight - 30, fill="white", tags=["installbutton"])) #Install button
screen.append(canvas.create_text(screenTitleX, screenHeight - 60, text="Install", font=headerFont, tags=["installbutton"])) #Install button text

def done(event): #Called by exit button
	sys.exit(0)

def install(event):
	#Clear screen and swap sidebar menus
	for item in screen:
		canvas.delete(item)
	
	canvas.itemconfigure(sidebarHome, fill=darkColor)
	canvas.itemconfigure(sidebarHomeText, fill="white")
	canvas.itemconfigure(sidebarInstall, fill="white")
	canvas.itemconfigure(sidebarInstallText, fill=darkColor)
	
	#Install menu text
	screen.append(canvas.create_text(screenTitleX, screenTitleY, text="Installing...", font=headerFont))
	screen.append(canvas.create_text(screenTitleX, screenTitleY + 100, text="Please wait while I install your theme..."))
	root.update() #Force screen refresh
	
	#Install theme
	urllib.request.urlretrieve(iconsURL, filename="icons.tar.gz") #Download icons
	urllib.request.urlretrieve(themeURL, filename="theme.zip") #Download theme
	urllib.request.urlretrieve(wallpaperURL, filename=wallpaperName) #Download walpaper
	os.system("unzip -o theme.zip; cp -r " + themeName + " ~/.themes/") #Install theme
	os.system("tar xvf icons.tar.gz; cp -r " + iconsName + " ~/.icons") #Install icons
	os.system("gsettings set org.gnome.desktop.interface gtk-theme \"" + themeName + "\"") #Set theme
	#os.system("gsettings set org.gnome.shell.extensions.user-theme name \"" + themeName + "\"") #Set shell theme (broken)
	os.system("gsettings set org.gnome.desktop.interface icon-theme \"" + iconsName + "\"") #Set icon theme
	os.system("cp " + wallpaperName + " ~/.themes/; gsettings set org.gnome.desktop.background picture-uri file:///home/$USER/.themes/" + wallpaperName) #Set wallpaper
	
	#Clear screen and swap sidebar menus
	for item in screen:
		canvas.delete(item)
	
	canvas.itemconfigure(sidebarInstall, fill=darkColor)
	canvas.itemconfigure(sidebarInstallText, fill="white")
	canvas.itemconfigure(sidebarComplete, fill="white")
	canvas.itemconfigure(sidebarCompleteText, fill=darkColor)
	
	#Complete text
	screen.append(canvas.create_text(screenTitleX, screenTitleY, text="Complete!", font=headerFont))
	screen.append(canvas.create_text(screenTitleX, screenTitleY + 100, text="Thank you for using the macOS Transformation Kit. Your theme is now ready."))
	
	#Exit button
	screen.append(canvas.create_rectangle(screenTitleX - 100, screenHeight - 90, screenTitleX + 100, screenHeight - 30, fill="white", tags=["donebutton"]))
	screen.append(canvas.create_text(screenTitleX, screenHeight - 60, text="Exit", font=headerFont, tags=["donebutton"]))
	canvas.tag_bind("donebutton", "<ButtonPress-1>", done) #Make exit button clickable

canvas.tag_bind("installbutton", "<ButtonPress-1>", install) #Make install button clickable
root.mainloop()
