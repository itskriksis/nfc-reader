import android

def on_new_intent(intent):
    extras = intent.getExtras()
    if extras and extras.containsKey('android.nfc.extra.TAG'):
        tag = extras.get('android.nfc.extra.TAG')
        print("Card detected:", tag)

droid = android.Android()
droid.makeToast("Bring an NFC card close to the phone's NFC sensor.")
droid.startTrackingNFC()
while True:
    event = droid.eventPoll(1).result
    if event and event['name'] == 'new_intent':
        intent = event['data']
        on_new_intent(intent)
