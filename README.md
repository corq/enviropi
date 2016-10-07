# enviropi
Code for running the Enviro pHat for the Raspberry Pi Zero

## Installation ##

* Copy `enviropi.service` to `/etc/systemd/system/`
* Copy `enviropi-web.service` to `/etc/systemd/system/`
* `systemctl enable enviropi.service`
* `systemctl start enviropi.service`
* `systemctl enable enviropi-web.service`
* `systemctl start enviropi-web.service`
