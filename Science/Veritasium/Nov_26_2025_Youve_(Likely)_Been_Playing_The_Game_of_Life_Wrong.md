## [Nov 26, 2025 You've (Likely) Been Playing The Game of Life Wrong](https://www.youtube.com/watch?v=HBluLfX2F_k)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Normal Distributions vs Power Laws

### Normal Distributions
- Most data clusters around an average value
- Examples: human height, IQ, apple sizes
- Clearly defined average with extreme outliers being rare
- Physically impossible to find values many times the average
- Standard deviation can be measured
- 95% of data falls within two standard deviations from the mean
- Created by Abraham de Moivre in the early 1700s
- Bell-shaped curve when plotted
- Occurs when random effects add up (additive processes)

### Power Laws
- Distribution that spans several orders of magnitude
- No inherent physical scale in the system
- Extreme events are much more likely than in normal distributions
- Can have values 5, 10, or even 100 times the average
- Standard deviation is infinite (no measurable width)
- Average doesn't converge - keeps increasing with more measurements
- Outliers can dominate the average
- Described by equation: number proportional to 1/x^α (where α is the power)
- Reveals fractal-like, self-similar structure
- Indicates system has no intrinsic scale (scale-free)
- Signature of systems in critical state

### Pareto's Discovery
- Italian engineer Vilfredo Pareto discovered power laws in late 1800s
- Studied income distributions across multiple European countries
- Found same pattern in Italy, England, France, Prussia
- Pattern still holds in most countries today
- Used log-log plots to transform curves into straight lines
- Gradient around negative 1.5 for income distributions
- Each doubling of income reduces number of people by factor of 2^1.5 (≈2.8)

## Three Casino Games

### Game 1: Additive Coin Tosses
- 100 coin tosses, win $1 for each heads
- Expected payout: $50 (probability 1/2 × $1 × 100 tosses)
- Follows normal distribution
- Small variations cancel out over many games
- Should pay less than expected value to play

### Game 2: Multiplicative Coin Tosses
- 100 coin tosses with multiplicative factors
- Heads: multiply winnings by 1.1
- Tails: multiply winnings by 0.9
- Expected factor per turn: (1.1 + 0.9)/2 = 1
- Expected payout: $1
- Median payout: around 61 cents
- Maximum possible: $1.1^100 ≈ $14,000 (extremely unlikely)
- Follows log normal distribution
- When plotted on logarithmic scale, becomes normal distribution
- Produces big inequalities with long tail
- Asymmetric: downside capped at zero, upside unlimited
- Occurs when random effects multiply (multiplicative processes)

### Game 3: St. Petersburg Paradox
- Coin toss game: start with $1, double payout each toss until heads appears
- Payout: $2^n where n is number of tosses until first heads
- Probability of n tosses: (1/2)^n
- Expected value of each outcome: $1
- Total expected value: infinite (St. Petersburg paradox)
- Distribution spans all orders of magnitude
- Follows power law: probability of payout x = 1/x = x^(-1)
- When both axes on log scale, shows straight line with gradient of -1
- Standard deviation is infinite
- Average doesn't converge with more samples

## Power Law Properties

### Mathematical Characteristics
- Formed when two exponentials combine
- Payout grows exponentially: x = 2^n
- Probability shrinks exponentially: (1/2)^n
- Combining exponentials creates power law relationship
- No measurable width or standard deviation
- Heavy tail: significant probability of extreme outliers

### Real-World Examples
- Earthquakes: frequency decreases exponentially with magnitude, energy increases exponentially
- Forest fires: size distribution follows power law
- Internet links: distribution of webpage connections
- City populations
- Stock price fluctuations
- Scientific paper citations
- War casualties
- Mass extinctions
- DNA sequencing patterns
- Species distribution in ecosystems

## Fractals and Power Laws

### Relationship
- Power laws reveal fractal-like structure
- Self-similar patterns at all scales
- Tree diagram of St. Petersburg paradox shows repeating structure
- Examples: leaf veins, river networks, blood vessels in lungs, lightning
- When zoomed in, same structure repeats at smaller scales
- No inherent scale to the system

## Critical States and Phase Transitions

