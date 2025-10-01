# [The Secret Life of Components - LEDs](https://www.youtube.com/watch?v=yvcITqw5iDY)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

## LED History and Development

### Early Development
- First observation of light emission from diodes (1900s)
- Henry Round's discovery with silicon carbide crystal
- First visible light LEDs available in 1960s
- Early applications in pocket calculators (1971)

### Basic LED Technology
- LED stands for Light Emitting Diode
- Semiconductor junction allowing one-way current flow
- Crystal radio "cat's whisker" as first semiconductor junction

## Basic LED Operation

### Electrical Properties
- Requires specific voltage (3V lithium coin cells work, 1.5V silver oxide don't)
- Must be connected with resistor to prevent overheating
- Polarity sensitive - marked with flat on negative side
- Positive wire longer than negative wire

### Safety and Protection
- LEDs won't be damaged by reverse connection
- Overvoltage causes immediate failure
- Resistor essential for normal operation
- 1k resistor commonly used for 12V supply

## LED Types and Characteristics

### Size and Brightness
- Various sizes: 2mm, 3mm, 5mm, 10mm
- Large LEDs not necessarily brighter than small ones
- Brightness measured in microcandelas (mcd) or lumens
- Viewing angle affects perceived brightness

### LED Varieties
- Diffused casing for wide-angle visibility
- Clear casing for narrow 15-degree beam
- Different colors available
- Flashing LEDs with built-in effects

## White LEDs

### Technology
- Blue LEDs with phosphor coating
- Phosphor converts blue/UV light to visible light
- Similar to fluorescent tube phosphors
- Different phosphor combinations create warm/cool white

### Color Mixing
- Primary color phosphors can be combined
- Ultraviolet excitation reveals true colors
- Warm white vs cool white variations

## Specialized LEDs

### Built-in Resistors
- LEDs with integrated resistors for 5V or 12V
- Rainbow LEDs that change color gradually
- Emergency scene LEDs (flashing blue/red)

### LED Strips
- 12V LED strips with three LEDs in series
- Self-adhesive backing
- Cuttable every three LEDs
- Common 18mm spacing (300 LEDs per 5m reel)
- 9mm spacing available (600 LEDs per reel)

## LED Strip Specifications

### Brightness Ratings
- Number prefixes indicate chip dimensions
- 5634 = 5.6mm x 3.4mm
- 2834 = 2.8mm x 3.4mm
- Larger chips = higher brightness

### Waterproof Strips
- Clear silicone casing
- More difficult to cut and join
- Shorter lifespan due to heat retention
- Best avoided unless outdoor use required

## Surface Mount LEDs

### Characteristics
- Extremely tiny components
- Soldered directly to circuit boards
- T-shaped marking (bar = positive)
- Self-adhesive copper tape method for soldering

### Soldering Requirements
- Adequate heat needed for proper joint
- Heat sinks built into components
- More challenging than through-hole LEDs

## LED Control and Dimming

### Traditional Dimming
- Variable resistor method
- Larger resistor = dimmer light
- Simple but inefficient

### PWM Dimming
- Rapid on/off switching
- Microcontroller controlled
- Proportion of on-time determines brightness
- More efficient than resistor method

## Addressable LEDs

### Technology
- Built-in control chips
- RGB (three primary colors)
- Single wire control
- Microcontroller required

### Applications
- Complex lighting effects
- Individual LED control
- Programmable patterns
- Requires programming knowledge

## LED Home Lighting

### Replacement Technology
- Replacing compact fluorescent lights
- More efficient and longer lasting
- No mercury pollution
- Various form factors available

### LED Bulb Types
- Traditional bulb shape with warm light
- Ring of tiny LEDs with optical diffusers
- LED tubes for fluorescent replacement
- Suspended ceiling panels

## LED Tubes

### Installation
- Cannot simply swap with fluorescent tubes
- Must remove ballast and starter
- Live at one end, neutral at other
- More directional light output

### Advantages
- No wasted backward light
- More efficient than fluorescent
- Easy installation with proper wiring

## LED Spotlights

### Characteristics
- Mostly 5W power rating
- ~30 degree beam angle
- GU10 fitting for mains voltage
- 12V versions still available

### Specialized Types
- 10 degree narrow beam (expensive)
- 8W high-power versions
- Various beam angles (25°, 40°)
- Car headlight-like focus

## Power LEDs

### High-Current LEDs
- Much higher current than standard LEDs
- Require heat sinks
- Star-shaped heatsink mounts
- 3.3-4V at 800mA rating

### Power Supply Options
- Constant current power supplies
- Constant voltage with proper resistor
- 12V supply with calculated resistance

## LED Resistor Calculations

### Ohm's Law Application
- V = I × R
- 12V supply, 0.8A current = 15Ω resistor
- Rough calculation method
- Experimental method more accurate

### Experimental Method
- Benchtop power supply with current limiting
- Variable resistor for testing
- Find transition point from current limiting
- Measure final resistance value

### Power Requirements
- Power = Volts × Amps
- 800mA × 12V = ~10W resistor needed
- Must use power resistors for heat dissipation

## LED Lenses and Optics

### Lens Types
- Various styles available
- Convert wide-angle to spotlight
- ~30 degree beam angle
- Perfect for machine applications

### Applications
- Internal machine lighting
- Focused illumination
- Similar to household spotlights
- Much smaller scale

## Terms

- **LED** - Light Emitting Diode, a semiconductor device that emits light when current flows through it
- **Semiconductor Junction** - The boundary between different semiconductor materials that allows current flow in one direction
- **Phosphor** - A material that converts higher energy light (blue/UV) into lower energy visible light
- **Microcandela (mcd)** - Unit measuring light intensity at the brightest point of an LED beam
- **Lumens** - Unit measuring total light output from an LED
- **Viewing Angle** - The angle over which an LED emits light effectively
- **PWM (Pulse Width Modulation)** - Method of controlling LED brightness by rapidly switching on/off
- **Addressable LED** - LED with built-in control chip allowing individual programming
- **RGB** - Red, Green, Blue color model for creating full color range
- **Heat Sink** - Component that dissipates heat from power LEDs
- **Ballast** - Electrical component in fluorescent fixtures that must be removed for LED tube installation
- **GU10** - Standard fitting type for mains voltage LED spotlights
- **Constant Current** - Power supply that maintains steady current regardless of load
- **Constant Voltage** - Power supply that maintains steady voltage regardless of load
- **Ohm's Law** - V = I × R, fundamental relationship between voltage, current, and resistance

///

## What does LED stand for?

---

A) Light Electronic Device

