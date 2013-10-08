#Support-demo   
DEMO_URL = "http://fsi.demos-internal-staging.goinstant.org/"   

#opening 2 browsers
#Chrome 
App.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
print "Chrome opened successfully"

#IE
App.open("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
print "Firefox opened successfully"
wait(2)

#focus region on chrome
chromeRegion = App("Google Chrome").window()
wait(2)
chromeRegion.highlight()

chromeRegion.click(Pattern("iw.png").similar(0.87))
type(DEMO_URL + Key.ENTER)
print "navigated to FSI-demo site in Chrome"
wait(2)
type(Key.F12)
chromeRegion.click(Pattern("Console.png").similar(0.89))
#click login on Chrome
chromeRegion.click(Pattern("AskForHelp.png").similar(0.92))
chromeRegion.click(Pattern("1375886120395.png").similar(0.78))
chromeRegion.doubleClick(Pattern("Ynurnrivmzvi.png").similar(0.76).targetOffset(-5,-6))
type("c", KEY_CTRL)

#focus on Firefox region
firefoxRegion = App("Firefox").window()
firefoxRegion.highlight()
firefoxRegion.doubleClick(Pattern("Ei.png").similar(0.78).targetOffset(3,1))

for i in range(50):
   type(Key.BACKSPACE)
type(DEMO_URL + Key.ENTER)
print "navigated to FSI-demo site in Firefox"
firefoxRegion.waitVanish(Pattern("FnrefuxConne.png").similar(0.84))
wait(9)
#click login in Firefox
firefoxRegion.click(Pattern("Username.png").similar(0.73).targetOffset(3,3))
type("admin")
firefoxRegion.click(Pattern("Password.png").similar(0.75).targetOffset(-5,-1))
type("service-cloud")
firefoxRegion.click(Pattern("1375887066824.png").targetOffset(-1,-3))
firefoxRegion.click(Pattern("CaseHistmQ.png").similar(0.83).targetOffset(-1,-1))
firefoxRegion.click(Pattern("Enterc0bruws.png").similar(0.86))
type("v",KEY_CTRL)
firefoxRegion.click(Pattern("1375891719591.png").similar(0.79))

chromeRegion.click(Pattern("Firstandlast-1.png").similar(0.81))
type("customer")
chromeRegion.click(Pattern("1375891945390.png").similar(0.79))
chromeRegion.click(Pattern("1375892013250.png").similar(0.82))

print("Customer and Agent joined session")

#verify the Mutual Funds
chromeRegion.click(Pattern("MUTUALFUNDS.png").similar(0.87))
#verify Personal Information on both the page

firefoxRegion.exists(Pattern("PersonalInfo.png").similar(0.93))
print("Personal Information page")

chromeRegion.click(Pattern("FirstName.png").similar(0.93))
type("qaFN")
#chromeRegion.click(Pattern("LastName-1.png").similar(0.89))
type(Key.TAB+ "qaLN")
chromeRegion.wheel(Pattern("PersonalInfo.png").similar(0.93), WHEEL_DOWN,5)
chromeRegion.click(Pattern("State.png").similar(0.88))
type("new")
#type(Key.DOWN + Key.ENTER)

chromeRegion.click(Pattern("NewYork.png").similar(0.89))

chromeRegion.click("U18.png")
chromeRegion.click(Pattern("3655.png").similar(0.86))
chromeRegion.click(Pattern("PasswordMusb.png").similar(0.88))
type("123456")
chromeRegion.click(Pattern("ComirmPasswo.png").similar(0.85))
type("123456")
chromeRegion.click(Pattern("1375893315443.png").similar(0.84))

chromeRegion.click(Pattern("Research.png").similar(0.84))
chromeRegion.click(Pattern("MutualFunds-1.png").similar(0.90))
chromeRegion.wheel(Pattern("MutualFunds-1.png").similar(0.90), WHEEL_DOWN,5)
firefoxRegion.exists(Pattern("Researchcomp.png").similar(0.88))
      
chromeRegion.click(Pattern("1375894616298.png").similar(0.86))
chromeRegion.wheel(Pattern("MutualFunds-1.png").similar(0.90), WHEEL_DOWN,10)
chromeRegion.click(Pattern("Additional.png").similar(0.79))

chromeRegion.click(Pattern("Internationa.png").similar(0.86))
chromeRegion.click(Pattern("LargeCap.png").similar(0.82))

chromeRegion.click(Pattern("SmallCap.png").similar(0.80))
chromeRegion.click(Pattern("Specialty.png").similar(0.86))
chromeRegion.click(Pattern("One8ourceFun.png").similar(0.89))
chromeRegion.click(Pattern("AllfundsatFS-1.png").similar(0.00).targetOffset(-67,1))
chromeRegion.click(Pattern("1375895042460.png").similar(0.83))
chromeRegion.click(Pattern("1375895097800.png").similar(0.76))
chromeRegion.click(Pattern("HVEIGQ1U.png").similar(0.82))
chromeRegion.click(Pattern("255U.png").similar(0.78))

chromeRegion.click(Pattern("Viewmatches5.png").similar(0.96))
#Screened Funds page
chromeRegion.click(Pattern("TGINX.png").similar(0.89).targetOffset(-18,1))
chromeRegion.click(Pattern("BClrA.png").similar(0.88).targetOffset(-26,1))
chromeRegion.click(Pattern("GLRBX.png").similar(0.83).targetOffset(-27,-2))
chromeRegion.click(Pattern("EXCPXIII.png").similar(0.00).targetOffset(-28,4))
chromeRegion.click(Pattern("1375986534314.png").similar(0.81))
chromeRegion.click(Pattern("ScheduleAppo.png").similar(0.86))
chromeRegion.wheel(Pattern("ScheduleAppo.png").similar(0.86), WHEEL_DOWN,5)
chromeRegion.click(Pattern("Selectadate.png").similar(0.87))
chromeRegion.doubleClick(Pattern("irSa.png").similar(0.88))
chromeRegion.doubleClick(Pattern("irSa.png").similar(0.88))
chromeRegion.click(Pattern("18.png").similar(0.94))
#firefoxRegion.exists()

chromeRegion.click(Pattern("1anQm1arr.png").similar(0.93).targetOffset(23,2))
#chromeRegion.click(Pattern("Tam.png").similar(0.93).targetOffset(3,3))
type(Key.DOWN+ Key.ENTER)

chromeRegion.click(Pattern("to-1.png").similar(0.91).targetOffset(20,0))
type(Key.DOWN+ Key.DOWN + Key.ENTER)

#chromeRegion.click(Pattern("10am-1.png").similar(0.92).targetOffset(7,1))
chromeRegion.click(Pattern("Phonenumber.png").similar(0.88))
type("902-555-5555")
chromeRegion.click(Pattern("1375988089686.png").similar(0.91).targetOffset(9,-2))
chromeRegion.click(Pattern("App0intmentC.png").similar(0.86))
chromeRegion.wheel(Pattern("App0intmentC.png").similar(0.86), WHEEL_DOWN,5)

chromeRegion.exists(Pattern("Thankyoufors.png").similar(0.90))
firefoxRegion.exists(Pattern("Thankyoufors-1.png").similar(0.90).targetOffset(26,2))
print("Appointment confirmed for customer and replicated to Agent")
#College Savings
chromeRegion.click(Pattern("anaccounttha.png").similar(0.90))

chromeRegion.wheel(Pattern("PersonalInfo.png").similar(0.93), WHEEL_DOWN,5)

chromeRegion.click(Pattern("1375893315443.png").similar(0.84))
chromeRegion.wheel(Pattern("CollegeSavin.png").similar(0.90), WHEEL_DOWN,5)
chromeRegion.click(Pattern("AddChlld.png").similar(0.80))
chromeRegion.click(Pattern("Child2-1.png").similar(0.90))
chromeRegion.click(Pattern("AddChlld.png").similar(0.80))
chromeRegion.click(Pattern("Child3.png").similar(0.93).targetOffset(-2,4))
chromeRegion.click(Pattern("Child2.png").similar(0.97).targetOffset(1,-1))
chromeRegion.click(Pattern("Childl-1.png").similar(0.90))

chromeRegion.type("exJohn.png", "qaFN qaLN")
chromeRegion.type(Pattern("1376081265734.png").similar(0.80), "6")
chromeRegion.doubleClick(Pattern("1376081314446.png").similar(0.90))
type("8800")
chromeRegion.doubleClick(Pattern("1376081355919.png").similar(0.90))
type("200")
chromeRegion.doubleClick(Pattern("1376081403092.png").similar(0.80))
type("1000")
#chromeRegion.wheel(Pattern("urrentannual.png").similar(0.80), WHEEL_DOWN,5)
chromeRegion.doubleClick("1376081432531.png")
type("9")
chromeRegion.dragDrop(Pattern("1376081629200.png").similar(0.80), Pattern("1376081637251.png").similar(0.98).targetOffset(13,0))
chromeRegion.wheel(Pattern("ofcostfunded.png").similar(0.90), WHEEL_DOWN,5)
chromeRegion.click(Pattern("Toreceivemor.png").similar(0.90))
chromeRegion.wheel(Pattern("ScheduleAppo.png").similar(0.86), WHEEL_DOWN,5)
chromeRegion.click(Pattern("1376082355032.png").similar(0.80))
chromeRegion.doubleClick(Pattern("irSa.png").similar(0.88))
chromeRegion.doubleClick(Pattern("irSa.png").similar(0.88))
chromeRegion.click(Pattern("18.png").similar(0.94))
#firefoxRegion.exists()

chromeRegion.click(Pattern("1anQm1arr.png").similar(0.93).targetOffset(23,2))
#chromeRegion.click(Pattern("Tam.png").similar(0.93).targetOffset(3,3))
type(Key.DOWN+ Key.DOWN + Key.ENTER)

chromeRegion.click(Pattern("to-1.png").similar(0.91).targetOffset(20,0))
type(Key.DOWN+ Key.DOWN + Key.DOWN + Key.ENTER)

#chromeRegion.click(Pattern("10am-1.png").similar(0.92).targetOffset(7,1))
chromeRegion.doubleClick(Pattern("1376083047331.png").similar(0.88).targetOffset(-42,-2))
type("902-555-6666")
chromeRegion.click(Pattern("1375988089686.png").similar(0.91).targetOffset(9,-2))
chromeRegion.click(Pattern("App0intmentC.png").similar(0.86))
chromeRegion.wheel(Pattern("App0intmentC.png").similar(0.86), WHEEL_DOWN,5)

chromeRegion.exists(Pattern("Thankyoufors.png").similar(0.90))
firefoxRegion.exists(Pattern("Thankyoufors-1.png").similar(0.90).targetOffset(26,2))

#INSURANCE


chromeRegion.click(Pattern("529plancanne.png").similar(0.88).targetOffset(-7,7))
chromeRegion.wheel(Pattern("PersonalInfo.png").similar(0.93), WHEEL_DOWN,5)
chromeRegion.click(Pattern("1375893315443.png").similar(0.84))
chromeRegion.wheel(Pattern("LifeInsuranc.png").similar(0.86), WHEEL_DOWN,5)
chromeRegion.click(Pattern("1376074423196.png").similar(0.78))
chromeRegion.wheel(Pattern("LifeInsuranc.png").similar(0.86), WHEEL_DOWN,10)
if chromeRegion.exists(Pattern("attnlstlrrNo.png").similar(0.86)):
    chromeRegion.click(Pattern("withFSIYesAd.png").similar(0.84))
else:
    print(" radio button is selected already")
    
chromeRegion.click(Pattern("Valuedellglp.png").similar(0.87).targetOffset(-19,-8))
if chromeRegion.exists(Pattern("eplaclngN0.png").similar(0.88)):
    chromeRegion.click(Pattern("AreyourYes.png").similar(0.87))
else:
    print(" radio button is selected already")
chromeRegion.click(Pattern("Continue.png").similar(0.80))
chromeRegion.wheel(Pattern("OptionalLife.png").similar(0.89), WHEEL_DOWN,5)
chromeRegion.click(Pattern("ClaimantSi.png").similar(0.86))
chromeRegion.click(Pattern("OnlineWillF.png").similar(0.90))
chromeRegion.click(Pattern("FlexPaymentp.png").similar(0.80))
chromeRegion.click(Pattern("Continue-1.png").similar(0.90))
chromeRegion.wheel(Pattern("FSILifeInsur.png").similar(0.89), WHEEL_DOWN,10)
chromeRegion.doubleClick(Pattern("sooooo.png").similar(0.83))
type("35000")
chromeRegion.click(Pattern("Term1U.png").similar(0.80))
type(Key.DOWN + Key.ENTER)
chromeRegion.click(Pattern("1376075744208.png").similar(0.89).targetOffset(-1,-4))
chromeRegion.doubleClick(Pattern("1376076738434.png").similar(0.90).targetOffset(0,2))
chromeRegion.doubleClick(Pattern("1376076738434.png").similar(0.90).targetOffset(0,2))
chromeRegion.click(Pattern("1376075873959.png").similar(0.86).targetOffset(4,-1))
chromeRegion.click(Pattern("Continua.png").similar(0.80))
chromeRegion.wheel(Pattern("LifeInsuranc-1.png").similar(0.86), WHEEL_DOWN,5)
chromeRegion.exists(Pattern("CoverageTerm.png").similar(0.80))
chromeRegion.click(Pattern("HuyOnline.png").similar(0.81))
chromeRegion.wheel(Pattern("LifeInsuranc-2.png").similar(0.80), WHEEL_DOWN,5)
chromeRegion.click(Pattern("Areyoumarrie.png").similar(0.81).targetOffset(66,8))
chromeRegion.click(Pattern("childrenYes.png").similar(0.90).targetOffset(23,-2))
chromeRegion.click(Pattern("55Yes.png").similar(0.90).targetOffset(12,-1))
chromeRegion.click(Pattern("zenYes.png").similar(0.90).targetOffset(18,0))
chromeRegion.click(Pattern("ifeBYes.png").similar(0.90))

chromeRegion.click(Pattern("Csntinue.png").similar(0.90))

chromeRegion.wheel(Pattern("LifeInsuranc-3.png").similar(0.90), WHEEL_DOWN,10)

chromeRegion.click(Pattern("lUIillplomat.png").similar(0.90).targetOffset(16,-6))
chromeRegion.click(Pattern("TiITiUIiEthc.png").similar(0.90))
chromeRegion.click(Pattern("ponedNo.png").similar(0.90))
chromeRegion.click(Pattern("tesforYes.png").similar(0.90))
chromeRegion.click(Pattern("tnotYes.png").similar(0.80))
chromeRegion.click(Pattern("Continue-2.png").similar(0.80))

chromeRegion.wheel(Pattern("LifeInsuranc-3.png").similar(0.90), WHEEL_DOWN,10)
chromeRegion.click(Pattern("lHolder.png").similar(0.90))
type("qaFN qaLN")
chromeRegion.click(Pattern("CardNumber.png").similar(0.90).targetOffset(-56,3))
type("1234" + Key.TAB + "5678" + Key.TAB + "1234" + Key.TAB + "5678")
chromeRegion.click(Pattern("Date-1.png").similar(0.80))
type(Key.DOWN+ Key.ENTER)
chromeRegion.click(Pattern("lE.png").similar(0.95))
type(Key.DOWN+ Key.ENTER)
chromeRegion.click(Pattern("CW-1.png").similar(0.90))
type("123")
chromeRegion.click(Pattern("monthsYes.png").similar(0.90))
chromeRegion.click(Pattern("1376078809225.png").similar(0.90))


chromeRegion.wheel(Pattern("LifeInsuranc-3.png").similar(0.90), WHEEL_DOWN,10)
chromeRegion.exists(Pattern("LIFEINSURANC-4.png").similar(0.80))

chromeRegion.click(Pattern("ViewOurIFCMu.png").similar(0.80))

chromeRegion.wheel(Pattern("PersonalInfo.png").similar(0.93), WHEEL_DOWN,5)

chromeRegion.click(Pattern("1375893315443.png").similar(0.84))
print("Workflow coverage ends")





#select dashboard and 
while ieRegion.exists(Pattern("Dashboard.png").similar(0.81)):
    find(Pattern("NameGues-1.png").similar(0.76)).right().click(Pattern("Action.png").similar(0.68))
    print "Clicked on go successfully"
#else:
 #   ieRegion.click(Pattern("Dashboard-1.png").similar(0.75))
  #  wait(2)
    #find(Pattern("NameGues-1.png").similar(0.87)).right().click(Pattern("Action.png").similar(0.84))
 


scrollWheel = ieRegion.wheel(Pattern("FinancialSer.png").similar(0.87), WHEEL_DOWN,5)













