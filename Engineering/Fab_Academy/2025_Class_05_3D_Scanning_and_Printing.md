## [3D Scanning and Printing Overview](https://www.youtube.com/watch?v=AHBIeRzd8rI)

> Import this file into [Mochi](https://mochi.cards/) or give it to your favorite AI tool and have it proxy a quiz and check your answers. When importing make sure you select Markdown as the format, "Multiple cards per .md file", and a ```triple backslash``` as the string delimiter. You can use the link to the raw file in GitHub instead of downloading and importing if you prefer.

### 3D Printing Fundamentals
- Distinction between additive (printing) and subtractive manufacturing
- Birth of 3D printing traced to America and France
- Key benefits of 3D printing:
  - Complexity is inexpensive (same time for complex vs. simple shapes)
  - Access to interior spaces during printing
  - Net shape production with minimal waste

### Printing Constraints
- Print failures: extrusion issues, nozzle plugging
- Resolution limitations compared to milling
- Time constraints: prints can take hours to days
- Material limitations
- Proprietary materials can be expensive

### Materials for 3D Printing
- Polymers:
  - PLA (polylactic acid): plant-based, renewable, low volatiles, somewhat brittle
  - PETG: oil-based but recyclable, tougher with good UV resistance
  - Specialty materials: PMMA, ABS, HIPS, TPU, PVA
- Composites: metal-infused, wood-fiber materials
- Material storage: hygroscopic materials require careful storage to prevent moisture absorption

### Design Rules for 3D Printing
- Supports: necessary for overhangs beyond certain angles
- Clearances: minimum gaps needed for parts separation
- Print angles: 30° angle prints without supports
- Overhangs: short overhangs don't need supports
- Bridging: works without supports between built-up areas
- Wall thickness: minimum thickness based on printer capabilities
- Dimensional accuracy: typical difference between design and printed dimensions
- Anisotropic properties: different strengths in different directions
- Surface finish: varies with angle
- Infill density: trade-off between strength and print time
- Corner design: avoiding sharp corners

### Print Parameters
- Bed leveling and distance between head and bed
- Bed adhesion: importance of clean surfaces at proper temperature
- Rafts and brims for improved adhesion
- Temperature control to prevent warping

### Post-Processing
- Smoothing: coatings to improve surface finish
- Electroplating: metalizing 3D printed parts

### Printing Processes and Technologies
- Stereolithography (SLA): high-resolution laser in resin bath
- Fused Deposition Modeling (FDM)/Fused Filament Fabrication (FFF): extruding polymers
- Direct Energy Deposition: metal wire extrusion with laser melting
- Binder Jetting: printing binder in powder bed
- PolyJet: multi-material printing with inkjet technology
- Selective Laser Sintering: laser fusing powder materials
- Two-photon printing: nano-resolution printing
- Bioprinting: extruding biopolymers

### Printer Models and Companies
- RepRap: self-replicating open-source printers
- Ultimaker: minimized moving mass for increased speed
- Prusa: open-source designs with hardened engineering
- Prusa XL: multi-head design for efficient multi-material printing
- Bamboo: sealed, HEPA-filtered printers with automation
- Formlabs: stereolithography printers
- Stratasys: high-end multi-material color printing

### File Formats for 3D Printing
- STL: simple list of triangles, widely supported but lacks units and material data
- PLY: attempt to add color to 3D printing
- AMF/3MF: emerging standards with more capabilities
- OBJ: convenient for color description
- Voxel-based formats: emerging for multi-material prints
- G-code: standard format for printer control

### Software for 3D Printing
- Mesh manipulation: Meshlab for optimization and repair
- Slicing software: Prusa Slicer, Cura
- Printer control: Print Run, OctoPrint for print farms
- Firmware: Klipper for printer operation

### Safety Considerations
- Ultrafine particle emissions: significant with ABS and other materials
- Volatile organic compound emissions: vary by material
- PLA and PETG safe for open printing
- Other materials require ventilation or HEPA filters
- Food safety concerns: material safety and difficulty cleaning printed items

### 3D Scanning Techniques
- X-ray tomography: high-resolution scanning down to micron level
- Probe scanning: atom resolution but slow and 2D
- Confocal microscopy: 3D scanning at micron resolution
- Serial sectioning: destructive scanning by slicing object
- Milk scanning: using opaque liquid to capture dimensions
- Digitizer arms: selective manual measurement
- Photogrammetry: reconstructing 3D models from multiple photos
- Speckle scanning: using random dot patterns to map surfaces
- Laser scanning: measuring position of laser reflections
- Structured light: projecting patterns and measuring distortion
- Stereo vision: using multiple cameras for 3D reconstruction
- LIDAR: measuring time for light to reflect back
- Light stage scanning: capturing complete light field data
- SLAM: Simultaneous Localization And Mapping for AR applications

### Service Bureaus and Production
- Prusa print farm: mass production with hundreds of printers
- Shapeways and other service bureaus for outsourcing prints
- PCB houses offering 3D printing services

### Terms
- Additive Manufacturing - Manufacturing process that builds objects by adding material layer by layer
- Subtractive Manufacturing - Manufacturing process that removes material to create objects
- PLA (Polylactic Acid) - Plant-based biodegradable polymer commonly used in 3D printing
- PETG - Oil-based recyclable polymer with good UV resistance and toughness
- STL (STereoLithography) - Common file format for 3D printing containing triangular mesh data
- FDM (Fused Deposition Modeling) - 3D printing technique that extrudes molten material layer by layer
- FFF (Fused Filament Fabrication) - Non-proprietary term for extrusion-based 3D printing
- Stereolithography (SLA) - 3D printing technique using laser to cure liquid resin
- Infill - Internal structure pattern and density of a 3D printed object
- Slicer - Software that converts 3D models into printer instructions (G-code)
- G-code - Machine instruction language used by 3D printers
- Bridging - Printing between two supports without additional supports underneath
- Overhang - Part of a 3D model that extends beyond the layer below at a significant angle
- Raft - Horizontal lattice structure printed beneath the object for improved bed adhesion
- Brim - Extended perimeter around the base of a print for improved bed adhesion
- Anisotropic - Having physical properties that vary in different directions
- HEPA Filter - High-Efficiency Particulate Air filter for trapping ultrafine particles
- Photogrammetry - Technique for creating 3D models from multiple photographs
- LIDAR - Light Detection And Ranging, measuring distance with laser light
- SLAM - Simultaneous Localization And Mapping, technique for 3D scanning while tracking position

///

What is the key distinction between 3D printing and traditional manufacturing?

---

A) 3D printing adds material rather than removing it

