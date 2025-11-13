## [The Capstone Project Part 2: Applying Every Skill You've Learned - Education Chapter 5 Lesson 17](https://www.youtube.com/watch?v=iwNP1y34DcA)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Capstone Project Part 2 Overview

### Project Continuation
- Continuing from part one of the capstone series
- Addressing interference between components
- Adding holes for hardware assembly
- Designing drawer component
- Completing the full assembly project

### Addressing Interference
- Creating clearance for flanges coming into shelf
- Using project tool to project flange areas
- Creating construction lines for reference
- Using offset tool to add clearance
- Adding 0.020 inch clearance (20,000 of an inch) for tolerance stackup
- Accounting for bend radiuses and cutting tolerances
- Adding corner radiuses for extra clearance (1/8 inch)
- Using isolate feature to focus on specific components
- Cutting clearance areas using extrude cut feature

### Adding Hardware Holes
- Creating through holes for mounting L brackets
- Using sketch on outside wall surface
- Projecting flanges onto sketch surface as construction lines
- Drawing center lines from midpoints to locate hole centers
- Using equal constraint to space holes equally from edges
- Setting dimension to 0.5 inch from edges
- Creating holes using solid hole feature
- Setting hole size to 0.12 inch for #6-32 hardware
- Holes go through both sides of part
- Using PEM hardware (nuts) on inside, screws from outside

### Tab and Slot Design
- Creating tabs on divider component
- Using equal constraint to make tabs consistent
- Setting tab thickness to 0.063 inch (flush with part outside)
- Positioning tabs 0.25 inch from top
- Using midpoint constraint to center bottom tab
- Extruding tabs using distance to object feature
- Creating slots by projecting tabs as construction lines
- Using offset with 0.010 inch tolerance (10,000 offset)
- Total clearance of 0.020 inch (10,000 on each side)
- Using mirror feature to create symmetric tabs
- Cutting slots through appropriate components only
- Accounting for powder coating by increasing slot size to 0.020 inch

### Drawer Design
- Creating offset plane 0.010 inch from bottom for clearance
- Projecting walls to define drawer boundaries
- Adding 0.25 inch spacing on each side for hardware clearance
- Setting drawer depth to 5/8 inch from back
- Creating sheet metal base flange
- Adding vertical flanges at 1.75 inches height
- Creating finger pull cutout (1.5 inch diameter circle)
- Adding corner radiuses for safety and aesthetics

### SendCutSend Plugin Usage
- Opening SendCutSend plugin from utilities
- Selecting bodies/components for quoting
- Naming bodies and components for clarity
- Material automatically selected based on thickness (0.063 inch)
- Material: 5052 aluminum, 0.063 inch thickness
- Quote shows cutting and bending costs automatically
- Adding parts to cart
- Adding secondary services (hardware operations)
- Selecting hardware from catalog (#6-32 nuts)
- Flipping hardware direction to inside of part
- Adding powder coating finishing service
- Selecting powder coat color (gloss red example)
- Viewing final cart with all parts and services

### Design Principles and Best Practices
- Using parametric design for easy modifications
- Changing one dimension at beginning updates entire assembly
- Understanding tolerance stackup considerations
- Accounting for manufacturing tolerances (plus or minus 0.005 inch)
- Considering finishing operations (powder coating) in design
- Using construction lines for reference geometry
- Isolating components for focused work
- Using distance to object for parametric relationships
- Ensuring proper clearance for assembly
- Testing design changes to verify parametric relationships

### Terms
- Interference - When components overlap or collide in an assembly, requiring clearance adjustments.
- Clearance - The intentional space added between components to prevent interference and account for manufacturing tolerances.
- Construction Line - A reference line in a sketch that helps define geometry but doesn't create features, typically used for projecting and aligning.
- Offset - A tool that creates a parallel copy of geometry at a specified distance, used for adding clearance in designs.
- Tolerance Stackup - The accumulation of manufacturing tolerances across multiple parts that can affect fit and assembly.
- PEM Hardware - Press-fit hardware components like nuts that are installed into parts during manufacturing, eliminating need for wrenches.
- Tab - A protrusion on a component designed to fit into a corresponding slot for alignment and assembly.
- Slot - An opening or cutout in a component designed to receive a tab from another component.
- Isolate - A CAD feature that hides all components except the selected one, allowing focused work on specific parts.
- Project - A CAD tool that creates geometry on a sketch plane by projecting edges or features from other components.
- Distance to Object - An extrusion method that automatically adjusts the extrusion distance based on a selected surface or object.
- Parametric Design - A design approach where dimensions are linked and changing one parameter automatically updates related features.
- SendCutSend Plugin - A utility within CAD software that allows direct integration with SendCutSend's manufacturing services for quoting and ordering.
- Secondary Services - Additional manufacturing operations beyond cutting and bending, such as hardware installation or finishing.
- Powder Coating - A finishing process that applies a protective and decorative powder coating to parts, requiring additional clearance in slots and holes.

///

## According to the video, what clearance amount was added for the flange interference?

---

A) 0.010 inch

