# [CAD Basics - Fully Defining Sketches with Dimensions](https://www.youtube.com/watch?v=Dad8iaUkwyY)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

### You can also import this file into [Mochi](https://mochi.cards/).
- When importing make sure you select Markdown as the format.
- Select "Multiple cards per .md file", 
- Set a ```triple backslash``` as the string delimiter, like this ///
- Use the link to the raw file in GitHub instead of downloading and importing if you prefer.

## Outline

### Introduction to Dimensions
- Building on constraints from previous lesson
- Dimensions as measurement rules
- Goal: fully defined black sketch (no blue objects)
- Dimensions define measurements in millimeters, inches, degrees

### Using Sketch Dimension Tool
- Located in Create menu under Sketch tab
- Default keyboard shortcut: D key
- Automatically applies appropriate dimension based on object type
- Circles get diameter or radius dimensions
- Lines get linear distance dimensions
- Follows current unit settings

### Setting and Editing Dimensions
- Click and drag to place dimension
- Type desired value when highlighted in blue
- Press Escape to exit dimension tool
- Double-click dimension to edit value
- Supports unit conversion (e.g., typing "150mm" when in inches)
- Built-in math calculator (e.g., "2 + 2" = "4 in")

### Unit Management
- Access through Document Settings → Units
- Change between millimeters, inches, centimeters
- Can set as default for future projects
- Dimensions automatically convert when units change

### Achieving Fully Defined Sketches
- Black lines indicate fully defined geometry
- Blue lines indicate undefined geometry that can still be moved
- Test by attempting to drag blue objects
- Add dimensions to fix remaining undefined elements
- Goal: all geometry becomes black and non-movable

### Introduction to Profiles
- Profile: completely enclosed area selectable for 3D object creation
- Required for creating three-dimensional objects from sketches
- Can select multiple profiles using Shift key
- Profiles make sketches "extrudable" for 3D modeling

### Advanced Constraints: Tangent
- Tangent constraint creates single point of contact between line and circle
- Line "barely kisses" the circle surface
- Multiple tangent lines possible from different directions
- Perfect mathematical tangent point in CAD software

### Combining Constraints and Dimensions
- Use tangent constraint to position circle relative to line
- Add coincident constraint to fix circle position
- Creates robust, fully defined geometry
- All elements maintain relationships when dimensions change

### Mirror Tool
- Located in Create menu
- Creates perfect duplication across a line
- Available in both Sketch and Extrude modes
- Select object to mirror, then select mirror line
- Creates secondary faint preview before confirmation

### Testing Sketch Robustness
- Change dimensions to verify all elements respond correctly
- Circles should maintain tangent relationships
- All geometry should scale proportionally
- Nothing should break or disconnect
- Demonstrates parametric design capabilities

### Terms
- **Dimension** – A measurement rule that defines the size or position of geometry using specific units
- **Profile** – A completely enclosed area in a sketch that can be selected to create three-dimensional objects
- **Tangent** – A constraint where a line touches a circle at exactly one point
- **Fully Defined Sketch** – A sketch where all geometry is black and cannot be moved or modified
- **Parametric Design** – Design approach where changing one dimension automatically updates all related geometry
- **Mirror Tool** – A feature that creates perfect duplication of geometry across a specified line
- **Coincident Constraint** – Forces two points to occupy the same location in space

///

## Quiz

What is the primary goal when creating sketches in CAD software?

---

A) To make sketches that are easy to move around

B) To create a fully defined black sketch with no blue objects

C) To make sketches as colorful as possible

D) To use as many constraints as possible

---

B) To create a fully defined black sketch with no blue objects

///

What keyboard shortcut is typically used for the Sketch Dimension tool?

---

A) C

B) S

C) D

D) M

---

C) D

///

When you click on a circle with the Sketch Dimension tool, what type of dimension does it automatically create?

---

A) Area calculation

B) Angle measurement

C) Linear distance

D) Diameter or radius

---

D) Diameter or radius

///

How do you edit an existing dimension in Fusion 360?

---

A) Use the keyboard shortcut Ctrl+E

B) Double-click with the left mouse button

C) Press the Delete key

D) Right-click and select "Edit"

---

B) Double-click with the left mouse button

///

What happens to your dimensions when you change the unit system in Document Settings?

---

A) Nothing changes

B) They become invalid and must be recreated

C) They automatically convert to the new units

