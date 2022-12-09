# CW308T-K82F

The Kinetis K82 contains a Cortex M4F core with various cryptographic and security features. This includes three (3!) separate AES engines, one of which has hardware masking support for side-channel (or ‘side band’ in the datasheet) protection.

In addition there is an AES accelerator for loading from flash memory, and a general-purpose higher-speed AES accelerator.

This target routes the trace pins onto the ChipWhisperer trace pins.

The Kinetis K82 has both 256KB of FLASH and SRAM, making it an ideal target for very resource-heavy algorithms.


---

## Specifications

| Feature | Notes/Range |
|---------|----------|
| Target Device | NXP MK82FN256VLL15 |
| Target Architecture | Arm Cortex-M4 |
| Vcc | 3.3V |
| Programming | JTAG |
| Hardware Crypto | Yes |
| Availability | Standalone  |
| Status | Prototype |
| Shunt | 10R |

## Power Supply

The K82F target runs from the 3.3v supply on the CW312T.

---

