## [This 3D-Printed RC Car Might Redefine What's Possible](https://www.youtube.com/watch?v=pdKnIPH3JQs)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Detailed Outline

### Project Overview
- Designer created a 3D printable RC car that can reach 40 miles per hour
- Challenge: redesign the drivetrain to be fully 3D printable
- Exploration of gear ratios, belt drives, involutes, belt tensioners, ball bearing designs, and all-wheel drive differentials

### Drive Shaft vs Belt Drive
- Most RC cars use drive shafts to transmit power from motor to wheels
- Problem with 3D printed drive shafts: 3D prints are grown layer by layer creating inherent weakness along layer lines
- 3D printed drive shafts are weak and prone to failure at layer lines
- Belt drive inspiration came from racing chassis design
- Belt drive advantages:
  - Doesn't rely on 3D printed drive shaft
  - Belt spreads load over multiple teeth
  - Spur gears concentrate all force into root of single 3D printed tooth
  - Better for 3D printing applications

### Differential Fundamentals
- Purpose: allows wheels to rotate at different speeds during turns
- In a turn, the outer wheel traces a larger circle and travels farther distance
- Outer wheel must spin faster than inner wheel during turns
- Without differential, wheels would skid or lose traction during turns
- Both wheels need to rotate independently at different speeds while receiving power from one motor

### Differential Design Evolution
- Started with spokes on inner end of each axle
- Added crosspiece to turn wheels in same direction at same rate
- Support holds crossbar against both spokes
- Crosspiece placed on pivot to allow differential rotation
- Multiple spokes needed to maintain constant contact
- Teeth designed for constant contact with no backlash
- Edges cut for smooth and silent operation
- Bevel gears designed as cones meeting at virtual point in center
- Four spider gears used instead of two to distribute load through more teeth

### Belt-Driven Differential Design
- Belt rotates the assembly and puts power into wheels instead of shaft
- Four spider gears distribute load through more teeth (3D printed parts)
- Spider gears and bevel gears orbit around virtual point in center
- Virtual point compared to black hole at center of Milky Way galaxy
- Assembly designed specifically for belt drive operation

### 3D Printed Ball Bearings
- Differential contains eight separate bearings
- Four bearings for spider gears (need to rotate independently)
- Two larger bearings on orange outputs (rotate relative to each other)
- Two large diameter bearings allow whole assembly to spin in unison
- Spider gears use off-the-shelf bearings
- Larger bearings custom designed and 3D printed
- Four main parts: outer race, inner race, ball, and cage
- Races designed with channels slightly larger than ball diameter
- Air gap between inner and outer race is exactly half the ball diameter
- Gap allows balls to fit when inner race is nudged over
- Balls positioned equidistant around circle to prevent inner race movement
- Cage has passive snaps that yield when force applied
- Cage allows ball to rotate freely once snapped in
- Angled faces guide out-of-position balls back to cradle
- Races designed directly into differential casing for space efficiency
- Assembly is delicate and finicky at RC scale
- Cage produces satisfying click when snapping into position

### All-Wheel Drive System
- Turning causes front and rear wheels to spin at different speeds
- Front wheels travel further distance than rear wheels in turns
- Need front and rear differential to split power between left and right sides
- Need center differential to split power between front and rear wheels
- Center differential design same as front and rear but with different outputs
- Center differential outputs to small belt drive pinion
- Purple input sprocket takes power directly from motor
- Longer belts output power to front and rear differentials

### Chassis Assembly and Features
- All components designed to 3D print without support
- Parts print quickly with excellent surface quality
- Enclosure clamped with threaded inserts and M3 fasteners
- Fasteners driven at slight angle so screw head can recess
- Spider gear bearings held by opposing side when differential screwed down
- Clamped fit tuned over numerous iterations for exact pressure
- Test: twist one output and opposite should rotate in opposite direction
- Chassis completely redesigned to support belt driven drivetrain

### Motor Mount and Thermal Management
- Concerns about motor heat melting 3D printed plastic
- Thermally insulated motor mount maintains air gap around hottest parts
- Standoffs created using M3 fasteners
- System allows micro adjustment of motor pitch and yaw

