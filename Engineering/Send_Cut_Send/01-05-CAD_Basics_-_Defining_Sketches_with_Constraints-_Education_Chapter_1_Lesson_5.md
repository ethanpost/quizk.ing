# CAD Basics - Defining Sketches with Constraints Quiz

## Outline

### Introduction to Constraints
- Constraints are the "rules" of CAD that prevent chaos
- Constraints keep sketches from falling apart over time
- Located in the constraints drawer within the Fusion toolbox

### Goal: Fully Defined Sketches
- The objective is to create fully defined sketches
- Fully defined features turn black instead of blue
- Blue color indicates undefined/chaotic elements
- Black color indicates fully constrained elements

### Constraint Types and Applications

#### Parallel Constraint
- Makes two lines parallel to each other
- First selected line drives the orientation of the second
- Lines remain blue (undefined) but maintain parallel relationship
- Can move lines anywhere while keeping them parallel

#### Horizontal/Vertical Constraint
- Forces a line to be perfectly horizontal or vertical
- Uses 45-degree rule: lines >45° become vertical, <45° become horizontal
- Only requires selecting one line
- When combined with parallel constraint, affects both lines

#### Coincident Constraint
- Based on points, not lines
- Attaches one point to another point
- Can attach sketch elements to origin or other reference points
- Partially defines elements (some parts turn black, others remain blue)

#### Equal Constraint
- Makes two lines equal in length
- Requires selecting two lines
- Creates relationship where changing one line's length affects the other
- Both lines maintain equal length automatically

#### Midpoint Constraint
- Places a point at the exact middle of a line
- Requires selecting a point and a line
- Point snaps to the center of the selected line
- Maintains midpoint relationship when line length changes

#### Perpendicular Constraint
- Makes two lines perpendicular (90-degree angle)
- Requires selecting two lines
- Significantly restricts movement options
- Lines can only move up/down and change length, not left/right

### Constraint Interaction and Power
- Multiple constraints work together in the background
- Two constraints can control three or more features
- Constraints build upon each other to create complex relationships
- Each constraint reduces degrees of freedom

### Visual Indicators
- Blue color = undefined/chaotic elements
- Black color = fully defined elements
- White dots = free-floating points
- Black dots = constrained points

### Next Steps
- Dimensions are needed to fully define sketches
- Constraints alone are not sufficient for complete definition
- Dimensions will be covered in the next lesson

### Terms
- **Constraint** – A rule in CAD that defines relationships between sketch elements
- **Fully Defined Sketch** – A sketch where all elements are black, indicating complete constraint
- **Parallel Constraint** – Forces two lines to remain parallel to each other
- **Horizontal/Vertical Constraint** – Forces a line to be perfectly horizontal or vertical
- **Coincident Constraint** – Attaches one point to another point
- **Equal Constraint** – Makes two lines equal in length
- **Midpoint Constraint** – Places a point at the exact middle of a line
- **Perpendicular Constraint** – Forces two lines to meet at a 90-degree angle
- **45-Degree Rule** – The rule that determines whether a line becomes horizontal or vertical based on its current angle

///

## Quiz Questions

What color indicates that a sketch element is fully defined?

---

A) Blue

B) Red

C) Black

D) Green

---

Black

///

True or False: Constraints are optional rules that can be ignored when creating CAD sketches.

---

A) True

B) False

---

False

///

When using the parallel constraint, which line determines the orientation of the other?

---

A) The second line selected

B) The first line selected

C) The longer line

D) The shorter line

---

The first line selected

///

What is the 45-degree rule used for?

---

A) Determining line length

B) Deciding between horizontal and vertical constraints

C) Creating perpendicular lines

D) Setting parallel relationships

---

Deciding between horizontal and vertical constraints

///

Which constraint requires selecting only one line?

---

A) Parallel

B) Equal

C) Horizontal/Vertical

D) Perpendicular

---

Horizontal/Vertical

///

What does the coincident constraint work with?

---

A) Lines only

B) Points only

C) Circles only

D) Both lines and points

---

Points only

///

True or False: When two lines have an equal constraint, changing the length of one automatically changes the length of the other.

---

A) True

B) False

---

True

///

The midpoint constraint places a point at what location on a line?

---

A) One-quarter from the end

B) The exact middle

C) Three-quarters from the end

D) At either endpoint

---

The exact middle

///

Which constraint significantly restricts movement to only up/down and length changes?

---

A) Parallel

B) Horizontal

C) Perpendicular

D) Equal

---

Perpendicular

///

What is the main goal when applying constraints to a sketch?

---

A) To make sketches colorful

B) To create a fully defined sketch

C) To make sketches move faster

D) To reduce file size

---

To create a fully defined sketch

///

True or False: Blue-colored elements in a sketch indicate that they are fully constrained.

---

A) True

B) False

---

False

///

How many constraints were used to control three features in the lesson example?

---

A) One

B) Two

C) Three

D) Four

---

Two

///

What happens to sketch elements when they are fully defined?

---

A) They turn blue

B) They turn red

C) They turn black

D) They disappear

---

They turn black

///

Which constraint would you use to attach a sketch point to the origin?

---

A) Parallel

B) Coincident

C) Equal

D) Perpendicular

---

Coincident

///

True or False: Constraints alone are sufficient to create a fully defined sketch.

---

A) True

B) False

---

False

///

## Master Answer Key

1. C – Black color indicates fully defined elements, while blue indicates undefined elements.

2. B – Constraints are essential rules that prevent chaos in CAD sketches and cannot be ignored.

3. B – The first line selected determines the orientation that the second line will adopt.

4. B – The 45-degree rule determines whether a line becomes horizontal (<45°) or vertical (>45°) when using the horizontal/vertical constraint.

5. C – The horizontal/vertical constraint only requires selecting one line, unlike parallel, equal, and perpendicular constraints which require two selections.

6. B – The coincident constraint works specifically with points, allowing you to attach one point to another.

7. A – The equal constraint creates a relationship where both lines maintain the same length automatically.

8. B – The midpoint constraint places a point at the exact middle of a line, as the name suggests.

9. C – The perpendicular constraint restricts movement significantly, allowing only vertical movement and length changes.

10. B – The main goal of applying constraints is to create a fully defined sketch where all elements are properly constrained.

11. B – Blue-colored elements indicate undefined/chaotic elements, not fully constrained ones.

12. B – Two constraints (parallel and horizontal) were used to control three features (both lines being parallel, both being horizontal).

13. C – Fully defined elements turn black, indicating they are properly constrained.

14. B – The coincident constraint is used to attach points together, such as attaching a sketch point to the origin.

15. B – Constraints alone are not sufficient; dimensions are also needed to fully define a sketch.
