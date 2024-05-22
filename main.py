import mapCreator
import searchAlgorithms
from graphClasses import Vertex, Edge, Graph

distance_file = open("results/distances.txt", "a")
loop_file = open("results/loops.txt", "a")

for i in range(0, 100):
    print(i)
    vertices = mapCreator.generate_vertices(100, 1000)
    direct_edges = mapCreator.generate_edges(vertices)
    random_edges = mapCreator.generate_edges(vertices, 10)

    # mapCreator.generate_image(vertices, direct_edges, [])

    direct_graph = Graph(vertices, direct_edges)
    random_graph = Graph(vertices, random_edges)

    direct_distance, direct_loop, direct_visited_vertices = searchAlgorithms.a_star(vertices, direct_graph)
    direct_visited_edges = mapCreator.generate_edges(direct_visited_vertices)

    random_distance, random_loop, random_visited_vertices = searchAlgorithms.a_star(vertices, random_graph)
    random_visited_edges = mapCreator.generate_edges(random_visited_vertices)

    enhanced_distance, enhanced_loop, enhanced_visited_vertices = searchAlgorithms.enhanced_star(vertices, random_graph)
    enhanced_visited_edges = mapCreator.generate_edges(random_visited_vertices)

    distance_file.write(f'{direct_distance},{random_distance},{enhanced_distance}\n')
    loop_file.write(f'{direct_loop},{random_loop},{enhanced_loop}\n')

    mapCreator.generate_image(vertices, random_edges, random_visited_edges, f'{i}_astar')
    mapCreator.generate_image(vertices, random_edges, enhanced_visited_edges, f'{i}_enhanced')

distance_file.close()
loop_file.close()