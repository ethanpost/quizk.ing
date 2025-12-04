## [Sep 30, 2025 Something Strange Happens When You Trace How Connected We Are](https://www.youtube.com/watch?v=CYlon2tvywA)

### Take the quiz [here](https://ethanpost.github.io/quizk.ing) by searching for the title.

## Outline

### Six Degrees of Separation
- Concept that any two people on Earth can be connected through six steps or less
- 1999 German newspaper experiment connecting falafel salesman to Marlon Brando in six steps
- Mathematical calculation: if each person knows 100 people, after 5 steps you reach 10^10 people (more than Earth's population)
- Paradox: despite local clustering, we can connect anyone in just six steps

### Small-World Problem
- Named after the phenomenon of meeting strangers who know your friends
- Veritasium experiment found average viewer was 2.7 degrees of separation from Derek
- Question: How is this possible in a world of 8 billion people?
- Affects disease spread, information travel, and social connections

### Watts and Strogatz Model (1990s)
- Studied networks between ordered (regular) and random
- Started with regular network: people arranged in circle, each connected to nearest neighbors
- Problem: In fully clustered network, connecting opposite sides would take 40 million steps
- Solution: Introduced random shortcuts by rewiring some links
- Key finding: With just 1% of links as shortcuts, average separation dropped from 50 to 10
- Clustering remained high while world became small
- Applied to 8 billion people: only 3 out of every 10,000 friendships need to be shortcuts for 6 degrees of separation

### Network Shortcuts
- Connections that link you to someone outside your normal circle
- Example: Internet Chess Club connection to someone in Holland
- Even a few shortcuts dramatically reduce degrees of separation
- Strength of weak ties: acquaintances (weak ties) often provide job opportunities, not close friends

### Clustering
- Measure of how many of your friends also know each other
- Real networks have high clustering (people know local neighbors)
- Watts-Strogatz model showed clustering can remain high even with shortcuts
- Allows networks to be both clustered and small-world simultaneously

### Testing the Model
- Tested on C. elegans worm neural network (282 neurons)
- Average degree of separation: 2.65 (vs 2.25 if completely random)
- Tested on Hollywood actors: average less than 4 degrees of separation
- Tested on power grids: also small-world networks
- Paper published in Nature 1998, now has 58,000 citations

### Disease Spread Simulation
- Regular network: infection takes 73 days to spread globally
- Small-world network (10% shortcuts): infection takes 26 days
- Random network: infection takes 25 days
- Key insight: Just 10% shortcuts makes spread almost as fast as completely random network
- For 8 billion people, less than 1% of links need to be shortcuts

### Barabasi's Hub Model
- Studied internet in 1998 (800 million webpages)
- Found average of 19 clicks to connect any two sites
- Expected bell curve distribution of links, but found long tail
- Discovered hubs: super-connectors like Yahoo with 100 times more links than average
- Hubs make networks small-world, not shortcuts

### Preferential Attachment
- Two principles of network growth:
  1. Networks grow over time (one node at a time)
  2. New nodes connect preferentially to already well-connected nodes
- Simulation: Start with few nodes, add new nodes that prefer connecting to nodes with more links
- Naturally creates hubs as network grows
- Examples: Chicago O'Hare airport, keystone species in food webs, ATP in metabolic networks, prefrontal cortex in brain

### Hub Examples
- Chicago O'Hare: Most connected US airport with 200+ direct destinations
- Feedback loop: More connections make airport more attractive, leading to more connections
- Keystone species: Atlantic cod connects hundreds of predators and prey
- Metabolic hubs: ATP governs hundreds of chemical reactions
- Neural hubs: Prefrontal cortex links hundreds of brain functions

### Achilles' Heel of Networks
- Hubs create vulnerability: failure of one hub affects entire network
- Example: Chicago O'Hare weather shutdown affected whole country within 24 hours
- Can be good (targeting disease hubs with drugs) or bad (cascading failures)
- Network medicine: developing drugs to target crucial parts of disease networks

### HIV Prevention in Thailand
- 1990s: Fastest-growing HIV epidemic
- Broad campaigns (posters, TV ads) failed
- 1991: Targeted hubs (brothels) requiring condom use
- Result: HIV infections among young men dropped by more than 50%
- Estimated prevention of over 5 million infections by 2013

### Prisoner's Dilemma and Cooperation
- Classic game theory problem: cooperate or defect
- One-time game: defection is rational choice
- Repeated games: cooperation wins (tit-for-tat strategy)
- Axelrod's tournament: nice strategies dominated
- Small clusters of cooperators can overcome defectors

### Network Structure and Cooperation
- Watts-Strogatz simulation: Players on network, play against connections
- Rule: Copy behavior of majority of connections
- Regular network: Cooperation spreads
- With shortcuts: Cooperators crushed, world of defectors
- Critical fraction of shortcuts beyond which cooperation drops to zero
- Same strategies, different connections = completely different outcomes

### Real-World Implications
- Cooperation fostered by clumps/clusters
- Internet/social media: Lack of communities discourages cooperation
- Keyboard warrior phenomenon: People say things online they wouldn't say in person
- Social media's net effect has been negative by many measures

### Watts' Human Experiments
- Tested with real human subjects using public goods game
- Initial finding: Network structure had no effect on cooperation
- Deeper analysis: Clustered networks more likely to copy each other
- Could tip either way (all cooperate or all defect) - "on a knife edge"
- When players could choose connections: More choice led to more cooperation
- Individual actions can start movements that change the world

### Key Insight
- Networks shape us, but our actions shape the networks
- Individual people have power to start movements
- Choose both networks and actions wisely

### Terms
- Six degrees of separation - The concept that any two people on Earth can be connected through a chain of six or fewer acquaintances
- Small-world problem - The phenomenon where networks are both highly clustered locally and have short path lengths globally, named after the experience of meeting strangers who know your friends
- Network shortcut - A connection that links a node to someone outside its normal local cluster, dramatically reducing path lengths in a network
- Clustering - A measure of network structure calculated as the fraction of a node's connections that are also connected to each other, or the fraction of your friends who are also friends with each other
- Hub - A super-connector node in a network that has many more connections than the average node, often 100 times more links
- Preferential attachment - The process by which new nodes joining a network are more likely to connect to nodes that already have many connections, leading to the natural emergence of hubs
- Degree of separation - The number of steps or hops required to connect two nodes in a network through a chain of connections
- Regular network - A network where nodes are arranged in an ordered structure, like a circle where each node connects only to its nearest neighbors
- Random network - A network where connections between nodes are made completely at random, with no preference for local or well-connected nodes
- Small-world network - A network that combines high local clustering (like regular networks) with short path lengths (like random networks)
- Weak tie - An acquaintance or casual connection, as opposed to a strong tie (close friend), often important for job opportunities and information flow
- Strength of weak ties - The sociological phenomenon where acquaintances (weak ties) are often more valuable than close friends for accessing new information and opportunities
- Achilles' heel of networks - The vulnerability created by hubs, where the failure of a single highly connected node can cascade and affect the entire network
- Prisoner's dilemma - A classic game theory problem where two players must choose to cooperate or defect, demonstrating how individual rationality can lead to suboptimal group outcomes
- Tit-for-tat - A game theory strategy that starts by cooperating and then copies the opponent's previous move, performing well in repeated prisoner's dilemma games
- Keystone species - A species in an ecosystem that has a disproportionately large effect on its environment relative to its abundance, functioning as a hub in the food web
- Network medicine - A field of research that develops drugs targeting crucial hub molecules in disease metabolic networks
- Public goods game - An experimental game used to study cooperation where players contribute to a common pool that benefits everyone
- Cascading failure - The phenomenon where the failure of one node (especially a hub) triggers failures in connected nodes, spreading throughout the network

///

## According to the video, how many steps did it take to connect the falafel salesman to Marlon Brando in the 1999 German newspaper experiment?

---

A) Four steps

