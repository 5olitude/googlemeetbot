# google meet bot 🤖

A simple Google meet bot so the bot can attend classes for you.(fuck the education system)
 
## REQUIREMENTS
      $ pip3 install selenium
      $ pip3 install pause
      $ pip3 install pynput
  I encourage you to work on a virtual enviornment like anaconda
  
### My Test Cases

* Firstly I work with with the selenium chrome-driver and uses chromium as the interface =  WORKS 
* Secondly I tested on a headless chrome = BUG 
* Mozilla headless driver works fine in mozilla firefox = WORKS

## Advantages of headless drivers?
   
   The program runs in background until you have a good internet connection and power . It never requires mozilla tab to be     opened . I really worked on chrome-headless but some bugs reported while running so i switched into the mozilla-headless it works cool .
   
### CODES
  * chromium.py
  * mozilla.py
  
#### Working of chromium.py
  
  
  * You can uncomment the pause.until in the chromium.py ie you can set the time and execute when to start the program
  
  * Replace the usernameStr and passwordStr with your gmailid and password
  
  * Replace the url meet with the meeting id
  
  * There are certain permissions to use our media by google meet i just blocked it all (micrphone and webcam) and set to a default value of 2(block) and 1(unblock)
  
  *In the last line before pause if you are a student in an organization replace the 'ask to join' with 'Join now'
  ##### note please: i tested on a chromium browser
 
### Working  of mozilla.py 

 * The cool headless functionality i implemeted her and it works pretty well there are more options like --disable gpu 
 
 *  You want to install geckodriver before executing
     
         # conda install -c conda-forge geckodriver
  
 * The headless option makes the program to run in background .even if the program terminated  we will be the particpants in the  meeting
  
 * The permission parameters are little different than in chrome-driver
  
# How to run the program effectively?
  
  * If you deploy it in a cloud then the fun begins you dont have to bother about the internet ,time and other stuffs .
  
  * If more than one meeting id or classes just use the sys arguments or argparse and pass the id as parameters 😀 cool 
  
  * Some helpfull link how to deploy a headless chrome in goole cloud platform i found in internet? 
  
  https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp
  
  * if you search for mozilla deploy you can find it too
  
   * you can also deploy in heroku too 
 ### HOW TO FIRE THE SCRIPT?
      for chromium browser
      
     # python3 chromium.py 
     
      for mozilla headless. if you want to see mozilla opening just uncomment the headless
      
     # python3 mozilla.py
  
  ##### Dedicating to the fucking indian education system which still uses the old syllabus and tears from my heart to the girl in kerala  who ended up her life ( due to unavailability of proper technologies for continuing her studies) . When a whole nation  and a state ruled by  a corrupted political system they cant never able to eradicate poverty but they still trying to make development where poverty is burried underneath .A great 🖕 to corrupted system all around the world
   
### HAVE A NICE DAY  ☕
