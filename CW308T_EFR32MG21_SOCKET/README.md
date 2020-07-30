# CW308T-EFR32MG21-SOCKET

The EFR32MG21 board features a QFN32 socket that matches the EFR32MG21A/B footprint from Silicon Labs. The EFR32MG21A/B device features a number of security features, including a dedicated “Secure Element” or “Secure Vault” core that performs a secure boot operation, and DPA countermeasures on cryptographic primitives.

The RF section is not broken out to a 50-ohm matched header, but instead a simple 3-pin header which allows potential usage in laboratory environments.

As this board contains a QFN socket, it is ideally suited for experiments such as template attacks, or potentially damaging attacks which require replacement of the main IC. In addition, this target can be easily shipped without restrictions as it does not contain any cryptographic functions (no IC at all is included).

![](Images/NAE-CW308-EFR32MG21-SOCKET_web.jpg)

!!! attention
    This target requires an external programmer to reload code.

---

## Quick Links

* [Buy on Mouser](https://www.mouser.com/Search/Refine?Keyword=NAE-CW308T-EFR32MG21-SOCKET)
* [Buy on Webstore](http://store.newae.com/efr32mg21-with-32qfn-socket-target-for-cw308/)
* [Download Schematic](https://github.com/newaetech/chipwhisperer-target-cw308t/raw/master/CW308T_EFR32MG21_SOCKET/NAE-CW308T-EFR32MG21-SOCKET_Schematic.PDF)

## Specifications

| Feature | Notes/Range |
|---------|----------|
| Target Device | Not Included (fits EFR32MG21A010F1024 etc) |
| Target Architecture | Arm Cortex M33 |
| Vcc | 1.2V |
| Programming | JTAG |
| Hardware Crypto | Yes |
| Availability | Standalone |
| Status | Production |
| Shunt | 22-ohm |

## Power Supply

Break-out for various voltage rails, allowing over-driving of internal regulator to reduce noise for DPA measurements, or for testing fault injection detection capability.

---

## Security Features

EFR32MG21A (“Mighty Gecko Multiprotocol Wireless SoC”) has a high-performance Cortex M33 (TrustZone-M) with  a seperate “secure element” core that handles the secure boot operation, along with multiple cryptographic accelerators (both AES and ECC) that include advertised DPA countermeasures.

The EFR32MG21B adds the "secure vault" feature.

---

## Programming

A JTAG programmer is typically required for these devices.

---
