## [How to Design Parts That Pass DFM - Education Chapter 5 Lesson 2](https://www.youtube.com/watch?v=PCSycUx0awY)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Outline

### Introduction
- Common problem: parts getting rejected in DFM (Design for Manufacturing)
- Lesson focus: how cutting process affects part geometry
- Key concepts from previous lesson: kerf and heat affected zone

### Kerf and Minimum Hole Size
- Kerf is the gap created during cutting process
- Created by laser with assist gas or CNC router removing material
- Automatically dictates minimum hole size
- Laser minimum hole size determined by:
  - Cutting progressively smaller holes until failure
  - Testing until pierce fails or hole becomes unclean
  - These tests establish minimum hole standards
- CNC router minimum hole size:
  - Limited by router bit size
  - Typically slightly larger than bit for interpolation
  - Interpolation ensures perfectly concentric holes

### Heat Affected Zone
- Heat affected zone works hand-in-hand with kerf
- Cutting puts heat and energy into the material
- Analogy: like a fuse in a car
  - Too much energy causes fuse to blow (disconnect)
  - More material in fuse allows more energy to pass through
  - Same principle applies to cutting: more material = more heat capacity

### Bridge Distance
- Distance between parallel lines being cut
- Example: edge of part and slot edge running parallel
- Represents a long moment where energy is applied
- Too much energy causes fuse-like effect (burning through)
- Solution: increase material distance
- Minimum distances required for manufacturability
- Determined by testing: making gaps smaller until failure, then backing off
- Rule of thumb: 50% of material thickness
  - Example: 100 thou aluminum = 50 thou minimum bridge distance
  - If below 50%, check SendCutSend guidelines for specific material and thickness

### Hole to Edge Distance
- Distance from hole or radius to an edge or another hole
- Different from bridge distance: only measures tangent distance (closest point)
- Brief moment of energy application compared to bridge's long moment
- Still subject to fuse effect if too much energy applied
- No rule of thumb (varies with radius size)
- Must check SendCutSend guidelines for specific values
- Can create bridging effect when radius placed in corner

### Floating Geometry
- Geometry that needs bridges to connect it to main part
- Common example: letters like "O" or "A" with internal spaces
- Bridges set at minimum thickness for that bridge
- Used to make connections as cosmetic as possible
- Width made as narrow as possible while still holding geometry
- Reference material guidelines for exact values

### Warping
- Directly affected by heat affected zone
- More energy put into part = more heat absorbed
- Less material available = more heat absorbed per unit
- Results in cupping and twisting
- Especially problematic with grills and many cutouts
- More internal geometry removed = more warping
- SendCutSend moves around cutting area to spread heat and reduce warping
- Too much material removed = insufficient material = warping occurs

### Terms
- Kerf - The gap created during the cutting process, either by laser with assist gas or CNC router removing material. This gap automatically dictates the minimum hole size.
- Heat Affected Zone - The area of material affected by heat during the cutting process. When cutting through material, heat and energy are put into the part, similar to how electricity flows through a fuse.
- Bridge Distance - The distance between parallel lines being cut. This represents a long moment where energy is applied during cutting, such as between the edge of a part and a slot edge.
- Hole to Edge - The distance from a hole or radius to an edge or another hole. This measures only the tangent distance (the closest point) between two surfaces, representing a brief moment of energy application compared to bridge distance.
- Floating Geometry - Geometry that needs bridges to connect it to the main part, such as the internal spaces in letters like "O" or "A". Bridges are set at minimum thickness to hold the geometry in place.
- Warping - Distortion of the part caused by heat from the cutting process, resulting in cupping and twisting. More internal geometry removal leads to more warping, especially with grills and many cutouts.
- Interpolation - A process used with CNC routers to make holes perfectly concentric by cutting slightly larger than the router bit size.
- Minimum Hole Size - The smallest hole that can be reliably cut through a material, determined by testing progressively smaller holes until failure occurs.

///

## According to the video, what is the kerf?

---

A) The gap created during the cutting process

B) The heat affected zone around the cut

C) The minimum distance between holes

D) The router bit diameter

---

The gap created during the cutting process

///

## How is minimum hole size determined for laser cutting?

---

A) By measuring the laser beam diameter

B) By using 50% of material thickness as a rule of thumb

C) By cutting progressively smaller holes until failure occurs

D) By matching the assist gas pressure

---

By cutting progressively smaller holes until failure occurs

///

## What limits the minimum hole size for CNC router cutting?

---

A) The router bit size

B) The material thickness

C) The cutting speed

D) The heat affected zone

---

The router bit size

///

## What is interpolation in CNC routing?

---

A) A method to reduce warping

B) A technique to minimize the heat affected zone

C) A process to make holes perfectly concentric

D) A way to calculate bridge distance

---

A process to make holes perfectly concentric

///

## The heat affected zone is compared to what in the video?

---

A) A fuse in a car

B) A welding torch

C) A heat sink

D) A cooling system

---

A fuse in a car

///

## What is bridge distance?

---

A) The distance from a hole to an edge

B) The minimum hole size

C) The distance between parallel lines being cut

D) The width of the kerf

---

The distance between parallel lines being cut

///

## What is hole to edge distance?

---

A) The distance between two parallel cuts

B) The minimum bridge thickness