B) 0.015 inch

C) 0.020 inch

D) 0.025 inch

---

0.020 inch

///

## What tool is used to create reference geometry from existing components?

---

A) Project

B) Extrude

C) Offset

D) Mirror

---

Project

///

## According to the video, what is the purpose of adding clearance between components?

---

A) To account for tolerance stackup and allow assembly flexibility

B) To make parts lighter

C) To reduce material costs

D) To improve aesthetics

---

To account for tolerance stackup and allow assembly flexibility

///

## What feature allows you to hide all components except the one you're working on?

---

A) Hide

B) Suppress

C) Isolate

D) Delete

---

Isolate

///

## According to the video, what size holes were created for the hardware?

---

A) 0.10 inch

B) 0.15 inch

C) 0.12 inch

D) 0.18 inch

---

0.12 inch

///

## What hardware size was used in the project?

---

A) #4-40

B) #8-32

C) #6-32

D) #10-24

---

#6-32

///

## How were the hole centers located on the flanges?

---

A) By measuring from edges

B) By using grid snap

C) By drawing center lines from midpoints

D) By manual placement

---

By drawing center lines from midpoints

///

## What constraint was used to make all tabs the same size?

---

A) Equal constraint

B) Horizontal constraint

C) Vertical constraint

D) Coincident constraint

---

Equal constraint

///

## According to the video, what thickness were the tabs designed to be?

---

A) 0.050 inch

B) 0.075 inch

C) 0.063 inch

D) 0.100 inch

---

0.063 inch

///

## What offset amount was used for the tab slots to account for tolerances?

---

A) 0.005 inch

B) 0.015 inch

C) 0.010 inch

D) 0.020 inch

---

0.010 inch

///

## According to the video, what is tolerance stackup?

---

A) The process of stacking parts

B) A type of fastener

C) The accumulation of manufacturing tolerances across multiple parts

D) A CAD feature

---

The accumulation of manufacturing tolerances across multiple parts

///

## What feature was used to create symmetric tabs on both sides?

---

A) Copy

B) Pattern

C) Mirror

D) Array

---

Mirror

///

## According to the video, why was an offset plane created for the drawer?

---

A) To make it easier to see

B) To align with other components

C) To add 0.010 inch clearance from the bottom

D) To reduce material usage

---

To add 0.010 inch clearance from the bottom

///

## What spacing was added on each side of the drawer for hardware clearance?

---

A) 0.125 inch

B) 0.375 inch

C) 0.25 inch

D) 0.50 inch

---

0.25 inch

///

## According to the video, what was the height of the drawer vertical flanges?

---

A) 1.5 inches

B) 2.0 inches

C) 1.75 inches

D) 2.25 inches

---

1.75 inches

///

## What diameter was the finger pull cutout on the drawer?

---

A) 1.0 inch

B) 1.25 inch

C) 2.0 inch

D) 1.5 inch

---

1.5 inch

///

## According to the video, what is PEM hardware?

---

A) A type of screw

B) A CAD feature

C) Press-fit hardware like nuts that eliminate need for wrenches

D) A material type

---

Press-fit hardware like nuts that eliminate need for wrenches

///

## What material and thickness was used in the project?

---

A) 5052 aluminum, 0.050 inch

B) 6061 aluminum, 0.063 inch

C) 5052 aluminum, 0.075 inch

D) 5052 aluminum, 0.063 inch

---

5052 aluminum, 0.063 inch

///

## According to the video, what happens when you change a dimension at the beginning of the design?

---

A) Nothing changes

B) Only that feature changes

C) The file becomes corrupted

D) All related components automatically update

---

All related components automatically update

///

## What is parametric design?

---

A) A design approach where dimensions are linked and changes update related features

B) A design with many parameters

C) A type of CAD software

D) A manufacturing process

---

A design approach where dimensions are linked and changes update related features

///

## According to the video, why was the slot size increased to 0.020 inch when adding powder coating?

---

A) To reduce weight

B) To improve aesthetics

C) To reduce cost

D) To account for powder coating buildup that could interfere with assembly

---

To account for powder coating buildup that could interfere with assembly

///

## What is a construction line used for?

---

A) Building construction projects

B) Drawing straight lines

C) Measuring distances

D) Creating reference geometry that helps define features but doesn't create geometry itself

---

Creating reference geometry that helps define features but doesn't create geometry itself

///

## According to the video, what is the purpose of using distance to object for extrusion?

---

A) To make extrusions longer

B) To automatically adjust if part thickness changes

C) To reduce file size

D) To improve rendering speed

---

To automatically adjust if part thickness changes

///

## What are secondary services in the SendCutSend context?

---

A) Additional CAD features

B) Backup services

C) Customer support

D) Manufacturing operations beyond cutting and bending, like hardware or finishing

---

Manufacturing operations beyond cutting and bending, like hardware or finishing

///

## According to the video, what does the SendCutSend plugin automatically show in the quote?

---

A) Only material cost