B) 3D printing is faster than traditional manufacturing

C) 3D printing requires less skill than traditional manufacturing

D) 3D printing uses only synthetic materials

---

3D printing adds material rather than removing it

///

Which of these is NOT a primary benefit of 3D printing?

---

A) Complexity is inexpensive

B) Superior material strength in all directions

C) Access to interior spaces during printing

D) Net shape production with minimal waste

---

Superior material strength in all directions

///

What is the minimum angle at which overhangs can typically be printed without supports?

---

A) 60°

B) 30°

C) 15°

D) 45°

---

30°

///

Which material is plant-based, renewable, and produces low volatile emissions?

---

A) TPU

B) ABS

C) PLA

D) PETG

---

PLA

///

What is "bridging" in 3D printing?

---

A) Creating a support structure under overhangs

B) Connecting two separate prints with adhesive

C) Printing between two built-up areas without supports underneath

D) Joining two different materials in one print

---

Printing between two built-up areas without supports underneath

///

Which safety concern is associated with 3D printing certain materials?

---

A) Magnetic field disruption

B) Electrical hazards

C) Ultrafine particle emissions

D) Radiation emissions

---

Ultrafine particle emissions

///

Which materials are generally considered safe for open printing without special ventilation?

---

A) Metal-infused filaments and wood composites

B) TPU and PVA

C) PLA and PETG

D) ABS and nylon

---

PLA and PETG

///

What is a common issue with 3D printing food-safe items?

---

A) The materials cannot withstand food temperatures

B) Fine seams can trap food and be difficult to clean

C) The colors leach into food

D) The print process creates toxic byproducts

---

Fine seams can trap food and be difficult to clean

///

What is the most common file format for 3D printing?

---

A) DXF

B) OBJ

C) STL

D) AMF

---

STL

///

What limitation does the STL file format have?

---

A) It can only handle small file sizes

B) It requires proprietary software to open

C) It doesn't specify units (millimeters or inches)

D) It only works with certain printers

---

It doesn't specify units (millimeters or inches)

///

What is "slicer" software used for in 3D printing?

---

A) Cutting 3D models into smaller printable pieces

B) Converting 3D models into printer instructions (G-code)

C) Scanning physical objects into digital models

D) Removing digital supports from finished models

---

Converting 3D models into printer instructions (G-code)

///

What is the purpose of a "raft" in 3D printing?

---

A) To smooth the bottom surface of the print

B) To protect the printer bed from damage

C) To provide a horizontal lattice structure beneath the object for better bed adhesion

D) To create a waterproof barrier on the bottom of prints

---

To provide a horizontal lattice structure beneath the object for better bed adhesion

///

Which printing technology uses a laser to cure liquid resin?

---

A) Fused Deposition Modeling (FDM)

B) Selective Laser Sintering (SLS)

C) Stereolithography (SLA)

D) PolyJet

---

Stereolithography (SLA)

///

What does "anisotropic" mean in the context of 3D printed parts?

---

A) The parts conduct electricity

B) The parts have different physical properties in different directions

C) The parts are water-resistant

D) The parts shrink over time

---

The parts have different physical properties in different directions

///

What 3D scanning technique reconstructs 3D models from multiple photographs?

---

A) LIDAR

B) Structured light

C) Confocal microscopy

D) Photogrammetry

---

Photogrammetry

///

What is a "HEPA filter" used for in 3D printing?

---

A) Removing moisture from filament

B) Cooling the printed parts

C) Trapping ultrafine particles from printer emissions

D) Sterilizing the printer bed

---

Trapping ultrafine particles from printer emissions

///

Which of the following is NOT a 3D scanning technique mentioned in the transcript?

---

A) Light stage scanning

B) Quantum resonance imaging

C) Milk scanning

D) X-ray tomography

---

Quantum resonance imaging

///

What is SLAM in the context of 3D scanning?

---

A) Structured Light And Measurement

B) Simultaneous Localization And Mapping

C) Scanners Learning Automated Movement

D) Sensors Leveraging Augmented Modeling

---

Simultaneous Localization And Mapping

///

What is the RepRap project's primary goal beyond 3D printing?

---

A) Creating the fastest possible 3D printer

B) Developing biodegradable printing materials

C) Making 3D printers that can self-replicate

D) Producing the lowest cost 3D printer

---

Making 3D printers that can self-replicate
