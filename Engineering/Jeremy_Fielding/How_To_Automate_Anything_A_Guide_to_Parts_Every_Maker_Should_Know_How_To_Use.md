# [How To Automate Anything: A Guide to Parts Every Maker Should Know How To Use](https://www.youtube.com/watch?v=S6GpV431nww)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

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

A) To switch other switches electrically

B) To increase voltage

C) To measure current

D) To store electrical energy

---

To switch other switches electrically

///

## According to the video, what are the two main categories of DC power supplies?

---

A) Large and small

B) AC and DC

C) High voltage and low voltage

D) Industrial and hobby/DIY level

---

Industrial and hobby/DIY level

///

## What voltage does a Raspberry Pi typically require?

---

A) 24 volts

B) 12 volts

C) 5 volts

D) 3.3 volts

---

5 volts

///

## What is the main advantage of proximity sensors over limit switches?

---

A) They work faster

B) They require no physical contact

C) They use less power

D) They are less expensive

---

They require no physical contact

///

## In a relay, what does "normally closed" mean?

---

A) The contact is never connected

B) The contact is always connected

C) The contact is connected when the coil is energized

D) The contact is connected when the coil is not energized

---

The contact is connected when the coil is not energized

///

## What is DIN rail used for?

---

A) Connecting wires

B) Cooling power supplies

C) Mounting electrical components

D) Measuring voltage

---

Mounting electrical components

///

## How many poles does a "four pole double throw" relay have?

---

A) Eight

B) Two

C) Four

D) Six

---

Four

///

## What does NPN stand for in proximity sensors?

---

A) Network Power Node

B) Negative Positive Negative

C) No Physical Contact

D) Normally Positive Normally

---

Negative Positive Negative

///

## What is the main benefit of using a contactor instead of a relay?

---

A) It's easier to wire

B) It's smaller

C) It can handle higher power

D) It's less expensive

---

It can handle higher power

///

## What is hysteresis in the context of limit switches?

---

A) The voltage it requires

B) The maximum current it can handle

C) The difference between engage and release points

D) The time it takes to activate

---

The difference between engage and release points

///

## What is the primary advantage of breakout boards?

---

A) They reduce power consumption

B) They provide wireless connectivity

C) They increase voltage

D) They convert pins to screw terminals

---

They convert pins to screw terminals

///

## What is the main reason for using small control cables with relays?

---

A) They carry more current

B) They are more reliable

C) They are much less expensive than power cables

D) They are easier to install

---

They are much less expensive than power cables

///

## What happens when a temperature sensor reaches its threshold?

---

A) It changes color

B) It increases voltage

C) It can open or close a circuit

D) It starts a timer

---

It can open or close a circuit

///

## What is the "normal position" of a relay?

---

A) When it's being tested

B) When the coil is not energized

C) When it's halfway activated

D) When the coil is energized

---

When the coil is not energized

///

## What does PNP mean in proximity sensors?

---

A) Power Network Protocol

B) Programmable Network Port

C) Positive Negative Positive

D) Proximity Non-Contact

---

Positive Negative Positive

///

## What is the primary application mentioned for reed switches?

---

A) Temperature monitoring

B) Detecting when a magnet is nearby

C) High-power switching

D) Pressure measurement

---

Detecting when a magnet is nearby

///

## What happens when a limit switch is activated in a normally closed configuration?

---

A) Current decreases

B) The circuit is opened

C) Voltage increases

D) The circuit is completed

---

The circuit is opened

///

## What is the main purpose of ventilation in power supplies?

---

A) To improve efficiency

B) To prevent dust buildup

C) To allow heat dissipation

D) To reduce noise

---

To allow heat dissipation

///
