import pyfprint, time, threading
pyfprint.fp_init()

try:
    dev = pyfprint.discover_devices()[0]
    dev.open()

    dev.identify_finger([])
    time.sleep(3)
    dev.stop_identify_finger_async()
except Exception as e:
    print e
finally:
    if(dev.dev):
        dev.close()
    pyfprint.exit()