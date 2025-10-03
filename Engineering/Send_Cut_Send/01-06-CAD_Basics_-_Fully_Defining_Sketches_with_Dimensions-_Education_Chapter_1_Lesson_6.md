# CAD Basics - Fully Defining Sketches with Dimensions

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

A) To make sketches as colorful as possible

B) To create a fully defined black sketch with no blue objects

C) To use as many constraints as possible

D) To make sketches that are easy to move around

---

To create a fully defined black sketch with no blue objects

///

What keyboard shortcut is typically used for the Sketch Dimension tool?

---

A) S

B) D

C) C

D) M

---

D

///

When you click on a circle with the Sketch Dimension tool, what type of dimension does it automatically create?

---

A) Linear distance

B) Diameter or radius

C) Angle measurement

D) Area calculation

---

Diameter or radius

///

How do you edit an existing dimension in Fusion 360?

---

A) Right-click and select "Edit"

B) Press the Delete key

C) Double-click with the left mouse button

D) Use the keyboard shortcut Ctrl+E

---

Double-click with the left mouse button

///

What happens to your dimensions when you change the unit system in Document Settings?

---

A) They disappear completely

B) They automatically convert to the new units

C) They become invalid and must be recreated

D) Nothing changes

---

They automatically convert to the new units

///

True or False: You can perform mathematical calculations directly within dimension values in Fusion 360.

---

A) True

B) False

---

True

///

What does a blue line in a sketch indicate?

---

A) The line is fully defined and cannot be moved

B) The line is undefined and can still be moved

C) The line is selected for editing

D) The line is locked in position

---

The line is undefined and can still be moved

///

What is a "profile" in CAD sketching?

---

A) A user's personal settings

B) A completely enclosed area that can be selected for 3D object creation

C) A type of constraint

D) A measurement tool

---

A completely enclosed area that can be selected for 3D object creation

///

What does the tangent constraint do?

---

A) Makes two lines parallel to each other

B) Creates a single point of contact between a line and circle

C) Forces two points to occupy the same location

D) Makes lines perpendicular to each other

---

Creates a single point of contact between a line and circle

///

How many tangent lines can touch a single circle?

---

A) Only one

B) Exactly two

C) Multiple lines from different directions

D) None

---

Multiple lines from different directions

///

What happens when you change a dimension in a well-designed parametric sketch?

---

A) Only that specific element changes

B) All related geometry updates automatically

C) The sketch becomes invalid

D) Nothing happens

---

All related geometry updates automatically

///

Where is the Mirror tool located in Fusion 360?

---

A) In the Constraints menu

B) In the Create menu

C) In the Modify menu

D) In the Sketch menu

---

In the Create menu

///

What does the coincident constraint do?

---

A) Makes two lines parallel

B) Forces two points to occupy the same location in space

C) Creates a tangent relationship

D) Measures the distance between two points

---

Forces two points to occupy the same location in space

///

True or False: The Mirror tool is only available in Sketch mode.

---

A) True

B) False

---

False

///

What is the best way to test if a sketch is fully defined?

---

A) Look at the color of the lines

B) Try to drag the blue objects around

C) Count the number of constraints

D) Check the dimension values

---

Try to drag the blue objects around

///

When using the Mirror tool, what do you need to select?

---

A) Only the object to mirror

B) Only the mirror line

C) Both the object to mirror and the mirror line

D) The entire sketch

---

Both the object to mirror and the mirror line

///

What unit conversion feature is available when typing dimension values?

---

A) You must manually calculate conversions

B) You can type units directly (e.g., "150mm" when in inches)

C) Only metric to imperial conversion is supported

D) No unit conversion is available

---

You can type units directly (e.g., "150mm" when in inches)

///

## Master Answer Key

1. B – The primary goal is to create a fully defined black sketch with no blue objects, meaning all geometry is constrained and cannot be moved.

2. B – The default keyboard shortcut for the Sketch Dimension tool is D, though users can customize this to any key they prefer.

3. B – When clicking on a circle, the Sketch Dimension tool automatically creates either a diameter or radius dimension, depending on the circle's position.

4. C – Double-clicking with the left mouse button opens the dimension for editing, allowing you to change the value directly.

5. B – Dimensions automatically convert to the new unit system when you change units in Document Settings, maintaining the same physical size.

6. A – True. Fusion 360 has a built-in calculator that allows mathematical operations directly within dimension values, such as "2 + 2" = "4 in".

7. B – Blue lines indicate undefined geometry that can still be moved and modified, while black lines are fully defined.

8. B – A profile is a completely enclosed area in a sketch that can be selected to create three-dimensional objects through extrusion.

9. B – The tangent constraint creates a single point of contact where a line "barely kisses" the surface of a circle.

10. C – Multiple tangent lines can touch a single circle from different directions, each creating a single point of contact.

11. B – In parametric design, changing one dimension automatically updates all related geometry, maintaining relationships and proportions.

12. B – The Mirror tool is located in the Create menu and allows you to create perfect duplications across a specified line.

13. B – The coincident constraint forces two points to occupy the exact same location in space, effectively making them one point.

14. B – False. The Mirror tool is available in both Sketch mode and Extrude mode, making it versatile for different modeling operations.

15. B – The best way to test if a sketch is fully defined is to try dragging the blue objects around to see if they can still be moved.

16. C – When using the Mirror tool, you must select both the object you want to mirror and the line across which to mirror it.

17. B – You can type units directly in dimension values (like "150mm" when working in inches), and Fusion 360 will automatically convert them.