B) Light Energy Diode

C) Light Emitting Diode

D) Light Emitting Device

---

Light Emitting Diode

///

## When were the first visible light LEDs available?

---

A) 1980s

B) 1960s

C) 1950s

D) 1970s

---

1960s

///

## What was the first semiconductor junction that allowed electricity to flow one way?

---

A) The integrated circuit

B) The vacuum tube

C) The crystal radio "cat's whisker"

D) The transistor

---

The crystal radio "cat's whisker"

///

## Who first observed that diodes could create light?

---

A) Alexander Graham Bell

B) Henry Round

C) Thomas Edison

D) Nikola Tesla

---

Henry Round

///

## What material did Henry Round use when he first observed LED light emission?

---

A) Germanium

B) Silicon

C) Silicon carbide

D) Gallium arsenide

---

Silicon carbide

///

## What voltage do lithium coin cells provide for LED experiments?

---

A) 9V

B) 6V

C) 1.5V

D) 3V

---

3V

///

## Why won't 1.5V silver oxide batteries work with basic LED experiments?

---

A) They are too large

B) They don't provide enough voltage

C) They provide too much current

D) They have the wrong polarity

---

They don't provide enough voltage

///

## What happens if you connect an LED to a large battery without a resistor?

---

A) It works perfectly

B) It fries the LED

C) Nothing happens

