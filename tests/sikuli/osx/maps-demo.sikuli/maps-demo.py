#Key bindings are setup for Mac OSX.
#Please use the Win Sikuli script for Windows systems instead. 

#Support-demo   
SETUP_URL = "https://www.gotesters.com/lib/qa-supported-files/sikuli-calibration.html"
DEMO_URL = "https://maps.demos-staging.goinstant.org/"   

#Opening 2 browsers
#Guest browser
App.open("Safari")
wait(5)
print "Safari opened successfully"
#Agent browser
App.open("Firefox")
print "Firefox opened successfully"
wait(5)

guest = App("Safari")
agent = App("Firefox")
guestRegion = App("Safari").window()
agentRegion = App("Firefox").window()

guestRegion.highlight()
guest.focus()
guestRegion.click(Pattern("1376323757064.png").targetOffset(227,11))
#Check browser size
type(SETUP_URL + Key.ENTER)
if exists("1376419963845.png"):
    print "Keep calm and begin testing"
else:
    print "Apparently, Didn't find the green square."
if exists("1376420028597.png"):
    print "Keep calm and begin testing"
else:
    print "or the blue circle, this could be a problem."
if exists("1376420075828.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Red Triangle not found.")
    wait(10)
if exists("1376420101520.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Black X not found.")
    wait(10)
#Start test
guest.focus()
guestRegion.click(Pattern("1376323757064.png").targetOffset(227,11))
type(DEMO_URL + Key.ENTER)
print "navigated to maps-demo site as guest"

#click login on guest
guestRegion.wait("1376504275634.png")
guestRegion.type(Pattern("1376504275634.png").targetOffset(-148,0), "Guest")
guestRegion.click("1376504275634.png")
guestRegion.wait("1376493465851.png")
guestRegion.click(Pattern("1376323757064.png").targetOffset(227,11))
type("c" , KeyModifier.CMD)
#Setup Agent Region
agentRegion.highlight()
agent.focus()
agentRegion.click(Pattern("1376324766059.png").targetOffset(97,-1))
#Check browser size
type(SETUP_URL + Key.ENTER)
if exists("1376419963845.png"):
    print "Keep calm and begin testing"
else:
    print "Apparently, Didn't find the green square."
if exists("1376420028597.png"):
    print "Keep calm and begin testing"
else:
    print "or the blue circle, this could be a problem."
if exists("1376420075828.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Red Triangle not found.")
    wait(10)
if exists("1376420101520.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Black X not found.")
    wait(10)
#Start test
agent.focus()
agentRegion.click(Pattern("1376324766059.png").targetOffset(97,-1))
type("v" , KeyModifier.CMD)
type(Key.ENTER)
if exists("1376504275634.png"):
    agentRegion.type(Pattern("1376504275634.png").targetOffset(-148,0), "Agent")
    agentRegion.click("1376504275634.png")
    agentRegion.wait("1376493513012.png")
else:
    print "Already joined maps-demo site in Firefox"
guest.focus()
guestRegion.exists("1376498399798.png")
guestRegion.click("1376498428465.png")
guestRegion.exists("1376498452504.png")
guestRegion.click(Pattern("1376498452504.png").targetOffset(-129,-28))
wait(2)
guestRegion.click("1376498539567.png")
agent.focus()
if agentRegion.exists(Pattern("1376498575793.png").targetOffset(-49,8)):
    print "carry on"
else:
    guest.focus()
    guestRegion.click("1376940954831.png")
    guestRegion.click("1376498539567.png")
agent.focus()
if agentRegion.exists(Pattern("1376498575793.png").targetOffset(-49,8)):
    print "carry on"
else:
    guest.focus()
    guestRegion.click("1376940954831.png")
    guestRegion.click("1376498539567.png")
guest.focus()
guestRegion.type(Pattern("1376498575793.png").targetOffset(-49,8), "Madison Square Garden")
guestRegion.click(Pattern("1376498575793.png").targetOffset(-157,22))
wait(2)
if exists(Pattern("1376498575793.png").targetOffset(-79,0)):
    guestRegion.type(Pattern("1376498575793.png").targetOffset(-49,8), "Madison Square Garden")
    guestRegion.click(Pattern("1376498575793.png").targetOffset(-157,22))
else:
    print "Nothing to see here, move on."               
for i in range(13):
   guestRegion.click(Pattern("1376499742783.png").targetOffset(0,37))
print "zoom map"
agent.focus()
agentRegion.exists(Pattern("1376687178344.png").similar(0.90).targetOffset(0,14))
guest.focus()
guestRegion.exists(Pattern("1376687213641.png").similar(0.88).targetOffset(-1,15))
guestRegion.dragDrop("1376499742783.png",Pattern("1376687213641.png").similar(0.88).targetOffset(-363,248))
guestRegion.exists(Pattern("1376941633185.png").similar(0.50).targetOffset(-17,1))
agent.focus()
agentRegion.exists(Pattern("1376941633185.png").similar(0.50).targetOffset(-17,1))
guest.focus()
for i in range(10):
    guestRegion.click(Pattern("1376941633185.png").similar(0.50).targetOffset(-17,1))
print "clockwise rotating successful!"
for i in range(3):
    guestRegion.click(Pattern("1376941633185.png").similar(0.50).targetOffset(0,-16))
print "view up successful!"
for i in range(3):
    guestRegion.click(Pattern("1376941633185.png").similar(0.50).targetOffset(0,18))
print "view down successful!"

for i in range(10):
    guestRegion.click(Pattern("1376941633185.png").similar(0.50).targetOffset(17,1))
print "anti-clockwise rotating successful!"
#How do we know these actions are successful??? ToDO
#popup("Click on the arrows inside the street view to verify manually for 20 secs")
#wait(20)
#popup("Times up! Did it work? else create an issue in github ")
#We cannot assume that a human will be watching this test run.
guestRegion.click("1376500222054.png")
wait(2)
if exists ("1376500222054.png"):
    guestRegion.click("1376500222054.png")
else:
    print "Good to go"
agent.focus()
agentRegion.exists("1376499955540.png")
guest.focus()
guestRegion.exists("1376499955540.png")
for i in range(13):
   guestRegion.click(Pattern("1376499742783.png").targetOffset(0,235))
print "reset map"

print("Workflow coverage ends")