### Magnets and Critical Temperature
- Each atom has magnetic moment (like tiny compass)
- At low temperatures: large domains where moments align
- Creates overall magnetic field
- At high temperatures: moments flip randomly, cancel out, lose magnetism
- Critical point: transition between magnetic and non-magnetic
- Occurs at specific temperature called Curie temperature
- At critical point: pattern becomes fractal-like
- Domains of all sizes (tens to millions of atoms)
- System becomes scale-free
- Domain size distribution follows power law
- Local influences chain together
- Effective range of influence becomes infinite at critical point
- Single flip can cascade throughout entire material
- System maximally unstable and unpredictable

### Self-Organized Criticality
- Some systems naturally drive themselves to critical state
- Forest fires: naturally tune to criticality through feedback
- Feedback mechanism: fires remove trees, then trees regrow
- If forest too dense, massive fire burns it back
- If too sparse, trees grow back to critical state
- Unlike magnets which must be manually tuned
- Sandpile model: dropping grains creates avalanches
- Avalanche sizes follow power law
- System self-organizes to critical state
- Earth's crust behaves similarly with earthquakes

## Forest Fires

### Yellowstone 1988 Fire
- Started from single lightning strike
- Grew to 1.4 million acres (size of Delaware)
- 70 times bigger than previous record (18,000 acres in 1931)
- 50 times area of all fires over previous 15 years combined
- Nothing special about the initial spark
- Same cause as small fires: single lightning strike
- Only difference: where it struck and forest makeup at that time

### Fire Suppression Policy
- 10:00 AM policy (1935): suppress all fires by 10 AM next day
- Strategy seemed logical but was extremely risky
- Suppressing small fires allows fuel buildup
- Leads to inevitable megafires
- Modern approach: let small fires burn, only intervene when necessary
- Controlled burns used to reduce buildup
- May take years to return forest to natural state after suppression

### Fire Distribution
- Most fires: 10 or fewer trees
- Less frequently: under 100 trees
- Rarely: massive fires affecting entire system
- All fires have same cause: single lightning strike
- Large fires are magnified versions of small ones
- Distribution follows power law
- At critical state, no special events cause massive fires

## Earthquakes

### Kobe Earthquake 1995
- January 17, 1995 in Kobe, Japan
- No major quake for centuries before
- Stress released near Nojima fault line
- Cascaded along 40 kilometers of crust
- Ground shifted up to 2 meters
- Energy equivalent of numerous atomic bombs
- Killed over 6,000 people
- Forced 300,000 from homes
- Destroyed thousands of homes and infrastructure

### Earthquake Mechanism
- Earth's crust constantly moving and rearranging
- Stresses build up slowly as tectonic plates rub
- Most movements: tiny earthquakes you can't feel
- Random movements can trigger powerful chain reactions
- How far earthquake propagates depends on chance and stress field organization
- Same physical process for all earthquakes
- Naturally produces events over enormous range of scales
- Distribution follows power law
- Cannot use past to predict future (unpredictable)

## Sandpile Model

### Per Bak's Model (1987)
- Simple thought experiment: drop grains of sand on grid
- Grains tumble when pile gets too steep
- Studied size of avalanches (reorganizations)
- Most simple version: drop grains at center
- When reaches 4 or more grains, topples
- Creates "fingers of instability"
- Avalanches can be tiny or cascade through entire system
- Distribution follows power law
- Closely resembles earthquake energy distribution
- Similar behavior to forest fires
- System tunes itself to critical state
- Real sandpiles don't behave this way (theory applies to other systems)

## Universality

### Concept
- At critical point, physical details don't matter
- Universal behavior regardless of system type
- Can model complex systems with simple toy models
- Understanding one system reveals behavior of entire class
- Examples: magnets, fluids (water, carbon dioxide), forest fires, sandpiles, earthquakes
- Some systems need tuning (magnets, fluids)
- Others self-organize (forests, sandpiles, earthquakes)
- Systems in same universality class behave identically

### Applications
- Disease spread (like forest fires but with people)
- Stock market crashes follow same power law as world wars
- DNA sequencing
- Ecosystem species distribution
- Mass extinctions
- Human systems: city populations, stock prices, paper citations, war deaths

## Practical Implications

### Insurance
- Designed to protect against large rare events
- Insurance companies face difficult job: must charge enough to cover extreme events
- Example: 2018 Paradise, California fire
- Merced Property & Casualty didn't plan for such huge event
- Company went bust when claims came in

