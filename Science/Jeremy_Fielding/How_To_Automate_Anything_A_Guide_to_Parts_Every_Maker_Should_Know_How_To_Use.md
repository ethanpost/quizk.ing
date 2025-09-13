# [How To Automate Anything: A Guide to Parts Every Maker Should Know How To Use](https://www.youtube.com/watch?v=S6GpV431nww)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

## Introduction to Automation
- Automation provides "superpower" capabilities for makers
- Relays and contactors are fundamental automation components
- Automation allows one switch to control multiple other switches
- Example: Automated dust collection system eliminates manual switching

## DC Power Supplies
- Essential first tool in automation toolbox
- Converts mains power (120-240V AC) to appropriate DC voltage
- Two main categories: Industrial and hobby/DIY level
- Industrial power supplies:
  - Mount using DIN rail brackets
  - More durable and long-lasting
  - Usually 24V, though other voltages available
  - More expensive than hobby versions
- Hobby/DIY power supplies:
  - Mount with screw holes
  - Smaller and more affordable
  - Can be as small as wall adapters
- Voltage selection considerations:
  - Match voltage to components (e.g., Raspberry Pi needs 5V)
  - Multi-voltage supplies available (e.g., 5V and 12V outputs)
- Current capacity important:
  - Must handle total current of all connected devices
  - Larger power supplies needed for more power
  - Ventilation required for heat dissipation
- Input voltage switching:
  - Some supplies have manual switches for 115V/230V
  - Wide range supplies (120-240V) work automatically
- Polarity identification:
  - Usually labeled on power supply
  - Wall adapters may not be labeled
  - Test with multimeter to verify positive/negative

## Relays and Contactors
- Most important electrical tool in automation toolbox
- Relay and contactor are essentially the same device
- Contactor is "big brother" of relay for high-power applications
- Four main benefits:
  1. No physical movement required - electrically controlled
  2. One switch controls many switches
  3. Sensors can trigger relays
  4. Low-power circuit controls high-power circuit
- Applications:
  - Computerized control systems
  - Thermostat operation
  - Dust collection automation
  - Central control panels
- Relay operation:
  - Normal position: coil off
  - Activated position: coil energized
  - Normally Closed (NC): connected when coil off
  - Normally Open (NO): connected when coil on
- Relay specifications:
  - Poles: number of switching contacts
  - Throw: single or double (switches between contacts)
  - Examples: 2-pole double throw, 4-pole single throw
- Wiring considerations:
  - Small control cables vs. large power cables
  - Place contactor near controlled device
  - Use small cables for control signals

## Proximity Sensors
- Detect presence of metal without physical contact
- Advantages over limit switches:
  - No physical contact required
  - Won't be damaged by overrun
  - More reliable for fast-moving machines
- Sensing distance varies by material:
  - Steel: good sensing distance
  - Aluminum: requires much closer proximity
- Wiring:
  - Brown wire: positive
  - Black wire: signal (NPN) or positive (PNP)
  - Blue wire: negative
- Specifications:
  - Supply voltage: 6-36V
  - Load current: typically 300mA maximum
- Applications:
  - CNC machine limit detection
  - Presence detection
  - Position sensing

## Limit Switches
- Physical switches activated by contact
- Two distinct positions:
  - Engage point: when switch activates
  - Release point: when switch deactivates
- Hysteresis: difference between engage and release points
- Applications:
  - End-of-travel detection
  - Home position sensing
  - Safety interlocks
- Configurations:
  - Rocker arm style
  - Push button style
  - Roller configurations (inline or 90°)
- Wiring: Can be normally open or normally closed

## Reed Switches
- Very small magnetic switches
- Activated by proximity of magnet
- Low current capacity
- Applications:
  - Magnetic door sensors
  - Position detection with magnets
  - Low-power switching applications

## Additional Sensor Types
- Temperature sensors:
  - Open/close circuit at threshold
  - Digital versions provide real-time feedback
  - Applications: thermal protection, process control
- Pressure sensors:
  - Detect pressure in chambers
  - Digital displays available
  - Applications: pneumatic systems, safety monitoring

## Breakout Boards
- Convert microelectronics pins to screw terminals
- Available for Raspberry Pi, Arduino, and other microcontrollers
- DIN rail mounting options
- Benefits:
  - No soldering required
  - Easy connections
  - Durable and reliable
  - Easy component swapping

