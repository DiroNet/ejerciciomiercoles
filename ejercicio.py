from heapq import heappush, heappop

# Dirección: arriba, abajo, izquierda, derecha
dir = [(-1,0), (1,0), (0,-1), (0,1)]

class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.g = 0  # Costo desde el inicio
        self.h = 0  # Heurística (distancia Manhattan)
        self.f = 0  # f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Distancia Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_set = set()

    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)
        closed_set.add(current_node.position)

        # ¿Llegamos al destino?
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Invertir camino

        for move in dir:
            row = current_node.position[0] + move[0]
            col = current_node.position[1] + move[1]
            new_pos = (row, col)

            # Validar movimiento
            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                continue
            if maze[row][col] != 0:
                continue
            if new_pos in closed_set:
                continue

            neighbor = Node(current_node, new_pos)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            # Verificar si ya hay uno mejor en open_list
            skip = False
            for open_node in open_list:
                if neighbor.position == open_node.position and neighbor.g >= open_node.g:
                    skip = True
                    break
            if not skip:
                heappush(open_list, neighbor)

    return None  # No hay camino

# --- PRUEBA ---

maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = a_star(maze, start, end)

if path:
    print("Camino encontrado:")
    print(path)
else:
    print("No se encontró un camino.")
