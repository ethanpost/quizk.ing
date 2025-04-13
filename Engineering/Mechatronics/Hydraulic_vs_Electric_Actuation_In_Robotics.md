# [Hydraulics and Robotics in Boston Dynamics](https://www.youtube.com/watch?v=6r6KPuJ689o)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

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

A) The public incorrectly views it as old-fashioned and messy

B) The public has an accurate understanding of its limitations

C) The public doesn't have any strong opinions about hydraulics

D) The public is generally enthusiastic about hydraulic systems

---

The public incorrectly views it as old-fashioned and messy

///

## What is a key advantage of hydraulic systems according to the transcript?

---

A) They're very quiet during operation

B) Low energy consumption

C) They never leak or drip

D) Strong performance in a lightweight package

---

Strong performance in a lightweight package

///

## When were most hydraulic control valves originally designed?

---

A) In the 1990s

B) In the 1970s

C) In the 1950s

D) In the 1930s

---

In the 1950s

///

## What was the original purpose of the hydraulic control valves mentioned?

---

A) For military vehicles

B) For agricultural equipment

C) For industrial manufacturing

D) For airplanes

---

For airplanes

///

## What is the approximate size of the integrated hydraulic power supply developed by Boston Dynamics?

---

A) Size of a microwave

B) Size of a car battery

C) Size of a baseball

D) Size of a football

---

Size of a football

///

## How much power does the integrated hydraulic power supply produce?

---

A) 3 kilowatts

B) 10 kilowatts

C) 1 kilowatt

D) 5 kilowatts

---

5 kilowatts

///

## What does Raibert consider important for creating natural robot movement?

---

A) Neither hardware nor software innovation is necessary

B) Only software innovation matters

C) Only hardware innovation matters

D) Hardware innovation remains crucial

---

Hardware innovation remains crucial

///

## What is the difference between servoing and the dynamic approach described in the transcript?

---

A) Servoing uses hydraulics, dynamic approach uses electric motors

B) Servoing is for quadrupeds, dynamic approach is for bipeds

C) Servoing looks forward in time, dynamic approach is reactive

D) Servoing is reactive (backward-looking), dynamic approach predicts future motion

---

Servoing is reactive (backward-looking), dynamic approach predicts future motion

///

## How far ahead does the planning system for Spot robot typically look?

---

A) Several minutes

B) About half a second

C) A few milliseconds

D) A couple of seconds

---

A couple of seconds

///

## What does the limited horizon approach do?

---

A) Only works when the terrain is completely flat

B) Only focuses on obstacles directly in front of the robot

C) Plans the entire route before the robot starts moving

D) Calculates expected motion outcomes for 1-1.5 seconds ahead and continuously recalculates

---

Calculates expected motion outcomes for 1-1.5 seconds ahead and continuously recalculates

///

## According to the transcript, why is sticking the landing difficult for a robot doing a somersault?

---

A) Because of software limitations

B) Because there's limited control while in the air

C) Because the robot is too heavy

D) Because the batteries might run out mid-jump

---

Because there's limited control while in the air

///

## When did Boston Dynamics first make a robot do a somersault?

---

A) 2005-2006

B) 1995-1996

C) 1985-1986

D) 1975-1976

---

1985-1986

///

## What is a "planar robot" as described in the transcript?

---

A) A robot that moves using continuous tracks instead of legs

B) A robot that has completely flat feet

C) A robot that can only move in two dimensions

D) A robot restricted to the surface of a sphere, with limited degrees of freedom

---

A robot restricted to the surface of a sphere, with limited degrees of freedom

///

## What special technique was required for robots to perform 3D somersaults?

---

A) Adding gyroscopes

B) Using additional motors

C) Increasing the power of the hydraulic system

D) Tucking (withdrawing legs) to increase rotation speed

---

Tucking (withdrawing legs) to increase rotation speed

///

## Who collaborated on the 3D somersault robot project at MIT?

---

A) A NASA engineer

B) A professional dancer

C) A former Olympic swimmer

D) A former champion gymnast named Rob

---

A former champion gymnast named Rob

///

## According to the transcript, which robot movement is more natural-looking - walking or running?

---

A) Neither looks natural

B) Both are equally natural

C) Walking

D) Running

---

Running

///

## What was Boston Dynamics' motto in the early days?

---

A) "Innovation through hydraulics"

B) "Fast and furious"

C) "Building tomorrow's robots today"

D) "You have to run before you can walk"

---

"You have to run before you can walk"

///

## How fast could the WildCat quadruped robot run?

---

A) 39 meters per hour

B) 29 meters per hour

C) 19 meters per hour

D) 9 meters per hour

---

19 meters per hour

///

## What engine type was used for the WildCat robot?

---

A) Racing go-kart engine

B) Jet engine

C) Electric motor

D) Diesel engine

---

Racing go-kart engine

///

## What is "compliance" in robotics as mentioned in the transcript?

---

A) Meeting regulatory requirements

B) Following programmed instructions exactly

C) Springiness or flexibility in robot joints

D) The ability to navigate obstacles

---

Springiness or flexibility in robot joints

///

## What is a quadruped?

---

A) A robot with wheels instead of legs

B) A robot with six legs

C) A robot with four legs

D) A robot with two legs

---

A robot with four legs