B) Five steps

C) Six steps

D) Seven steps

---

Six steps

///

## What is the mathematical reason given for why six degrees of separation works, assuming each person knows 100 people randomly?

---

A) 100 to the fourth power equals 100 million people

B) 100 to the fifth power equals 10 billion people, more than Earth's population

C) 100 to the sixth power equals 1 trillion people

D) 100 times 100 equals 10,000 people in two steps

---

100 to the fifth power equals 10 billion people, more than Earth's population

///

## In a fully clustered network where people are arranged in a circle and each knows only their 100 nearest neighbors, how many steps would it take on average to connect any two people?

---

A) 40 million steps

B) Six steps

C) 10,000 steps

D) 80 million steps

---

40 million steps

///

## According to Watts and Strogatz's model, what percentage of links need to be rewired as shortcuts to drop the average degree of separation from 50 to 10?

---

A) 0.1%

B) 1%

C) 10%

D) 50%

---

1%

///

## When applied to 8 billion people on Earth, how many out of every 10,000 friendships need to be shortcuts for the average degree of separation to drop to six?

---

A) One

B) Three

C) Ten

D) One hundred

---

Three

///

## What did Derek's own experiment find about the average Veritasium viewer's degree of separation from him?

---

A) 1.5 degrees

B) 2.7 degrees

