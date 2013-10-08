#Key bindings are setup for Mac OSX.
#Please use the Win Sikuli script for Windows systems instead. 

#Support-demo   
SETUP_URL = "https://www.gotesters.com/lib/qa-supported-files/sikuli-calibration.html"
DEMO_URL = "http://fsi.demos-internal-staging.goinstant.org/"   

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
    popup("Your browser is not calibrated. Green Square not found.")
    wait(10)
    guestRegion.highlight()
if exists("1376420028597.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Blue Circle not found.")
    wait(10)
    guestRegion.highlight()

if exists("1376420075828.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Red Triangle not found.")
    wait(10)
    guestRegion.highlight()
if exists("1376420101520.png"):
    print "Keep calm and begin testing"
else:
    popup("Your browser is not calibrated. Black X not found.")
    wait(10)
    guestRegion.highlight()   

#Start test
guest.focus()
guestRegion.click(Pattern("1376323757064.png").targetOffset(227,11))
type(DEMO_URL + Key.ENTER)
print "navigated to FSI-demo site as guest"

#click login on guest
guestRegion.wait(Pattern("AskForHelp.png").similar(0.90))
guestRegion.click(Pattern("AskForHelp.png").similar(0.90))
guestRegion.click(Pattern("1375886120395.png").similar(0.78))
guestRegion.doubleClick(Pattern("Ynurnrivmzvi.png").similar(0.76).targetOffset(-5,-23))
type("c", KeyModifier.CMD)

#Setup Agent Region
agentRegion.highlight()
agent.focus()
agentRegion.click(Pattern("1376324766059.png").targetOffset(97,-1))

type(DEMO_URL + Key.ENTER)
print "navigated to FSI-demo site in Firefox"
agentRegion.click(Pattern("1376324848327.png").targetOffset(0,45))
type("admin")
agentRegion.click(Pattern("1376324848327.png").targetOffset(0,92))
type("service-cloud")
agentRegion.click(Pattern("1376324848327.png").targetOffset(-34,142))
if exists("1376335959290.png"):
    agentRegion.click(Pattern("1376324848327.png").targetOffset(0,45))
    type("admin")
    agentRegion.click(Pattern("1376324848327.png").targetOffset(0,92))
    type("service-cloud")
    agentRegion.click(Pattern("1376324848327.png").targetOffset(-34,142))
else:
    print "Keep calm and login."
if exists("1376325262369.png"):
    agentRegion.click(Pattern("1376325262369.png").targetOffset(47,-36))

else:
    print "Keep calm and co-browse."
agentRegion.click(Pattern("1376324972147.png").targetOffset(100,-1))
agentRegion.click(Pattern("Enterc0bruws.png").similar(0.50))
type("v", KeyModifier.CMD)
agentRegion.click(Pattern("1375891719591.png").similar(0.55))
guest.focus()
guestRegion.click(Pattern("Firstandlast-1.png").similar(0.81))
type("Guest")
guestRegion.click(Pattern("1375891945390.png").similar(0.65))
guestRegion.click(Pattern("1375892013250.png").similar(0.82))

print("Customer and Agent joined session")

#verify the Mutual Funds
guestRegion.click(Pattern("1376338112964.png").similar(0.50).targetOffset(-94,2))
#verify Personal Information on both the page
agent.focus()
agentRegion.exists(Pattern("PersonalInfo.png").similar(0.93))
print("Personal Information page")
guest.focus()
guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(86,-137))
type("qaFN")
guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(135,-91))
type("qaLN")
guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(107,-39))
type("new")
guestRegion.click(Pattern("1376338893540.png").targetOffset(-11,40))

guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(273,11))
guestRegion.click(Pattern("1376339201870.png").targetOffset(0,10))
guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(153,83))
type("123456")
guestRegion.click(Pattern("1376338354854.png").similar(0.25).targetOffset(131,135))
type("123456")
guestRegion.click(Pattern("1375893315443.png").similar(0.84))
guestRegion.click(Pattern("1376339336658.png").targetOffset(81,88))
agent.focus()
agentRegion.exists("1376339399003.png")   
guest.focus()
guestRegion.wait(Pattern("1375894616298.png").similar(0.86))
guestRegion.click(Pattern("1375894616298.png").similar(0.86))
guestRegion.click(Pattern("1376339701225.png").targetOffset(-46,30))

