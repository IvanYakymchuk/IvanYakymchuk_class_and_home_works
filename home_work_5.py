"""18.7"""

class Material:
    def __init__(self, material_type, material_name, naturalness):
        self.material_type = material_type
        self.material_name = material_name
        self.naturalness = naturalness

    def create_material(self):
        print("Creating material...")

    def display_material(self):
        print(f"Material Type: {self.material_type}")
        print(f"Material Name: {self.material_name}")
        print(f"Naturalness: {self.naturalness}")


class FunctionalAccessory:
    def __init__(self, accessory_name, age_recommendations):
        self.accessory_name = accessory_name
        self.age_recommendations = age_recommendations

    def create_accessory(self):
        print("Creating functional accessory...")

    def display_accessory(self):
        print(f"Accessory Name: {self.accessory_name}")
        print(f"Age Recommendations: {self.age_recommendations}")


class Furniture(Material, FunctionalAccessory):
    def __init__(self, furniture_type, furniture_name, material_type, material_name, naturalness,
                 accessory_name, age_recommendations):
        Material.__init__(self, material_type, material_name, naturalness)
        FunctionalAccessory.__init__(self, accessory_name, age_recommendations)
        self.furniture_type = furniture_type
        self.furniture_name = furniture_name

    def create_furniture(self):
        print("Creating furniture...")

    def display_furniture(self):
        print("Furniture Details:")
        Material.display_material(self)
        FunctionalAccessory.display_accessory(self)
        print(f"Furniture Type: {self.furniture_type}")
        print(f"Furniture Name: {self.furniture_name}")


# Приклад використання класів
material_instance = Material("Wood", "Oak", "Natural")
material_instance.create_material()
material_instance.display_material()
print("\n" + "=" * 30 + "\n")

accessory_instance = FunctionalAccessory("Child Chair", "0-3 years")
accessory_instance.create_accessory()
accessory_instance.display_accessory()
print("\n" + "=" * 30 + "\n")

furniture_instance = Furniture("Table", "Dining Table", "Wood", "Oak", "Natural", "Child Chair", "0-3 years")
furniture_instance.create_furniture()
furniture_instance.display_furniture()
