#!/usr/bin/env python
# coding: utf-8

# In[1]:


import keyboard, time, subprocess
import pandas as pd
from datetime import datetime
import pyautogui


# ### Reading Meting Details

# In[74]:


df = pd.read_csv('D:/Schedule.csv')
df.Time.values


# ### Continous loop which keeps running in the background

# In[75]:


df1 = pd.DataFrame()


# In[77]:


while(True):
    # Get current time
    timestr = datetime.now().strftime("%H:%M")
    
    #Check if the current time is mentioned in the Dataframe containing meeting details
    if timestr in df.Time.values:
        df1 = df[df['Time'].astype(str).str.contains(timestr)]
        
        #Open the Zoom app
        subprocess.Popen("C:/Users/Malee/AppData/Roaming/Zoom/bin/Zoom.exe")
        time.sleep(5)
        
        #Locate the position of the join button on the screen
        JoinButtonlocation = pyautogui.locateOnScreen('D:/JOIN_BUTTON1.png')
        
        #Move the cursor to the position of the button
        pyautogui.moveTo(JoinButtonlocation)
        
        #Perform click operation
        pyautogui.click()
        time.sleep(2)
                
        #Write the meeting ID from the dataframe onto the Zoom App
        keyboard.write(df1.iloc[0,1])
        

        #For tapping the Turn off video option on Zoom app
        TurnOffVideolocation = pyautogui.locateOnScreen("D:/turn_off_vid_button.png")
        pyautogui.moveTo(TurnOffVideolocation)
        pyautogui.click()
        time.sleep(2)
        
        #For tapping on the Join button
        JoinButton2location = pyautogui.locateOnScreen("D:/JOIN_BUTTON2.png")
        pyautogui.moveTo(JoinButton2location)
        pyautogui.click()
        time.sleep(4)
        
        #Reads the Meeting Passcode from the dataframe and enters into the zoom app
        keyboard.write(str(df1.iloc[0,2]))
        time.sleep(2)

        #For finally joining the meeting
        JoinMeetingPostPassword = pyautogui.locateOnScreen("D:/JOIN_BUTTON3.png")
        pyautogui.moveTo(JoinMeetingPostPassword)
        pyautogui.click()
        time.sleep(2)

        #Wait for one minute before the next iteration starts
        time.sleep(60)

