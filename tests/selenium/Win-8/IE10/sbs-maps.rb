require "json"
require "rubygems"
require "selenium-webdriver"
gem "test-unit"
require "test/unit"

class SbsMaps < Test::Unit::TestCase
    $browser = "internet_explorer"
    $version = "10"
    $platform = "Windows 8"

  def setup
    caps = Selenium::WebDriver::Remote::Capabilities.send($browser)
    caps.version = $version
    caps.platform = $platform
    caps[:name] = "SBS Maps - #{$platform} - #{$browser} #{$version}"

    puts "Sauce Labs Started - #{$platform} - #{$browser} #{$version}"

    @driver = Selenium::WebDriver.for(
      :remote,
      :url => "http://se_tester:857e9cee-e5c8-416a-85dd-38bb32a744d3@ondemand.saucelabs.com:80/wd/hub",
      :desired_capabilities => caps)
    @base_url = "https://web-staging.goinstant.org"
    @accept_next_alert = true
    @driver.manage.timeouts.implicit_wait = 30
    @verification_errors = []
  end
  
  def teardown
    @driver.quit
    puts "Teardown : SBS Maps - #{$platform} - #{$browser} #{$version}"
    #assert_equal [], @verification_errors
  end
  
  def test_sbs_maps
    @driver.get(@base_url + "/how-it-works")
    assert !5.times{ break if (element_present?(:id, "demo-left") rescue false); sleep 1 }
    assert !5.times{ break if (element_present?(:id, "demo-right") rescue false); sleep 1 }
    # ERROR: Caught exception [ERROR: Unsupported command [waitForFrameToLoad | id=demo-left | 5000]]
    # ERROR: Caught exception [ERROR: Unsupported command [waitForFrameToLoad | id=demo-right | 5000]]
    #sleep(2.5)
    #assert !5.times{ break if (element_present?(:css, ".gi-collapse > span:nth-child(1)") rescue false); sleep 1 }
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | id=demo-left | ]]
    # use switch_to.frame instead of selectFrame
    @driver.switch_to.frame "demo-left"
    verify { assert !element_present?(:css, "div.gi-collapse.collapsed > span") }
    @driver.find_element(:css, ".gi-collapse > span:nth-child(1)").click
    verify { assert element_present?(:css, "div.gi-collapse.collapsed > span") }
    # ERROR: Caught exception [ERROR: Unsupported command [selectWindow |  | ]]
    # use switch_to.default_content instead of selectWindow
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-right"
    verify { assert !element_present?(:css, "div.gi-collapse.collapsed > span") }
    @driver.find_element(:css, ".gi-collapse > span:nth-child(1)").click
    verify { assert element_present?(:css, "div.gi-collapse.collapsed > span") }
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-left"
    @driver.find_element(:css, "div.gi-collapse.collapsed > span").click
    verify { assert element_present?(:css, ".gi-collapse > span:nth-child(1)") }
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-right"
    @driver.find_element(:css, "div.gi-collapse.collapsed > span").click
    verify { assert element_present?(:css, ".gi-collapse > span:nth-child(1)") }
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-left"
    @driver.find_element(:id, "search-bar").send_keys "new york"
    assert !5.times{ break if (element_present?(:css, "div.pac-item-refresh:nth-child(1)") rescue false); sleep 1 }
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-right"
    @driver.find_element(:id, "search-bar").send_keys "new york"
    assert !5.times{ break if (element_present?(:css, "div.pac-item-refresh:nth-child(1)") rescue false); sleep 1 }
    i = 0
    zoom = 9
    while i <= zoom do
      @driver.find_element(:css, "div[title=\"Zoom in\"]").click
      i +=1
    end
    assert !5.times{ break if (element_present?(:css, "div[title=\"Rotate map 90 degrees\"] > img") rescue false); sleep 1 }
    @driver.switch_to.default_content
    @driver.switch_to.frame "demo-left"
    assert !5.times{ break if (element_present?(:css, "div[title=\"Rotate map 90 degrees\"] > img") rescue false); sleep 1 }
  end
  
  def element_present?(how, what)
    @driver.find_element(how, what)
    true
  rescue Selenium::WebDriver::Error::NoSuchElementError
    false
  end
  
  def alert_present?()
    @driver.switch_to.alert
    true
  rescue Selenium::WebDriver::Error::NoAlertPresentError
    false
  end
  
  def verify(&blk)
    yield
  rescue Test::Unit::AssertionFailedError => ex
    @verification_errors << ex
  end
  
  def close_alert_and_get_its_text(how, what)
    alert = @driver.switch_to().alert()
    alert_text = alert.text
    if (@accept_next_alert) then
      alert.accept()
    else
      alert.dismiss()
    end
    alert_text
  ensure
    @accept_next_alert = true
  end
end
