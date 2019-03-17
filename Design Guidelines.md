# CW308 Target Design Guidelines #
## Schematic Guidelines ##
Template: 
Start with StandardSch_Letter_Template.SchDoc found in TARGET_TEMPLATE Use two schematic sheets for more complex designs, one with header connections and one for all others

Net Names:
Begin power net names with a sign, do not use decimal points (eg. +3v3, -5v)
Use GND as ground net, prepend letters for other grounds (eg. AGND, DGND)
Label all significant nets to aid in routing and readability

Wiring Schematic:
Avoid 4-way junctions is schematic, can create bad behavior in Altium, Minimize wire crossover
Attempt to organize parts into functional blocks on schematic sheets

Annotating Schematics:
Annotate components as you finish functional blocks, aid readability by starting in the upper-left corner
Set the project Name, license, and Revision by right clicking on the project>Project Options>Parameters
Revisions start at -01
Title sheets by right-clicking in the sheet >Options>Document Parameters
Number sheets by clicking tools>Annotation>Number Schematic Sheets

## PCB Layout ##
Template:
Start with NewAE_PCB_Target_Template.PcbDoc found in TARGET_TEMPLATE
Board size should already be correct (2055x2540mil) and basic design rules configured

Component placement:
Place components beginning with the main connector headers (align at bottom of board)
Place main chip while thinking about the following priorities
1.	Power measurement, sense lines should be uncrowded and not change layers
2.	UART and JTAG should be easy to route if possible
3.	Keep clock lines isolated if at all possible

Must-Have checklist:
•	Power in, core voltage through filter
•	Clock in (including termination resistor)
•	Power measurement, low noise routing
•	Serial connection
•	Trigger (gpio) on GPIO4
•	Bootloader enable on PDIC (if valid)
•	JTAG/SWD interface
•	All GND and Vref connections to UFO board

If possible checklist:
•	GPIO pins out to LEDs
•	Special interfaces like USB, RF
•	Extra GPIO out to H pins

Silkscreen:
Place component designator to be read from left-to-right or bottom-to-top
Favor designator placement above or to the right of the component
Favor designator placement that aligns with the component
Label breakout pins as corresponding pins on the chip (ie. PA01 for a GPIO)

## Panelization ##
Template:
Start with Target_Panel_Template.PcbDoc found in TARGET_TEMPLATE

Board Array:
Double click the board array object and link to the target board PCB3
Space the boards 5mils apart horizontally and vertically
If everything is sized correctly vscore lines should be equidistant to all board edges 
IF NOT, board is probably different size. Adjust spacing to correct

## Production Files ##
Variants:
If board has optional components, create a production variant (Project>Variants>Add Variant)
Change optional components to Not Fitted on production variant
Ensure changes are pushed to PCB and Panel

Outjob:
Start with newae_outjob.OutJob found in Dropbox>CW308T>TARGET_TEMPLATE
Select production variant
Select PCB file as the source for the Gerber, NC Drill, and IPC-2581 outputs
Select Panel file as the source for both panel outputs
Generate content

File Packaging:
From output folder, copy all gerber files (with extensions beginning with G) to new folder named after the board revision (eg. -01)
From output folder, copy the NC drill files to the new folder, change extension to .NCDRILL

Copy README.txt from TARGET_TEMPLATE to new folder, verify it is correct
Zip up contents of folder
Zip up just the .GTP file as the stencil source

**WATCH FOR 4-LAYER PCBS - DEFAULT OUTJOB AND README DO NOT INCLUDE THESE FILES**




