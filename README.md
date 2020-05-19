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
   
   The task I am going to solve in this repository is a task with continuous action space.
   
   **Do not confound the concept of continuing tasks and tasks with continuous action space (sometimes reffered as continuous task)**

## Part 1: Project description
   - Single Reacher Environment                                                                                                             
   In the environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. 
   
      The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.
   
   - Multiple Reacher Environment                                                                                         
   The multiple environment consists of 20 identical reachers, each with the same set up as the reacher in the single reacher environment.
   
   - Solving the environment                                                                                                                   
   To solve the single reacher environment, the agent must get an average score of +30 over 100 consecutive episodes.
   To solve the multiple reacher environment, the average score of the 20 agents must be +30 over 100 consecutive episodes.
   
## Part 2: Idea for solving the problem
   - Algorithm                                                                                                                                                     
   I adapted the [DDPG algorithm](https://arxiv.org/pdf/1509.02971.pdf) to solve both the single reacher environment and multiple reacher environment.
   The 

## Part 3: Project implementation

## Part 4: Demonstration of trained agent
