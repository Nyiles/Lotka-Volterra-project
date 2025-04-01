"# Lotka-Volterra-project" 
An Extension in Mathematical Nature
Nyiles Spann
Predator-Prey relationships are extremely complex in nature and have been a topic which many biological based researchers and have spent countless years observing. There are countless factors which effect exactly how these relationships play out in nature. Luckily, the Lotka Volterra model is a concise mathematical set of equations which uses differential equations of calculus to predict the possible growth rate of both a predator and prey. While the Lotka Volterra model is a great starting point of understanding possible outcomes of predator and prey relationships, it however does have its limitations. Using the basis of the Lotka Volterra model, I will go further in depth to portray how a predator and prey dynamic may occur using calculus. 
1.Introduction
Before getting into the goals of the project, laying some important groundwork for exactly what the Lotka Volterra model is is necessary. With that being said, in 1920, mathematicians named Lotka and Volterra independently studied a “mathematical model for the population dynamics for the population dynamics of a predator and prey, and these Lotka-Volterra predator-prey equations have since become an iconic model of mathematical biology.” According to author Fishwick, the Lotka-Volterra model makes the following assumptions of simplification:
1. Only two species exist, being the predator and the prey
2. There are no other cofounding variables such as poor weather or other environmental impediments.
3. Prey dies only through predation, and predators only die over a period of time through natural causes.
4. the predator feeds on the prey population with an unlimited appetite
5. The number of specific predator decay exponentially in the absence of prey
6. The number of the specific prey increase exponentially in the absence of predators
The specific goal of the project it to extend on the first limitation listed, where only two species exist. In this project, I have added another species of predation into the mix. Adding another species will add an interesting element of competition. They will both require the same resource of food, so it will be interesting to see exactly how adding another species will play out. With all these fundamental ideas, it is safe to say that model the Lotka-Volterra model and my model are simplified versions of actual nature of course, as removing all of these elements of simplicity and achieving completely correct accuracy would result in a nearly impossible task, but hopefully my series of equations will lead a step in the right direction of how realistic relationships between predator and prey occur in actual nature.
One last important note before getting into the necessary equations, is that populations of species do not go extinct in the Lotka-Volterra model, which although rare, there is of course a possibility that prey go extinct to predators in real life or predators going extinct because of their lack of ability to catch prey.
In this model, as long given the inputs (which we will talk more about later) are reasonable, then an oscillation or repeat of the pattern of population is typically presented, so therefore, no extinction is able to occur. 
Now that the scientific part of the Lotka Volterra model has been explained, lets us move onto the math portion.
The original, one predator, one prey Lotka Volterra follows these mathematical equations.
Prey Growth Rate = dU/dt = aU−bUV

Predator Growth Rate = dV/dt = cbUV−eV

U represents the current population of the prey. V represents the current population of the predator. a represents the birth rate pf the prey. b represents the predation rate of the predator. c represents the conversion efficiency of the predator. Finally, e represents the death rate of the wolves. All of these variables are observable inputs and are driving factors of the growth rate of each species.
While the creation of these equations is elaborate and impressively designed by Lotka and Volterra and may even seem complex in understanding in the beginning, it makes perfect sense once the values are explained. For example, it makes sense that the population of prey will be negatively affected when they are both more predators and prey because there is more prey to die and there more predators that can hunt the prey.
The extended version of the equations, with two predators follows:
Prey Growth Rate = dU/dt = aU−bUV – cUW
 
First Growth Predator = dV/dt = ebUV−fV

Second Growth Predator = dW/dt = gcWU – hW

U and V once again represents the recent population of the prey and the first predator respectively. W represents the current population of the second predator. a represents the birth rate of prey. b and c are the predation rate of the first and second species of predators respectively. e and g are the conversion rate of food to a new born predator of the first and second species respectively. Then finally, f and h are the predators death rates.
This extended version is not too different on the mathematical inputs, when compared to the original differential equations, however, it is expected to produce very different results.
The growth rate of each of the predators is an important step, because we can use the growth rate, and then integrate it over time, which will then give us a population at a certain point. The integration uses a python importation, which is friendly to the user, as I simply put in the inputs listed earlier, with a list of time certain time periods where I want to observe the population. 
2. Methods
A theme I wanted to incorporate in these different forms of analysis is animations. I think that progressing through a graph, or the simulation, or the heatmap is important as you get to visualize the time passing as opposed to a static graph, where you can see all the information is just spewed. 
For the sake of naming, the prey I will refer to are bunnies. The first predator, which I often refer to as the ‘first predator,’ are wolves. The second predator, which I again will also often refer to as the ‘second predator,’ are foxes for this project.
 
Figure 1: displays the animation of species partially drawn out.
 
Figure 2: displays the animation of three species fully drawn out.

The simulation portion was created using the Pygame GUI extension in python. Pygame authorizes the formation of an ‘animated’ experience by its frame-by-frame framework.
 I use a 16x16 tiled board for readability. Each of the animals’ positions are pseudo randomly drawn on a tile and the positions are appended to a list using an x and y coordinate style format. 
