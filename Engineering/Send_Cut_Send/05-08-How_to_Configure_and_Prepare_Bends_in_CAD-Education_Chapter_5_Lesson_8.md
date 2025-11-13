## [How to Configure and Prepare Bends in CAD- Education Chapter 5 Lesson 8](https://www.youtube.com/watch?v=KlULfLlZJkU)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Outline

### Creating Sheet Metal Parts in CAD
- Starting with a sketch (example: 5 in x 5 in sketch)
- Using the sheet metal area of the ribbon
- Creating a base flange from a profile
- Selecting orientation side (side one, centered, or second side)
- Choosing operation type (new component vs new body)

### Sheet Metal Components vs Bodies
- Components have independent sheet metal rules
- Components allow individual rule changes
- Bodies are associated with the master file
- Recommendation: move all sheet metal parts into new components

### Sheet Metal Rules
- Rules are associated with specific components
- Rules can be obtained from SendCutSend for Fusion and SolidWorks
- Rules can be switched and edited easily
- Rules include: material thickness, K factor, bend radius, relief shape, bend relief dimensions, corner conditions

### Sheet Metal Rule Configuration
- Rule name: can be named anything (SendCutSend rules come pre-named)
- Material thickness: critical for calculating bend allowance and bend deduction
- K factor: important for accurate calculations
- Bend conditions: includes bend radius (dictated by punch) and relief shape (round, straight, or tear)
- Bend relief: width and depth calculations when associating with a cut along a line
- Corner conditions: for two bends intersecting (square or round shapes)
- Corner size: area for size input

### Creating Additional Flanges
- Flange tool can create base flanges and additional bends
- Height option: bend or flange length
- Height measurement options: outer edge, inner face, or tangent point
- Recommended: measure from outer face (standard way)
- Bend position: inside, outside, or adjacent to the selected edge

### Bend Relief Situations
- Full edge vs two sides option in flange dialog
- Two sides option allows flange edge within bend line
- Automatically creates relief slot following sheet metal rules
- Relief is editable through modify > sheet metal rules

### Corner Relief Situations
- Two different ways to create corners show up differently
- Creating new flange on existing flange creates different corner relief
- Creating two flanges simultaneously creates different corner relief pattern
- One method creates tighter corner suitable for weldments
- Corner relief can be changed from square to round in sheet metal rules

### Flat Pattern Creation
- Used to get DXF form for manufacturer
- SendCutSend accepts STEP files directly (properly configured with bend radiuses)
- Flat pattern creation: sheet metal > create > flat pattern
- Requires selecting a stationary face (typically the starting face)
- Shows reliefs, bend lines, and bend radius lines
- Can export directly to DXF with bend lines

### Bending Limits and Considerations
- Bend length limitations
- Material thickness limitations
- Material type limitations
- Reasons for limits: shipping, tonnage, tooling, operator safety, preventing punch/die shattering

### Maximum and Minimum Bend Angles
- Dictated by material characteristics
- Some materials yield better than others
- Some handle more or less angle
- Thicker materials may crack, deform, or require too much tonnage at certain angles
- Longer bends require more stretching, stress, and tonnage

### U Channel Ratio
- U channel: two bends across from each other
- If bends too close, corner contacts tooling and prevents second bend completion
- Safe ratio for metal: 2:1 (base must be twice as long as flanges)
- Safe ratio for plastics: 3:1
- Plastic requires larger channel due to overbending and springback

### Parallel Lines to Bends
- Bends need parallel lines for backstop alignment
- Backstop ensures bend is in right orientation
- Center line must be centered underneath punch
- Requires parallel edge for proper alignment
- Can be achieved through tabs or other parallel features
- DFM may request parallel edge if missing