B) Total assembly cost

C) Shipping costs

D) Cutting and bending costs

---

Cutting and bending costs

///

## What is powder coating?

---

A) A type of paint

B) A material type

C) A CAD feature

D) A finishing process that applies protective and decorative powder coating to parts

---

A finishing process that applies protective and decorative powder coating to parts

///

## According to the video, what corner radius was added for extra clearance?

---

A) 1/16 inch

B) 3/16 inch

C) 1/4 inch

D) 1/8 inch

---

1/8 inch

///

## What is the total clearance created when using a 0.010 inch offset on each side of a slot?

---

A) 0.010 inch

B) 0.015 inch

C) 0.025 inch

D) 0.020 inch

---

0.020 inch

///

## According to the video, what manufacturing tolerance was mentioned for the thin aluminum?

---

A) Plus or minus 0.003 inch

B) Plus or minus 0.010 inch

C) Plus or minus 0.015 inch

D) Plus or minus 0.005 inch

---

Plus or minus 0.005 inch

///

## Master Answer Key

1. **C) 0.020 inch** - The video specifies adding 0.020 inch (20,000 of an inch) clearance for the flange interference to account for tolerance stackup.

2. **A) Project** - The project tool is used to create reference geometry by projecting edges or features from other components onto a sketch plane.

3. **A) To account for tolerance stackup and allow assembly flexibility** - Clearance is added to prevent interference and accommodate manufacturing tolerances that accumulate across multiple parts.

4. **C) Isolate** - The isolate feature hides all components except the selected one, allowing focused work on specific parts.

5. **C) 0.12 inch** - Holes were created at 0.12 inch diameter for the #6-32 hardware to pass through.

6. **C) #6-32** - The project used #6-32 hardware, with PEM nuts on the inside and screws from the outside.

7. **C) By drawing center lines from midpoints** - Center lines were drawn from the midpoints of projected flanges to locate hole centers accurately.

8. **A) Equal constraint** - The equal constraint was used to make all tabs the same size by constraining them to be equal to each other.

9. **C) 0.063 inch** - Tabs were designed to be 0.063 inch thick, which matches the material thickness and makes them flush with the outside of the part.

10. **C) 0.010 inch** - A 0.010 inch offset was used on each side of the tab slots, creating 0.020 inch total clearance for tolerances.

11. **C) The accumulation of manufacturing tolerances across multiple parts** - Tolerance stackup refers to how manufacturing tolerances add up across multiple components, affecting fit and assembly.

12. **C) Mirror** - The mirror feature was used to create symmetric tabs on both sides of the component efficiently.

13. **C) To add 0.010 inch clearance from the bottom** - An offset plane was created 0.010 inch from the bottom to provide clearance and prevent interference.

14. **C) 0.25 inch** - A quarter inch (0.25 inch) spacing was added on each side of the drawer to provide clearance for hardware like nuts.

15. **C) 1.75 inches** - The vertical flanges of the drawer were set to 1.75 inches in height.

16. **D) 1.5 inch** - The finger pull cutout was created as a 1.5 inch diameter circle in the front of the drawer.

17. **C) Press-fit hardware like nuts that eliminate need for wrenches** - PEM (Press-fit) hardware is installed during manufacturing and doesn't require wrenches for installation.

18. **D) 5052 aluminum, 0.063 inch** - The project used 5052 aluminum at 0.063 inch thickness, which was automatically detected by the SendCutSend plugin.

19. **D) All related components automatically update** - This demonstrates parametric design, where changing one dimension at the beginning causes all related features to update automatically.

20. **A) A design approach where dimensions are linked and changes update related features** - Parametric design uses linked dimensions so modifications propagate through the design automatically.

21. **D) To account for powder coating buildup that could interfere with assembly** - When powder coating is applied, material builds up on surfaces, so slots need to be larger to maintain proper fit.

22. **D) Creating reference geometry that helps define features but doesn't create geometry itself** - Construction lines are reference geometry used for alignment and projection but don't create actual features.

23. **B) To automatically adjust if part thickness changes** - Using distance to object creates a parametric relationship that automatically updates if the target surface or part thickness changes.

24. **D) Manufacturing operations beyond cutting and bending, like hardware or finishing** - Secondary services include additional operations like hardware installation (PEM nuts) and finishing (powder coating).

25. **D) Cutting and bending costs** - The SendCutSend plugin automatically calculates and displays the costs for cutting and the number of bends required.

26. **D) A finishing process that applies protective and decorative powder coating to parts** - Powder coating is a finishing service that adds both protection and decorative color to manufactured parts.

27. **D) 1/8 inch** - A 1/8 inch corner radius was added for extra clearance in the corners where flanges meet.

28. **D) 0.020 inch** - When using a 0.010 inch offset on each side of a slot, the total clearance is 0.020 inch (0.010 + 0.010).

29. **D) Plus or minus 0.005 inch** - The video mentions that SendCutSend's tolerances are plus or minus 0.005 inch for the thin aluminum material used.

