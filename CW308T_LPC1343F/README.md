# CW308T-LPC1343

This board supports the NXP LPC1343 microcontroller.

![](Images/CW308T_LPC1343.PNG)

---

## Specifications

| Feature | Notes/Range |
|---------|----------|
| Target Device | LPC1343 |
| Target Architecture | Arm Cortex-M3 |
| Vcc | 3.3V |
| Programming | UART, USB, SWD |
| Hardware Crypto | No |
| Availability | Source files |
| Status | In development |
| Shunt | TBD |

## Power Supply

The core of the LPC1343 chip runs from a 3.3v supply. This is supplied
through the CW308T filter and delivered across a shunt resistor for
power analysis. The I/O buses are also supplied with 3.3v.

---

## Code Read Protection

The LPC13\*\* family uses a code read protection feature to restrict
access to application code after programming. This read protection
can be bypassed using voltage glitching.

---

## Programming

UART and USB bootloaders are supported on these devices.

Serial Wire Debug (SWD) is supported for programming and debugging
applications.

---

## Schematic and Layout

See GIT Repo for design files.