### Terms
- Sheet Metal Rules - Configuration settings that define material thickness, K factor, bend radius, relief shapes, and corner conditions for sheet metal parts
- Component - An independent part in CAD that can have its own sheet metal rules separate from other components
- Body - A part created under the master file that shares sheet metal rules with the master file
- Flange - A bent section of sheet metal that extends from a base or another flange
- K Factor - A value used in calculations to determine bend allowance and bend deduction based on material properties
- Bend Radius - The radius of the bend, dictated by the punch used in the bending machine
- Relief Shape - The shape of the relief cut (round, straight, or tear) used when a bend intersects with a cut
- Bend Relief - A cut or slot made when a bend line intersects with another feature, defined by width and depth
- Corner Relief - A relief feature created when two bends intersect at a corner, can be square or round
- Corner Conditions - Settings that define how corners are handled when two bends intersect (square or round shapes)
- Flat Pattern - The unfolded 2D representation of a 3D sheet metal part, showing all bends, reliefs, and dimensions
- U Channel - A sheet metal part with two parallel bends creating a U-shaped cross-section
- U Channel Ratio - The ratio between the base length and flange length in a U channel (2:1 for metal, 3:1 for plastics)
- Parallel Lines to Bends - Edges or features that must be parallel to a bend line to allow proper backstop alignment in the bending machine
- Backstop - A machine component that positions the material to ensure the bend is in the correct orientation and centered under the punch
- Bend Position - The location of the bend relative to the selected edge (inside, outside, or adjacent)
- Stationary Face - The face selected when creating a flat pattern that remains fixed during the unfolding process

///

## According to the video, what is the recommended approach for organizing sheet metal parts in CAD?

---

A) Create all parts as bodies under the master file

B) Move all sheet metal parts into new components

C) Keep all parts in a single component

D) Create separate files for each part

---

B) Move all sheet metal parts into new components

///

## True or False: Sheet metal rules can be obtained directly from SendCutSend for both Fusion and SolidWorks.

---

A) True

B) False

---

True

///

## What happens if the material thickness in sheet metal rules is incorrect?

---

A) The part will not render in 3D

B) The bend lines and flanges will not be correct

C) The part will be too heavy

D) The part cannot be exported

---

B) The bend lines and flanges will not be correct

///

## According to the video, what are the three options for relief shape in bend conditions?

---

A) Square, round, and triangular

B) Round, straight, and tear

C) Square, round, and straight

D) Round, tear, and square

---

B) Round, straight, and tear

///

## What is the K factor used for in sheet metal design?

---

A) Determining material cost

B) Calculating bend allowance and bend deduction

C) Setting the bend angle

D) Choosing the punch size

---

B) Calculating bend allowance and bend deduction

///

## True or False: The bend radius is dictated by the punch used in the bending machine.

---

A) True

B) False

---

True

///

## What are the two corner condition shapes available when two bends intersect?

---

A) Square and triangular

B) Round and square

C) Round and tear

D) Square and straight

---

B) Round and square

///

## According to the video, what is the recommended way to measure flange height?

---

A) From the inner face

B) From the tangent point

C) From the outer face

D) From the center point

---

C) From the outer face

///

## What happens when you change a flange from "full edge" to "two sides"?

---

A) The flange becomes longer

B) The flange edge moves within the bend line, setting up a bend relief situation

C) The bend angle changes

D) The material thickness increases

---

B) The flange edge moves within the bend line, setting up a bend relief situation

///

## True or False: Creating two flanges simultaneously produces the same corner relief as creating them one at a time.

---

A) True

B) False

---

False

///

## According to the video, why might someone create flanges one at a time instead of simultaneously?

---

A) It's faster to do one at a time

B) It creates a tighter corner that is easier to weld

C) It uses less material

D) It produces stronger bends

---

B) It creates a tighter corner that is easier to weld

///

## What file format can be directly uploaded to SendCutSend if the part is properly configured with bend radiuses?

---

A) DXF file

B) STEP file

C) PDF file

D) DWG file

---

B) STEP file

///

## When creating a flat pattern, what does the software ask you to select?

---

A) A bend line

B) A stationary face

C) A corner point

D) An edge

---

B) A stationary face

///

## True or False: The flat pattern shows reliefs, bend lines, and bend radius lines.

---

A) True

B) False

---

True

///

## What are some reasons for bending limitations mentioned in the video?

---

A) Cost and time constraints only

B) Shipping, tonnage, tooling, and operator safety reasons