### Belt Tensioners
- Belts come in predetermined lengths from AliExpress
- Tensioners account for stretch and small length differences
- Main drive belts use idler pulley on lever arm adjusted by set screw
- Quick and simple to adjust tension mid-session
- Idler pulleys constructed with 3D printed parts and off-the-shelf bearings
- System accommodates different gear ratios
- Center differential uses eccentric tensioner
- Motor output shaft is eccentric to circular motor mount
- Rotating motor mount moves output shaft closer/further from center differential input gear
- Provides fine control of belt tension and robust mounting

### Additional Improvements
- Structural members added to stiffen chassis
- Softer springs used on oil shocks due to lighter chassis weight
- Servo and electronics added

### Field Testing and Failure Analysis
- iPhone bracket mounted above rear axle to film belt drive
- Goal: drive until something breaks then analyze failure
- Tested on trails to pressure test all-wheel drive system
- After 20 minutes on-road driving, center differential failed
- Crown ejected from side, ball bearings spilled onto chassis plate
- Motor mount came loose, pinion friction melted surrounding plastic
- Both ejected cages crushed and creased as if bound and fractured
- Theory: ball bearings embedded or got hung up after heating
- Traffic jam inside ball bearing race caused cage collapse
- Outer races showed uneven wear, suggesting more friction on one side
- Evidence of too much heat or centrifugal force
- Spherical indents visible along outer race on one side
- Differential bevel gears in excellent condition with minimal friction
- Cause of failure uncertain, related to ball bearings

### Terms
- **Differential** - A mechanical device that allows wheels to rotate at different speeds while both receiving power from the motor, essential for turning.
- **Drive Shaft** - A mechanical component that transmits power from the motor to the wheels using metal gears and shafts.
- **Belt Drive** - A power transmission system using belts and pulleys instead of shafts to transfer power from motor to wheels.
- **Layer Lines** - The horizontal lines created in 3D printed objects where each layer bonds to the next, representing a structural weakness point.
- **Spur Gear** - A gear with straight teeth that concentrates force through the root of individual teeth.
- **Involute** - A specific curved shape used in gear tooth design for smooth meshing.
- **Spider Gears** - Small gears inside a differential that rotate on their own axis and allow the axles to turn at different speeds.
- **Bevel Gears** - Cone-shaped gears that mesh at an angle, designed to meet at a virtual point in the center of the differential.
- **Backlash** - The amount of play or space between gear teeth that can cause jerky action.
- **Ball Bearing** - A type of rolling-element bearing that uses balls to maintain separation between bearing races and reduce rotational friction.
- **Outer Race** - The outer ring of a ball bearing that contains a channel for the balls to roll in.
- **Inner Race** - The inner ring of a ball bearing that rotates relative to the outer race with balls in between.
- **Cage** - The component in a ball bearing that keeps the balls equidistant from each other and prevents them from falling out.
- **Idler Pulley** - A pulley that doesn't transmit power but is used to guide or tension a belt.
- **Belt Tensioner** - A device that maintains proper tension on a belt by taking up slack in the system.
- **Eccentric Tensioner** - A type of belt tensioner where the motor shaft center point is offset from the mounting point, allowing rotation to adjust tension.
- **Center Differential** - A differential that splits power between the front and rear axles in an all-wheel drive system.
- **Gear Ratio** - The relationship between the number of teeth on two gears that determines the speed and torque relationship.
- **Pinion** - A small gear that meshes with a larger gear or rack to transmit power.
- **Threaded Insert** - A metal component inserted into plastic to provide strong threads for bolts or screws.
- **Off-the-shelf** - Pre-manufactured standard parts that can be purchased rather than custom made.

///

## What is the maximum speed the 3D printable RC car is designed to reach?

---

A) 35 miles per hour

B) 45 miles per hour

C) 40 miles per hour 

D) 30 miles per hour

---

40 miles per hour

///

## Why are 3D printed drive shafts considered a bad idea for RC cars?

---

A) They require special tools to install

B) They are too expensive to manufacture

