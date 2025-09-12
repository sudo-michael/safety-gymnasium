import safety_gymnasium

env = safety_gymnasium.make("SafetyPointCircle1-v0")
for i in range(100):
    obs, info = env.reset()  # pylint: disable=unused-variable
print('done')