C) Material availability only

D) Software limitations only

---

B) Shipping, tonnage, tooling, and operator safety reasons

///

## According to the video, what happens to tonnage requirements as bend length increases?

---

A) Tonnage decreases

B) Tonnage stays the same

C) Tonnage increases

D) Tonnage is not affected

---

C) Tonnage increases

///

## What is the safe U channel ratio for metal materials?

---

A) 1:1

B) 2:1

C) 3:1

D) 4:1

---

B) 2:1

///

## True or False: The U channel ratio for plastics is 3:1 because plastics require severe overbending and springback.

---

A) True

B) False

---

True

///

## What happens if two bends in a U channel are too close to each other?

---

A) The material will crack

B) The corner will contact the tooling and prevent completing the second bend

C) The part will be too weak

D) The bends will not form properly

---

B) The corner will contact the tooling and prevent completing the second bend

///

## According to the video, why do bends need parallel lines?

---

A) For aesthetic purposes

B) For the backstop to ensure proper alignment and centering under the punch

C) To reduce material waste

D) To make the part stronger

---

B) For the backstop to ensure proper alignment and centering under the punch

///

## What is a Component in the context of sheet metal design?

---

A) A measurement tool

B) An independent part in CAD that can have its own sheet metal rules

C) A type of bend

D) A material property

---

B) An independent part in CAD that can have its own sheet metal rules

///

## True or False: A Body is created under the master file and shares sheet metal rules with the master file.

---

A) True

B) False

---

True

///

## What is a Flange?

---

A) A type of material

B) A bent section of sheet metal that extends from a base or another flange

C) A measurement unit

D) A software tool

---

B) A bent section of sheet metal that extends from a base or another flange

///

## According to the video, what does the K Factor determine?

---

A) Material cost

B) Bend allowance and bend deduction based on material properties

C) Punch selection

D) Material thickness

---

B) Bend allowance and bend deduction based on material properties

///

## What is the Bend Radius?

---

A) The angle of the bend

B) The radius of the bend, dictated by the punch used

C) The length of the flange

D) The material thickness

---

B) The radius of the bend, dictated by the punch used

///

## True or False: Relief Shape refers to the shape of the relief cut used when a bend intersects with a cut, and can be round, straight, or tear.

---

A) True

B) False

---

True

///

## What is Bend Relief?

---

A) A type of material

B) A cut or slot made when a bend line intersects with another feature

C) A measurement tool

D) A software setting

---

B) A cut or slot made when a bend line intersects with another feature

///

## According to the video, what is Corner Relief?

---

A) A type of material finish

B) A relief feature created when two bends intersect at a corner

C) A measurement technique

D) A software bug

---

B) A relief feature created when two bends intersect at a corner

///

## What is a Flat Pattern?

---

A) A 3D model of the part

B) The unfolded 2D representation of a 3D sheet metal part

C) A type of material

D) A measurement tool

---

B) The unfolded 2D representation of a 3D sheet metal part

///

## True or False: A U Channel is a sheet metal part with two parallel bends creating a U-shaped cross-section.

---

A) True

B) False

---

True

///

## What is the U Channel Ratio for plastics?

---

A) 1:1

B) 2:1

C) 3:1

D) 4:1

---

C) 3:1

///

## According to the video, what are Parallel Lines to Bends?

---

A) Decorative features

B) Edges or features that must be parallel to a bend line for proper backstop alignment

C) Measurement lines

D) Software guidelines

---

B) Edges or features that must be parallel to a bend line for proper backstop alignment

///

## What is a Backstop?

---

A) A type of material

B) A machine component that positions material for proper bend orientation

C) A software tool

D) A measurement unit

---

B) A machine component that positions material for proper bend orientation

///

## True or False: Bend Position refers to the location of the bend relative to the selected edge and can be inside, outside, or adjacent.

---

A) True

B) False

---

True

///

## What is a Stationary Face?

---

A) A type of material finish

B) The face selected when creating a flat pattern that remains fixed during unfolding

C) A measurement technique

D) A software setting

---

