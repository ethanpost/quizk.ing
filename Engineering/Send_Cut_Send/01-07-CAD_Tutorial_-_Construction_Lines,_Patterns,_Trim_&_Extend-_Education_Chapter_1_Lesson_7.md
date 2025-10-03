# [CAD Tutorial: Construction Lines, Patterns, Trim & Extend - Lesson 7](https://www.youtube.com/watch?v=6J4zy_D-lWE)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

## Multiple Approaches to CAD Design

### Core Philosophy
- There's always more than one way to design a part in CAD
- Different methods can achieve the same result
- Choose the approach that works best for your specific situation

### Washer Design Methods

#### Method 1: Two Circles with Dimensions
- Create outer circle with dimension (100mm example)
- Create inner circle with separate dimension (60mm example)
- Simple approach with two independent dimensions
- Requires manual constraint management

#### Method 2: Offset Tool
- Create outer circle with dimension
- Use offset tool under modify section
- Type negative value (-20mm) to create inner circle
- Automatically creates concentric constraint
- Inner circle references outer circle as driven dimension
- More parametric approach

### Construction Lines

#### Purpose and Benefits
- Used for reference geometry that doesn't affect final profile
- Appear as dotted lines in CAD
- Don't interfere with profile selection during extrusion
- Still usable as reference points for constraints

#### Creating Construction Lines
- Draw standard line through center of part
- Add vertical constraint
- Add midpoint constraint to origin
- Convert to construction line using sketch palette
- Select line → sketch palette → construction under line type

### Patterns in CAD

#### Circle Pattern
- Creates multiple copies of geometry around a center point
- Located in create section of toolbar
- Allows specification of quantity and distribution
- Can be full (360°) or partial pattern
- Counts initial geometry plus additional copies

#### Rectangular Pattern
- Creates grid-like patterns in two axes
- Useful for creating arrays of features
- Allows control of spacing and quantity in both directions
- Example: 3x2 pattern creates 6 total features

#### Mirror Pattern
- Reflects geometry across a reference line
- Uses construction lines as mirror axis
- Creates symmetrical features efficiently

### Trim and Extend Tools

#### Trim Tool
- Located in modify section
- Acts like scissors to remove unwanted lines
- Cleans up drawings for better visibility
- Removes unnecessary geometry from profiles
- Can affect constraint relationships

#### Extend Tool
- Opposite of trim tool
- Extends lines to meet other geometry
- Useful for connecting separate profiles
- Located next to trim tool in modify section

### Key Design Process

#### Creating Keys on Washer
- Use construction line as reference
- Draw half of key shape with perpendicular lines
- Add dimensions for positioning and sizing
- Use mirror tool to create symmetrical key
- Apply circle pattern to create multiple keys at 120° intervals

#### Dimensioning Strategy
- Reference outer circle for positioning
- Use half-width dimensions for symmetry
- Re-establish constraints after trimming operations

### Terms

- **CAD** – Computer-Aided Design software for creating technical drawings and 3D models
- **Construction Line** – Reference geometry that appears as dotted lines and doesn't affect final profiles
- **Constraint** – Rules that define relationships between geometric elements
- **Dimension** – Numerical values that specify size and position of geometry
- **Extrude** – Process of converting 2D profiles into 3D objects
- **Mirror** – Tool that creates symmetrical copies of geometry across a reference line
- **Offset** – Tool that creates parallel copies of geometry at specified distances
- **Pattern** – Tool that creates multiple copies of geometry in circular or rectangular arrangements
- **Profile** – Closed 2D shape used for creating 3D features
- **Trim** – Tool that removes unwanted portions of lines or curves
- **Extend** – Tool that lengthens lines to meet other geometry

///

## What is the main philosophy emphasized throughout this CAD lesson?

---

A) Follow exact procedures for consistency

B) There's always more than one way to design a part

C) Avoid using advanced tools when possible

D) Always use the simplest method available

---

B) There's always more than one way to design a part

///

## Which method automatically creates a concentric constraint between circles?

---

A) Using construction lines

B) Drawing two separate circles with dimensions

C) Using the offset tool

D) Using the trim tool

---

C) Using the offset tool

///

## What visual characteristic identifies construction lines in CAD?

---

A) They appear with arrows at the ends

B) They appear in different colors

