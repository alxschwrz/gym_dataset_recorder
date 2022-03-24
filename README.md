# gym-dataset-recorder
Package to record Transitions in OpenAI Gym Environments.

## Installation
```bash
git clone https://github.com/alxschwrz/gym-dataset-recorder.git
cd gym-dataset-recorder
pip3 install -e .
```
## Run example
```
python3 example.py
```
##
Recorded data is stored as csv-file containing the following information: 
- `observations`: An [N x observation] dimensional array of observations.
- `actions`: An [N x action] dimensional array of actions.
- `terminals`: An [N x dimensional] array of episode termination flags. This is true when episodes end due to termination conditions such as falling over.
- `rewards`: An [N] dimensional array of rewards.
- `next_observations`: (optional) An [N x observation] dimensional array of the following observations.
- `goal`: (optional) An [N] dimensional array of the current goals
- `infos`: An [N] dimensional dict containing optional task-specific debugging information.