Then, each of the animals are drawn by using lines, ellipses and arcs. The animals can then officially be drawn based on their position in the list. To draw all of the animals, I use a loop which draws the amount of a given argument. The argument is determined by the population which was solved with the integration of the growth rate. 
	The animation part of this simulation was created by popping the first of the list of each of the list. The pop method removes the first element of the list and then shifts all the elements to one index left than where it previously was. Since the Pygame extension is capable of running a loop based on frame rate, the draw method is called, and replaces the missing elements and randomizes its position, which causes it to “travel” across the screen. The frame rate is set to a slow speed, so the prey is not jumping around too rapidly where it would be impossible to grasp the current population of each species.
	After the user starts running the simulation, it responds to the user pressing any key. When the user presses a key, The time is shifted one unit forward and permanently deletes or adds the necessary species based on the overall population of each species in the next measurement of time. Therefore, the user can progress in time at their own speed. The simulation can run up to 500 different time periods initialized by a count variable, but at any point, the user can exit the program. After the simulation is exited, a follow up graph is drawn using animations. The overall approach to the simulation is to add an element immersion rather than just staring at graphs. 
	The graph gradually draws the population of each of the species over the time period between zero and however many times the user pressed the key. 
 
Figure 3: Displays the GUI simulation at time count of zero units.
 
Figure 4: displays the GUI simulation at time count of 32 units.
	Finally, we can observe the population of the species using three separate heatmaps. Originally, I initialize a 16 by 16 two-dimensional array full of zeros. Then based on what the population is, I update the two-dimensional array based on the population, and change the some of the array’s elements from 0 to 1. The 2D array fills the first row up with 1’s and then moves onto the next row. This changes the color of the heatmap from orange to white. Then, the two-dimensional arrays values are displayed in animated heatmap. The frames of the heatmap start from zero and then goes to the total length of time. Then when the overall population decreases based on the differential equation, the heatmap responds by changing the most recently added 1’s back to zero. To openly know when the population is decreasing, the heatmap ‘blinks’ by frame.
The goal of the heat map is to grasp the how quickly the change in population occurs relative to the units of time. 
 
Figure 5: Displays the bunny heatmap while its population is on the rise.
All three of the species have a population of one unit for a long period of time, but the predators seem to spend more time at the lowest population. All the species gradually increase in population and reach their peak for a very short time period. Then all the species rapidly decrease once they have reached their peak.
	Looking back on the equation, the specific observable inputs I am using for this model is the following:
a (Prey birth rate) = .1
b (Predation rate for predator one) = .05
c (Conversion efficiency for predator one) =.1
d (Predator death rate for predator one) =.1
e (predation rate for predator two) =.02
f(Conversion efficiency for predator two) =.1
g(Predator death rate for predator two) =.1
with the starting population being 10,10,2. These inputs are very consistent and stable relative to each other. Also, it is important to note that both predators share the same conversion rate and the same death rate. The differences are their initial population, and their predation rate.

 
Figure 6: The graph of the three-predator model for time 0 to 400.
Looking at the graph, and based on the given stability of the inputs, the output population of each of the is calculated. In other words, all of the populations go as expected. The first predator and the prey immediately start with a drop off, as the predators have fed off all the bunnies, and there seemingly is still not enough food. The population of the first predator is already low, but it still has a slight drop off. Then the bunnies can flourish because of the small number of predators. The prey population peaks in the hundreds. Then the predators can catch up and grow, in size, however, since each of their conversion rate is small, their numbers do not peak too highly. The bunny’s population rapidly drops and then oscillation occurs. The last thing I noticed was the second predator struggled more than the first predator, which makes sense as both of its inputs are lower.
Now what if we compare this graph to each of the graphs of when just the singular predator comes into the equation, keeping everything else constant.
 
Figure 7: The two species model equated by the original Lotka-Volterra model, with the predator species being the wolves.
Compared to the first graph, this graph oscillates a little bit less, meaning that the levels of wolves and bunnies are depicted to be a little bit more stable. What surprisingly did not change is that the wolves share about the same peak population as they did in the first graph, which may suggest an overall dominance of competition by the wolves in the scenario with two predators. The last surprising bit of information is that the bunnies had a way higher peak (around 100 more units in population) in the graph with two predators, than in this scenario with just one predator. This can be explained to when some of the complexity comes in when you add competition. In the first graph, at numerous points, both species experience extremely low levels of population, which allowed the bunnies to thrive for a longer period of time.
 
