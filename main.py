import nfc
import binascii

def on_connect(tag):
    print("Card connected:")
    print(tag)

def on_release(tag):
    print("Card released")

def read_card(tag):
    print("Reeading card data:")
    print("UID:", binascii.hexlify(tag.identifier).decode('utf-8'))

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        print("NFC readeer initialized. Press Ctrl-C to exit.")
        clf.connect(rdwr={'on-connect': on_connect, 'on-release': on_release, 'on-startup': read_card})
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()