C) They are inherently weak along layer lines created during 3D printing

D) They are too heavy for the motor to turn

---

They are inherently weak along layer lines created during 3D printing

///

## What is a key advantage of a belt drive over a spur gear system for 3D printed parts?

---

A) Belt drives are easier to design

B) Belt drives spread load over multiple teeth while spur gears concentrate force in a single tooth root

C) Belt drives cost less than gears

D) Belt drives are quieter than gears

---

Belt drives spread load over multiple teeth while spur gears concentrate force in a single tooth root

///

## During a turn, what happens to the wheel on the outside versus the inside of the turn?

---

A) Both wheels spin at exactly the same speed

B) The inside wheel stops rotating completely

C) The outside wheel spins slower than the inside wheel

D) The outside wheel traces a larger circle and spins faster than the inside wheel

---

The outside wheel traces a larger circle and spins faster than the inside wheel

///

## What would happen if both wheels were rigidly connected without a differential during a turn?

---

A) The car would turn faster

B) Nothing would change

C) One or both wheels would have to skid, slip, or lose traction

D) The motor would work more efficiently

---

One or both wheels would have to skid, slip, or lose traction

///

## How many spider gears does the designer use in the differential and why?

---

A) Six spider gears for maximum strength

B) Two spider gears for simplicity

C) Three spider gears for balance

D) Four spider gears to distribute load through more teeth since they are 3D printed

---

Four spider gears to distribute load through more teeth since they are 3D printed

///

## What geometric concept is used to describe how bevel gears are designed?

---

A) They are designed as cylinders meeting end to end

B) They are designed as cones meeting at a virtual point in the center

C) They are designed as spheres meeting at tangent points

D) They are designed as cubes meeting at corners

---

They are designed as cones meeting at a virtual point in the center

///

## How many bearings are contained in the differential assembly?

---

A) Ten bearings

B) Eight bearings

C) Four bearings

D) Six bearings

---

Eight bearings

///

## What is the purpose of the cage in a ball bearing?

---

A) To make the bearing rotate faster

B) To keep the balls equidistant from each other and prevent them from falling out

C) To make the bearing easier to manufacture

D) To reduce the weight of the bearing

---

To keep the balls equidistant from each other and prevent them from falling out

///

## What is the air gap between the inner race and outer race designed to be?

---

A) Equal to the ball diameter

B) One-quarter of the ball diameter

C) Twice the ball diameter

D) Exactly half the ball diameter

---

Exactly half the ball diameter

///

## Why is the air gap between races exactly half the ball diameter?

---

A) To improve heat dissipation

B) To make manufacturing easier

C) So that when the inner race is nudged over, there is exactly one ball diameter space to fit balls into the race

D) To reduce weight

---

So that when the inner race is nudged over, there is exactly one ball diameter space to fit balls into the race

///

## Where did the designer integrate the races for the custom bearings?

---

A) On the outside of the chassis

B) As separate removable components

C) Straight into the casing of the differential for space efficiency

D) Attached to the motor mount

---

Straight into the casing of the differential for space efficiency

///

## What term describes the small metal components used to support the spider gears?

---

A) Custom 3D printed bearings

B) Off-the-shelf bearings

C) Washers

D) Bushings

---

Off-the-shelf bearings

///

## In an all-wheel drive system, why is a center differential needed?

---

A) To make the car go faster

B) To reduce motor strain

C) To split power between front and rear wheels since they spin at different speeds during turns

D) To improve fuel efficiency

---

To split power between front and rear wheels since they spin at different speeds during turns

///

## During a turn, which wheels travel a further distance?

---

A) The front wheels

B) The rear wheels

C) The left wheels only

D) All wheels travel the same distance

---

The front wheels

///

## How does the center differential differ from the front and rear differentials?

---

A) It uses more bearings

B) The orange outputs connect to belt drive pinions rather than wheel axle cups

C) It doesn't use spider gears

D) It is much larger in size

---

The orange outputs connect to belt drive pinions rather than wheel axle cups

///

## What component takes power directly from the motor in the all-wheel drive system?

---

A) The front differential

B) The chassis frame