guestRegion.click(Pattern("1376339701225.png").targetOffset(-47,79))
guestRegion.click(Pattern("1376339701225.png").targetOffset(-47,153))

guestRegion.click(Pattern("1376339863652.png").targetOffset(161,33))
guestRegion.click(Pattern("1376339892246.png").similar(0.00).targetOffset(-19,19))
guestRegion.click(Pattern("1376339997860.png").targetOffset(-28,32))
guestRegion.click(Pattern("1376339997860.png").targetOffset(100,32))
guestRegion.wheel("1376339997860.png", WHEEL_DOWN, 100)
guestRegion.click(Pattern("1376340165815.png").targetOffset(-37,29))
guestRegion.click(Pattern("1376340165815.png").targetOffset(84,30))
#verify Fund Categories
agent.focus()
agentRegion.exists("1376404361251.png")
print("Fund Categories")
guest.focus()
guestRegion.click("1376414893547.png")
#Screened Funds page
guestRegion.click(Pattern("1376404431350.png").targetOffset(-45,65))
guestRegion.click(Pattern("1376404431350.png").targetOffset(-44,200))
#verify Screened Funds
agent.focus()
agentRegion.wheel(Pattern("1376404431350.png").targetOffset(-6,2), WHEEL_DOWN, 100)
agentRegion.exists("1376416472153.png")
print("Screened Funds")
guest.focus()
guestRegion.click(Pattern("1376404431350.png").targetOffset(-45,140))
#verify Screened Funds
guestRegion.exists("1376416519716.png")
print("Screened Funds")
guestRegion.click("1376416548903.png")
guestRegion.click(Pattern("1376404777492.png").targetOffset(319,87))
guestRegion.doubleClick("1376404847196.png")
guestRegion.doubleClick("1376404847196.png")
guestRegion.click(Pattern("1376404777492.png").targetOffset(194,175))
guestRegion.click(Pattern("1376404777492.png").similar(0.00).targetOffset(164,142))
guestRegion.click(Pattern("1376404777492.png").similar(0.00).targetOffset(141,187))
guestRegion.click(Pattern("1376404777492.png").similar(0.00).targetOffset(242,140))
guestRegion.click(Pattern("1376404777492.png").similar(0.00).targetOffset(216,190))
guestRegion.click(Pattern("1376404777492.png").similar(0.00).targetOffset(97,192))
type("902-555-5555")
guestRegion.click("1376416603349.png")
#verify Screened Funds
agent.focus()
agentRegion.exists("1376405258227.png")
print("Appointment Confirmaton")
guest.focus()
guestRegion.exists("1376405258227.png")
#College Savings
guestRegion.click(Pattern("1376405367636.png").targetOffset(-9,222))
guestRegion.click(Pattern("1375893315443.png").similar(0.84))
#verify Screened Funds
agent.focus()
agentRegion.exists("1376406051197.png")
print("College Savings")
guest.focus()
guestRegion.exists("1376406051197.png")
guestRegion.click("1376413585471.png")
guestRegion.type(Pattern("1376413825884.png").targetOffset(297,-61), "qaFN qaLN")
guestRegion.type(Pattern("1376413825884.png").targetOffset(292,-21), "6")
guestRegion.doubleClick(Pattern("1376413825884.png").targetOffset(318,22))
type("8800")
guestRegion.doubleClick(Pattern("1376413825884.png").targetOffset(320,58))
type("200")
guestRegion.wheel(Pattern("1376413825884.png").targetOffset(0,1), WHEEL_DOWN, 100)
guestRegion.doubleClick(Pattern("1376413978402.png").targetOffset(286,-38))
type("1000")
guestRegion.doubleClick(Pattern("1376413978402.png").targetOffset(262,2))
type("9")
guestRegion.dragDrop(Pattern("1376413978402.png").similar(0.50).targetOffset(408,33), Pattern("1376413978402.png").similar(0.50).targetOffset(536,32))
guestRegion.click(Pattern("1376413978402.png").similar(0.50).targetOffset(-40,503))
guestRegion.exists("1376416603349.png")
guestRegion.click("1376416603349.png")
#verify Appointment
agent.focus()
agentRegion.exists("1376405258227.png")
print("Appointment Confirmaton")
guest.focus()
guestRegion.exists("1376405258227.png")
#INSURANCE
guest.focus()
guestRegion.click(Pattern("1376416891205.png").targetOffset(0,140))
guestRegion.click(Pattern("1375893315443.png").similar(0.84))
guestRegion.click("1376416990863.png")
guestRegion.wheel("1376417297106.png", WHEEL_DOWN,100)
guestRegion.click(Pattern("1376417297106.png").targetOffset(-29,184))
guestRegion.click(Pattern("1376417297106.png").targetOffset(-82,273))
guestRegion.click("1376417447517.png")
#verify Benefits
agent.focus()
agentRegion.exists("1376417492068.png")
print("Benefits Confirmaton")
guest.focus()
guestRegion.exists("1376417492068.png")
guestRegion.click(Pattern("1376417492068.png").targetOffset(-130,88))
guestRegion.click(Pattern("1376417492068.png").targetOffset(-131,133))
guestRegion.click("1376417560996.png")
#verify Quote
agent.focus()
agentRegion.exists("1376417617641.png")
print("Quote Confirmaton")
guest.focus()
guestRegion.exists("1376417617641.png")
guestRegion.doubleClick(Pattern("1376417617641.png").targetOffset(-96,160))
type("35000")
guestRegion.click(Pattern("1376417617641.png").targetOffset(95,284))
type(Key.DOWN + Key.ENTER)
guestRegion.click("1376417717135.png")
#verify Results
agent.focus()
agentRegion.exists("1376417807867.png")
print("Results Confirmaton")
guest.focus()
guestRegion.exists("1376417807867.png")
guestRegion.click("1376417826647.png")
guestRegion.click(Pattern("1376417871567.png").targetOffset(47,145))
guestRegion.click(Pattern("1376417871567.png").targetOffset(49,195))
guestRegion.click(Pattern("1376417871567.png").targetOffset(100,244))
guestRegion.click(Pattern("1376417871567.png").targetOffset(101,292))
guestRegion.click(Pattern("1376417871567.png").targetOffset(45,343))
guestRegion.click("1376418012271.png")
#verify Results
agent.focus()
agentRegion.exists("1376418033431.png")
print("Results Confirmaton")
guest.focus()
guestRegion.exists("1376418033431.png")
guestRegion.wheel("1376418033431.png", WHEEL_DOWN,100)
guestRegion.click(Pattern("1376418033431.png").targetOffset(299,166))
guestRegion.click(Pattern("1376418033431.png").targetOffset(301,285))
guestRegion.click(Pattern("1376418033431.png").targetOffset(297,377))
guestRegion.click(Pattern("1376418033431.png").targetOffset(300,423))
guestRegion.click("1376418012271.png")
#verify Results
agent.focus()
agentRegion.exists("1376418033431.png")
print("Results Confirmaton")
guest.focus()
guestRegion.exists("1376418033431.png")
guestRegion.wheel("1376418033431.png", WHEEL_DOWN,100)
guestRegion.click(Pattern("1376418033431.png").targetOffset(114,140))
type("qaFN qaLN")
guestRegion.click(Pattern("1376418033431.png").targetOffset(56,190))
type("1234" + Key.TAB + "5678" + Key.TAB + "1234" + Key.TAB + "5678")
guestRegion.click(Pattern("1376418033431.png").similar(0.50).targetOffset(133,242))
type(Key.DOWN+ Key.ENTER)
guestRegion.click(Pattern("1376418033431.png").similar(0.50).targetOffset(243,243))
type(Key.DOWN+ Key.ENTER)
guestRegion.click(Pattern("1376418033431.png").similar(0.50).targetOffset(59,291))
type("123")
guestRegion.click(Pattern("1376418033431.png").similar(0.50).targetOffset(-131,459))
guestRegion.click("1376418540570.png")
#verify Results
agent.focus()
agentRegion.exists("1376418613094.png")
print("Results Confirmaton")
guest.focus()
guestRegion.exists("1376418613094.png")
print("Workflow coverage ends")