C) They appear thicker than regular lines

D) They appear as dotted lines

---

D) They appear as dotted lines

///

## True or False: Construction lines affect the final profile when extruding.

---

A) False

B) True

---

A) False

///

## How many total features does a circle pattern with quantity set to 3 create?

---

A) 6 features

B) 4 features

C) 3 features

D) 2 features

---

C) 3 features

///

## What is the primary advantage of using the offset tool over drawing two separate circles?

---

A) It creates smoother curves

B) It automatically maintains concentric relationship

C) It uses less memory

D) It creates more accurate dimensions

---

B) It automatically maintains concentric relationship

///

## Where is the circle pattern tool located in the CAD interface?

---

A) Dimension toolbar

B) Create section

C) Modify section

D) Sketch palette

---

B) Create section

///

## What happens when you trim a line that was created using the offset tool?

---

A) The dimensions are automatically updated

B) Nothing changes

C) Both circles disappear

D) The constraint relationship is lost

---

D) The constraint relationship is lost

///

## True or False: The trim tool can be used to clean up drawings for better visibility.

---

A) False

B) True

---

B) True

///

## What type of pattern creates a grid-like arrangement of features?

---

A) Linear pattern

B) Mirror pattern

C) Circle pattern

D) Rectangular pattern

---

D) Rectangular pattern

///

## Which tool is described as "the exact opposite of trim"?

---

A) Pattern

B) Mirror

C) Extend

D) Offset

---

C) Extend

///

## When creating keys on a washer, what angle spacing is used for three keys?

---

A) 360 degrees

B) 90 degrees

C) 180 degrees

D) 120 degrees

---

D) 120 degrees

///

## What constraint is automatically created when using the offset tool?

---

A) Horizontal constraint

B) Tangent constraint

C) Concentric constraint

D) Vertical constraint

---

C) Concentric constraint

///

## True or False: Construction lines can still be used as reference points for constraints.

---

A) False

B) True

---

B) True

///

## What is the main purpose of cleaning up drawings with trim and extend tools?

---

A) To speed up processing

B) To improve visibility and ease of modification

C) To reduce file size

D) To increase accuracy

---

B) To improve visibility and ease of modification

///

## Which method requires manually managing constraints between circles?

---

A) Using construction lines

B) Using the mirror tool

C) Drawing two separate circles with dimensions

D) Using the offset tool

---

C) Drawing two separate circles with dimensions

///

## What happens to the inner circle dimension when the outer circle dimension is changed using the offset method?

---

A) It becomes undefined

B) It changes proportionally

C) It remains unchanged

D) It maintains the offset relationship

---

D) It maintains the offset relationship

///

## True or False: The extend tool can be used to connect separate profiles.

---

A) False

B) True

---

B) True

///

## What is the recommended approach for creating symmetrical features like keys?

---

A) Use only circle patterns

B) Draw complete shapes and then trim

C) Draw each feature individually

D) Draw half and use mirror tool

---

D) Draw half and use mirror tool

///

## Which tool allows you to specify both quantity and distribution angle for patterns?

---

A) Mirror pattern

B) Circle pattern

C) Linear pattern

D) Rectangular pattern

---

B) Circle pattern

///

## Master Answer Key

1. B – The lesson emphasizes that there are multiple valid approaches to achieve the same CAD design result
2. C – The offset tool automatically creates a concentric constraint
3. D – Construction lines appear as dotted lines
4. A – Construction lines do not affect final profiles during extrusion
5. C – A circle pattern with quantity 3 creates 3 total features
6. B – The offset tool automatically maintains concentric relationship
7. B – The circle pattern tool is located in the create section
8. D – Trimming offset lines breaks the constraint relationship
9. B – The trim tool can be used to clean up drawings
10. D – Rectangular patterns create grid-like arrangements
11. C – The extend tool is the opposite of trim
12. D – Three keys are spaced at 120-degree intervals
13. C – The offset tool creates concentric constraints
14. B – Construction lines can be used as reference points
15. B – Cleaning up improves visibility and ease of modification
16. C – Drawing separate circles requires manual constraint management
17. D – The offset method maintains dimensional relationships
18. B – The extend tool can connect separate profiles
19. D – Drawing half and using mirror is recommended for symmetry
20. B – Circle patterns specify both quantity and distribution angle
