import networkx
# helper functions to use three of the networkx algorithms
def dijkstra(graph,start,end):
    path = networkx.dijkstra_path(graph,start,end)
    print(f'Dijkstra shortest path from {start} -> {end}: {path}')
def astar(graph,start,end):
    path = networkx.astar_path(graph,start,end)
    print(f'A* shortest path from {start} -> {end}: {path}')
def bfs(graph,start):
    bfs_edges = networkx.bfs_edges(graph,start)
    print(f'Breadth-first search from {start}: {list(bfs_edges)}')
# create empty directional graph
example_graph = networkx.DiGraph()
# directional edges with weights from example graph
example_edges = [
    ('s','A',1), ('s','D',4), ('s','G',6),
    ('A','B',2), ('A','E',2),
    ('B','C',2),
    ('C','t',4),
    ('D','A',3), ('D','E',3),
    ('E','C',2), ('E','F',3), ('E','I',3),
    ('F','C',1), ('F','t',3),
    ('G','D',2), ('G','E',1), ('G','H',6),
    ('H','E',2), ('H','I',6),
    ('I','F',1), ('I','t',4)
]
# create nodes and graph based on edges with weights
example_graph.add_weighted_edges_from(example_edges)
# shortest path using dijkstra's algorithm
dijkstra(example_graph,'s','t')
dijkstra(example_graph,'A','I')
# shortest path using a* algorithm
astar(example_graph,'s','t')
astar(example_graph,'A','I')
# breadth-first sorting, list of possible paths from a starting node
bfs(example_graph,'D')
bfs(example_graph,'E')
# custom graph
custom_graph = networkx.Graph()
# 
custom_edges = [
    ('Seattle','Portland',3), ('Seattle','Boise',12), ('Seattle','Billings',9),
    ('Portland','Boise',13), ('Portland','San Francisco',24),
    ('Boise','Billings',12), ('Boise','Cheyenne',24), ('Boise','San Francisco',23),
    ('Boise','Salt Lake City',8),
    ('Billings','Cheyenne',9),
    ('Cheyenne','Denver',0), ('Cheyenne','Omaha',14),
    ('Denver','Salt Lake City',21), ('Denver','Santa Fe',13), ('Denver','Kansas City',16), ('Omaha','Kansas City',5),
    ('San Francisco','Salt Lake City',27), ('San Francisco','Las Vegas',14),
    ('San Francisco','Los Angeles',9),
    ('Los Angeles','San Diego',3), ('Los Angeles','Las Vegas',9),
    ('San Diego','Las Vegas',9), ('San Diego','Phoenix',14),
    ('Las Vegas','Salt Lake City',18), ('Las Vegas','Santa Fe',27), ('Las Vegas','Phoenix',15),
    ('Salt Lake City','Santa Fe',28),
    ('Phoenix','Santa Fe',18),
    ('Santa Fe','Kansas City',16), ('Santa Fe','Oklahoma City',15), ('Santa Fe','Dallas',16), ('Santa Fe','Houston',21),
    ('Kansas City','Oklahoma City',8), ('Kansas City','Memphis',12),
    ('Oklahoma City','Dallas',3), ('Oklahoma City','Memphis',14),
    ('Dallas','Houston',5), ('Dallas','Memphis',12), ('Dallas','New Orleans',12),
    ('Houston','New Orleans',8),
    ('Memphis','Birmingham',6), ('Memphis','New Orleans',7),
    ('New Orleans','Birmingham',11),
]
# create nodes and graph based on board game edges with weights
custom_graph.add_weighted_edges_from(custom_edges)
# shortest path using dijkstra's algorithm
dijkstra(custom_graph,'Portland','New Orleans')
dijkstra(custom_graph,'Phoenix','Denver')
# shortest path using a* algorithm
astar(custom_graph,'Portland','New Orleans')
astar(custom_graph,'Phoenix','Denver')
# breadth-first sorting, list of possible paths from a starting node
bfs(custom_graph,'San Diego')
bfs(custom_graph,'Memphis')

