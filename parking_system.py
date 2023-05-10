class ParkingSystem:
    def __init__(self):
        self.available_spots = list(range(1, 41))
        self.assigned_spots = {}

    def assign_spot(self, vehicle_number):
        if not self.available_spots:
            print('No parking space is empty')  # Parking lot is full
            return None

        spot = self.available_spots.pop(0)
        self.assigned_spots[vehicle_number] = spot
        print(f'parking spot for vehicle Number: {vehicle_number} is :{spot}')
        return spot

    def get_spot(self, vehicle_number):
        spot = self.assigned_spots[vehicle_number]
        if vehicle_number not in self.assigned_spots:
            print(f'There is no vehicle with this :{vehicle_number} Number,Please check the number and try again ')
            return None  # Vehicle not found
        if int(spot) < 20:
            print(f'"level":A,"spot":{self.assigned_spots[vehicle_number]}')
        else:
            print(f'"level":B,"spot":{self.assigned_spots[vehicle_number]}')
        return f'"level":b,"spot":{self.assigned_spots[vehicle_number]}'
