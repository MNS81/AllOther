from math import pi
sphere_volume = lambda r: pi * r ** 2                                       # площадь круга
cylinder_capacity = lambda r, h: pi * r ** 2 * h                            # объем цилиндра
cylinder_surface_area = lambda r, h: 2 * pi * r * (r + h)                   # площадь поверхности цилиндра
sphere_capacity = lambda r: 4 / 3 * pi * r ** 3                             # объем сферы
sphere_surface_area = lambda r: 4 * pi * r ** 2                             # площадь сферы
parallelepiped_volume = lambda x, y, z: x * y * z                           # объем параллелепипеда
parallelepiped_surface_area = lambda x, y, z: 2 * (x * y + y * z + x * z)   # площадь поверхности паралелепипеда
parallelepiped_edges_sum = lambda x, y, z: 4 * (x + y + z)                  # сумма всех ребер паралелепипеда

