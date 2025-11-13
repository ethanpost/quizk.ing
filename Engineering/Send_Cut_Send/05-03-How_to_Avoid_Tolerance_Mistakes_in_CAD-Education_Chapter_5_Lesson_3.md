## [How to Avoid Tolerance Mistakes in CAD - Education Chapter 5 Lesson 3](https://www.youtube.com/watch?v=UDo5vV6mmHw)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## How to Avoid Tolerance Mistakes in CAD Overview

### Introduction
- Manufacturing cannot achieve perfect CAD dimensions
- Cutting process directly affects tolerancing
- Tolerancing determines how close parts come to CAD design

### Understanding Tolerancing
- Definition: Accounting of manufacturing process accounting for multiple key factors
- Factors affecting tolerancing:
  - Machine movement or "slop"
  - Room temperature
  - Workholding
  - Various other manufacturing factors
- Format: Unit plus or minus a value
- Example: ±0.005 inches tolerance
  - Represents one to two human hairs of movement
  - Defines acceptable window for a good part
- Tolerance range example:
  - For 2-inch dimension with ±0.005 tolerance
  - Acceptable range: 1.995 to 2.005 inches
- Cost implications:
  - Tighter tolerances require fancier machines and increase cost
  - Looser tolerances allow cruder materials/machines and reduce cost
- Tolerancing must be built into parts
- Directly affects cost and manufacturability

### Tolerance Stacking
- Definition: Accumulation of tolerances from multiple sources
- Types of tolerance stacking:

#### Manufacturing Process Stacking
- Kerf width creates tolerance between waist and good part
- Taper effect from top to bottom of part in laser process
- Different dimensions on top vs. bottom of part
- Curve adds tolerance depending on which side of part is used

#### Part to Part Stacking
- Example: Part A with tapped holes, Part B with through holes
- Both parts have same dimension (edge to hole center = 1 inch)
- Individual part tolerance: ±0.005 inches
- Assembly tolerance: ±0.010 inches (double the individual tolerance)
- When parts are at opposite extremes of tolerance, total difference is 0.010 inches
- Design consideration: Through holes must account for assembly tolerance
- If through holes are too tight, bolts won't align properly
- Multiple parts require accounting for combined tolerances

#### Operation to Operation Stacking
- Multiple operations add tolerance
- Example: Cutting part out, then separate tapping operation
- Each operation adds tolerance from:
  - Different mounting processes
  - Different setups
  - Different machines handling the part
- More operations = more tolerance accumulation
- Important for complex parts with secondary operations
- Applies to bending, hardware installation, and other secondary operations

#### Dimensioning Method Stacking
- Using manufacturer like SendCutSend with DXF: Overall tolerance ±0.005 inches
- With hand drawings or CAD drawings: Dimensioning method affects tolerance
- Correct method: Dimension from common origin point
  - Each dimension referenced to same origin
  - Tolerances don't stack
- Incorrect method: Chain dimensioning
  - First hole dimensioned from edge
  - Each subsequent hole dimensioned from previous hole
  - Each dimension has ±0.005 tolerance
  - Final hole can be over 0.020 inches off from intended position
- Best practice: Pick common origin so tolerancing is with respect to that origin
- Note: SendCutSend uses DXF/STEP files directly, so this is less of an issue

### Additional Factors Affecting Fitment
- Tabs from workholding
- Tabs on inside of holes interfere with bolt fitment
- Tabs on outside interfere with part seating
- Tabs can be sanded away but require secondary operation
- Should account for tabs in design if secondary operation not desired

### Terms
- Tolerance - The allowable variation from a specified dimension, accounting for manufacturing process limitations and expressed as plus or minus a value (e.g., ±0.005 inches).
- Tolerancing - The process of accounting for manufacturing variations and establishing acceptable dimensional ranges for parts.
- Tolerance Stacking - The accumulation of tolerances from multiple sources such as manufacturing processes, multiple parts, multiple operations, or dimensioning methods, which can compound to create larger total variations.
- Kerf - The width of material removed during cutting, which creates a gap between the cut edge and the intended part dimension.
- Workholding - The method or device used to secure a part during manufacturing operations.
- Assembly Tolerance - The combined tolerance when multiple parts with individual tolerances are assembled together, typically the sum of individual part tolerances.
- Chain Dimensioning - An incorrect dimensioning method where each feature is dimensioned from the previous feature, causing tolerances to stack.
- Common Origin Dimensioning - The correct dimensioning method where all features are dimensioned from a single reference point, preventing tolerance stacking.