### Industries Built on Power Laws
- Venture capital: most investments lose money, few outliers generate most returns
- Horsley Bridge: top 6% of investments generated 60% of profit
- Y Combinator: 75% of returns from just 2 out of 280 startups
- Book publishing: most titles flop, rare hits (like Harry Potter) transform companies
- Streaming: top 6% of Netflix shows account for over half of viewing hours
- YouTube: less than 4% of videos reach 10,000 views, but account for 93% of all views
- Principle: majority of wealth goes to richest few (Pareto principle)

### Industries Not Suited for Power Laws
- Restaurants: need consistent customers, can't rely on one busy night
- Airlines: need to fill seats on each flight, can't squeeze all passengers on one plane
- These follow normal distributions where average matters

### Strategic Implications
- Normal distribution world: consistency and average performance important
- Power law world: persistence more important than consistency
- Take riskier bets hoping one pays off huge
- Most bets will fail, but one success pays for all
- Cannot know beforehand which bet will succeed (maximally unpredictable)
- Next bet could do nothing, a little, or change entire life
- Early work benefits from snowball effect (preferential attachment)
- Need to understand which game you're playing

### Preferential Attachment
- Albert-László Barabási studied internet in early 2000s
- Found power law distribution of webpage links
- Prediction: new sites more likely to link to well-known pages
- Simulation: new nodes connect to those with most links
- Power law emerged with power around -2
- Matched real internet data
- Runaway effect: successful become more successful
- "Rich get richer" phenomenon

## Terms

- Normal Distribution - A bell-shaped probability distribution where most data clusters around an average value, with extreme outliers being rare. Occurs when random effects add up (additive processes).

- Power Law - A mathematical relationship where one quantity is proportional to a power of another. In distributions, it means the probability of an event is proportional to 1/x^α, creating a heavy tail with no inherent scale.

- Pareto Distribution - A specific type of power law distribution discovered by Vilfredo Pareto in income data, where a small fraction of the population holds most of the wealth.

- Log Normal Distribution - A probability distribution that appears normal when plotted on a logarithmic scale. Occurs when random effects multiply (multiplicative processes), creating asymmetric distributions with long tails.

- St. Petersburg Paradox - A gambling paradox where a game with infinite expected value seems to have only finite worth to players. The game involves doubling payouts until a coin lands on heads.

- Expected Value - The average outcome of a random process calculated by summing all possible outcomes multiplied by their probabilities.

- Standard Deviation - A measure of the spread or width of a distribution. In normal distributions it's finite, but in power laws it's infinite.

- Critical Point - The specific condition (like temperature) where a system undergoes a phase transition, exhibiting scale-free, fractal-like behavior and power law distributions.

- Curie Temperature - The specific temperature at which a magnetic material loses its magnetism, marking the critical point of the magnetic phase transition.

- Self-Organized Criticality - The phenomenon where certain systems naturally drive themselves to a critical state without external tuning, such as forest fires or sandpiles.

- Fractal - A geometric pattern that repeats at different scales, showing self-similarity. Power laws are intrinsically linked to fractal structures.

- Scale-Free - A property of systems that have no inherent characteristic size or scale, often indicated by power law distributions.

- Universality - The principle that at critical points, different physical systems exhibit identical behavior regardless of their specific details, allowing simple models to describe complex systems.

- Preferential Attachment - A process where new elements in a network are more likely to connect to nodes that already have many connections, leading to power law distributions (the "rich get richer" effect).

- Heavy Tail - A distribution property where extreme events have significant probability, unlike normal distributions where outliers are extremely rare.

- Log-Log Plot - A graph where both axes use logarithmic scales, used to identify power law relationships which appear as straight lines.

- Phase Transition - A transformation between different states of matter or system organization, such as magnetic to non-magnetic, often occurring at critical points.

- Domain - A region in a material (like a magnet) where properties are uniform, such as aligned magnetic moments.

- Avalanche - In the sandpile model, a cascade of toppling grains that can range from tiny to system-wide, following a power law distribution.

- Outlier - An extreme value that deviates significantly from the average. In power laws, outliers are common and can dominate averages.

///

## According to the video, what type of distribution do human height, IQ, and apple sizes follow?

---

A) Normal distribution

B) Power law

C) Log normal distribution

D) Pareto distribution

---

Normal distribution

///

## True or False: In a normal distribution, you can find values that are 100 times the average.

---

A) True

B) False

---

False

///

## What did Vilfredo Pareto discover about income distributions in the late 1800s?

---

A) Income is evenly distributed across populations

B) Income distributions vary randomly by country

C) Income follows a power law distribution

D) Income follows a normal distribution

---

Income follows a power law distribution

///

