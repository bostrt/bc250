# BC250 fan curve

This directory contains the files for the target BC250 system:

- `bc250-fancurve` -> `/usr/local/bin/bc250-fancurve`
- `bc250-fancurve.conf` -> `/etc/bc250-fancurve.conf`
- `bc250-fancurve.service` -> `/etc/systemd/system/bc250-fancurve.service`

The controller uses only the Python 3 standard library. It discovers `nct6686`
and `k10temp` from their hwmon `name` files each time it starts.

## Curve configuration

In `[curve]`, each numeric key is an inclusive maximum CPU temperature in
degrees Celsius and its value is the PWM setting to use from 0 through 255.
Thresholds may be integers or decimals and are sorted numerically. Temperatures
above the highest threshold use `default`.

`poll_interval_seconds` must be greater than zero. If the configuration file is
missing, the controller uses built-in defaults matching `bc250-fancurve.conf`.
Malformed or incomplete configuration files still cause startup to fail, so
configuration mistakes are not silently ignored. Restart the service on the
target system after changing the configuration.