## Terms
- **Relay** - An electrically operated switch that uses a low-power signal to control a high-power circuit
- **Contactor** - A high-power version of a relay used for controlling large electric motors and machines
- **DC Power Supply** - A device that converts alternating current (AC) from the wall outlet to direct current (DC) for electronic components
- **DIN Rail** - A standardized metal rail used for mounting electrical components in industrial applications
- **Proximity Sensor** - A sensor that detects the presence of metal objects without physical contact
- **Limit Switch** - A mechanical switch activated by physical contact to indicate position or limit travel
- **Reed Switch** - A small magnetic switch that closes when a magnet is brought near it
- **Normally Closed (NC)** - A switch contact that is connected when the relay coil is not energized
- **Normally Open (NO)** - A switch contact that is connected when the relay coil is energized
- **Pole** - The number of switching contacts in a relay
- **Throw** - Whether a relay contact switches between two positions (double throw) or just on/off (single throw)
- **NPN Sensor** - A proximity sensor where the signal line goes negative when activated
- **PNP Sensor** - A proximity sensor where the signal line goes positive when activated
- **Breakout Board** - A circuit board that converts small electronic component pins into larger, easier-to-use screw terminals
- **Hysteresis** - The difference between the engage and release points of a switch, providing stability

///

## What is the primary function of a relay in automation?

---

A) To increase voltage

B) To switch other switches electrically

C) To store electrical energy

D) To measure current

---

To switch other switches electrically

///

## According to the video, what are the two main categories of DC power supplies?

---

A) High voltage and low voltage

B) AC and DC

C) Industrial and hobby/DIY level

D) Large and small

---

Industrial and hobby/DIY level

///

## What voltage does a Raspberry Pi typically require?

---

A) 3.3 volts

B) 5 volts

C) 12 volts

D) 24 volts

---

5 volts

///

## What is the main advantage of proximity sensors over limit switches?

---

A) They are less expensive

B) They require no physical contact

C) They work faster

D) They use less power

---

They require no physical contact

///

## In a relay, what does "normally closed" mean?

---

A) The contact is connected when the coil is energized

B) The contact is connected when the coil is not energized

C) The contact is always connected

D) The contact is never connected

---

The contact is connected when the coil is not energized

///

## What is DIN rail used for?

---

A) Measuring voltage

B) Mounting electrical components

C) Connecting wires

D) Cooling power supplies

---

Mounting electrical components

///

## How many poles does a "four pole double throw" relay have?

---

A) Two

B) Four

C) Six

D) Eight

---

Four

///

## What does NPN stand for in proximity sensors?

---

A) Negative Positive Negative

B) Normally Positive Normally

C) No Physical Contact

D) Network Power Node

---

Negative Positive Negative

///

## What is the main benefit of using a contactor instead of a relay?

---

A) It's smaller

B) It can handle higher power

C) It's less expensive

D) It's easier to wire

---

It can handle higher power

///

## What is hysteresis in the context of limit switches?

---

A) The time it takes to activate

B) The difference between engage and release points

C) The maximum current it can handle

D) The voltage it requires

---

The difference between engage and release points

///

## What is the primary advantage of breakout boards?

---

A) They increase voltage

B) They convert pins to screw terminals

C) They reduce power consumption

D) They provide wireless connectivity

---

They convert pins to screw terminals

///

## What is the main reason for using small control cables with relays?

---

A) They are more reliable

B) They are much less expensive than power cables

C) They carry more current

D) They are easier to install

---

They are much less expensive than power cables

///

## What happens when a temperature sensor reaches its threshold?

---

A) It increases voltage

B) It can open or close a circuit

C) It starts a timer

D) It changes color

---

It can open or close a circuit

///

## What is the "normal position" of a relay?

---

A) When the coil is energized

B) When the coil is not energized

C) When it's halfway activated

D) When it's being tested

---

When the coil is not energized

///

## What does PNP mean in proximity sensors?

---

A) Positive Negative Positive

B) Proximity Non-Contact

C) Power Network Protocol

D) Programmable Network Port

---

Positive Negative Positive

///

## What is the primary application mentioned for reed switches?

---

A) High-power switching

B) Detecting when a magnet is nearby

C) Temperature monitoring

D) Pressure measurement

---

Detecting when a magnet is nearby

///

## What happens when a limit switch is activated in a normally closed configuration?

---

A) The circuit is completed

B) The circuit is opened

C) Voltage increases

D) Current decreases

---

The circuit is opened

///

## What is the main purpose of ventilation in power supplies?

---

A) To reduce noise

B) To allow heat dissipation

C) To prevent dust buildup

D) To improve efficiency

---

To allow heat dissipation

///
