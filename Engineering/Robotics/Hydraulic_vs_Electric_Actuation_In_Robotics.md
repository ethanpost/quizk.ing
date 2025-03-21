# [Hydraulics and Robotics in Boston Dynamics](https://www.youtube.com/watch?v=6r6KPuJ689o)

## Hydraulics Technology

### Marc Raibert's Perspective
- Founder and former CEO of Boston Dynamics
- Still loves hydraulics despite public perception
- Technology viewed as old-fashioned or "icky" by many
- Occasional dripping is a challenge but manageable
- Provides excellent strength-to-weight ratio

### Innovation in Hydraulic Systems
- Most hydraulic control valves designed in 1950s for aircraft
- Limited innovation in basic design for decades
- Boston Dynamics engineers redesigned valves
  - New control circuits
  - More efficient use
  - Smaller and lighter components
- Created integrated hydraulic power supply
  - Size of a football
  - 5 kilograms weight
  - Produces 5 kilowatts of power (equivalent to about 6.7 horsepower)
  - Enough power to run a small household or drive a compact electric car
  - Significant output for a device of its size, demonstrating the efficiency of their hydraulic systems
  - Integrates motor, pump, filters, heat exchanger

## Robot Movement Design

### Natural Movement Philosophy
- Hardware innovation remains crucial
- Dynamic approach to motion planning
  - Predicts future motion evolution
  - Avoids just reactive servoing (backward-looking adjustments)

### Time Horizon Planning
- Only needs to look ahead a couple of seconds for Spot robot
- Uses limited horizon approach
  - Calculates what will happen in next 1-1.5 seconds
  - Continuously recalculates (every tenth of a second)
  - Coordinates obstacle avoidance, foot placement, and balance
- Longer planning horizons for complex movements
  - Somersaults require coordinating momentum and rotation at launch
  - Landing must be calculated from beginning

### Mastering the Somersault
- First robotic somersault achieved with a planar robot (1985-1986)
  - Restricted to surface of a sphere
  - Could move forward/backward, up/down, and rotate
- Calculations involve:
  - Jump height (determines time in air)
  - Rotation speed
  - Managing rotational and linear momentum for landing
- 3D somersaults later developed at MIT
  - Required tucking (withdrawing legs) for sufficient rotation
  - Collaborated with former champion gymnast (Rob)

### Walking vs. Running
- Running motion closer to human-like than walking
- Walking remains challenging to make natural
- Requires precise folding/unfolding of knees
- Compliance (springiness) in design is important
- Boston Dynamics motto: "You have to run before you can walk"

### Speed Achievements
- WildCat quadruped reached 19 meters per hour on flat terrain
- Possibly the fastest quadruped robot in the world
- Also noted as being extremely loud (used racing go-kart engine)

## Terms
- Hydraulics - A fluid power technology that uses pressurized oil to transmit force and motion
- Servoing - A backward-looking control mechanism that adjusts based on current position rather than future predictions
- Limited Horizon Approach - A planning method that calculates expected motion outcomes for a short time period (1-1.5 seconds) ahead and continuously recalculates
- Planar Robot - A robot constrained to move along the surface of a sphere, with restricted degrees of freedom
- Quadruped - A four-legged robot design, modeled after four-legged animals
- Compliance - Springiness or flexibility in robot joints and components that allows for more natural movement
- Dynamic Approach - A motion control philosophy that focuses on predicting future states rather than just reacting to current conditions


///

## What is Marc Raibert's opinion about the public perception of hydraulics technology?

---

A) The public has an accurate understanding of its limitations

B) The public incorrectly views it as old-fashioned and messy

C) The public is generally enthusiastic about hydraulic systems

D) The public doesn't have any strong opinions about hydraulics

---

The public incorrectly views it as old-fashioned and messy

///

## What is a key advantage of hydraulic systems according to the transcript?

---

A) They never leak or drip

B) They're very quiet during operation

C) Strong performance in a lightweight package

D) Low energy consumption

---

Strong performance in a lightweight package

///

## When were most hydraulic control valves originally designed?

---

A) In the 1930s

B) In the 1950s

C) In the 1970s

D) In the 1990s

---

In the 1950s

///

## What was the original purpose of the hydraulic control valves mentioned?

---