C) The rear differential

D) The purple input sprocket on the center differential

---

The purple input sprocket on the center differential

///

## What is a key advantage of designing components without support structures?

---

A) They require special printers

B) They print quickly and have excellent surface quality

C) They use more material

D) They are heavier and more durable

---

They print quickly and have excellent surface quality

///

## What holds the spider gear bearings in place?

---

A) Magnets

B) The opposing side of the differential after it's screwed down

C) Glue

D) Clips

---

The opposing side of the differential after it's screwed down

///

## How can you test if a differential is working properly?

---

A) Check if it makes noise

B) Submerge it in water

C) Twist one output and the opposite output should rotate in the opposite direction

D) Measure its weight

---

Twist one output and the opposite output should rotate in the opposite direction

///

## What concern prompted the designer to create a thermally insulated motor mount?

---

A) Motor consuming too much battery power

B) Motor vibrations damaging the chassis

C) Motor being too heavy

D) Motor generating enough heat to melt the 3D printed plastic

---

Motor generating enough heat to melt the 3D printed plastic

///

## How does the thermally insulated motor mount protect the plastic chassis?

---

A) It uses metal shielding

B) It includes a cooling fan

C) It maintains an air gap around the hottest parts of the motor

D) It uses special heat-resistant plastic

---

It maintains an air gap around the hottest parts of the motor

///

## What additional benefit does the motor mount system provide?

---

A) It reduces motor weight

B) It allows micro adjustment of motor pitch and yaw

C) It improves battery life

D) It increases motor power

---

It allows micro adjustment of motor pitch and yaw

///

## Where did the designer source the predetermined length belts?

---

A) Custom manufacturer

B) Local hardware store

C) AliExpress

D) Amazon

---

AliExpress

///

## What is the purpose of belt tensioners in the system?

---

A) To improve acceleration

B) To make the belts last longer

C) To reduce noise

D) To account for stretch and small differences in belt length

---

To account for stretch and small differences in belt length

///

## What type of tensioner is used for the main drive belts?

---

A) Spring-loaded tensioner

B) Automatic tensioner

C) Idler pulley on a lever arm adjusted by set screw

D) Hydraulic tensioner

---

Idler pulley on a lever arm adjusted by set screw

///

## What advantage does the set screw adjustment provide?

---

A) Elimination of maintenance

B) Quick and simple adjustment even mid-session

C) Permanent tension setting

D) Automated tension control

---

Quick and simple adjustment even mid-session

///

## What type of tensioner is used for the belt transferring power from motor to center differential?

---

A) Spring tensioner

B) Eccentric tensioner

C) Ratchet tensioner

D) Hydraulic tensioner

---

Eccentric tensioner

///

## Why is the motor mount called an "eccentric" tensioner?

---

A) It was designed by an eccentric engineer

B) It has an unusual shape

C) The motor output shaft doesn't share the same center point as the circular motor mount

D) It rotates in the opposite direction

---

The motor output shaft doesn't share the same center point as the circular motor mount

///

## What happens when you rotate the eccentric motor mount?

---

A) The motor spins faster

B) The chassis lifts up

C) The belt breaks

D) The motor output shaft gets closer to and further from the center differential input gear

---

The motor output shaft gets closer to and further from the center differential input gear

///

## Why did the designer use softer springs on the oil shocks?

---

A) Harder springs were not available

B) The chassis ended up being lighter than the original

C) Softer springs are cheaper

D) Softer springs provide better traction

---

The chassis ended up being lighter than the original

///

## What was the designer's goal for the field test?

---

A) To achieve maximum speed

B) To drive until something breaks and then analyze what happened

C) To compare with other RC cars

D) To test on different terrains

---

To drive until something breaks and then analyze what happened

///

## How long did the car run on roads before experiencing failure?

---

A) 30 minutes

B) 5 minutes

C) 20 minutes

D) 10 minutes

---

20 minutes

///

## What component failed during the road test?

---

A) The front differential

B) The motor

C) The center differential

D) The rear differential

---

The center differential

///

## What happened when the center differential failed?

---

A) The wheels fell off

