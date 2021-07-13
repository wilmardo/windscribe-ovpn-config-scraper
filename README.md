# windsribe-ovpn-config-scraper
Super easy and hacky openvpn config scraper for Windscribe.
Needs python >3.6!

## Updating

* Login on the Windscribe website with Chrome
* Go to https://windscribe.com/getconfig/openvpn
* Right click and choose 'View page source'
* Copy standard locations around line 202
* Paste them in the script at line 10 and adapt them with a multiline cursor edit

## Usage

* Login on the Windscribe website with Chrome
* Go to https://windscribe.com/getconfig/openvpn
* Open Network tools (F12) and switch to the Network tab
* Download a random config
* You will see an openvpn request, right mouseclick on it and choose for Copy as cURL
* Copy the value after the `-H 'cookie: ` which looks something like this
```
__cfduid=dc44f3d700cffdf4980471ef690d864f01549308117; ref=https%3A%2F%2Fwindscribe.com%2F; i_can_has_cookie=1; ws_session_auth_hash=16816824-1-1549308123-2375217c78912343458426d-41cdce3ac39c1e94ddf6; _pk_ref.3.1dc7=%5B%22%22%2C%22%22%2C1549310671%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.3.1dc7=*; _pk_id.3.1dc7=94d4b78104084f2a.1649308119.2.1549311565.1549310671.'
```

* Run the script like this:
```
python scraper.py "__cfduid=dc44f3d700cffdf4980471ef690d864f01549308117; ref=https%3A%2F%2Fwindscribe.com%2F; i_can_has_cookie=1; ws_session_auth_hash=16816824-1-1549308123-2375217c78912343458426d-41cdce3ac39c1e94ddf6; _pk_ref.3.1dc7=%5B%22%22%2C%22%22%2C1549310671%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.3.1dc7=*; _pk_id.3.1dc7=94d4b78104084f2a.1649308119.2.1549311565.1549310671."
```
