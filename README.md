Black.AI design challenge submission by Dr. Nick Downing, 31/1/2019.

# Introduction

In this challenge I am asked to create an enclosure for a CUS30M power supply.
The enclosure must allow for 240V input, 12V output, and airflow. It must be
manufacturable within one week at a budget of AUD90 or less.

# Casing

I have selected a Jaycar Jiffy Box as the casing. The Jiffy Box has external
dimensions of 130 x 68 x 44 mm. Referring to the Mouser catalogue entry for the
CUS30M (see doc/ directory), the CUS30M has dimensions 76.2 x 50.8 x 21.7mm.
This gives about 50 mm spare, in the longest axis, which I will use about half
of for the 240V connector. There will be ample air space around the CUS30M.

The casing will need to be modified to the application, as follows:
* Cut out a 18.5 x 15 mm rectangle on one end for the 240V input.
* Cut out a 7 x 7.5 mm rectangle on the other end for the 12V output.
* Drill a grid of 3 x 3 holes on each side, at a spacing one quarter the height
of the box, biased towards the end of the power supply which gets hottest, this
might need to be adjusted based on experiment.

I will carry out these steps manually, using a Vernier caliper to measure, and
a sharp knife and a hand drill. Since a timeframe of one week is specified,
I assume that the request is for a prototype and that manufacturing issues can
be put on hold for the time being. Should a short production run be ordered, I
would consider either making a cutting template or requesting a quote for CNC.

# Fixing the CUS30M

I have not provided screw holes for mounting the CUS30M, since if there are
metal protrusions the case would need to be grounded. Instead I will place a
blob of silicon adhesive at each corner and simply glue it to the base of the
Jiffy Box, with some clearance underneath the PCB for cooling airflow.

# Connecting to the CUS30M

According to page 5/14 of the CUS30M installation manual, the connectors for
the 240V and 12V are J.S.T. B2P3-VH(LF)(SN) and B4P-VH(LF)(SN) respectively.

To manufacture this properly, the specified connector pins, housings, and wire
will have to be sourced and the specified crimping tool YC-930R or YC-931R
used. I have not attempted to source these as of yet, since it is a significant
hassle to do so. For the time being I'll simply solder to the PCB or the pins.

# 12V connector

I have selected from Digikey the Tensility International Corp 10-02950 cable
assembly. It will slide into the 7 x 7.5mm hole in the case and hold itself in
position. It has bare wire connectors, which I will solder onto the CUS30M.

# 240V connector

I have selected from Digikey the Qualtek 770W-X2/10. It is intended as a PCB
mounted part, but due to the selected case it must be mounted flush with the
base of the case. To avoid the PCB through-hole pins and locator tabs hitting
the case, I will mount this upside down. It will hold itself securely in place,
even though there is a small gap underneath due to the upside-down orientation.
For more robustness, this gap can optionally be filled with silicon adhesive.

I will solder some short wires from the PCB through-hole pins to the CUS30M.

# Airflow

The case is designed to be attached to a wall. The Jiffy Box selected is of the
Bulkhead type, meaning that it has built-in wings with screw mounting holes.
It should be mounted so that one set of air holes is at the bottom and the
other set at the top. This should allow natural convection to cool the CUS30M.
The cooling is probably also sufficient even if not mounted in the ideal way.

# Bill of materials

Jiffy Box: AUD 4.45
Tensility 10-02950 (12V cable assembly): USD 2.82
Qualtek 770W-X2_10 (240V socket connector): USD 0.76
Parfix 40g clear all-purpose silicone: AUD 4.45
Sundries such as wire, solder, etc: negligible

This is well within the specified price range, the only concern is labour cost.

# 3D model

The model has been constructed in FreeCAD. It consists of four parts, the
base, the lid, the DC connector and the AC connector. I have used an exploded
view, to show how these come together while allowing to see inside the case.

The requested .STEP file is saved as "cus30m_case.step". In case of any issue,
the original FreeCAD file has also been saved, as "cus30m_case.fcstd".

In addition to this, the Python script file "cus30m_case.py" used to generate
the model may also be of interest. I started building the model using the 2D
sketcher and extruder, but I had trouble with things like getting FreeCAD to
snap to grid properly and so on. Hence, it was easiest to create the model
using FreeCAD's scripting language, which I've used extensively in the past.

As an added benefit, the script is parametric, and so it was a trivial matter
to regenerate it for the 130 x 68 x 44 mm Jiffy Box when I realized that the
originally planned 83 x 54 x 31 mm Jiffy Box would not give enough room.

# Source documents

All of the documents that I worked from (containing the quoted prices,
dimensions etc) are in the doc/ directory of the repository, in pdf format.