///

## According to the video, what is tolerancing?

---

A) An accounting of the manufacturing process accounting for multiple key factors

B) The exact measurement of a part dimension

C) The cost of manufacturing a part

D) The speed at which parts can be manufactured

---

An accounting of the manufacturing process accounting for multiple key factors

///

## What factors can affect tolerancing according to the video?

---

A) Only machine movement

B) Machine movement, room temperature, and workholding

C) Only room temperature

D) Only workholding

---

Machine movement, room temperature, and workholding

///

## According to the video, what does a ±0.005 inch tolerance represent?

---

A) One millimeter of movement

B) One centimeter of movement

C) One to two human hairs of movement

D) One inch of movement

---

One to two human hairs of movement

///

## If a part has a 2-inch dimension with ±0.005 tolerance, what is the acceptable range?

---

A) 1.995 to 2.005 inches

B) 1.990 to 2.010 inches

C) 2.000 to 2.010 inches

D) 1.995 to 2.000 inches

---

1.995 to 2.005 inches

///

## According to the video, what happens to cost when tolerances are tightened?

---

A) Cost increases

B) Cost decreases

C) Cost stays the same

D) Cost is not affected

---

Cost increases

///

## What is tolerance stacking?

---

A) The process of manufacturing multiple parts at once

B) The accumulation of tolerances from multiple sources

C) The measurement of a single part dimension

D) The cost calculation for manufacturing

---

The accumulation of tolerances from multiple sources

///

## According to the video, how does the kerf affect tolerancing?

---

A) It has no effect on tolerancing

B) It only affects the top of the part

C) It creates tolerance between the waist and good part, and the taper adds tolerance depending on which side of the part is used

D) It only affects the bottom of the part

---

It creates tolerance between the waist and good part, and the taper adds tolerance depending on which side of the part is used

///

## In the part-to-part stacking example, if Part A has a dimension of 1.0025 inches and Part B has 0.9975 inches, both within ±0.005 tolerance, what is the assembly tolerance?

---

A) ±0.0025 inches

B) ±0.005 inches

C) ±0.0075 inches

D) ±0.010 inches

---

±0.010 inches

///

## According to the video, why is it important to account for assembly tolerance when designing through holes?

---

A) To ensure bolts can align properly when parts are at opposite extremes of their individual tolerances

B) To make the holes larger

C) To reduce manufacturing cost

D) To make the holes smaller

---

To ensure bolts can align properly when parts are at opposite extremes of their individual tolerances

///

## What happens to tolerance when multiple operations are performed on a part?

---

A) Tolerance stays the same

B) Tolerance accumulates with each operation

C) Tolerance decreases

D) Tolerance is eliminated

---

Tolerance accumulates with each operation

///

## According to the video, what is the correct way to dimension multiple holes?

---

A) Chain dimensioning from one hole to the next

B) Dimensioning from the edge for each hole

C) Dimensioning each hole from a common origin point

D) Not dimensioning the holes at all

---

Dimensioning each hole from a common origin point

///

## What problem occurs with chain dimensioning according to the video?

---

A) It makes parts cheaper

B) It makes parts more accurate

C) It has no effect on tolerance

D) Each dimension has its own tolerance, and these can stack up so the final hole can be over 0.020 inches off from the intended position

---

Each dimension has its own tolerance, and these can stack up so the final hole can be over 0.020 inches off from the intended position

///

## According to the video, what is the overall tolerance that SendCutSend holds for holes in a DXF file?

---

A) ±0.005 inches

B) ±0.010 inches

C) ±0.002 inches

D) ±0.020 inches

---

±0.005 inches

///

## What can tabs from workholding affect according to the video?

---

A) The cost of the part only

B) The fitment of parts, interfering with bolt fitment or part seating

C) The color of the part

D) The material of the part

---