C) 4.2 degrees

D) 6.0 degrees

---

2.7 degrees

///

## What is clustering in a network?

---

A) The total number of connections in a network

B) The fraction of your friends who are also friends with each other

C) The average distance between any two nodes

D) The number of hubs in a network

---

The fraction of your friends who are also friends with each other

///

## What organism did Watts and Strogatz test their small-world model on first?

---

A) Fruit flies

B) C. elegans worm

C) Mice

D) Humans

---

C. elegans worm

///

## How many neurons does the C. elegans worm have, and what was the average degree of separation between any two neurons?

---

A) 100 neurons, 1.5 degrees of separation

B) 282 neurons, 2.65 degrees of separation

C) 500 neurons, 3.2 degrees of separation

D) 1000 neurons, 4.1 degrees of separation

---

282 neurons, 2.65 degrees of separation

///

## In the Hollywood actors database, what was the average degree of separation?

---

A) Less than two

B) Less than four

C) Less than six

D) Less than eight

---

Less than four

///

## In the disease spread simulation, how many days did it take for infection to spread globally in a regular network versus a small-world network with 10% shortcuts?

---

A) 50 days vs 20 days

B) 60 days vs 25 days

C) 73 days vs 26 days

D) 80 days vs 30 days

---

73 days vs 26 days

///

## What did Barabasi discover about the distribution of links on the internet that surprised him?

---

A) It followed a perfect bell curve

B) It had a long tail with hubs having 100 times more links than average

C) All websites had exactly the same number of links

D) Most websites had no links at all

---

It had a long tail with hubs having 100 times more links than average

///

## What are the two fundamental principles that Barabasi identified for how networks grow?

---

A) Networks are static and connections are random

B) Networks grow over time and new nodes prefer connecting to well-connected nodes

C) Networks shrink over time and new nodes avoid hubs

D) Networks are fixed in size and connections are evenly distributed

---

Networks grow over time and new nodes prefer connecting to well-connected nodes

///

## What is the process called where new nodes are more likely to connect to nodes that already have many connections?

---

A) Random attachment

B) Preferential attachment

C) Clustered attachment

D) Uniform attachment

---

Preferential attachment

///

## Which airport is mentioned as the most connected airport in the United States with direct flights to over 200 destinations?

---

A) Los Angeles International

B) Chicago O'Hare

C) John F. Kennedy International

D) Hartsfield-Jackson Atlanta

---

Chicago O'Hare

///

## What happened when thunderstorms shut down Chicago O'Hare in August 2025?

---

A) Only local flights were affected

B) 280 flights were canceled and the effects spread to at least six other US airports within 24 hours

C) No other airports were affected

D) Only international flights were canceled

---

280 flights were canceled and the effects spread to at least six other US airports within 24 hours

///

## What is the "Achilles' heel of networks"?

---

A) The tendency for networks to grow too large

B) The vulnerability created by hubs, where failure of one hub can affect the entire network

C) The difficulty of adding new nodes to a network

D) The high cost of maintaining network connections

---

The vulnerability created by hubs, where failure of one hub can affect the entire network

///

## What is the prisoner's dilemma?

---

A) A game where players must choose to cooperate or defect, demonstrating how individual rationality can lead to suboptimal outcomes

B) A game where players always cooperate

C) A game where players always defect

D) A game with no strategic choices

---

A game where players must choose to cooperate or defect, demonstrating how individual rationality can lead to suboptimal outcomes

///

## What was the winning strategy in Axelrod's prisoner's dilemma tournament?

---

A) Always defect

B) Always cooperate

C) Tit-for-tat (cooperate first, then copy opponent's move)

D) Random choice

---

Tit-for-tat (cooperate first, then copy opponent's move)

///

## In Watts and Strogatz's prisoner's dilemma simulation on a network, what happened when they added shortcuts to a regular network?

---

A) Cooperation increased

B) Cooperation remained the same

C) Cooperators were crushed and the world became all defectors

D) The network became unstable

---

Cooperators were crushed and the world became all defectors

///

## According to Strogatz, what fosters cooperation in networks?

---

A) Having many shortcuts

