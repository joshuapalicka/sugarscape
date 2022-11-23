<h1 align="center">sugarscape</h1>
==========

Python implementation of Epstein and Axtell's large scale agent-based computational model, the Sugarscape, to explore the role of social phenomenon such as seasonal migrations, pollution, sexual reproduction, combat, and transmission of disease and even culture.  
In other words: Cellular Automata + Agents = Sugarscape.

Code based on previous work by Hervé Lange: https://github.com/langerv/sugarscape

### Results

###### Evolution from random distribution under rules ({environment}, {agents}) = ({G1}, {M}):
![](results/sgEvolution0.png) ![](results/sgEvolution500.png)

###### Emergent diagonal waves of migration under rules ({G1}, {M}):
![](results/sgMigration0.png) ![](results/sgMigration6.png) ![](results/sgMigration20.png)

###### Seasonal migration and Hibernation resulting from rules ({S[1,8,50]}, {M}) and random distribution of agents:
![](results/sgSeasonal0.png) ![](results/sgSeasonal49.png) ![](results/sgSeasonal99.png)

###### Societal evolution through crossover of Genetic Attributes in Sexual Reproduction under rules ({G1}, {M, S}) coloring by agent vision:
![](results/sgSocietal0.png) ![](results/sgSocietal50.png) ![](results/sgSocietal500.png)

###### Cultural transmission by tag-flipping under rules ({G1}, {M, K}) coloring by tribes:
![](results/sgCultural0.png) ![](results/sgCultural132.png) ![](results/sgCultural694.png)

###### Combat between two tribbes under rules ({G1}, {Cinf}), with various outcomes: a) coexistence between Blue and Red b) Red dominance c) Blue dominance:
![](results/sgCombatCinfInitial.png) ![](results/sgCombatCinf10.png) ![](results/sgCombatCinf20.png)  
![](results/sgCombatCinfCoexistence.png) ![](results/sgCombatCinfRedDominance.png) ![](results/sgCombatCinfBlueDominance.png)

###### Trench war and front line between two tribes fighting under rules ({G1}, {C2, R[60, 100]}) coloring by tribes:
![](results/sgCombatC2Trench0.png) ![](results/sgCombatC2Trench100.png) ![](results/sgCombatC2Trench150.png)

###### Combat eliminates waves under rules ({G1}, {C2}):
![](results/CombatC20.png) ![](results/CombatC26.png) ![](results/CombatC21100.png)

###### Combat and Cultural Transmission under rules ({G1}, {Cinf,K}):
![](results/sgCombatCultural0.png) ![](results/sgCombatCultural10.png) ![](results/sgCombatCultural1000.png)

###### A realization of the Proto-History under rules ({G1}, {M,S,K}) and random distribution of agents, showing: migration, spatial segregation, mating, cultural transmission and finally tribes interaction such as collisions, penetrations, and conversions producing complex social histories :
![](results/sgProtoHistoryInitial.png) ![](results/sgProtoHistorySegregation.png) ![](results/sgProtoHistory100.png)

### Instructions
Install Python 3.6 and above: https://www.python.org.  
Install Pygame 2.1 package: http://www.pygame.org.  
On command schell, execute: `python sugarscape.py`.  
Edit `sugarscape.py` and uncomment settings for the wanted simulation, run again.

##### Available controls during simulation:
- **[F1]**  : show current agents population.
- **[F2]**  : show current agents whealth histogram.
- **[F3]**  : show current agents metabolism and vision mean values.
- **[F12]** : start / pause / resume simulation.

### Todo
- Trading rules.
- Diseases.

### Reference
- Schelling, Thomas C. (1978). Micromotives and Macrobehavior, Norton.
- Epstein, Joshua M.; Axtell, Robert L. (1996). Growing Artificial Societies: Social Science From the Bottom Up, MIT/Brookings Institution.
