#Key bindings are setup for Windows.
#Please use the OSX Sikuli script for OSX systems instead. 

#Support-demo   
SETUP_URL = "https://www.gotesters.com/lib/qa-supported-files/sikuli-calibration.html"
DEMO_URL = "https://maps.demos-staging.goinstant.org/"   

#Opening 2 browsers
#Guest browser
App.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
wait(5)
print "Chrome opened successfully"
#Agent browser
App.open("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
print "Firefox opened successfully"
wait(5)

guest = App("Google Chrome")
agent = App("Firefox")
guestRegion = App("Google Chrome").window()
agentRegion = App("Firefox").window()

guestRegion.highlight()
guest.focus()
#guestRegion.click(Pattern("1377782186475.png").similar(0.52).targetOffset(105,0))
#Check browser size
#type(SETUP_URL + Key.ENTER)
#if exists("1377118754039.png"):
   # print "Keep calm and begin testing"
#else:
    #print "Apparently, Didn't find the green square."
#if exists("1377118773990.png"):
   # print "Keep calm and begin testing"
#else:
    #print "or the blue circle, this could be a problem."
#if exists("1377121838772.png"):
   # print "Keep calm and begin testing"
#else:
  #  popup("Your browser is not calibrated. Red Triangle not found.")
   # wait(10)
#if exists("1377121848443.png"):
 #   print "Keep calm and begin testing"
#else:
  #  popup("Your browser is not calibrated. Black X not found.")
   # wait(10)
#Start test
guest.focus()
guestRegion.click(Pattern("1377782186475.png").similar(0.52).targetOffset(105,0))
type(DEMO_URL + Key.ENTER)
print "navigated to maps-demo site as guest"

#click login on guest
guestRegion.wait("1377118860636.png")
guestRegion.type(Pattern("1377118874684.png").targetOffset(-138,-1), "Guest")
guestRegion.click("1377118860636.png")
guestRegion.wait(Pattern("1377118930715.png").similar(0.90).targetOffset(-7,1))
guestRegion.click(Pattern("1377782115396.png").similar(0.75).targetOffset(109,-1))
type("a", KEY_CTRL)
type("c" , KeyModifier.CTRL)
#Setup Agent Region
#agentRegion.highlight()
#agent.focus()
#agentRegion.click(Pattern("1377782115396.png").similar(0.75).targetOffset(109,-1))
#Check browser size
#type(SETUP_URL + Key.ENTER)
#if exists("1377119216996.png"):
  #  print "Keep calm and begin testing"
#else:
#    print "Apparently, Didn't find the green square."
#if exists("1377119232204.png"):
  #  print "Keep calm and begin testing"
#else:
   # print "or the blue circle, this could be a problem."
#if exists("1377119243774.png"):
   # print "Keep calm and begin testing"
#else:
 #   popup("Your browser is not calibrated. Red Triangle not found.")
 #   wait(10)
#if exists("1377119260418.png"):
 #   print "Keep calm and begin testing"
#else:
 #   popup("Your browser is not calibrated. Black X not found.")
  #  wait(10)
#Start test
agentRegion.highlight()
agent.focus()
agentRegion.click(Pattern("1377782115396.png").similar(0.75).targetOffset(109,-1))
type("v" , KeyModifier.CTRL) #KeyModifier.DMD for OSX
type(Key.ENTER)
wait(2)
if agentRegion.exists("1377119602051.png"):
    print("Invite alert is present")
#else:
    #print("Already joined maps-demo site in firefox")
agentRegion.highlight()
agentRegion.hover(Pattern("1377178434970.png").targetOffset(-20,4))
if agentRegion.exists(Pattern("1377178434970.png").targetOffset(-20,4)):
    agentRegion.type(Pattern("1377119875715.png").similar(0.81).targetOffset(-139,-3), "Agent")
    agentRegion.click("1377178460922.png")
    agentRegion.wait("1377120027751.png")
else:
    print "Already joined maps-demo site in Firefox"
guest.focus()
guestRegion.exists("1377120062694.png")
guestRegion.click("1377120080670.png")
guestRegion.exists("1377120099525.png")
guestRegion.click(Pattern("1377120099525.png").targetOffset(-132,-33))
wait(2)
guestRegion.click("1377120153974.png")
agent.focus()
if agentRegion.exists(Pattern("1377120206147.png").targetOffset(-56,0)):
    print "carry on"
else:
    guest.focus()
    guestRegion.click("1377120327238.png")
    guestRegion.click("1377120354439.png")
agent.focus()
if agentRegion.exists(Pattern("1377120206147.png").targetOffset(-56,0)):
    print "carry on"
else:
    guest.focus()
    guestRegion.click("1377120327238.png")
    guestRegion.click("1377120354439.png")
guest.focus()
guestRegion.type(Pattern("1377120484604.png").targetOffset(-75,-1), "Madison Square Garden")
guestRegion.click(Pattern("1377120534606.png").targetOffset(-69,26))
wait(2)
if exists("1377120645337.png"):
    guestRegion.type(Pattern("1377120484604.png").targetOffset(-75,-1), "Madison Square Garden")
    guestRegion.click(Pattern("1377120534606.png").targetOffset(-69,26))
else:
    print "Nothing to see here, move on."               
for i in range(12):
   guestRegion.click(Pattern("1377120718039.png").targetOffset(0,38))
print "zoom map"
if guestRegion.exists("1377180922261.png"):
    guestRegion.click(Pattern("1377182624747.png").similar(0.90).targetOffset(-2,1))
    print("Shows street map with terrain")
else:
    print("Maps displays in Satellite view")
if guestRegion.exists("1377179963499.png"):
    guestRegion.click(Pattern("1377182669081.png").similar(0.85).targetOffset(-5,1))
    print("Shows Satellite imagery view")
else:
    print("Maps displays in Terrain view")
agent.focus()
agentRegion.exists("1377121214747.png")
guest.focus()
guestRegion.exists("1377121225338.png")
guestRegion.dragDrop("1377120718039.png",Pattern("1377121243878.png").targetOffset(-8,16))
guestRegion.exists("1377121297970.png")
agent.focus()
agentRegion.exists("1377120986464.png")
guest.focus()
for i in range(10):
    guestRegion.click(Pattern("1377121353254.png").targetOffset(-17,-2))
print "clockwise rotating successful!"
for i in range(3):
    guestRegion.click(Pattern("1377121297970.png").targetOffset(16,0))
print "view up successful!"
for i in range(3):
    guestRegion.click(Pattern("1377121297970.png").targetOffset(-1,-17))
print "view down successful!"

for i in range(10):
    guestRegion.click(Pattern("1377121297970.png").targetOffset(-1,16))
print "anti-clockwise rotating successful!"
#How do we know these actions are successful??? ToDO
#popup("Click on the arrows inside the street view to verify manually for 20 secs")
#wait(20)
#popup("Times up! Did it work? else create an issue in github ")
#We cannot assume that a human will be watching this test run.
guestRegion.click("1377121414606.png")
wait(2)
if exists ("1377121425173.png"):
    guestRegion.click("1377121436949.png")
else:
    print "Good to go"
agent.focus()
agentRegion.exists("1377121485866.png")
guest.focus()
guestRegion.exists("1377121499684.png")
for i in range(13):
   guestRegion.click(Pattern("1377121568249.png").similar(0.93).targetOffset(-1,0))
print "reset map"

print("Workflow coverage ends")