B) Having little clumps or clusters of people

C) Having random connections

D) Having no connections

---

Having little clumps or clusters of people

///

## What did Watts find when he allowed players in his experiment to choose who they played with?

---

A) Cooperation decreased

B) Cooperation remained the same

C) The more choice players had, the more likely they were to cooperate

D) Players always chose to defect

---

The more choice players had, the more likely they were to cooperate

///

## What is a "weak tie" in sociology?

---

A) A close friend

B) An acquaintance or casual connection

C) A family member

D) A business partner

---

An acquaintance or casual connection

///

## According to the "strength of weak ties" phenomenon, how do people typically find jobs?

---

A) Through close friends

B) Through acquaintances (weak ties)

C) Through family members

D) Through random connections

---

Through acquaintances (weak ties)

///

## What is a keystone species?

---

A) A species that is the most abundant in an ecosystem

B) A species that has a disproportionately large effect on its environment relative to its abundance, functioning as a hub

C) A species that is at the top of the food chain

D) A species that is about to go extinct

---

A species that has a disproportionately large effect on its environment relative to its abundance, functioning as a hub

///

## What molecule is mentioned as a hub in metabolic networks that governs hundreds of chemical reactions?

---

A) DNA

B) ATP

C) Glucose

D) Protein

---

ATP

///

## What brain region is mentioned as a neural hub that links hundreds of different functions?

---

A) Hippocampus

B) Prefrontal cortex

C) Cerebellum

D) Amygdala

---

Prefrontal cortex

///

## How many citations does the Watts and Strogatz paper have today?

---

A) About 5,800

B) About 58,000

C) About 580,000

D) About 5.8 million

---

About 58,000

///

## What is network medicine?

---

A) A field that studies how diseases spread through networks

B) A field that develops drugs targeting crucial hub molecules in disease networks

C) A field that maps all disease networks

D) A field that prevents network formation

---

A field that develops drugs targeting crucial hub molecules in disease networks

///

## According to the video, what is the key insight about networks and individual actions?

---

A) Networks shape us, but our actions do not matter

B) Networks shape us, and our actions shape the networks

C) Networks do not affect us at all

D) Only networks matter, not individual actions

---

Networks shape us, and our actions shape the networks

///

## What did Barabasi find was the average number of clicks to connect any two websites on the internet in 1998?

---

A) Six clicks

B) 12 clicks

C) 19 clicks

D) 25 clicks

---

19 clicks

///

## In the disease spread simulation, how many days did it take for infection to spread in a completely random network?

---

A) 20 days

B) 25 days

C) 30 days

D) 35 days

---

25 days

///

## What is the main difference between how Watts-Strogatz model and Barabasi's model explain small-world networks?

---

A) Watts-Strogatz uses shortcuts, Barabasi uses hubs

B) Watts-Strogatz uses hubs, Barabasi uses shortcuts

C) Both use only shortcuts

D) Both use only hubs

---

Watts-Strogatz uses shortcuts, Barabasi uses hubs

///

## According to Strogatz, why has social media had a negative net effect?

---

A) It connects too many people

B) It lacks communities and pockets, discouraging cooperation

C) It has too many hubs

D) It prevents shortcuts from forming

---

It lacks communities and pockets, discouraging cooperation

///

## What did Watts discover about clustered networks in his human experiments?

---

A) They always lead to cooperation

B) They always lead to defection

C) They are "on a knife edge" - could tip either way depending on initial conditions

D) They have no effect on behavior

---

They are "on a knife edge" - could tip either way depending on initial conditions

///

## Master Answer Key

1. **C) Six steps** - The experiment successfully connected the falafel salesman to Marlon Brando through a chain of six acquaintances, demonstrating the six degrees of separation concept.

2. **B) 100 to the fifth power equals 10 billion people, more than Earth's population** - This mathematical calculation shows that with exponential growth through connections, you quickly reach more people than exist on Earth, explaining why six degrees works.

3. **A) 40 million steps** - In a fully clustered network without shortcuts, connecting opposite sides of the circle would require approximately 40 million steps on average, demonstrating why shortcuts are necessary.

4. **B) 1%** - Watts and Strogatz found that rewiring just 1% of links as shortcuts dramatically reduced the average degree of separation from 50 to 10.

5. **B) Three** - When applied to 8 billion people, only 3 out of every 10,000 friendships need to be shortcuts for the average degree of separation to drop to six.

6. **B) 2.7 degrees** - Derek's own experiment found that Veritasium viewers were on average only 2.7 degrees of separation from him, even closer than the six degrees concept.

