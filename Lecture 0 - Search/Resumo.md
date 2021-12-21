Result: picks a state, and returns this state after executing some action

State space: set of all states reachable from the initial state by any sequence of actions

Goal test: way to determine whether a given state is a goal state

Path cost: numerical cost associated with a given path

Node: data structure that keeps track of a state, a parent, an action and a path cost

# Solving Search Problems

## Approach: 
- Start with a frontier that contains the initial state
- Repeat: 
    - If the frontier is empty, then there is no solution
    - Else: remove a node from the frontier
    - If node = goal, return the solution
    - Else: expand node, add resulting nodes to the frontier

Problem with this approach: may cause an infinite loop, since we can have a state A that points to B, but that state B can point to A and C at the same time.

## Revised Approach:
- Start with a frontier that contains the initial state
- Start with an empty explored set
- Ex.: Frontier = [] and Explored = []
- Repeat:
    - If the frontier is empty, then there is no solution
    - Else: remove a node from the frontier
    - If node = goal, return the solution
    - Add the node to the explored set
    - Expand node, add resulting nodes to the frontier only if they aren't already there or on the explored set

Problem: when removing a node from the frontier, we are not always choosing the best one

# Depth First Search (DFS)
- Search algorithm that always expands the deepest node in the frontier

- Not necessarily the optimal solution, kind of luck dependant.

## Stack
- LIFO data type: last-in first-out

- Example: imagine a stack of shirts in a store. The last shirt to be put on that stack will be the first one to get out.

# Breadth-First Search (BFS)
- Search algorithm that always expands the shallowest node in the frontier

- Instead of exploring a path till the end, like DFS, BFS explores multiple paths after a decision point at the same time, with the same depth. 

- BFS isn't necessarily always better than DFS

## Queue 
- FIFO data type: first-in first-out. Opposite of LIFO.

# Uninformed Search
- Search strategy that uses no problem-specific knowledge

# Informed Search 
- Opposite lol

# Greedy Best-First Search (GBFS)
- Search algorithm that expands the node that it thinks is the closest to the goal, estimated by a heuristic function h(n)

- Example: knowing the (x,y) coordinates of the initial state and the goal state, we can know with intermediate points, such as C and D, which one is closest to the goal. In this case, the heuristic function is called the Manhattan distance (A.K.A Taxicab Geometry)

- Not necessarily optimal

# A* Search
- Search algorithm that expands node with lowest value of g(n) + h(n)

- g(n) = cost to reach node
- h(n) = estimated cost to goal

- Instead of just considering the Heuristic, it also considers how long it took to get to some state

- Optimal, if: h(n) is admissible (never overestimates the true cost) and h(n) is consistent (for every node n and sucessor n' with step cost c, h(n) <= h(n') + c)

# Adversarial Search
- Another agent is trying to make you not reach the goal state, like in a tic-tac-toe game 

## Minimax


- Example: in a tic-tac-toe game, you are X, so O winning is -1, a tie is 0 and X winning is 1

- MAX (X) aims to maximize score
- MIN (O) aims to minimize score

### Game 
- S0: initial state
- Player(s): a function that receives a state and returns which player's turn is it
- Actions(s): returns legal moves in a state s
- Result(s, a): returns state after action a taken in state s
- Terminal(s): checks if state s is a terminal state
- Utility(s): find numerical value for a terminal state s

- Watch lecture at around 1:19:00 for the gameplay
#
- Given a state s:
    - MAX picks action a in Actions(s) that produces highest value of Min-Value(Result(s, a))
    - MIN picks action a in Actions(s) that produces smallest value of Max-Value(Result(s, a))

function Max-Value(state):
    if Terminal(state):
        return Utility(state)
    v = -inf
    for action in Actions(state):
        v = Max(v, Min-Value(Result(state, action)))
    return v

- Value v is -infinity and, for every action possible, v is going to be the max value between it's current value and the minimum value that the opponent can get 

function Min-Value(state):
    if Terminal(state):
        return Utility(state)
    v = inf
    for action in Action(state):
        v = Min(v, Max-Value(Result(state, action)))
    return v

# Alpha-Beta Pruning
- When the Max player wants to choose between states, they don't need to look at all the trees that could be generated with an action, since, if one of the branches is already lower than say another branch, we can't get a higher value in any of the sub-branches, so we don't even need to look into them. Kinda confusing when writing, watch lecture at around 1:41:00.
- Could get heavy depending on the game, such as chess, which has 10^29000 possible combinations, this number being a lower bound.

# Depth-Limited Minimax
- After a certain amount of moves, we stop, because it might get too heavy.

## Evaluation function
- Function that estimates the expected utility of the game from a given state. Example: Chess' StockFish Bar that estimates the advantage a player has.