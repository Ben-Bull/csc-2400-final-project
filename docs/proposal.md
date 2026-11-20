# Project:  Finding the fastest method of a “Full Reset” run in “The Farmer was Replaced”

The Farmer was Replaced is a programming game where you must program a drone to automatically farm crops for you. Many of the crops in the game focus on certain aspects of programming, such as sorting algorithms, data validation, or parallel programming. The normal progression of the game includes completing an “unlock tree” that houses all of the types of crops, and new programming functions that you can utilize in your drone’s programming.   
	  
	A “Full Reset” run of the game is a challenge set forth by the game to completely code and automate the game from start to finish, including automatically purchasing necessary upgrades, like unlocking the various kinds of crops, as well as the various programming tools, like functions, loops, etc., to finally reach and unlock the “Leaderboards” node in the unlock tree. Creating such a script proposes many challenges, including deciding exactly how you instruct your drone to do things, which upgrades to get first, or whether you should focus on upgrading the crops you already have to increase their yield, or focusing on getting each new node first. We will use different implementations of algorithms to determine which method is the fastest to complete the Full Reset.   
	  
	There is an in-game leaderboard of the top 300 players with their respective times to completion, and they range from 12:15 to 1:13:18. These numbers may not be super accurate however, because the 200-300 range is within \~3 seconds of each other, meaning they all likely copied someone else’s existing code from online and ran it using that. We will not be writing all of the code ourselves, namely finding an optimized method to farming certain crops, but we will not be copying the entire script, so we will implement the route, what order the drone purchases upgrades in, ourselves. Using the leaderboards as a reference, the run should be around an hour of real time, however the game does allow massive speed up on the simulation so you do not have to sit there and watch the whole thing.

# How are we implementing this?

	  
	We will be “replicating” the upgrade tree from the game with a weighted directed graph, that instead of using normal pre-defined weights, will use a system of “dynamic weights” which will represent a “time to completion” for any given task, which will be calculated using all currently obtained upgrades, like drone speed multipliers, crop yield multipliers, and other mechanics like watering soil, or the energy resource that makes the drone move faster.

	Rather than attempting to simulate the algorithms in the actual game itself, making an accurate representation of the game’s progression in code will be much easier to run algorithms on. An output from the algorithm will be a set of steps laid out in order of completion, as well as an estimated elapsed time for the whole script to run in-game. We will then implement the script in the game for demonstration purposes. We will be able to compare the runtimes for each different algorithm to achieve a conclusive result.

	The Algorithm that we chose was the A\* algorithm. By choosing this method it makes finding a node (Goal or trophy) very fast and efficient as the A\* algorithm is an informed search algorithm that uses external information to execute. Given a weighted source node and a goal node (in this case a “full reset”) the algorithm will find the shortest path from its source to its goal with respect to its weights, being the time taken from one node to the next, making it have a time complexity of O(\|E\|+\|V\|); which can be efficient as the algorithm terminates once it finds the most optimal path rather than building a tree of all possible paths.

	The brute force method we will be implementing will work towards completing the first goal (i.e. node) on the graph and then run through nodes until it finds the trophy node. It will then restart and run a different possible combination of nodes until all sequences of nodes have been attempted. This will ensure the most optimal solution is found this way, but because of the nature of this brute force method, it will have a computation time of O(n\!). With fourteen required nodes and twenty more optional nodes (sourced from an image below), that’s ever so slightly under 2.95 \* 10 ^ 33 possible routes and 8.72 \* 10 ^ 10 or so routes that ignore optional nodes. So, the most optimal solution will be found, but it will take a while this way.  
	  
	We will implement a genetic algorithm but it is not required for this part of the project, so we did not work that part out yet.  
	

# 

# Proposal questions:

* What problem are you solving?

	Completing a “Full Reset” run of the game “The Farmer was Replaced”

* What does an input look like?  
  The input will be a weighted directed graph, which will be an abstract representation of the game’s upgrade tree.   

* What does a solution look like?  
  A solution is a list of steps that ends with unlocking the Unlocks.Leaderboard (hereby referred to as the “trophy”) module on the upgrade tree.  

* What makes one solution better than another?  
  A solution can be made better either by making the script size smaller or, in this case, optimizing the runtime of the script by finding a more efficient method of completing the game  