B) The motor stopped working

C) The crown ejected from the side and ball bearings spilled onto the chassis plate

D) The chassis cracked in half

---

The crown ejected from the side and ball bearings spilled onto the chassis plate

///

## What additional damage occurred related to the motor mount?

---

A) The motor fell out of the chassis

B) The motor mount came loose and the pinion friction melted surrounding plastic

C) The motor wiring disconnected

D) The motor overheated and shut down

---

The motor mount came loose and the pinion friction melted surrounding plastic

///

## What condition were both cages found in after the failure?

---

A) Missing completely

B) Slightly worn but functional

C) Perfectly intact

D) Crushed and creased as if bound and fractured

---

Crushed and creased as if bound and fractured

///

## What does the cage damage suggest happened inside the bearing?

---

A) Manufacturing defect

B) Normal wear and tear

C) Ball bearings embedded or got hung up causing a traffic jam in the bearing race

D) Cage was installed incorrectly

---

Ball bearings embedded or got hung up causing a traffic jam in the bearing race

///

## What evidence of uneven wear was observed on the outer races?

---

A) Both races were equally worn

B) One race appeared colored with pencil lead suggesting more friction on one side

C) The races showed no wear

D) Cracks in the plastic

---

One race appeared colored with pencil lead suggesting more friction on one side

///

## What does the uneven wear pattern support as a possible cause?

---

A) Normal operation

B) Manufacturing variation

C) Too much heat or centrifugal force causing ball bearings to embed into soft plastic race

D) Improper assembly

---

Too much heat or centrifugal force causing ball bearings to embed into soft plastic race

///

## What visible evidence remained on the outer race surface?

---

A) Discoloration only

B) Cracks

C) Scratches

D) Spherical indents along the outer race on one side

---

Spherical indents along the outer race on one side

///

## What was surprising about the condition of the differential bevel gears after failure?

---

A) They were partially melted

B) They were in really good shape and looked almost new

C) They were completely destroyed

D) They were missing

---

They were in really good shape and looked almost new

///

## What does the good condition of the bevel gears indicate?

---

A) They were poorly designed

B) There's not much friction and heat going through the differential itself

C) They were the cause of failure

D) They need to be redesigned

---

There's not much friction and heat going through the differential itself

///

## What is backlash in a gear system?

---

A) The force pushing gears apart

B) The speed at which gears rotate

C) The amount of play or space between gear teeth that can cause jerky action

D) The noise gears make when operating

---

The amount of play or space between gear teeth that can cause jerky action

///

## What is an involute in gear design?

---

A) A type of motor mount

B) A metal fastener

C) A specific curved shape used in gear tooth design for smooth meshing

D) A type of bearing

---

A specific curved shape used in gear tooth design for smooth meshing

///

## What is a pinion?

---

A) A type of bearing cage

B) A small gear that meshes with a larger gear or rack to transmit power

C) A large gear used for final drive

D) A belt tensioning device

---

A small gear that meshes with a larger gear or rack to transmit power

///

## What is a threaded insert used for?

---

A) To reduce friction

B) To increase weight

C) To provide strong threads in plastic for bolts or screws

D) To improve electrical conductivity

---

To provide strong threads in plastic for bolts or screws

///

## What does "off-the-shelf" mean in the context of this project?

---

A) Components that must be custom manufactured

B) Parts that are stored on shelves

C) Pre-manufactured standard parts that can be purchased rather than custom made

D) Discontinued components

---

Pre-manufactured standard parts that can be purchased rather than custom made

///

## What is a gear ratio?

---

A) The weight comparison between two gears

B) The relationship between the number of teeth on two gears that determines speed and torque

C) The color difference between gears

D) The distance between two gears

---

The relationship between the number of teeth on two gears that determines speed and torque

///

## What design feature allows the belt tensioner system to accommodate different gear ratios?

---

A) Multiple belt options

B) Interchangeable pulleys

C) Adjustable motor mounts

D) Enough variability in belt length to work with different sized gears

---

Enough variability in belt length to work with different sized gears

///

---

# Master Answer Key

[Answer key section remains unchanged]