Figure 8: The two species model equated by the original Lotka-Volterra model, with the predator species being the foxes.
Comparing this scenario to the first graph, it is important to remember that this is the predator with the lower inputs of predation rate and conversion efficiency. In this graph plenty of oscillations occurs in this time period. Furthermore, there seems to be a ‘healthy’ dynamic between the bunnies and the foxes as the populations of both species rise steadily and fall steadily. What is interesting is the bunnies have the lower peak population despite the predator having a lower input of food conversion. This is likely because their population is unable to grow to an unsustainable amount, to the point where they would almost all die off and let the prey grow exponentially, which occurred in the graph with two species. All in all, species which may often do well without having to share a food supply may struggle with the addition of another species hunting their food.
An important thing to note is that at no point could either of the predator species go extinct based off the model equations, due to competition between each other. Again, while either species going extinct is very rare, it has happened before.
Overall, the goal is to provide a deeper understanding of how predator and prey relationships may occur in nature through removing a simplification of the Lotka- Volterra model, adding to the realism. Then provide immersion using the Pygame GUI and the animation of the two-predator graph and the three heatmaps. Also, making multiple comparisons along the way provide details of just how much the model changes when we go from one species of predators to two species of predators.
Now how differently would a new graph look if we added back the second predator but looked at a potential combination of different input variables. 
 
Figure 9: A three-species graph with a different set of input arguments
The inputs used in this new graph are the following:
a (Prey birth rate) = .3
b (Predation rate for predator one) = .2
c (Conversion efficiency for predator one) =.3
d (Predator death rate for predator one) =.1
e (predation rate for predator two) =.1
f(Conversion efficiency for predator two) =.2
g(Predator death rate for predator two) =.1
In this graph, the peaks are just as frequent, however, the peaks in population, especially for the prey appear to occur for an even shorter period of time before falling back down. Next, the species with the higher population in the beginning quickly falls below the species with the low population. The predator which starts with the lower population thrives when compared to the other predator, due to its greater ability to hunt the prey and its higher conversion efficiency, which allows it to convert the same amount of food into new births of its species. So overall, it wins the competition against its other predator.
3. Discussion
In summary, in this project, I used differential equations and observable inputs in an extended version of the famously known Lotka-Volterra model. I used multiple animations to try and create immersion in the understanding of how the population changes over a certain period of time. This was done through animating the plot, creating a heat map for each species, then creating a Graphical User Interface simulation for an environmental aspect. Through this we were able to see how each species grew and fell off in real time measurements.
A common goal of one majoring in computer science is to deliver a useful way of understanding a tough scientific or mathematical study through innovative methods of programming, and what better way for a computer science major to do it than by creating a simulation through the use of a GUI. 
I also made multiple comparisons using various graphs, which compared the extended model to the original model. Then I made observations on what would happen if we looked at specific, yet different inputs. Through these comparisons, we were able to fully digest the concept of competition, and how a change of factors such predator conversion rate drastically changes the course of populations.
Looking at some short comings, there were two features which seemed to be a little bit buggy. The first appeared on the simulation, when I tried to make sure that the overlapping of species on a tile did not occur. To achieve this, I made an empty set which zipped the paired values of the x and y coordinates of all the species. In theory and testing this method would work until I used it for the simulation, as the simulation would not run. Therefore, I failed to implement this goal. Then, the second shortcoming was what appeared to be a performance issue on the heatmap. The heatmap would struggle to change all the necessary values from 0 and turning them into one, despite the method giving the correct answer for the number of values necessary.
Finally, some possible extensions may be adding cofounding variables, and researching how cofounding variables such as storms or the addition of other bad weather may affect the population, while keeping the other three out of the five assumptions of the Lotka Volterra model constant. I could also add even more species of both predators and prey into the model to establish further grounds of how an ecosystem may act out entirely.

4. Appendices 
-	Main.py – uses Pygame to run a simulation for the user and prints the analysis graphs afterwards.
-	Heatmap.py – uses a heatmap to present further analysis on the species of prey.
-	Heatmap1.py- uses a heatmap to present further analysis on the species of predator one.
-	Heatmap2.py – uses a heatmap to present further analysis on the species of predator two.
-	Comparisons.py – created the graphs of the original Lotka-Volterra model to compare to my updated version.	

References
Chasnov, Jeffrey R. "The Lotka-Volterra Predator-Prey Model." LibreTexts, Hong Kong University of Science and Technology, 2008. Accessed April 2024. https://math.libretexts.org/Bookshelves/Applied_Mathematics/Mathematical_Biology_(Chasnov)/01%3A_Population_Dynamics/1.04%3A_The_Lotka-Volterra_Predator-Prey_Model.
"Lotka-Volterra Model." ScienceDirect, Elsevier, Accessed April 2024. www.sciencedirect.com/topics/earth-and-planetary-sciences/lotka-volterra-model.
Lalith, S. "A Generalization of the Lotka-Volterra Model for Predator-Prey Systems." University of Washington, June 2016 . Accessed April 2024. https://sites.math.washington.edu/~morrow/336_16/2016papers/lalith.pdf#:~:text=This%20model%20is%20a%20very%20slight%20generalization%20of,the%20food%20chain%20and%20z%20preys%20on%20both%29.
