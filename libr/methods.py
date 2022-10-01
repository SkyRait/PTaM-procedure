from libr.classes import *


def create_container() -> Container:
    """
    This function creates transport container
    :return: transport container
    """
    clear(Container())
    return Container()


def add(container: Container, transport) -> None:
    """
    This function adds transport to container
    :param container: Container: transport's container;
    :param transport: transport objects
    :return: None
    """
    # Check for container is not full
    if container.size >= container.max_size:
        raise BufferError

    # Add data
    container.data.append(transport)
    container.size += 1


def create_train_class(speed, distance, weight_now, wagons):
    """
    This function parses data and creates Train class
    :param speed: int: speed transport
    :param distance: int: distance transport
    :param weight_now: int: weight_now transport
    :param wagons: int: wagons Train
    :return: Train class
    """

    return Transport(speed=int(speed), distance=int(distance), weight_now=int(weight_now),
                     transport_class=Train(wagons=wagons))


def create_plane_class(speed, distance, weight_now, flying_range, capacity):
    """
    This function parses data and creates Plane class
    :param speed: int: speed transport
    :param distance: int: distance transport
    :param weight_now: int: weight_now transport
    :param flying_range: int: flying_range plane
    :param capacity: int: capacity plane
    :return: Plane class
    """

    return Transport(speed=int(speed), distance=int(distance), weight_now=int(weight_now),
                     transport_class=Plane(flying_range=int(flying_range), capacity=int(capacity)))


def clear(container: Container) -> None:
    """
    This function clears container
    :param container: container to clear
    :return: None
    """
    container.size = 0
    container.data.clear()


def write_file(container: Container, file_out: str) -> None:
    """
    This function prints container tmp
    :param container: container with tmp
    :param file_out: path to output file
    :return: None
    """
    with open(file_out, "w") as file:
        print(f"Transport count: {container.size}.", end=" ")
        file.write(f"Transport count: {container.size}. ")
        if container.size > 0:
            print("Transport:")
            file.write("Transport:\n")
        else:
            print()

        for i in range(container.size):
            transport = string_conversion(container.data[i])
            file.write(f"{i + 1}: {transport}\n")
            print(f"{i + 1}: {transport}")


def string_conversion(transport) -> str:
    """
    This function converses Transport object to string
    :param transport: Train or Plane object to converse
    :return: conversed to string Transport object
    """
    if type(transport.transport_class) == Train:
        return f"Type: train.\t\tSpeed: {transport.speed}.\tDistance: {transport.distance}. \t" + \
               f"Weight_now: {transport.weight_now}.\tWagons: {transport.transport_class.wagons}."
    elif type(transport.transport_class) == Plane:
        return f"Type: plane.\t\tSpeed: {transport.speed}.\tDistance: {transport.distance}. \t" + \
               f"Weight_now: {transport.weight_now}.\tFlying_range: {transport.transport_class.flying_range}.\t" \
               f"Capacity: {transport.transport_class.capacity}"


def read_file(container: Container, file_in: str) -> None:
    """
    This function reads input file and puts data to container
    :param container: container to save tmp
    :param file_in: path to the file
    :return: None
    """

    with open(file_in) as file:
        lines = file.readlines()
        for line in lines:
            transport = parse_line_and_create_transport_class(line)
            add(container, transport)


def parse_line_and_create_transport_class(line):
    """
    This function parses data from line of file and returns transport class
    :param line: str: file line
    :return: transport object
    """
    line = line.replace("\n", "").split()

    if len(line) == 5:
        description = {
            "type": line[0].lower(),
            "speed": int(line[1].lower()),
            "distance": int(line[2].lower()),
            "weight_now": int(line[3].lower()),
            "wagons": int(line[4].lower())
        }
        # Parse data for Train
        transport = create_train_class(description["speed"], description["distance"], description["weight_now"],
                                       description["wagons"])

        return transport
    if len(line) == 6:
        description = {
            "type": line[0].lower(),
            "speed": int(line[1].lower()),
            "distance": int(line[2].lower()),
            "weight_now": int(line[3].lower()),
            "flying_range": int(line[4].lower()),
            "capacity": int(line[5].lower())
        }
        # Parse data for Plane
        transport = create_plane_class(description["speed"], description["distance"], description["weight_now"],
                                       description["flying_range"], description["capacity"])

        return transport

    else:
        raise ValueError
