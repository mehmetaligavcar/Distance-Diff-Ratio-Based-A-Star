import math
import copy
import sys


def a_star(vertices, graph):
    loop_counter = 0
    current_point = copy.deepcopy(vertices[0])
    current_distance = 0
    end_point = copy.deepcopy(vertices[len(vertices) - 1])
    visited = [copy.deepcopy(current_point)]
    queue = []
    while not (current_point.id == end_point.id and is_it_shortest_path(current_distance, queue)):
        for edge in graph.get(current_point):
            queue.append({
                "vertex": edge.vertex2,
                "so_far_distance": current_distance + edge.weight,
                "so_far_visited": visited,
                "estimated_distance": current_distance + edge.weight + distance_to_end(edge.vertex2)
            })
        queue.sort(key=estimated_distance_of_queue_element)
        current_point = copy.deepcopy(queue[0]["vertex"])
        current_distance = copy.deepcopy(queue[0]["so_far_distance"])
        visited = copy.deepcopy((queue[0]["so_far_visited"]))
        queue.pop(0)
        while is_visited(current_point, visited):
            current_point = copy.deepcopy(queue[0]["vertex"])
            current_distance = copy.deepcopy(queue[0]["so_far_distance"])
            visited = copy.deepcopy((queue[0]["so_far_visited"]))
            queue.pop(0)
        visited.append(current_point)
        loop_counter += 1
    return current_distance, loop_counter, visited


def enhanced_star(vertices, graph):
    loop_counter = 0
    current_point = copy.deepcopy(vertices[0])
    current_distance = 0
    end_point = copy.deepcopy(vertices[len(vertices) - 1])
    visited = [copy.deepcopy(current_point)]
    queue = []
    while not (current_point.id == end_point.id and is_it_shortest_path(current_distance, queue)):
        for edge in graph.get(current_point):
            queue.append({
                "vertex": edge.vertex2,
                "so_far_distance": current_distance + edge.weight,
                "so_far_visited": visited,
                "estimated_distance": current_distance + estimated_remaining_distance(edge)
            })
        queue.sort(key=estimated_distance_of_queue_element)
        current_point = copy.deepcopy(queue[0]["vertex"])
        current_distance = copy.deepcopy(queue[0]["so_far_distance"])
        visited = copy.deepcopy((queue[0]["so_far_visited"]))
        queue.pop(0)
        while is_visited(current_point, visited):
            current_point = copy.deepcopy(queue[0]["vertex"])
            current_distance = copy.deepcopy(queue[0]["so_far_distance"])
            visited = copy.deepcopy((queue[0]["so_far_visited"]))
            queue.pop(0)
        visited.append(current_point)
        loop_counter += 1
    return current_distance, loop_counter, visited


def is_visited(vertex, visited):
    for visited_vertex in visited:
        if vertex.id == visited_vertex.id:
            return True
    return False


def distance_to_end(vertex):
    return math.sqrt(pow(999 - vertex.x, 2) + pow(999 - vertex.y, 2))


def estimated_distance_of_queue_element(element):
    return element["estimated_distance"]


def estimated_remaining_distance(edge):
    if distance_to_end(edge.vertex1) > distance_to_end(edge.vertex2):
        return edge.weight * distance_to_end(edge.vertex1) / (
                distance_to_end(edge.vertex1) - distance_to_end(edge.vertex2))
    else:
        return edge.weight + distance_to_end(edge.vertex2)


def is_it_shortest_path(current_distance, queue):
    queue.sort(key=estimated_distance_of_queue_element)
    if len(queue) == 0:
        return True
    if current_distance < queue[0]["estimated_distance"]:
        return True
    return False


def print_vertex_array(array):
    str = ""
    for vertex in array:
        str += vertex.__str__() + " "
    print(str)
