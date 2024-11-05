class Crop:
    def __init__(self, name, growth_time, water_needed, fertilizer_needed):
        self.name = name
        self.growth_time = growth_time  # in days
        self.water_needed = water_needed  # in liters
        self.fertilizer_needed = fertilizer_needed  # in kg
        self.days_grown = 0
        self.is_harvested = False

    def grow(self):
        if not self.is_harvested:
            self.days_grown += 1
            print(f"{self.name} has grown for {self.days_grown} days.")
            if self.days_grown >= self.growth_time:
                self.is_harvested = True
                print(f"{self.name} is ready for harvest!")
        else:
            print(f"{self.name} has already been harvested.")

    def water(self, amount):
        if amount >= self.water_needed:
            print(f"{self.name} has been watered successfully.")
        else:
            print(f"{self.name} needs more water. {self.water_needed} liters required.")

    def fertilize(self, amount):
        if amount >= self.fertilizer_needed:
            print(f"{self.name} has been fertilized successfully.")
        else:
            print(f"{self.name} needs more fertilizer. {self.fertilizer_needed} kg required.")


class Farm:
    
    def __init__(self):
        self.crops = []

    def add_crop(self, crop):
        self.crops.append(crop)
        print(f"{crop.name} has been added to the farm.")

    def manage_crops(self):
        for crop in self.crops:
            crop.grow()


# Example usage
if __name__ == "__main__":
    # Create a farm
    my_farm = Farm()

    # Add crops to the farm
    corn = Crop(name="Corn", growth_time=90, water_needed=200, fertilizer_needed=50)
    wheat = Crop(name="Wheat", growth_time=120, water_needed=150, fertilizer_needed=30)

    my_farm.add_crop(corn)
    my_farm.add_crop(wheat)

    # Simulate growing and managing crops
    for day in range(1, 121):  # Simulate for 120 days
        print(f"\nDay {day}:")
        my_farm.manage_crops()
        corn.water(250)  # Watering with more than needed
        corn.fertilize(40)  # Fertilizing with more than needed
        wheat.water(120)  # Watering with more than needed
        wheat.fertilize(40)  # Fertilizing with more than needed

        # Check if crops are ready for harvest
        if corn.is_harvested:
            print("Harvesting Corn!")
            break  # Stop simulation after harvesting corn
        if wheat.is_harvested:
            print("Harvesting Wheat!")
            break  # Stop simulation after harvesting wheat