D) It dims the LED

---

It fries the LED

///

## What is the flat side of an LED base always connected to?

---

A) Neutral

B) Ground

C) Negative

D) Positive

---

Negative

///

## Which wire is longer on an LED - positive or negative?

---

A) They are the same length

B) Positive

C) It varies by manufacturer

D) Negative

---

Positive

///

## What resistor value is commonly used with a 12V power supply for LEDs?

---

A) 500Ω

B) 10kΩ

C) 100Ω

D) 1kΩ

---

1kΩ

///

## How much voltage is dropped across the LED when using a 1kΩ resistor with 12V supply?

---

A) 12V

B) 1V

C) 2V

D) 10V

---

2V

///

## What is the viewing angle of a clear LED?

---

A) 180 degrees

B) 15 degrees

C) 30 degrees

D) 5 degrees

---

15 degrees

///

## What are large LEDs compared to small ones in terms of brightness?

---

A) Much dimmer

B) Much brighter

C) No brighter

D) Slightly brighter

---

No brighter

///

## What unit measures light intensity at the brightest point of an LED beam?

---

A) Watts

B) Microcandelas (mcd)

C) Lux

D) Lumens

---

Microcandelas (mcd)

///

## What unit measures the total amount of light that comes out of an LED?

---

A) Watts

B) Amperes

C) Microcandelas (mcd)

D) Lumens

---

Lumens

///

## What are white LEDs actually made from?

---

A) Red, green, and blue LEDs combined

B) White semiconductor material

C) Blue LEDs with phosphor coating

D) Yellow LEDs with filters

---

Blue LEDs with phosphor coating

///

## What does the phosphor in white LEDs do?

---

A) Controls the current flow

B) Converts blue and UV light to visible light

C) Generates electricity

D) Provides structural support

---

Converts blue and UV light to visible light

///

## What are the three primary color phosphors?

---

A) Orange, green, purple

B) Red, yellow, blue

C) Red, green, blue

D) Cyan, magenta, yellow

---

Red, green, blue

///

## What type of LED changes color gradually from one to the next?

---

A) Power LED

B) Rainbow LED

C) Addressable LED

D) Flashing LED

---

Rainbow LED

///

## How many LEDs are typically connected in series on a 12V LED strip?

---

A) Four

B) One

C) Three

D) Two

---

Three

///

## How many LEDs are on a standard 5-meter LED strip with 18mm spacing?

---

A) 450

B) 600

C) 150

D) 300

---

300

///

## How many LEDs are on a 5-meter LED strip with 9mm spacing?

---

A) 300

B) 900

C) 600

D) 450

---

600

///

## What do the numbers 5634 represent in LED specifications?

---

A) Current rating

B) Voltage rating

C) Chip dimensions in millimeters

D) Brightness rating

---

Chip dimensions in millimeters

///

## What are the dimensions of a 5634 LED chip?

---

A) 3.4mm x 2.8mm

B) 5.6mm x 3.4mm

C) 5.6mm x 2.8mm

D) 5.6mm x 5.6mm

---

5.6mm x 3.4mm

///

## Why are waterproof LED strips generally not recommended?

---

A) They produce less light

B) They are more expensive

C) They don't last as long due to heat retention

D) They are harder to install

---

They don't last as long due to heat retention

///

## What is the most common mistake when soldering surface mount LEDs?

---

A) Using the wrong type of solder

B) Soldering too quickly

C) Using too much solder

D) Not putting enough heat into the joint

---

Not putting enough heat into the joint

///

## What does PWM stand for in LED dimming?

---

A) Power Wave Management

B) Power Width Management

C) Pulse Width Modulation

D) Pulse Wave Modulation

---

Pulse Width Modulation

///

## How does PWM dimming work?

---

A) By changing the voltage

B) By rapidly switching the LED on and off

C) By using a variable resistor

D) By changing the current

---

By rapidly switching the LED on and off

///

## What type of LED has a built-in control chip?

---

A) Power LED

B) Addressable LED