## When Pareto plotted income data on a log-log plot, what did the curve transform into?

---

A) A straight line

B) A bell curve

C) A U-shaped curve

D) An exponential curve

---

A straight line

///

## What was the approximate gradient of Pareto's income distribution graph?

---

A) Negative 0.5

B) Negative 1.0

C) Negative 1.5

D) Negative 2.0

---

Negative 1.5

///

## In the first casino game (additive coin tosses), what is the expected payout for 100 tosses?

---

A) $25

B) $75

C) $100

D) $50

---

$50

///

## What type of distribution does the second casino game (multiplicative coin tosses) produce?

---

A) Normal distribution

B) Power law

C) Log normal distribution

D) Uniform distribution

---

Log normal distribution

///

## What is the median payout in the multiplicative coin toss game?

---

A) 50 cents

B) 75 cents

C) $1.00

D) 61 cents

---

61 cents

///

## The St. Petersburg paradox game has what expected value?

---

A) $1

B) $10

C) $100

D) Infinite

---

Infinite

///

## In the St. Petersburg paradox, if you get heads on the nth toss, what is your payout?

---

A) n dollars

B) 2n dollars

C) 2^n dollars

D) n^2 dollars

---

2^n dollars

///

## What power law does the St. Petersburg paradox follow?

---

A) Probability proportional to 1/x

B) Probability proportional to 1/x^2

C) Probability proportional to x

D) Probability proportional to x^2

---

Probability proportional to 1/x

///

## True or False: Power laws have a measurable standard deviation.

---

A) True

B) False

---

False

///

## According to the video, what happens to the average when you take more samples from a power law distribution?

---

A) It keeps increasing

B) It converges to a fixed value

C) It decreases

D) It oscillates randomly

---

It keeps increasing

///

## Why can a single outlier dominate the average in power law distributions?

---

A) The mean is always zero

B) Outliers are very common

C) There are no outliers in power laws

D) The heavy tail gives significant probability to extreme events

---

The heavy tail gives significant probability to extreme events

///

## What creates a power law when two exponentials combine?

---

A) One exponential growing and one shrinking

B) Two exponentials both growing

C) Two exponentials both shrinking

D) Any combination of exponentials

---

One exponential growing and one shrinking

///

## In earthquakes, what two exponential relationships combine to create a power law?

---

A) Frequency and magnitude both increase exponentially

B) Frequency and energy both decrease exponentially

C) Magnitude and energy both increase exponentially

D) Frequency decreases exponentially with magnitude, energy increases exponentially with magnitude

---

Frequency decreases exponentially with magnitude, energy increases exponentially with magnitude

///

## True or False: Power laws reveal fractal-like, self-similar structures.

---

A) True

B) False

---

True

///

## What is the name of the temperature at which a magnet loses its magnetism?

---

A) Curie temperature

B) Absolute zero

C) Critical temperature

D) Phase transition temperature

---

Curie temperature

///

## At the critical point of a magnet, what happens to the effective range of influence?

---

A) It becomes zero

B) It becomes finite

C) It becomes infinite

D) It oscillates

---

It becomes infinite

///

## What phenomenon describes systems that naturally drive themselves to a critical state?

---

A) Self-organized criticality

B) Phase transition

C) Universality

D) Preferential attachment

---

Self-organized criticality

///

## The 1988 Yellowstone fire burned how many acres?

---

A) 1.4 million acres

B) 140,000 acres

C) 14 million acres

D) 140 million acres

---

1.4 million acres

///

## True or False: The 1988 Yellowstone fire was caused by a special, unusual event.

---

A) True

B) False

---

False

///

## What was the name of the fire suppression policy established in 1935?

---

A) The 9:00 AM policy

B) The same-day policy

C) The zero-tolerance policy

D) The 10:00 AM policy

---

The 10:00 AM policy

///

## Why was the 10:00 AM fire suppression policy risky?

---

A) It was too expensive

B) It didn't work fast enough

C) It required too many resources

D) It allowed fuel buildup leading to megafires

---

It allowed fuel buildup leading to megafires

///

## The Kobe earthquake of 1995 cascaded along how many kilometers of crust?

---

A) 4 kilometers

B) 400 kilometers

C) 4,000 kilometers

D) 40 kilometers

---

40 kilometers

///

## True or False: Earthquakes are predictable based on past events.

---

A) True

B) False

---

False

///

## Who created the sandpile model to study power laws?

---

A) Per Bak

