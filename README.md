# Solving-a-randomly-generated-maze

### Path finding on a randomly genearted maze
1. A maze is randomly generated with only black and white pixels. The probability of a pixel of being black is maintained at 30%.
2. BFS, DFS, Dijkstra's algorithm, Greedy BFS and A* --- these five path finding algorithm is used to find path between the top-left and bottom-right corner pixel.
- Output video links:
1. [Dijkastra's Algorithm](https://drive.google.com/file/d/1CKLQo8_5_CNS0BOI-rjV-KWv16_1JIf7/view)
2. [Greedy Algorithm](https://drive.google.com/file/d/1niu1XV2odjv3zFeOKkYcIbrWOvoLbJ15/view)
3. [Depth First Search](https://drive.google.com/file/d/1ILl8wGcM75kXyMab18l5JlHYdvD1BIsS/view)
4. [Breadth First Search](https://drive.google.com/file/d/1ftRGQB5IvUtlaoP0nXN_le71Us9tdu5V/view)
5. [A* Algorithm](https://drive.google.com/file/d/1-POaKRuBWTw0sOFrRIT7ohHA7QbmRxDL/view)
- Some snapshots:
![Screenshot from 2022-12-29 11-10-38](https://user-images.githubusercontent.com/100329968/209908163-4c1887e9-24f4-4bc5-bb61-c2a90b1f36d5.png)


### Path finding on a map
Finding a route between **start point**(126,19) and the **end point**(257,183) on the given map(276x431).
![map](https://user-images.githubusercontent.com/100329968/209906908-544052e3-d46d-458a-864f-18e604f48588.png)
- Output video links:
1. [Dijkastra's Algorithm](https://drive.google.com/file/d/1FaKQP-tDU8ebnDLGrog6Wjoomov4_dlP/view)
2. [Greedy Algorithm](https://drive.google.com/file/d/1PHTpjJcHLO_Fbpivv0J3ghlYaEezpoBP/view)
3. [Depth First Search](https://drive.google.com/file/d/1I7CYoaMq3wa-1ihh9otayP_nQrioL02l/view)
4. [Breadth First Search](https://drive.google.com/file/d/1ENVpW2L9yntk7nHxAh4hIGIJKrZ76mHH/view)
5. [A* Algorithm](https://drive.google.com/file/d/1JoEXrD14GLxgjZloqkaOjqzOMUg40Eed/view)
- Some snapshots:
![Screenshot from 2022-12-29 11-14-05](https://user-images.githubusercontent.com/100329968/209908380-99073359-2692-44ab-a4d0-418a3e75e2e2.png)


### Presentation Link:
[Link](https://docs.google.com/presentation/d/1E-vr3htqHtmaNFpuvqLZoRdWdHFZeTRu/edit#slide=id.p2) of the presentation of the project.



# Implementation of RRT in python

### What is RRT?
  It is one of the various path planning algorithms. It’s a sampling-based algorithm that makes it very useful to plan high-dimensional robot paths.
  It starts with an empty tree. Then it generates random nodes in each iteration. Once a node is generated, it searches for an existing node present in the tree, which would have the minimum distance from that newly generated node. If there are no obstacles between the two nodes, a new edge is created between these two nodes and added to the tree. That’s how the tree expands and eventually finds its goal. Once the goal is reached, the path is shown between the starting node and the goal.


### Features of RRT
1. It doesn’t ensure an optimal path.
2. The growth of trees is heavily biased towards unexplored regions.
3. Using a growth factor restricts the chances of going too far in the wrong direction, making the path smoother.
4. The generation of a random state precisely at the position of the goal or final state is very unlikely. That’s why a predefined area around the final state is kept.
5. It is better than search-based algorithms like A* when dealing with high-dimension robots. 
6. Path found in RRT differs on average by a factor of 1.3 to 2.0 from the optimal path.
7. In the beginning, the tree expands non-uniformly to explore the four corners first. Once it’s achieved, the tree expands uniformly over the free space.
8. The generation of random vertices is independent of the position of the root vertex or starting point.
9. Once a tree is generated to find a goal state, we need not generate another new tree from scratch if the goal state position is changed, given that obstacles are not changing their position.


- Some snapshots:
![500](https://user-images.githubusercontent.com/97786651/209921161-c2db47db-5547-4d3a-bb33-ebe73147b229.png)
![1k](https://user-images.githubusercontent.com/97786651/209921212-e0d8a65e-e5fe-4748-93ac-a9cddef6797a.png)
![2k](https://user-images.githubusercontent.com/97786651/209921239-fa932c50-d596-4d63-8e62-f695d042242a.png)
