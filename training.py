import numpy as np
import time
import os

# create environment
env = Env()

qtable = np.random.rand(env.stateCount, env.actionCount).tolist()     # QTable 

# hyperparameters
epochs = 50
gamma = 0.1
epsilon = 0.08
decay = 0.1

# training loop
for i in range(epochs):
    state, reward, done = env.reset()
    steps = 0

    while not done:
        os.system('clear')
        print("epoch #", i+1, "/", epochs)
        env.render()
        time.sleep(0.05)

        steps += 1      # count steps to finish game

        if np.random.uniform() < epsilon:       # act randomly sometimes to allow exploration
            action = env.randomAction()
        else:                                     # if not select max action in Qtable
            action = qtable[state].index(max(qtable[state]))

        next_state, reward, done = env.step(action)

        qtable[state][action] = reward + gamma * max(qtable[next_state])  ################## update qtable value with Bellman equation

        state = next_state      # update state
   
    epsilon -= decay*epsilon

    print("\nDone in", steps, "steps".format(steps))
    time.sleep(0.8)