B) The face selected when creating a flat pattern that remains fixed during unfolding

///

## Master Answer Key

1. **B** - Components allow independent sheet metal rules for each part, making it easier to manage different materials and configurations separately.

2. **True** - SendCutSend provides sheet metal rules for both Fusion and SolidWorks that can be downloaded from their website.

3. **B** - Material thickness is critical for calculating bend allowance and bend deduction. If incorrect, the bend lines and flanges will not be accurate.

4. **B** - The three relief shape options are round, straight, and tear, which determine how the relief cut appears when a bend intersects with another feature.

5. **B** - The K factor is a material property value used in calculations to determine bend allowance and bend deduction accurately.

6. **True** - The bend radius is determined by the physical punch tool used in the bending machine, not by software settings alone.

7. **B** - When two bends intersect, the corner can be configured as either square or round, affecting how the material is cut at the intersection.

8. **C** - Measuring from the outer face is the standard industry practice and ensures consistent measurements across different parts.

9. **B** - Changing to "two sides" moves the flange edge within the bend line, which automatically triggers the creation of a bend relief slot.

10. **False** - Creating flanges simultaneously produces different corner relief patterns than creating them sequentially, as shown in the video demonstration.

11. **B** - Creating flanges one at a time produces a tighter corner that is more suitable for weldments, making welding easier.

12. **B** - If properly configured with correct bend radiuses, a STEP file can be directly uploaded to SendCutSend without needing a flat pattern.

13. **B** - The flat pattern tool requires selecting a stationary face, which serves as the reference point for unfolding the 3D part into 2D.

14. **True** - The flat pattern displays all the relief cuts, bend lines, and bend radius lines that will be used in manufacturing.

15. **B** - Bending limitations exist for multiple practical reasons including shipping constraints, machine tonnage capacity, available tooling, and most importantly, operator safety.

16. **C** - Longer bends require more material stretching and stress, which increases the tonnage needed to complete the bend operation.

17. **B** - For metal materials, the base must be at least twice as long as the flanges (2:1 ratio) to prevent tooling interference.

18. **True** - Plastics require a 3:1 ratio because they need to be severely overbent to account for springback, requiring more clearance.

19. **B** - If bends are too close, the corner of the material will physically contact the machine tooling, preventing the second bend from being completed.

20. **B** - Parallel lines are essential for the backstop mechanism to properly align the material and center the bend line under the punch.

21. **B** - Components are independent parts that can have their own sheet metal rules, unlike bodies which share rules with the master file.

22. **True** - Bodies are created under the master file structure and inherit or share the sheet metal rules from the master file level.

23. **B** - A flange is a bent section that extends from either a base flat section or from another existing flange.

24. **B** - The K factor is a material-specific constant used in mathematical formulas to calculate how much material is needed for accurate bends.

25. **B** - The bend radius is physically determined by the size and shape of the punch tool that will be used in the actual bending machine.

26. **True** - Relief shapes determine the appearance of cuts made when bends intersect other features, with round, straight, and tear being the three options.

27. **B** - Bend relief is an automatically or manually created cut/slot that prevents material deformation when a bend line intersects with another feature.

28. **B** - Corner relief is a special type of relief feature that appears specifically at corners where two bends intersect each other.

29. **B** - A flat pattern is the 2D unfolded version of a 3D sheet metal part, showing all dimensions and features as they would appear before bending.

30. **True** - A U channel is defined by having two parallel bends that create the characteristic U-shaped cross-section when viewed from the end.

31. **C** - Plastics require a 3:1 ratio (base three times longer than flanges) due to the overbending and springback characteristics of plastic materials.

32. **B** - Parallel lines are required features that allow the machine's backstop to properly position and align the material for accurate bending.

33. **B** - The backstop is a physical machine component that holds the material in the correct position to ensure the bend line is properly centered under the punch.

34. **True** - Bend position is a setting that determines where the actual bend occurs relative to the selected edge, with three options: inside, outside, or adjacent.

35. **B** - The stationary face is the reference face that remains fixed when the software unfolds the 3D part into a 2D flat pattern representation.

