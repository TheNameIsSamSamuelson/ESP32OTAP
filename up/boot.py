from main.ota_updater import OTAUpdater
import machine
from scron.week import simple_cron
from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
led.off()

simple_cron.run() # You have to run it once. This initiates the SimpleCRON action, and reserve one timmer.
def download_and_install_update_if_available():
    try:
        led.on()
        adress = 'https://github.com/TheNameIsSamSamuelson/esp32'
        wifiAuth = []
        wifiAuth.append(["dasda", "asdasda"])
        wifiAuth.append(["aa", "12345678"])
        ota_updater = OTAUpdater(adress,wifiAuth)
        for i in range(5):
            if ota_updater.is_network_avaliable():
                ota_updater.download_and_install_update_if_available()
                if ota_updater.check_for_update_to_install_during_next_reboot():
                    led.off()
                    machine.reset()
        led.off()
    except:
        # Little light freakOut so I get it that something went wrong on updating
        led.off()
        for i in range(50):
            led.value(not led.value())
            sleep(0.05)
        led.off()
def start():
    print("ds")
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    print("ds")

def boot():
    download_and_install_update_if_available()
    start()

# Schedule download_and_install_update_if_available() to run every fourth minute.
simple_cron.add('Every fourth minute',lambda *a,**k: download_and_install_update_if_available(),minutes=range(0, 59, 4),seconds=0)


boot()