C) The heat affected zone width

D) The distance from a hole or radius to an edge or another hole

---

The distance from a hole or radius to an edge or another hole

///

## Why is bridge distance different from hole to edge distance?

---

A) Bridge distance is always larger

B) Hole to edge has a rule of thumb but bridge distance does not

C) Bridge distance only applies to lasers, not routers

D) Bridge distance represents a long moment of energy application, while hole to edge is a brief tangent distance

---

Bridge distance represents a long moment of energy application, while hole to edge is a brief tangent distance

///

## What is the rule of thumb for bridge distance and hole size?

---

A) 25% of material thickness

B) 75% of material thickness

C) 100% of material thickness

D) 50% of material thickness

---

50% of material thickness

///

## If you have 100 thou aluminum, what is the rule of thumb minimum bridge distance?

---

A) 25 thou

B) 75 thou

C) 100 thou

D) 50 thou

---

50 thou

///

## What should you do if your bridge distance is below the 50% rule of thumb?

---

A) Increase the material thickness

B) Use a different cutting method

C) Accept that the part cannot be manufactured

D) Check SendCutSend guidelines for the specific material and thickness

---

Check SendCutSend guidelines for the specific material and thickness

///

## Is there a rule of thumb for hole to edge distance?

---

A) Yes, it's 50% of material thickness

B) Yes, it's 25% of material thickness

C) No, it changes with the radius size

D) Yes, it's the same as bridge distance

---

No, it changes with the radius size

///

## What is floating geometry?

---

A) Geometry that moves during cutting

B) Geometry that causes warping

C) Geometry that is too small to cut

D) Geometry that needs bridges to connect it to the main part

---

Geometry that needs bridges to connect it to the main part

///

## Why are bridges used with floating geometry typically set at minimum thickness?

---

A) To reduce material cost

B) To increase strength

C) To prevent warping

D) To make the connection as cosmetic as possible

---

To make the connection as cosmetic as possible

///

## What causes warping in cut parts?

---

A) The kerf being too wide

B) The bridge distance being too small

C) The hole size being too large

D) The heat affected zone putting too much energy into the part

---

The heat affected zone putting too much energy into the part

///

## When is warping especially problematic?

---

A) With thick materials

B) With small holes

C) With large bridge distances

D) With grills and many cutouts

---

With grills and many cutouts

///

## What happens when too much internal geometry is removed from a part?

---

A) The part becomes stronger

B) The part becomes lighter

C) The cutting speed increases

D) More warping occurs

---

More warping occurs

///

## How does SendCutSend try to reduce warping?

---

A) By using slower cutting speeds

B) By using larger router bits

C) By reducing the number of cuts

D) By moving around in the cutting area to spread heat out

---

By moving around in the cutting area to spread heat out

///

## True or False: The kerf automatically dictates the minimum hole size.

---

A) True

B) False

---

True

///

## True or False: Bridge distance and hole to edge distance are the same thing.

---

A) True

B) False

---

False

///

## True or False: The rule of thumb for bridge distance applies to all materials and thicknesses.

---

A) True

B) False

---

False

///

## Master Answer Key

1. **A** - Kerf is the gap created during cutting, not the heat zone, minimum distance, or bit diameter.

2. **C** - Laser minimum hole size is determined by testing progressively smaller holes until failure, not by beam diameter, rule of thumb, or gas pressure.

3. **A** - CNC router minimum hole size is limited by the router bit size, which must fit inside the hole.

4. **C** - Interpolation is the process of making holes perfectly concentric by cutting slightly larger than the bit size.

5. **A** - The heat affected zone is compared to a fuse in a car, where too much energy causes failure.

6. **C** - Bridge distance is the distance between parallel lines being cut, not hole-to-edge, minimum hole size, or kerf width.

7. **D** - Hole to edge is the distance from a hole or radius to an edge or another hole, measuring the closest tangent point.

8. **D** - Bridge distance involves a long moment of energy application along parallel lines, while hole to edge is just a brief tangent distance.

9. **D** - The rule of thumb is 50% of material thickness for both bridge distance and hole size.

10. **D** - For 100 thou aluminum, 50% equals 50 thou minimum bridge distance.

11. **D** - If below the rule of thumb, check SendCutSend's specific guidelines rather than assuming it won't work.

12. **C** - Hole to edge distance has no rule of thumb because it varies with radius size.

13. **D** - Floating geometry needs bridges to connect it to the main part, like internal spaces in letters.

14. **D** - Bridges are set at minimum thickness to make connections as cosmetic as possible while still functional.

15. **D** - Warping is caused by the heat affected zone putting too much energy into the part, especially when there's less material to absorb heat.

16. **D** - Warping is especially problematic with grills and many cutouts because they remove a lot of internal geometry.

17. **D** - More internal geometry removal means less material to absorb heat, leading to more warping.

18. **D** - SendCutSend moves around the cutting area to spread heat out and reduce localized warping.

19. **A** - True. The kerf (gap created during cutting) automatically determines the minimum hole size that can be made.

20. **B** - False. Bridge distance is between parallel lines, while hole to edge is from a hole/radius to an edge, and they measure different things.

21. **B** - False. The 50% rule of thumb is a general guideline, but specific materials and thicknesses may have different requirements that should be checked in the guidelines.

