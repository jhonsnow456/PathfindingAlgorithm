# PathfindingAlgorithm

## Description:
The A* algorithm is one of the most effective path finding algorithms used to find the shortest path between two points. It was first published in 1968 by Peter Hart, Nils Nilsson and Bertram Raphael. Although it initially can be seen as an extension of Dijkstra’s algorithm, it has become one of the most frequently used pathfinding algorithms today.

## Algorithm:
The A* algorithm basically reaches the optimum result by calculating the positions of all the other nodes between the starting node and the ending node. In addition, it is faster than Dijkstra’s algorithm due to the heuristic function.

f(n) = g(n) + h(n)

f(n) : Calculated total cost of path

g(n): The cost of path between the first node and the current node

h(n): Heuristic function

![fig 1](https://miro.medium.com/max/700/1*8KbswpUrSZr9jdHKu4tn7A.png)

Let’s say we are trying to get from point X to point Y. Since the point X is not moved to a different node, the g(n) cost does not occur and its value is 0. The heuristic value of this point is the value 5 written on the node in red. In such problems, the heuristic value in general is the air distance between the current node and the desired node. There are two points to go from point X.
In case of going to point A, g(n) = 5 (path cost) because it moves to a new node. The heuristic is set to h(n) = 1. The f(n) value of point A is found as 5+1 = 6. If we want to find the f(n) values ​​of all points using this method,

X— A => g(A) + f(A) = 5 + 1 = 6,

A — Y=> g(Y) + f(Y) = 6+ 0= 6,

X— B => g(B) + f(B) = 1+ 4= 5,

B — C => g(C) + f(C) = 3+ 2= 5,

C — Y=> g(Y) + f(Y) = 5 + 0= 5,

As seen in the simple example above, the shortest path is the X-B-C-Y route. The cost of this road is 5 units, while the cost of the alternative X-A-Y route is 6 units.

![fig 2](https://miro.medium.com/max/2400/1*YBxYjiDJ0I5enuH7rxC8hw.png)

Let’s say we want to reach node A from node J. There are 2 points (B and F), that can be reached from point A. Calculating the overhead costs, we get f(B) = 8 + 6 = 14 and f(F) = 3+6 =9.Since the least cost is at point F, the A* algorithm continues from here. There are 2 paths at point F. f(G) = 4 +5 = 9 and f(H) = 10 + 3 = 13. Since the least cost is at point G, we can do it from that point. Then, following the I and J nodes, we get f(I) = 7 + 1 = 8 , f(J) = 10. Since all the values ​​obtained after going to the F node are less than the f(B) node, it was not returned to the B node. But in a different scenario, let’s assume that f(I) is greater than f(B) after nodes F and G (f(I) > 14). In this case, according to the A* algorithm, the process is interrupted here and the path is continued with the B node. Here, as soon as f(C) > f(I), the path determination process continues again from the I node.
