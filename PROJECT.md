# BC-250 Project Context

Canonical, compact context for this AMD BC-250 build. Keep durable facts and decisions here; use GitHub issues only for unresolved work.

## Hardware

- AMD BC-250
- Enclosure: https://www.printables.com/model/1737913-amd-bc-250-industrial-style-case-for-flexatx-witho

## Linux / cooling

- Custom fan-control script: `/usr/local/bin/bc250-fancurve`
- Fan-curve configuration: `/etc/bc250-fancurve.conf`
- Fan controller hwmon device: `nct6686`
- CPU temperature hwmon device: `k10temp`
- `/sys/class/hwmon/hwmonN` numbering is not stable across reboots or kernel changes; scripts should discover devices using `/sys/class/hwmon/hwmon*/name`.
- Fan control is intended to run under systemd and restart after unexpected failure.

## References

- BC-250 documentation: https://elektricm.github.io/amd-bc250-docs/
- Enclosure / print notes: https://www.printables.com/model/1737913-amd-bc-250-industrial-style-case-for-flexatx-witho

## Tracking convention

- Put stable system facts, hardware choices, configuration conventions, and reference links in this file.
- Create GitHub issues only for concrete work that still needs investigation, implementation, purchase, testing, or repair.
- Keep issue bodies short and link back to this file instead of repeating project background.
