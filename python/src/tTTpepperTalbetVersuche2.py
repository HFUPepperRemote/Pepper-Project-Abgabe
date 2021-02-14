#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use showWebview Method"""

import qi
import argparse
import sys
import time
from PIL import Image
import naoqi
from naoqi import *
from threading import Event

global brightness
brightness=1.0


exit = Event()



class HumanGreeter(object):
    

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(HumanGreeter, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("MovementDetection/MovementDetected")
        self.subscriber.signal.connect(self.on_human_tracked)
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        self.movement_detection = session.service("ALMovementDetection")
        self.movement_detection.subscribe("HumanGreeter")
        self.got_movement = False
        

    def on_human_tracked(self, value):
        """
        Callback for event FaceDetected.
        """
        if value == []:  # empty value when the face disappears
            self.got_movement = False
        elif not self.got_movement:  # only speak the first time a face appears
            self.got_movement = True
            print "I saw a face!"
            self.tts.say("Hallo Smart Home Besucher. Bitte registriere dich über den auf meinem Tablet angezeigten Q R Code. Dannach kannst du dich gerne noch über die Hygiene Bestimmungen in dem Labor informieren sowie aktuelle Informationen über Corona erhalten. Klicke einfach auf Weiter. Bitte vergiss nicht die Sitzung zu beenden damit ich mich für den nächsten besucher richten kann.")
            myPepper.loadApplication()
            while True:
              brightness = myPepper.getBrightness()
              time.sleep(3)
              print brightness
              if  brightness == 1.0:
                print 'schleife'
              elif brightness > 0.7:
                time.sleep(20)
                myPepper.beendeDieWebanzeige()
                print 'website schleife'
                myPepper.webviewBeenden()
              else:
                break
            print 'loop beendet'
            myPepper.webviewBeenden()
            exit.set()

              
          

    def run(self):
        while not exit.is_set():
          print "Starting HumanGreeter"
          try:
              exit.wait(18000)
          except KeyboardInterrupt:
              print "Interrupted by user, stopping HumanGreeter"
              self.movement_detection.unsubscribe("HumanGreeter")
              #stop
              sys.exit(0)
              
    def quit(signo, _frame):
        print("Interrupted by %d, shutting down" % signo)
        exit.set()

            
            
class Pepper():
  
  def __init__(self):
    pass
    
  def defaultPosture(self):
    try:
        goToPosture = session.service("ALRobotPosture")
        
        goToPosture.goToPosture("StandInit", 0.5)
        print "die goToPosture Methode wurde aufgerufen"
        
    except Exception, e:
        print "Error was: ", e
  
  
  def autonomusLife(self):
    #ich will, dass der Pepper Leuten in die Augen schaut
    life_service = session.service("ALAutonomousLife")
    life_service.setAutonomousAbilityEnabled("BasicAwareness", True)
    print("autonomus Life Methode wurde aufgerufen")
  def autonomusLifeOff(self):
    #ich will, dass der Pepper Leuten in die Augen schaut
    life_service = session.service("ALAutonomousLife")
    life_service.setAutonomousAbilityEnabled("BasicAwareness", False)
    print("autonomus Life OFF Methode wurde aufgerufen")
  
  
  
  
  
  def preLoadImage(self):
    
    #hier versuche ich ein Bild in den Cache zu laden
    try:
        tabletService = session.service("ALTabletService")
        
        # The ip of the robot from the tablet is 198.18.0.1
        tabletService.preLoadImage("http://198.18.0.1/apps/vasTest/Bilder/")
        print "die preLoad Methode wurde aufgerufen"
        time.sleep(1)
        
    except Exception, e:
        print "Error was: ", e
  
  
  def showImage(self):
    
    #hier versuche ich ein Bild anzuzeigen
    try:
        tabletService = session.service("ALTabletService")
        
        # The ip of the robot from the tablet is 198.18.0.1
        tabletService.showImage("http://198.18.0.1/apps/vasTest/Bilder/Start2.jpg")
        print "die show Image Methode wurde aufgerufen"
        
        
        
    except Exception, e:
        print "Error was: ", e
        
    
    

  def webviewAufrufen(self):
    """
    This example uses the showWebview method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")

        # Ensure that the tablet wifi is enable
        #tabletService.enableWifi()

        # Display a web page on the tablet
        #tabletService.showWebview("http://www.google.com")

        #time.sleep(5)

        # Display a local web page located in boot-config/html folder
        # The ip of the robot from the tablet is 198.18.0.1
        tabletService.showWebview("http://198.18.0.1/apps/vasTest/index.html")
        #tabletService.hideWebview()
        # Hide the web view

    except Exception, e:
        print "Error was: ", e
        
        
        
    
        
        
        
        
        
        
  def webviewBeenden(self):
    """
    This example uses the showWebview method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")

        # Ensure that the tablet wifi is enable
        #tabletService.enableWifi()

        # Display a web page on the tablet
        #tabletService.showWebview("http://www.google.com")

        #time.sleep(5)

        # Display a local web page located in boot-config/html folder
        # The ip of the robot from the tablet is 198.18.0.1
      #tabletService.showWebview("http://198.18.0.1/apps/vasTest/index.html")
        
        tabletService.hideWebview()
        
        time.sleep(2)
        
        tabletService.showWebview("http://198.18.0.1/apps/vasTest/hauptseite.html")
        myPepper.setBrightness()

        # Hide the web view

    except Exception, e:
        print "Error was: ", e
        
    
    def websitewebviewBeenden(self):
      try:
        tabletService = session.service("ALTabletService")
        tabletService.hideWebview()
        time.sleep(2)
        myPepper.setBrightness()
      except Exception, e:
        print "Error was: ", e
        
        
        
  def playVideo(self):
    #hier versuche ich ein Video abzuspielen
    try:
        tabletService = session.service("ALTabletService")
        tabletService.playVideo("http://198.18.0.1/apps/vasTest/videos/gandalf.mp4")
        time.sleep(20)
    # stop the video and hide the player
        tabletService.stopVideo()
    except Exception, e:
        print "Error was: ", e
        
  
  
 


  
  
  
  
  def getBrightness(b):
    #hier versuche ich ein Video abzuspielen
    try:
        tabletService = session.service("ALTabletService")
        print tabletService.getBrightness()
        b = tabletService.getBrightness()
        return b
        
    # stop the video and hide the player
        #tabletService.stopVideo()
    except Exception, e:
        print "Error was: ", e
        
  def beendeDieWebanzeige(self):
    try:
      tabletService = session.service("ALTabletService")
      tabletService.hideWebview()
      time.sleep(2)
      myPepper.setBrightness()
    except Exception, e:
      print "Error was: ", e
        
        
  
  def setBrightness(self):
    #hier stelle ich die Helligkeit ein
    try:
      tabletService = session.service("ALTabletService")
      tabletService.setBrightness(1.0)
      print 'die Helligkeit wurde geändert'
      # stop the video and hide the player
      #tabletService.stopVideo()
    except Exception, e:
      print "Error was: ", e
      
      
      
  
  
  #loadApplication muss wieder weg!
  def loadApplication(self):
    try:
      tabletService = session.service("ALTabletService")
      # Display the index.html page of a behavior name j-tablet-browser
      # The index.html must be in a folder html in the behavior folder
      tabletService.loadApplication("vasTest")
      tabletService.showWebview("http://198.18.0.1/apps/vasTest/index.html")
    except Exception, e:
      print "Error was: ", 
        
        
  
  
  
    
        
  


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
        app = qi.Application(["HumanGreeter", "--qi-url=" + "192.168.0.41"])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);
    myPepper=Pepper()
    myPepper.autonomusLife()
    #myPepper.preLoadImage()
    #myPepper.showImage()
    #myPepper.loadApplication() #diese änderung muss wieder weg.
    #myPepper.webviewAufrufen()
    #myPepper.getBrightness()
    #myPepper.playVideo()
    #myPepper.autonomusLifeOff()
    while True:
          myPepper.setBrightness()
          time.sleep(1)
          human_greeter = HumanGreeter(app)
          human_greeter.run()
          exit.clear()
          myPepper.defaultPosture()
          myPepper.showImage()
          continue      
    #myPepper.getBrightness()
    #myPepper.setBrightness()
   
    
    
    