B) Vilfredo Pareto

C) Albert-László Barabási

D) Abraham de Moivre

---

Per Bak

///

## In the sandpile model, what happens when a stack reaches 4 or more grains?

---

A) It topples

B) It stops growing

C) It becomes magnetic

D) It changes color

---

It topples

///

## True or False: Real sandpiles behave exactly like Per Bak's sandpile model.

---

A) True

B) False

---

False

///

## What is the principle that at critical points, different systems exhibit identical behavior regardless of their specific details?

---

A) Self-organized criticality

B) Preferential attachment

C) Scale-free property

D) Universality

---

Universality

///

## According to the video, what percentage of Y Combinator's returns came from just 2 out of 280 startups?

---

A) 50%

B) 65%

C) 75%

D) 85%

---

75%

///

## On YouTube, what percentage of videos account for over 93% of all views?

---

A) Less than 1%

B) Less than 2%

C) Less than 4%

D) Less than 10%

---

Less than 4%

///

## True or False: Restaurants and airlines operate in power law environments.

---

A) True

B) False

---

False

///

## In a power law world, what is more important than consistency?

---

A) Persistence

B) Speed

C) Perfection

D) Efficiency

---

Persistence

///

## What process did Barabási discover that creates power laws in networks like the internet?

---

A) Random attachment

B) Uniform distribution

C) Normal distribution

D) Preferential attachment

---

Preferential attachment

///

## In Barabási's internet simulation, what was the power of the resulting power law?

---

A) Negative 1

B) Negative 1.5

C) Negative 2

D) Negative 2.5

---

Negative 2

///

## According to the video, what follows the same power law as stock market crashes?

---

A) Forest fires

B) Earthquakes

C) World wars

D) City populations

---

World wars

///

## True or False: In power law systems, you can know beforehand which bet will succeed.

---

A) True

B) False

---

False

///

## What is a log-log plot?

---

A) A graph with one logarithmic axis

B) A graph showing only logarithms

C) A graph with exponential scales

D) A graph with both axes on logarithmic scales

---

A graph with both axes on logarithmic scales

///

## What term describes a system that has no inherent characteristic size or scale?

---

A) Normal

B) Uniform

C) Standard

D) Scale-free

---

Scale-free

///

## What are regions in a magnet where magnetic moments are aligned called?

---

A) Zones

B) Sections

C) Areas

D) Domains

---

Domains

///

## In the sandpile model, what are the cascades of toppling grains called?

---

A) Landslides

B) Collapses

C) Cascades

D) Avalanches

---

Avalanches

///

## What property of distributions means extreme events have significant probability?

---

A) Light tail

B) Normal tail

C) Short tail

D) Heavy tail

---

Heavy tail

///

## What is the transformation between different states of matter or system organization called?

---

A) Critical transition

B) State change

C) System shift

D) Phase transition

---

Phase transition

///

## Answer Key

**1. A) Normal distribution** - Human height, IQ, and apple sizes cluster around an average value with rare extreme outliers, which is characteristic of normal distributions.

**2. B) False** - In normal distributions, extreme outliers are extremely rare and physically impossible. You would never find someone 100 times the average height.

**3. C) Income follows a power law distribution** - Pareto discovered that income distributions span many orders of magnitude and follow a power law, not a normal distribution.

**4. A) A straight line** - When Pareto plotted income data on a log-log plot, the broad curve transformed into a straight line, revealing the power law relationship.

**5. C) Negative 1.5** - The gradient of Pareto's income distribution graph was around negative 1.5, meaning each doubling of income reduces the number of people by a factor of about 2.8.

**6. D) $50** - The expected payout is calculated as probability (1/2) × payout ($1) × number of tosses (100) = $50.

**7. C) Log normal distribution** - Multiplicative processes create log normal distributions, which appear normal when plotted on a logarithmic scale.

**8. D) 61 cents** - The median payout in the multiplicative game is around 61 cents, meaning if you play once, you have even odds of getting more or less than this amount.

**9. D) Infinite** - The St. Petersburg paradox has infinite expected value because you keep adding $1 for each possible outcome, and there are infinitely many possible outcomes.

**10. C) 2^n dollars** - If it takes n tosses to get the first heads, the payout is 2^n dollars, doubling with each additional toss needed.

**11. A) Probability proportional to 1/x** - The St. Petersburg paradox follows the power law where probability of payout x equals 1/x or x to the power of negative one.