* Why did you pick this question to solve?  
  The original proposition was to find an algorithm to beat Minecraft efficiently; however, this game will not only improve our coding abilities, but also be a bit easier to explain and implement  

* How could brute force solve it?  
  A brute force approach would aim to unlock the trophy module using the first possible unlock in the tree and then that unlock’s child until it’s impossible, then iterate to the next possible unlockable module  

* What third algorithm are you considering?  
  We will be using the A\* algorithm to find the quickest path to completion  

* What question are you trying to answer?  
  Which algorithm creates the most efficient route to completing the run?  

* How might you compare the algorithms?  
  Comparing the route that each one takes, including when the algorithm buys upgrades and how many levels of each.  

* What challenges do you expect?  
  Getting accurate time measurements for each type of crop, as well as laying out accurate formulas to calculate the time to completion for each kind of crop. Since there are so many different upgrades that the drone can get, and they all work in slightly different ways, figuring out how to account for them correctly will be difficult. An example would be the size of the farm, because the size does affect some things a lot more than others, namely pumpkins that gain an increasing multiplier on yield for how big of a pumpkin you plant.  

* What sources have you found?  
  [https\://thefarmerwasreplaced.wiki.gg](https://thefarmerwasreplaced.wiki.gg)   
  	This is the wiki for the game, it has information like how much each upgrade costs etc.

[https\://github.com/RubenNijhuis/the-farmer-was-replaced](https://github.com/RubenNijhuis/the-farmer-was-replaced)
	This is some guy’s code that we are stealing from github because why invent bread if someone else already sliced it.

* What does the workload balance between team members look like?

  ## Only one group member is familiar with the game, so they will be doing a majority of the code writing (its python anyone could probably), other members will help with code writing, planning, etc. Meetings will occur as needed throughout the semester and communication will go through a group text thread.       

  ## Algorithm Notes:

	Algorithm 1: (genetic)

	Not covering yet (as of proposal date)

	Algorithm 2: (Brute force)

	The brute force approach takes into account all accessible nodes and visits them in order, similar to breadth first search, then will look at the new accessible nodes and repeat, until the end goal is achieved. Across the many different runs, the algorithm will unlock things in different orders, eventually finding the quickest path. The runtime for this algorithm will be incredibly slow.

	Algorithm 3: (A\*)

	The A\* algorithm will combine the best parts of both Dijkstra’s and a greedy algorithm to find the best path. It has a level of foresight from given information that it will use to look ahead and see what possible options it can take that will satisfy the greedy algorithm’s goal for the smallest total weight. Instead of “wandering around blindly” like the brute force algorithm will, the A\* approach will have a “plan” which should make the runtime significantly faster than the brute force to find the quickest path.

## Stuff needed to win: 

(from [https\://thefarmerwasreplaced.wiki.gg/wiki/Unlocks\_Data](https://thefarmerwasreplaced.wiki.gg/wiki/Unlocks_Data))

Leaderboard unlock:

	Items.Bone: 2000000

	Items.Gold: 1000000

Bones unlock:

	Items.Cactus: 2000

Gold unlock:

	Items.Weird\_Substance: 1000

Cactus unlock:

	Items.Pumpkin: 5000

Fertilizer unlock (gives weird substance):

	Items.Wood: 500

Pumpkin Unlock:

Items.Wood: 500

Items.Carrot: 200

Carrot Unlock:

	Items.Wood: 50

Plant() function (Wood) unlock:

	Items.Hay: 50

Watering unlock (not a required resource, but is required to unlock fertilizer)

	Items.Wood: 50

Loops unlock (first node in tree)

	Items.Hay: 5

Debug unlock (another required unlock):

	Items.Hay: 50

	Items.Wood: 50

Timing unlock (required):

	Items.Pumpkin: 1000

Simulation unlock (also required):

Items.Gold: 5000

Speed unlock:

Items.Hay: 20

Optional Unlocks:

Expand Unlock (makes farm bigger, can farm more at once):

Items.Hay: 30

## Context:

Hay grows passively on all ground that doesn’t have anything else planted on it, so no unlock needed.

Unlocking the Plant() function comes with being able to plant a bush which drops wood when harvested. Trees also drop wood at a much higher rate, so we could have the “smarter” algorithm utilize those instead.

Fertilizer makes a plant grow faster, but also infects the plant, which makes half of its output become weird substance, so it could be farmed at the same time as other crops.

