# rpi-music-synth
A Raspberry Pi music synthesizer developed in Python using analog/digital GPIO input. Programmed using the Pygame library. Created as my HS Capstone Project (June 2024-May 2025)

# Key Functionality
- 12 keys
- 8 preloaded instruments
- 8 preloaded octaves
- Volume control
- Fade-In slider
- Fade-Out slider
- Sample maxtime slider
- Sample looping slider

# Materials:

## Electronic Components:
- Raspberry Pi (Model 4b)
- RPi GPIO Extension Board & Ribbon Cable (Optional)
- 330 Ohm Resistors
- 12x [SPST Momentary Pushbuttons](https://www.amazon.com/gp/product/B0752RMB7Q/ref=ox_sc_act_image_1?smid=A2O4FZXIRZDLHA&psc=1)
- 1x [8-position Rotary Switch](https://www.microcenter.com/product/503961/adafruit-industries-mini-8-way-sp8t-rotary-selector-switch)
- 1x [DPDT Toggle Switch](https://www.amazon.com/mxuteuk-Terminal-momentary-Miniature-Dashboard/dp/B07XHQ8WB4/ref=sr_1_1_sspa?crid=1773VVCD7SDNM&dib=eyJ2IjoiMSJ9.5Z_yWvlQfiTKf29To1uc0QIPQaWVbt-wvVpYmgMLAirgE7DWbOZxQLEFCPUIXwVQxRs64aOuSqRgqlS7u2fgF1vG2X3d-InTJce6sGhB5oIV8CR6ruXM-CouFz1W96Y1zLh_r-ulZ5LMdTtzt5BM3peDr2Tpir3OKhJcr02Mv08PnmBv0Co97xMSls0f3c7yBUa4SdS3XI5TrCGQMc996RPrrprBguMf82B0HWh_7B287bkTQBfhaYKenjxPG3--2pIadT1btp5s-Sy6y6dhzRHdsK6DYXzpz80DqEx0VBQ.FlkuBf6ml4ksVzmfxKNdycWG05C_ZgP-5Y1ni0xUUSs&dib_tag=se&keywords=DPDT%2Bmomentary%2Btoggle%2Bswitch%2Bsmall&qid=1724120175&s=automotive&sprefix=dpdt%2Bmomentary%2Btoggle%2Bswitch%2Bsmal%2Cautomotive%2C97&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
- 1x [MCP3008 Analog-to-Digital Converter](https://www.amazon.com/Bridgold-MCP3008-I-8-Channel-Converters-Interface/dp/B0C5774W5S/ref=sr_1_3_pp?dib=eyJ2IjoiMSJ9.l233e6wO95Dr2Efw5ALMwapiEDjEAGz7MbIF96Owz6KqvZ-xAz2_EXAONa9inPHxk7N68GQD_ogK-XgHf2fWSSH7s-lCzvSvdAFkJ1ZM5YadeEsz0K26R29tS4wqlB8uwcx_WvQ5K0b4p4B6dgAx6FmC3h-Rwp5EfdPD-yldbAbscsd0O-SVqhuyr5jkgVTMSoyHUJCry95k7adsFLYmKEqqtrYIlvGsEdBCbiXhfVE.ENTCglBKgeKIMuJor5lv3A5YeklPDd38JuN7ViWU3Pg&dib_tag=se&keywords=mcp3008+-+8-channel+10-bit+adc+with+spi+interface&qid=1757521384&sr=8-3) (This is required to take analog input on rpi!)
- 1x [Rotary Potentiometer](https://www.amazon.com/DGZZI-Potentiometer-Breadboard-Raspberry-3386MP-103/dp/B07ZYVS2W6/ref=sr_1_1_sspa?crid=W5QH3PKLVY26&dib=eyJ2IjoiMSJ9.hIoYTLYwhX42jpUQ-hv-c-ftjWzcYw_9SR0w16RrMg6SnRgooK6pN-C4G8kI0Fqy40etedxaerX7hg4OHSl_djABM4zkCDyOnpSU3UVP2Adl3ojgEzxbO-tCXWbBmpOW5_q0lZM86zIfLSHSM3cy7_8t9DxaHpMhTzzgGLFy-RJigTrg7ZdwDs5w86BeonX6VAVzhlevXDlxiqvPUjZ5kbMQjvnjERCDTUhYIJf1Od8.THdtucpndPN7q4d6xQsM0pzLDbNchZAhjp6CMQKq1Nc&dib_tag=se&keywords=raspberry+pi+potentiometer&qid=1723496022&sprefix=raspberry+pi+potentiomete%2Caps%2C92&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- 4x [Slide Potentiometer](https://www.amazon.com/uxcell-Variable-Resistors-Potentiometer-Potentiometers/dp/B07VY7V23Q?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1THAZDOWP300U)
Learn about the compenents in this [short video](https://drive.google.com/file/d/1tuv9_5-nAZ0iDRsu3ioJO4GTKNPm3BZK/view?usp=drive_link)

## Fabrication
- SD or MicroSD Card (no need for a lot of storage)
- Double Sided PCB Prototyping Boards
- Small breadboard
- 22awg Solid-Core Wire (or any easily breadboardable wire)
- 8/10mm M3 Hex-Head Machine Screws, Nuts
- 3D Printed Housing
- External Speaker with Headphone Jack (rpi has the port built-in)
 
## Equipment
- Soldering Iron
- FDM 3D Printing
- Allen Key

[The internals will look like the above...](DALAL_rpi-music-synth_Guts_Image.jpg)
  
[But the final product will be much cleaner!](DALAL_rpi-music-synth_Product_Image.jpg)

To learn more about the process, see my [Presentation](https://drive.google.com/file/d/1W-1bLab3v_ig_CBMy4-p-iqJWPmVLeuu/view?usp=drive_link), which won me the Project of Excellence Award! 