C) Basic LED

D) Surface mount LED

---

Addressable LED

///

## How many primary colors do RGB LEDs have?

---

A) Four

B) One

C) Two

D) Three

---

Three

///

## What programming language is commonly used with Arduino for LED control?

---

A) Java

B) JavaScript

C) C++

D) Python

---

C++

///

## What replaced compact fluorescent lights in home lighting?

---

A) Neon lights

B) LEDs

C) Halogen bulbs

D) Incandescent bulbs

---

LEDs

///

## What was the main problem with compact fluorescent lights?

---

A) They were too bright

B) They used too much power

C) They were too expensive

D) They contained mercury and didn't last long

---

They contained mercury and didn't last long

///

## What must be removed when installing LED tubes to replace fluorescent tubes?

---

A) The mounting hardware

B) The electrical wiring

C) The tube itself

D) The ballast and starter

---

The ballast and starter

///

## How do LED tubes differ from fluorescent tubes in light direction?

---

A) LED tubes only shine downward

B) LED tubes are more directional

C) LED tubes shine light in all directions

D) LED tubes only shine upward

---

LED tubes are more directional

///

## What is the typical power rating of LED spotlights?

---

A) 20W

B) 2W

C) 5W

D) 10W

---

5W

///

## What is the typical beam angle of LED spotlights?

---

A) 60 degrees

B) 45 degrees

C) 15 degrees

D) 30 degrees

---

30 degrees

///

## What fitting type is used for mains voltage LED spotlights?

---

A) E14

B) GU10

C) B22

D) E27

---

GU10

///

## What is the beam angle of specialized narrow-beam LED spotlights?

---

A) 20 degrees

B) 15 degrees

C) 10 degrees

D) 5 degrees

---

10 degrees

///

## What do power LEDs require that basic LEDs don't?

---

A) Different wiring

B) Special resistors

C) Heat sinks

D) Higher voltage

---

Heat sinks

///

## What is the typical current rating of power LEDs?

---

A) 200mA

B) 500mA

C) 800mA

D) 100mA

---

800mA

///

## What voltage range are power LEDs typically rated for?

---

A) 5-6V

B) 9-12V

C) 1.5-3V

D) 3.3-4V

---

3.3-4V

///

## What is the formula for Ohm's Law?

---

A) V = I ÷ R

B) V = I × R

C) V = I + R

D) V = I - R

---

V = I × R

///

## What resistor value is calculated for 12V supply and 0.8A current?

---

A) 25Ω

B) 10Ω

C) 15Ω

D) 20Ω

---

15Ω

///

## What is the power requirement for an 800mA, 12V LED circuit?

---

A) 15W

B) 5W

C) 20W

D) 10W

---

10W

///

## What do LED lenses convert wide-angle LEDs into?

---

A) Color-changing LEDs

B) Spotlights

C) Diffused light sources

D) Flashing LEDs

---

Spotlights

///

## What beam angle do LED lenses typically provide?

---

A) 60 degrees

B) 45 degrees

C) 30 degrees

D) 15 degrees

---

30 degrees

///

## True or False: LEDs can be damaged by connecting them backwards.

---

A) False

B) True

---

False

///

## True or False: Large LEDs are always brighter than small LEDs.

---

A) False

B) True

---

False

///

## True or False: Waterproof LED strips are recommended for all outdoor applications.

---

A) True

B) False

---

False

///

## True or False: PWM dimming is more efficient than resistor dimming.

---

A) False

B) True

---

True

///

## True or False: Addressable LEDs require a microcontroller to control them.

---

A) True

B) False

---

True

///

## True or False: LED tubes can be directly swapped with fluorescent tubes.

---

A) True

B) False

---

False

///

## True or False: Power LEDs always require heat sinks.

---

A) False

B) True

---

True

///

## True or False: The experimental method for calculating LED resistors is more accurate than the theoretical calculation.

---

A) True

B) False

---

True

///

---

# Complete Answer Key

[Answer key updated to match new answer distributions]