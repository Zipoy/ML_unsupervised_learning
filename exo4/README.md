# part 4 : exploitation/exploration compromise 

If the agent is at the leftmost position, move right. 

If the agent is at the rightmost position, move left. 

Otherwise, choose the action that leads to the highest known reward and if the rewards are equal for both positions it choose randomly with wright or left. 

To implent this policy I tried to maximise the reward, so move towards highest known reward or stay if already at the hightest reward.