A) For industrial manufacturing

B) For agricultural equipment

C) For airplanes

D) For military vehicles

---

For airplanes

///

## What is the approximate size of the integrated hydraulic power supply developed by Boston Dynamics?

---

A) Size of a baseball

B) Size of a football

C) Size of a microwave

D) Size of a car battery

---

Size of a football

///

## How much power does the integrated hydraulic power supply produce?

---

A) 1 kilowatt

B) 3 kilowatts

C) 5 kilowatts

D) 10 kilowatts

---

5 kilowatts

///

## What does Raibert consider important for creating natural robot movement?

---

A) Only software innovation matters

B) Only hardware innovation matters

C) Hardware innovation remains crucial

D) Neither hardware nor software innovation is necessary

---

Hardware innovation remains crucial

///

## What is the difference between servoing and the dynamic approach described in the transcript?

---

A) Servoing looks forward in time, dynamic approach is reactive

B) Servoing is reactive (backward-looking), dynamic approach predicts future motion

C) Servoing uses hydraulics, dynamic approach uses electric motors

D) Servoing is for quadrupeds, dynamic approach is for bipeds

---

Servoing is reactive (backward-looking), dynamic approach predicts future motion

///

## How far ahead does the planning system for Spot robot typically look?

---

A) A few milliseconds

B) About half a second

C) A couple of seconds

D) Several minutes

---

A couple of seconds

///

## What does the limited horizon approach do?

---

A) Only focuses on obstacles directly in front of the robot

B) Calculates expected motion outcomes for 1-1.5 seconds ahead and continuously recalculates

C) Plans the entire route before the robot starts moving

D) Only works when the terrain is completely flat

---

Calculates expected motion outcomes for 1-1.5 seconds ahead and continuously recalculates

///

## According to the transcript, why is sticking the landing difficult for a robot doing a somersault?

---

A) Because the robot is too heavy

B) Because there's limited control while in the air

C) Because the batteries might run out mid-jump

D) Because of software limitations

---

Because there's limited control while in the air

///

## When did Boston Dynamics first make a robot do a somersault?

---

A) 1975-1976

B) 1985-1986

C) 1995-1996

D) 2005-2006

---

1985-1986

///

## What is a "planar robot" as described in the transcript?

---

A) A robot that can only move in two dimensions

B) A robot restricted to the surface of a sphere, with limited degrees of freedom

C) A robot that has completely flat feet

D) A robot that moves using continuous tracks instead of legs

---

A robot restricted to the surface of a sphere, with limited degrees of freedom

///

## What special technique was required for robots to perform 3D somersaults?

---

A) Using additional motors

B) Tucking (withdrawing legs) to increase rotation speed

C) Adding gyroscopes

D) Increasing the power of the hydraulic system

---

Tucking (withdrawing legs) to increase rotation speed

///

## Who collaborated on the 3D somersault robot project at MIT?

---

A) A former Olympic swimmer

B) A former champion gymnast named Rob

C) A NASA engineer

D) A professional dancer

---

A former champion gymnast named Rob

///

## According to the transcript, which robot movement is more natural-looking - walking or running?

---

A) Walking

B) Running

C) Both are equally natural

D) Neither looks natural

---

Running

///

## What was Boston Dynamics' motto in the early days?

---

A) "Fast and furious"

B) "You have to run before you can walk"

C) "Innovation through hydraulics"

D) "Building tomorrow's robots today"

---

"You have to run before you can walk"

///

## How fast could the WildCat quadruped robot run?

---

A) 9 meters per hour

B) 19 meters per hour

C) 29 meters per hour

D) 39 meters per hour

---

19 meters per hour

///

## What engine type was used for the WildCat robot?

---

A) Electric motor

B) Diesel engine

C) Racing go-kart engine

D) Jet engine

---

Racing go-kart engine

///

## What is "compliance" in robotics as mentioned in the transcript?

---

A) Following programmed instructions exactly

B) The ability to navigate obstacles

C) Springiness or flexibility in robot joints

D) Meeting regulatory requirements

---

Springiness or flexibility in robot joints

///

## What is a quadruped?

---

A) A robot with two legs

B) A robot with four legs

C) A robot with six legs

D) A robot with wheels instead of legs

---

A robot with four legs
