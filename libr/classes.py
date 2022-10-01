from dataclasses import dataclass
from collections import deque

MAX_CONTAINER_SIZE = 128


@dataclass
class Ship:
    """
        This is class of the Ship
    """
    displacement: int
    ship_type: list


@dataclass
class Plane:
    """
    This is class of the Plane
    """
    flying_range: int
    capacity: int


@dataclass
class Train:
    """
    This is class of the Train
    """
    wagons: int


@dataclass
class Transport:
    """
    This is general class for any Transport
    """
    speed: int
    distance: int
    transport_class: dataclass


@dataclass
class Container:
    """
    This is container class
    """
    max_size = MAX_CONTAINER_SIZE
    data = deque(maxlen=max_size)
    size = 0
