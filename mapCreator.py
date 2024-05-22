import math
from graphClasses import Vertex, Edge, Graph
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

image_height = 1000
image_width = 1000


def generate_vertices(vertex_count, map_size):
    vertices = [Vertex(0, 0, 0)]
    # total_distance = round(math.sqrt(2*pow(map_size, 2)))
    # distance_change = total_distance/vertex_count
    for i in range(1, vertex_count - 1):
        random_x = random.randint(0, map_size - 1)
        random_y = random.randint(0, map_size - 1)
        vertices.append(Vertex(i, random_x, random_y))
    vertices.append(Vertex(vertex_count - 1, map_size - 1, map_size - 1))
    vertices.sort(key=distance_to_start)
    return vertices


def generate_edges(vertices, random_edge_count=0):
    edges = []
    for i in range(len(vertices) - 1):
        vertex1 = vertices[i]
        vertex2 = vertices[i + 1]
        edge = Edge(vertex1, vertex2, distance(vertex1, vertex2))
        edges.append(edge)

    for i in range(random_edge_count):
        vertex1 = random.choice(vertices)
        vertex2 = random.choice([x for x in vertices if x != vertex1])
        if distance_to_end(vertex1) > distance_to_end(vertex2):
            edge = Edge(vertex1, vertex2, distance(vertex1, vertex2))
        else:
            edge = Edge(vertex2, vertex1, distance(vertex1, vertex2))
        edges.append(edge)
    return edges


def distance_to_start(vertex):
    return math.sqrt(pow(vertex.x, 2) + pow(vertex.y, 2))


def distance_to_end(vertex):
    return math.sqrt(pow(999 - vertex.x, 2) + pow(999 - vertex.y, 2))


def distance(vertex1, vertex2):
    return math.sqrt(pow(vertex1.x - vertex2.x, 2) + pow(vertex1.y - vertex2.y, 2))


def generate_image(vertices, edges, visited_edges, file_name):
    # Radius of circle
    radius = 5

    # Blue color in BGR
    vertex_color = (0, 0, 255)

    # Red color in BGR
    edge_color = (255, 63, 63)

    # White color in BGR
    visited_color = (255, 255, 255)

    map_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    for edge in edges:
        # Points
        start_point = (edge.vertex1.x, edge.vertex1.y)
        end_point = (edge.vertex2.x, edge.vertex2.y)
        cv2.line(map_image, start_point, end_point, edge_color, 5)

    for edge in visited_edges:
        # Points
        start_point = (edge.vertex1.x, edge.vertex1.y)
        end_point = (edge.vertex2.x, edge.vertex2.y)
        cv2.line(map_image, start_point, end_point, visited_color, 2)

    for vertex in vertices:
        # Center coordinates
        center_coordinates = (vertex.x, vertex.y)
        cv2.circle(map_image, center_coordinates, radius, vertex_color, -1)

    # my_image[random_int-2:random_int+2, random_int-2:random_int+2] = [255, 255, 255]
    # plt.imshow(map_image)
    # plt.show()
    cv2.imwrite(f'output/{file_name}.png', map_image)
