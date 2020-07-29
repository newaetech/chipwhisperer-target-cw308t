# CW308T-EFM32GG11

This board supports the Silicon Labs EFM32 Giant Gecko 11
microcontroller. The chip mounted on the target board is the
EFM32GG11B1.

This is a BETA target and not yet available. This page will continue to be updated until release. Gerbers are available in the GIT repo if you live dangerously.

![](Images/CW308T-EFM32GG11.PNG)

---

## Specifications

| Feature | Notes/Range |
|---------|----------|
| Target Device | EFM32GG11 |
| Target Architecture | Arm Cortex M4 |
| Vcc | 1.2V |
| Programming | Serial Bootloader |
| Hardware Crypto | Yes |
| Availability | Source files |
| Status | In development |
| Shunt | TBD |

## Power Supply

The core of the Giant Gecko chip runs from a 1.2v supply. This is
supplied and filtered through the CW308T. The I/O buses are supplied
with 3.3v.

---

## Security Features

For a full list of security features see the product family data
sheet\[1\]

---

## Programming

A serial bootloader is implemented on the Giant Gecko series of chips.
Details for the use of this feature are described in Silicon Labs
application note AN0042\[2\].

---

## Schematic and Layout

See GIT Repo for design files.

---


1.  <https://www.silabs.com/documents/public/data-sheets/efm32gg-datasheet.pdf>
2.  <https://www.silabs.com/documents/public/application-notes/an0042-efm32-usb-uart-bootloader.pdf>
