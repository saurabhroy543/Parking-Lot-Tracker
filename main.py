from parking_system import ParkingSystem


def main():
    parking_lot = ParkingSystem()

    while True:
        command = input("Enter a command (assign, get, quit): ")
        if command == "assign":
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.assign_spot(vehicle_number)
        elif command == "get":
            vehicle_number = input("Enter vehicle number: ")
            parking_lot.get_spot(vehicle_number)
        elif command == "quit":
            break
        else:
            print("Invalid command")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