D) They disappear completely

---

C) They automatically convert to the new units

///

True or False: You can perform mathematical calculations directly within dimension values in Fusion 360.

---

A) False

B) True

---

B) True

///

What does a blue line in a sketch indicate?

---

A) The line is selected for editing

B) The line is undefined and can still be moved

C) The line is locked in position

D) The line is fully defined and cannot be moved

---

B) The line is undefined and can still be moved

///

What is a "profile" in CAD sketching?

---

A) A measurement tool

B) A type of constraint

C) A completely enclosed area that can be selected for 3D object creation

D) A user's personal settings

---

C) A completely enclosed area that can be selected for 3D object creation

///

What does the tangent constraint do?

---

A) Makes lines perpendicular to each other

B) Makes two lines parallel to each other

C) Forces two points to occupy the same location

D) Creates a single point of contact between a line and circle

---

D) Creates a single point of contact between a line and circle

///

How many tangent lines can touch a single circle?

---

A) None

B) Only one

C) Multiple lines from different directions

D) Exactly two

---

C) Multiple lines from different directions

///

What happens when you change a dimension in a well-designed parametric sketch?

---

A) Nothing happens

B) The sketch becomes invalid

C) Only that specific element changes

D) All related geometry updates automatically

---

D) All related geometry updates automatically

///

Where is the Mirror tool located in Fusion 360?

---

A) In the Modify menu

B) In the Create menu

C) In the Sketch menu

D) In the Constraints menu

---

B) In the Create menu

///

What does the coincident constraint do?

---

A) Creates a tangent relationship

B) Makes two lines parallel

C) Forces two points to occupy the same location in space

D) Measures the distance between two points

---

C) Forces two points to occupy the same location in space

///

True or False: The Mirror tool is only available in Sketch mode.

---

A) False

B) True

---

A) False

///

What is the best way to test if a sketch is fully defined?

---

A) Check the dimension values

B) Count the number of constraints

C) Try to drag the blue objects around

D) Look at the color of the lines

---

C) Try to drag the blue objects around

///

When using the Mirror tool, what do you need to select?

---

A) The entire sketch

B) Only the mirror line

C) Only the object to mirror

D) Both the object to mirror and the mirror line

---

D) Both the object to mirror and the mirror line

///

What unit conversion feature is available when typing dimension values?

---

A) Only metric to imperial conversion is supported

B) You must manually calculate conversions

C) You can type units directly (e.g., "150mm" when in inches)

D) No unit conversion is available

---

C) You can type units directly (e.g., "150mm" when in inches)

///

## Master Answer Key

1. B – The primary goal is to create a fully defined black sketch with no blue objects, meaning all geometry is constrained and cannot be moved.

2. C – The default keyboard shortcut for the Sketch Dimension tool is D, though users can customize this to any key they prefer.

3. D – When clicking on a circle, the Sketch Dimension tool automatically creates either a diameter or radius dimension, depending on the circle's position.

4. B – Double-clicking with the left mouse button opens the dimension for editing, allowing you to change the value directly.

5. C – Dimensions automatically convert to the new unit system when you change units in Document Settings, maintaining the same physical size.

6. B – True. Fusion 360 has a built-in calculator that allows mathematical operations directly within dimension values, such as "2 + 2" = "4 in".

7. B – Blue lines indicate undefined geometry that can still be moved and modified, while black lines are fully defined.

8. C – A profile is a completely enclosed area in a sketch that can be selected to create three-dimensional objects through extrusion.

9. D – The tangent constraint creates a single point of contact where a line "barely kisses" the surface of a circle.

10. C – Multiple tangent lines can touch a single circle from different directions, each creating a single point of contact.

11. D – In parametric design, changing one dimension automatically updates all related geometry, maintaining relationships and proportions.

12. B – The Mirror tool is located in the Create menu and allows you to create perfect duplications across a specified line.

13. C – The coincident constraint forces two points to occupy the exact same location in space, effectively making them one point.

14. A – False. The Mirror tool is available in both Sketch mode and Extrude mode, making it versatile for different modeling operations.

15. C – The best way to test if a sketch is fully defined is to try dragging the blue objects around to see if they can still be moved.

16. D – When using the Mirror tool, you must select both the object you want to mirror and the line across which to mirror it.

17. C – You can type units directly in dimension values (like "150mm" when working in inches), and Fusion 360 will automatically convert them.
