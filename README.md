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
   
## Part 2: Idea and implementation
   - Algorithm                                                                                                                                                      
   I adapted the [DDPG algorithm](https://arxiv.org/pdf/1509.02971.pdf) to solve both the single reacher environment and multiple reacher environment. 
   While adating the algorithm, i referenced the [openai ddpg document](https://spinningup.openai.com/en/latest/algorithms/ddpg.html), the [udacity discussion](https://knowledge.udacity.com/questions/98687) (may need a udacity account to have access) and [gcolmen's github](https://github.com/gcolmen/actor-critic-ddpg) as reference.
   
   - Implementation detail                                                                                                               
   For detailed implementation description, see [report.pdf](https://github.com/CenturyLiu/RL-Project-Reacher/blob/master/report.pdf).
   
## Part 3: Code navigation
   - Prerequisite                                                                                                             
     To run the codes in this repository, please follow instruction on [Udacity deep reinforcement learning](https://github.com/udacity/deep-reinforcement-learning) to setup the environment.
     After setting up the environment, download the files in this repository and put them into /your path/deep-reinforcement-learning/p2_continuous-control
     Download the reacher environment for your computer.
     One agent:
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)
        
     Multiple agents:
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
        
   - Solutions
      - OUNoise Multi-agent solution                                                                                                                    
      package: [ddpg multiple](https://github.com/CenturyLiu/RL-Project-Reacher/tree/master/ddpg_multiple) 
      
      |File name|description|
      |---|---|
      |model.py|implementation of actor and critic network|
      |ddpg_agent.py|implementation of ddpg agent with OUNoise|
      |continuous_control.py|main function for training with multiple agent|
      |watch_agent.py|see the trained agents, the trained weights are stored in the two .pth files|
      
      ![multiple agents](https://github.com/CenturyLiu/RL-Project-Reacher/blob/master/plots%20and%20demo/multi_OU_108.png)
      > The OUNoise implementation uses 108 episode to solve the multi-agent environment.
      
      - Single agent solution with [OUNoise](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)                          
      package: [ddpg single](https://github.com/CenturyLiu/RL-Project-Reacher/tree/master/ddpg_single_3)
        
      |File name|description|
      |---|---|
      |model.py|implementation of actor and critic network|
      |ddpg_agent.py|implementation of ddpg agent with OUNoise|
      |continuous_control.py|main function for training with single agent|
      |watch_agent.py|see the trained agents, the trained weights are stored in the two .pth files|
      
      ![single agent](https://github.com/CenturyLiu/RL-Project-Reacher/blob/master/plots%20and%20demo/single_OU_592.png)
      > The OUNoise implementation uses 592 episode to solve the single-agent environment.
      
      - Single agent solution with uncorrelated, mean-zero Gaussian noise                                            
      package: [ddpg_single_Gaussian_noise](https://github.com/CenturyLiu/RL-Project-Reacher/tree/master/ddpg_single_normal_distribution_noise_2)
      
      |File name|description|
      |---|---|
      |model.py|implementation of actor and critic network|
      |ddpg_agent.py|implementation of ddpg agent with OUNoise|
      |continuous_control.py|main function for training with single agent|
      |watch_agent.py|see the trained agents, the trained weights are stored in the two .pth files|
      
      ![single agent with white noise](https://github.com/CenturyLiu/RL-Project-Reacher/blob/master/plots%20and%20demo/single_gauss_192.png)
      > The gaussian noise implementation solves the single agent envrionment in 192 episodes.
      
      Please remember to change the file path to the reacher environment in "continuous_control.py" before use.

## Part 4: Demonstration of trained agent
