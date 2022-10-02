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


def allowed_ship_types() -> list:
    """
    This function returns list of the allowed ship types
    :return: list of allowed ship types
    """
    return ["liner", "tug", "tanker", "cruiser", "caravelle"]


def create_ship_class(speed, distance, displacement, types):
    """
    This function parses data and creates Ship class
    :param speed: int: speed transport
    :param distance: int: distance transport
    :param displacement: int: displacement ship
    :param types: str: ship type
    :return: Ship class
    """
    successful_parsed_types = []
    types = types.split("+")
    for ship_type in types:
        if ship_type in allowed_ship_types():
            successful_parsed_types.append(ship_type)
    if len(successful_parsed_types) == 0:
        raise ValueError

    return Transport(speed=int(speed), distance=int(distance),
                     transport_class=Ship(displacement=int(displacement), ship_type=successful_parsed_types))


def create_train_class(speed, distance, wagons):
    """
    This function parses data and creates Train class
    :param speed: int: speed transport
    :param distance: int: distance transport
    :param wagons: int: wagons Train
    :return: Train class
    """

    return Transport(speed=int(speed), distance=int(distance), transport_class=Train(wagons=wagons))


def create_plane_class(speed, distance, flying_range, capacity):
    """
    This function parses data and creates Plane class
    :param speed: int: speed transport
    :param distance: int: distance transport
    :param flying_range: int: flying_range plane
    :param capacity: int: capacity plane
    :return: Plane class
    """

    return Transport(speed=int(speed), distance=int(distance),
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
               f"Wagons: {transport.transport_class.wagons}."
    elif type(transport.transport_class) == Plane:
        return f"Type: plane.\t\tSpeed: {transport.speed}.\tDistance: {transport.distance}. \t" + \
               f"Flying_range: {transport.transport_class.flying_range}.\tCapacity: {transport.transport_class.capacity}"
    elif type(transport.transport_class) == Ship:
        return f"Type: ship.\t\tSpeed: {transport.speed}.\tDistance: {transport.distance}. \t" + \
               f"Displacement: {transport.transport_class.displacement}.\t" \
               f"Ship_type: {', '.join(transport.transport_class.ship_type)}"


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

    print_filtered_data(container)


def filter_data(container, transport_class):
    """
    Filter transport by given class
    :param container: container
    :param transport_class: class of the transport
    :return: list of transport filtered by given class
    """
    return [transport for transport in container.data if type(transport.transport_class) is transport_class]


def print_filtered_data(container):
    """
    This method prints data filtered by transport class
    :param container: container
    :return: None
    """
    for transport_class in [Plane]:
        print(f"\nFilter by {transport_class.__name__}:")
        filtered_data = filter_data(container, transport_class)

        for transport in filtered_data:
            print(string_conversion(transport))


def parse_line_and_create_transport_class(line):
    """
    This function parses data from line of file and returns transport class
    :param line: str: file line
    :return: transport object
    """
    line = line.replace("\n", "").split()

    if len(line) == 4:
        description = {
            "type": line[0].lower(),
            "speed": int(line[1].lower()),
            "distance": int(line[2].lower()),
            "wagons": int(line[3].lower())
        }
        # Parse data for Train
        transport = create_train_class(description["speed"], description["distance"], description["wagons"])

        return transport

    if len(line) == 5:

        if line[0] == "Ship":

            description = {
                "type": line[0].lower(),
                "speed": int(line[1].lower()),
                "distance": int(line[2].lower()),
                "displacement": int(line[3].lower()),
                "ship_type": line[4].lower()
            }
            # Parse data for Train
            transport = create_ship_class(description["speed"], description["distance"], description["displacement"],
                                          description["ship_type"])

            return transport

        else:

            description = {
                "type": line[0].lower(),
                "speed": int(line[1].lower()),
                "distance": int(line[2].lower()),
                "flying_range": int(line[3].lower()),
                "capacity": int(line[4].lower())
            }
            # Parse data for Train
            transport = create_plane_class(description["speed"], description["distance"], description["flying_range"],
                                           description["capacity"])

            return transport

    else:
        raise ValueError
