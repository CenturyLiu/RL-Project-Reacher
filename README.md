# RL-Project-Reacher
Using policy based reinforcement learning techniques to control a reacher to reach desired position.
## Part 0: Description of reinforcement learning concepts involved                                                                                         
   - Policy based method versus value based method                                                                                                                                  
   The goal for reinforcement learning is to find the optimal policy(i.e. policy lead to largest expected reward). The policy based method is directly learning / approximating the optimal policy, while the value based method is approaching the optimal policy by first getting the value function (state value or state-action value) and then choose the policy based on the value function. 
   
   - Episodic tasks versus continuing tasks                                                                                                     
   Based on whether the interation has well-defined end, reinforcement learning tasks can be divided in to episodic tasks and continuing tasks. Episodic tasks have well-defined begin and end point (eg. Drive a car from your position to destination). Continuing tasks will run forever (eg. The car is running on an endless road). The reacher project here is an episodic task.                                                                                                                                              
   
   - Continuous action space versus discrete action space                                                                                  
   The action space for reinforment learning tasks can be either continuous or discrete. For tasks with discrete action space, the policy choose one action from all actions to execute at any timestep. For tasks with continuous action space, each action is defined within a certain range. Our policy needs to give each action a value at every timestep.
   
   Example:
   Suppose we are driving a car with discrete action space control.
   |Action|Probability of choosing the action|
   |---|---|
   |Move forward|0.1|
   |Move backward|0.6|
   |Turn left|0.1|
   |Turn right|0.2|
   
   We will then choose to move backward, which has the largest probability to be optimal.
   
   If the action space is continuous,
   |Action|min|max|output|
   |---|---|---|---|
   |Pedal|-1|1|-0.6|
   |Steer|-1|1|-0.05|
   
   Then the output this time will be pedal == -0.6, steer == -0.05. Each action will be given a specified value.
   
   **Do not confound the concept of continuing tasks and tasks with continuous action space (sometimes reffered as continuous task)**

## Part 1: Project description
 
## Part 2: Idea for solving the problem

## Part 3: Project implementation

## Part 4: Demonstration of trained agent