**12. B) False** - Power laws have infinite standard deviation, meaning there is no measurable width to the distribution.

**13. A) It keeps increasing** - With power laws, the more you measure, the bigger the average becomes because extreme outliers keep skewing it upward.

**14. D) The heavy tail gives significant probability to extreme events** - Power laws have heavy tails where extreme events have significant probability, allowing single outliers to dominate averages.

**15. A) One exponential growing and one shrinking** - Power laws form when one exponential (like payout growing) combines with another exponential shrinking (like probability decreasing).

**16. D) Frequency decreases exponentially with magnitude, energy increases exponentially with magnitude** - These two exponential relationships combine to create the power law distribution of earthquake energy.

**17. A) True** - Power laws reveal fractal-like structures that are self-similar at different scales, as seen in the tree diagram of the St. Petersburg paradox.

**18. A) Curie temperature** - This is the specific temperature named after Pierre Curie where a magnetic material loses its magnetism at the critical point.

**19. C) It becomes infinite** - At the critical point, local influences chain together so that the effective range of influence becomes infinite, allowing a single flip to cascade throughout the material.

**20. A) Self-organized criticality** - This describes systems like forest fires and sandpiles that naturally drive themselves to a critical state without external tuning.

**21. A) 1.4 million acres** - The 1988 Yellowstone fire burned 1.4 million acres, which is about the size of Delaware and 70 times larger than the previous record.

**22. B) False** - The fire had the same cause as any small fire: a single lightning strike. There was nothing special about the initial event.

**23. D) The 10:00 AM policy** - Established in 1935, this policy required suppressing every fire by 10:00 AM on the day following its report.

**24. D) It allowed fuel buildup leading to megafires** - By suppressing all fires, the policy allowed trees and fuel to accumulate, making massive fires inevitable when they finally occurred.

**25. D) 40 kilometers** - The Kobe earthquake cascaded along 40 kilometers of crust, shifting the ground up to 2 meters and releasing enormous energy.

**26. B) False** - Earthquakes are famously unpredictable. You cannot use past events to predict future earthquakes in critical systems.

**27. A) Per Bak** - Danish physicist Per Bak created the sandpile model in 1987 to study how simple systems can produce power law distributions.

**28. A) It topples** - When a stack reaches 4 or more grains in the sandpile model, it becomes unstable and topples, redistributing grains to neighboring squares.

**29. B) False** - Real sandpiles don't behave like the model. Per Bak acknowledged this, saying the theory applies to the systems it applies to, not literally to sandpiles.

**30. D) Universality** - This principle states that at critical points, different physical systems exhibit identical behavior regardless of their specific details.

**31. C) 75%** - Y Combinator calculated that 75% of their returns came from just 2 out of 280 startups, demonstrating the power law nature of venture capital.

**32. C) Less than 4%** - On YouTube, less than 4% of videos reach 10,000 views, but those videos account for over 93% of all views on the platform.

**33. B) False** - Restaurants and airlines operate in normal distribution worlds where consistency and average performance matter, not power law environments.

**34. A) Persistence** - In power law worlds, persistence (taking many bets) is more important than consistency because you need that one outlier success.

**35. D) Preferential attachment** - Barabási discovered that new webpages are more likely to link to already well-connected pages, creating a "rich get richer" effect.

**36. C) Negative 2** - Barabási's simulation produced a power law with power around negative 2, which almost exactly matched real internet data.

**37. C) World wars** - The distribution of world war sizes (measured by casualties) follows virtually the same power law as stock market crashes.

**38. B) False** - Power law systems are maximally unpredictable. You cannot know beforehand which bet will succeed - it could do nothing, a little, or change your entire life.

**39. D) A graph with both axes on logarithmic scales** - Log-log plots use logarithmic scales on both axes and are used to identify power law relationships, which appear as straight lines.

**40. D) Scale-free** - A scale-free system has no inherent characteristic size or scale, which is indicated by power law distributions and fractal structures.

**41. D) Domains** - In magnets, domains are regions where magnetic moments are aligned in the same direction, creating the overall magnetic field.

**42. D) Avalanches** - In the sandpile model, avalanches are the cascades of toppling grains that can range from tiny to system-wide events.

**43. D) Heavy tail** - A heavy tail means extreme events have significant probability, unlike normal distributions where outliers are extremely rare.

**44. D) Phase transition** - This is the transformation between different states, such as magnetic to non-magnetic, often occurring at critical points where power laws emerge.