7. **B) The fraction of your friends who are also friends with each other** - Clustering measures how interconnected your local network is, indicating how many of your connections know each other.

8. **B) C. elegans worm** - This was the first organism with a fully mapped neural network that Watts and Strogatz could test their model on.

9. **B) 282 neurons, 2.65 degrees of separation** - The worm has 282 neurons with an average degree of separation of 2.65, very close to the 2.25 it would be if completely random, proving it's a small-world network.

10. **B) Less than four** - The Hollywood actors database showed that actors are even more connected than the general population, with less than four degrees of separation on average.

11. **C) 73 days vs 26 days** - The simulation dramatically showed how just 10% shortcuts can make disease spread almost three times faster.

12. **B) It had a long tail with hubs having 100 times more links than average** - Barabasi expected a bell curve but found a power-law distribution with a few super-connected hubs.

13. **B) Networks grow over time and new nodes prefer connecting to well-connected nodes** - These two principles explain how hubs naturally emerge in growing networks.

14. **B) Preferential attachment** - This is the name Barabasi gave to the process where new nodes are biased toward connecting to already well-connected nodes.

15. **B) Chicago O'Hare** - This airport became a hub through a feedback loop where more connections made it more attractive, leading to even more connections.

16. **B) 280 flights were canceled and the effects spread to at least six other US airports within 24 hours** - This demonstrates the "Achilles' heel" vulnerability of hub networks.

17. **B) The vulnerability created by hubs, where failure of one hub can affect the entire network** - Hubs create efficiency but also create single points of failure that can cascade through the network.

18. **B) Targeting hubs (brothels) requiring condom use** - Instead of broad campaigns, targeting the network hubs where transmission occurred was far more effective.

19. **B) More than 50%** - The hub-targeting strategy was highly successful, reducing infections by more than half among young men.

20. **A) A game where players must choose to cooperate or defect, demonstrating how individual rationality can lead to suboptimal outcomes** - The prisoner's dilemma shows how rational individual choices can create worse outcomes for everyone.

21. **C) Tit-for-tat (cooperate first, then copy opponent's move)** - This simple strategy won Axelrod's tournament by being nice but retaliatory.

22. **C) Cooperators were crushed and the world became all defectors** - Adding shortcuts to the network destroyed the clusters that allowed cooperation to thrive.

23. **B) Having little clumps or clusters of people** - Cooperation emerges from familiarity and repeated interactions within local clusters.

24. **C) The more choice players had, the more likely they were to cooperate** - When people can choose their connections, they avoid defectors and cooperation increases.

25. **B) An acquaintance or casual connection** - Weak ties are people you know but aren't close friends with, often more valuable for new information.

26. **B) Through acquaintances (weak ties)** - The "strength of weak ties" shows that job opportunities often come from casual connections, not close friends.

27. **B) A species that has a disproportionately large effect on its environment relative to its abundance, functioning as a hub** - Keystone species act as hubs in food webs, connecting many other species.

28. **B) ATP** - This molecule functions as a metabolic hub, participating in hundreds of chemical reactions in cells.

29. **B) Prefrontal cortex** - This brain region acts as a neural hub, linking together many different cognitive functions.

30. **B) About 58,000** - The paper has been extremely influential, cited more than Higgs' paper on the Higgs boson and almost three times Watson and Crick's DNA paper.

31. **B) A field that develops drugs targeting crucial hub molecules in disease networks** - Understanding network structure allows targeting the most important nodes (hubs) for treatment.

32. **B) Networks shape us, and our actions shape the networks** - This is the key takeaway: we are influenced by our networks, but we also have power to shape them through our choices.

33. **C) 19 clicks** - Despite 800 million webpages, the average path between any two sites was just 19 clicks, showing the web is a small world.

34. **B) 25 days** - A completely random network spreads disease in 25 days, almost identical to a small-world network with just 10% shortcuts.

35. **A) Watts-Strogatz uses shortcuts, Barabasi uses hubs** - These are two different mechanisms that both create small-world networks: shortcuts connect distant clusters, while hubs concentrate connections.

36. **B) It lacks communities and pockets, discouraging cooperation** - Without local clusters where people interact repeatedly, cooperation breaks down and negative behavior increases.

37. **C) They are "on a knife edge" - could tip either way depending on initial conditions** - Clustered networks are highly sensitive to initial conditions, where one person's choice can determine whether everyone cooperates or defects.