The fitment of parts, interfering with bolt fitment or part seating

///

## According to the video, what is kerf?

---

A) The tolerance of a part

B) The cost of manufacturing

C) The speed of cutting

D) The width of material removed during cutting

---

The width of material removed during cutting

///

## What is workholding?

---

A) The cutting process

B) The tolerance of a part

C) The material being cut

D) The method or device used to secure a part during manufacturing operations

---

The method or device used to secure a part during manufacturing operations

///

## According to the video, what is assembly tolerance?

---

A) The combined tolerance when multiple parts with individual tolerances are assembled together

B) The tolerance of the cutting machine

C) The tolerance of a single part

D) The tolerance of the material

---

The combined tolerance when multiple parts with individual tolerances are assembled together

///

## What is chain dimensioning?

---

A) Dimensioning all features from a common origin

B) An incorrect dimensioning method where each feature is dimensioned from the previous feature

C) Dimensioning features from the edge

D) Not dimensioning features at all

---

An incorrect dimensioning method where each feature is dimensioned from the previous feature

///

## According to the video, what is common origin dimensioning?

---

A) Chain dimensioning from one feature to the next

B) Dimensioning from multiple edges

C) The correct dimensioning method where all features are dimensioned from a single reference point

D) Not using any reference point

---

The correct dimensioning method where all features are dimensioned from a single reference point

///

## According to the video, what happens to tolerances as parts get more complex with secondary operations?

---

A) Tolerances are eliminated

B) Tolerances become less important

C) Tolerances stay the same regardless of complexity

D) Tolerances need to be accounted for more carefully

---

Tolerances need to be accounted for more carefully

///

## Master Answer Key

1. **A** - Tolerancing is an accounting of the manufacturing process that accounts for multiple key factors like machine movement, temperature, and workholding, not just an exact measurement.

2. **B** - Multiple factors affect tolerancing including machine movement, room temperature, and workholding, not just one single factor.

3. **C** - A ±0.005 inch tolerance represents one to two human hairs of movement, which is a very small but measurable variation.

4. **A** - With ±0.005 tolerance on a 2-inch dimension, the acceptable range is 1.995 to 2.005 inches (2.000 - 0.005 to 2.000 + 0.005).

5. **A** - Tighter tolerances require fancier machines and increase manufacturing cost, as stated in the video.

6. **B** - Tolerance stacking is the accumulation of tolerances from multiple sources such as manufacturing processes, multiple parts, operations, or dimensioning methods.

7. **C** - The kerf creates tolerance between the waist and good part, and the taper effect means different dimensions on top vs. bottom, adding tolerance depending on which side is used.

8. **D** - When two parts each have ±0.005 tolerance and are at opposite extremes, the assembly tolerance is ±0.010 inches (the sum of the individual tolerances).

9. **A** - Assembly tolerance must be accounted for in through hole design to ensure bolts can align when parts are at opposite extremes of their individual tolerances.

10. **B** - Each operation adds tolerance from different mounting processes, setups, and machines, so tolerance accumulates with each additional operation.

11. **C** - The correct method is to dimension all holes from a common origin point, which prevents tolerance stacking.

12. **D** - Chain dimensioning causes each dimension's tolerance to stack, potentially making the final hole over 0.020 inches off from the intended position.

13. **A** - SendCutSend holds holes to an overall tolerance of ±0.005 inches when using DXF files.

14. **B** - Tabs from workholding can interfere with bolt fitment (if inside holes) or part seating (if on outside), affecting fitment.

15. **C** - Kerf is the width of material removed during cutting, which creates the gap between the cut edge and intended part dimension.

16. **D** - Workholding is the method or device used to secure a part during manufacturing operations.

17. **A** - Assembly tolerance is the combined tolerance when multiple parts with individual tolerances are assembled together, typically the sum of individual tolerances.

18. **B** - Chain dimensioning is an incorrect method where each feature is dimensioned from the previous feature, causing tolerance stacking.

19. **C** - Common origin dimensioning is the correct method where all features are dimensioned from a single reference point, preventing tolerance stacking.

20. **D** - As parts get more complex with secondary operations like bending and hardware installation, tolerances need to be accounted for more carefully.

