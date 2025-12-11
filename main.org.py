import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time


warnings.filterwarnings("ignore", category=DeprecationWarning)

def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print("A new version is available. Please download the latest version from GitHub.")
            time.sleep(3)
            return False
        return True
    except:
        return True


def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")
        return ""


def main():
    if not check_for_updates():
        return
    
    os.system(f"title Kichi779 - Twitch Viewer Bot @kichi#0779 ")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/u4T67NU6xb    
                             Github  github.com/kichi779    """)))
    announcement = print_announcement()
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")
    print("")
    

    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # Selecting proxy server
    print(Colors.green, "Proxy Server 1 Is Recommended")
    print(Colorate.Vertical(Colors.green_to_blue, "Please select a proxy server(1,2,3..):"))
    for i in range(1, 8):
        print(Colorate.Vertical(Colors.red_to_blue, f"Proxy Server {i}"))
    proxy_choice = int(input("> "))
    proxy_url = proxy_servers.get(proxy_choice)

    twitch_username = input(Colorate.Vertical(Colors.green_to_blue, "Enter your channel name (e.g Kichi779): "))
    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, "How many proxy sites do you want to open? (Viewer to send)")))
    
    # Ask if user wants to run without headless mode for debugging
    print(Colorate.Vertical(Colors.green_to_blue, "\nDo you want to see the browser windows? (Recommended for troubleshooting)"))
    show_browser = input("Enter 'y' for yes or 'n' for no (default: n): ").lower().strip()
    
    os.system("cls")
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/u4T67NU6xb    
                             Github  github.com/kichi779    """)))
    print('')
    print('')
    print(Colors.red, Center.XCenter("Starting viewer bot... Please wait for pages to load"))


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    
    # Add more realistic browser behavior
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Add a realistic user agent
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    # Only add headless if user doesn't want to see browser
    if show_browser != 'y':
        chrome_options.add_argument('--headless=new')  # Use new headless mode
    
    # ADBLOCK EXT - only in non-headless mode
    extension_path = 'adblock.crx'
    if os.path.exists(extension_path) and show_browser == 'y':
        chrome_options.add_extension(extension_path)
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Execute script to make Selenium undetectable
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # Maximize window if visible
    if show_browser == 'y':
        driver.maximize_window()
    
    driver.get(proxy_url)
    
    # Wait longer for first page
    print("Waiting for first page to load completely...")
    time.sleep(5)

    successful_tabs = 0
    failed_tabs = 0

    for i in range(proxy_count):
        try:
            print(f"\n[Tab {i+1}/{proxy_count}] Opening new tab...")
            
            # Open new tab
            driver.execute_script("window.open('" + proxy_url + "')")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(proxy_url)
            
            # Wait for page to load - increased time
            print(f"[Tab {i+1}/{proxy_count}] Waiting for page to load...")
            time.sleep(3)
            
            # Wait for page to be fully loaded
            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            time.sleep(2)
            
            print(f"[Tab {i+1}/{proxy_count}] Searching for URL input field...")
            
            # Try to find the input field with ID 'url' directly using JavaScript
            text_box = None
            try:
                text_box = driver.find_element(By.ID, 'url')
                # Verify it's the right input (type text, visible)
                if text_box.get_attribute('type') == 'text' and text_box.get_attribute('name') == 'url':
                    print(f"[Tab {i+1}/{proxy_count}] Found URL input field!")
                else:
                    text_box = None
            except:
                pass
            
            # If not found, try alternative method
            if text_box is None:
                try:
                    text_box = driver.find_element(By.CSS_SELECTOR, 'input[name="url"][type="text"]')
                    print(f"[Tab {i+1}/{proxy_count}] Found URL input field using CSS selector!")
                except:
                    pass
            
            if text_box is None:
                print(f"[Tab {i+1}/{proxy_count}] ERROR: Could not find URL input field")
                failed_tabs += 1
                continue
            
            # Now interact with the element
            print(f"[Tab {i+1}/{proxy_count}] Preparing to interact with input field...")
            
            # Wait a moment for any JavaScript to finish
            time.sleep(1)
            
            # Try to close any popups or overlays
            try:
                driver.execute_script("""
                    var overlays = document.querySelectorAll('[class*="modal"], [class*="popup"], [class*="overlay"]');
                    overlays.forEach(function(el) { el.style.display = 'none'; });
                """)
            except:
                pass
            
            # Scroll to element and click it first
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text_box)
            time.sleep(0.5)
            
            # Try clicking the element first to focus it
            try:
                text_box.click()
            except:
                # If normal click fails, try JavaScript click
                driver.execute_script("arguments[0].click();", text_box)
            
            time.sleep(0.5)
            
            # Clear and send keys using JavaScript as fallback
            print(f"[Tab {i+1}/{proxy_count}] Entering Twitch URL...")
            try:
                text_box.clear()
                time.sleep(0.3)
                text_box.send_keys(f'www.twitch.tv/{twitch_username}')
                time.sleep(0.5)
                text_box.send_keys(Keys.RETURN)
            except ElementNotInteractableException:
                # Fallback: use JavaScript to set value
                print(f"[Tab {i+1}/{proxy_count}] Using JavaScript fallback...")
                driver.execute_script(f"arguments[0].value = 'www.twitch.tv/{twitch_username}';", text_box)
                time.sleep(0.3)
                # Try to trigger the form submission
                driver.execute_script("""
                    var event = new Event('input', { bubbles: true });
                    arguments[0].dispatchEvent(event);
                """, text_box)
                time.sleep(0.3)
                # Submit the form
                try:
                    text_box.send_keys(Keys.RETURN)
                except:
                    driver.execute_script("arguments[0].form.submit();", text_box)
            
            successful_tabs += 1
            print(f"[Tab {i+1}/{proxy_count}] ✓ Successfully sent viewer!")
            
            # Wait for Twitch page to load in the proxy
            print(f"[Tab {i+1}/{proxy_count}] Waiting for Twitch to load...")
            time.sleep(5)
            
            # Try to unmute and play the video (helps with viewer count)
            try:
                driver.execute_script("""
                    setTimeout(function() {
                        var video = document.querySelector('video');
                        if (video) {
                            video.muted = false;
                            video.play();
                        }
                    }, 3000);
                """)
            except:
                pass
            
            # Delay between tabs
            time.sleep(2)
            
        except ElementNotInteractableException as e:
            print(f"[Tab {i+1}/{proxy_count}] ERROR: Element not interactable - {str(e)[:100]}")
            failed_tabs += 1
        except Exception as e:
            print(f"[Tab {i+1}/{proxy_count}] ERROR: {str(e)[:100]}")
            failed_tabs += 1

    print(f"\n{'='*50}")
    print(f"SUMMARY: {successful_tabs} successful | {failed_tabs} failed")
    print(f"{'='*50}\n")
    
    input(Colorate.Vertical(Colors.red_to_blue, "Press Enter to close all browser windows and exit..."))
    driver.quit()


if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================