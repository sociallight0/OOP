"""
Object-Oriented Programming: Superhero Universe 🦸‍♂️🦸‍♀️
===========================================================
Assignment 1: Custom Class Design with Inheritance
Assignment 2: Polymorphism Challenge with move() methods
"""

from abc import ABC, abstractmethod
import random
from datetime import datetime

# =============================================================================
# ASSIGNMENT 1: DESIGN YOUR OWN CLASS - SUPERHERO THEME 🦸‍♂️
# =============================================================================

class Superhero:
    """
    Base Superhero class demonstrating OOP principles:
    - Encapsulation: Private attributes with getters/setters
    - Constructor: Initialize objects with unique values
    - Methods: Bring the class to life with actions
    """
    
    # Class variable (shared by all instances)
    total_heroes = 0
    
    def __init__(self, name, real_name, power_level=50, primary_power="Super Strength"):
        """
        Constructor to initialize each superhero with unique values.
        
        Args:
            name (str): Superhero name
            real_name (str): Secret identity
            power_level (int): Power strength (1-100)
            primary_power (str): Main superpower
        """
        # Public attributes
        self.name = name
        self.real_name = real_name
        self.primary_power = primary_power
        
        # Private attributes (encapsulation)
        self.__power_level = self._validate_power_level(power_level)
        self.__secret_identity = True
        self.__health = 100
        self.__experience_points = 0
        
        # Instance creation tracking
        Superhero.total_heroes += 1
        self.hero_id = Superhero.total_heroes
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"🦸‍♂️ New hero created: {self.name} (ID: {self.hero_id})")
    
    def _validate_power_level(self, power_level):
        """Private method to validate power level."""
        return max(1, min(100, power_level))  # Ensure 1-100 range
    
    # Getter and Setter methods (Encapsulation)
    def get_power_level(self):
        """Get the hero's power level."""
        return self.__power_level
    
    def set_power_level(self, new_level):
        """Set the hero's power level with validation."""
        self.__power_level = self._validate_power_level(new_level)
        print(f"⚡ {self.name}'s power level updated to {self.__power_level}")
    
    def get_health(self):
        """Get current health status."""
        return self.__health
    
    def reveal_identity(self):
        """Reveal the secret identity."""
        if self.__secret_identity:
            self.__secret_identity = False
            print(f"🎭 {self.name} reveals their identity as {self.real_name}!")
        else:
            print(f"🔍 {self.name}'s identity as {self.real_name} is already known.")
    
    def use_power(self):
        """Use the superhero's primary power."""
        if self.__health > 20:
            self.__health -= 10
            self.__experience_points += 5
            print(f"💥 {self.name} uses {self.primary_power}! (Health: {self.__health}, XP: {self.__experience_points})")
            return True
        else:
            print(f"😴 {self.name} is too tired to use powers. Need rest!")
            return False
    
    def rest(self):
        """Rest to recover health."""
        self.__health = min(100, self.__health + 30)
        print(f"😌 {self.name} rests and recovers. Health: {self.__health}")
    
    def move(self):
        """Base movement method (will be overridden by subclasses)."""
        print(f"🏃‍♂️ {self.name} moves with superhuman agility!")
    
    def display_stats(self):
        """Display hero statistics."""
        identity_status = "Secret" if self.__secret_identity else "Revealed"
        print(f"""
🦸‍♂️ === {self.name.upper()} STATS ===
Hero ID: {self.hero_id}
Real Name: {self.real_name}
Primary Power: {self.primary_power}
Power Level: {self.__power_level}/100
Health: {self.__health}/100
Experience: {self.__experience_points} XP
Identity: {identity_status}
Created: {self.created_date}
        """)
    
    def __str__(self):
        """String representation of the hero."""
        return f"{self.name} (Power: {self.__power_level})"
    
    @classmethod
    def get_hero_count(cls):
        """Class method to get total number of heroes."""
        return cls.total_heroes

# =============================================================================
# INHERITANCE LAYER - SPECIALIZED HERO CLASSES 🌟
# =============================================================================

class FlyingHero(Superhero):
    """Flying superheroes with aerial abilities."""
    
    def __init__(self, name, real_name, power_level=60, flight_speed=100):
        super().__init__(name, real_name, power_level, "Flight")
        self.flight_speed = flight_speed  # mph
        self.altitude = 0  # feet
    
    def move(self):
        """Override: Flying movement."""
        print(f"✈️ {self.name} soars through the sky at {self.flight_speed} mph!")
    
    def fly_up(self, feet=1000):
        """Fly to specific altitude."""
        self.altitude += feet
        print(f"🚁 {self.name} flies up to {self.altitude} feet!")
    
    def dive_attack(self):
        """Special flying attack."""
        if self.altitude > 500:
            self.altitude = 0
            print(f"🦅 {self.name} performs a devastating dive attack from the sky!")
            return self.use_power()
        else:
            print(f"⚠️ {self.name} needs more altitude for a dive attack!")
            return False

class SpeedsterHero(Superhero):
    """Super-speed heroes with time manipulation."""
    
    def __init__(self, name, real_name, power_level=70, top_speed=300):
        super().__init__(name, real_name, power_level, "Super Speed")
        self.top_speed = top_speed  # mph
        self.speed_force_energy = 100
    
    def move(self):
        """Override: Speed movement."""
        print(f"💨 {self.name} runs at {self.top_speed} mph, leaving lightning trails!")
    
    def time_travel(self):
        """Special speedster ability."""
        if self.speed_force_energy >= 50:
            self.speed_force_energy -= 50
            print(f"⚡ {self.name} vibrates through time using the Speed Force!")
            return True
        else:
            print(f"⚠️ {self.name} doesn't have enough Speed Force energy!")
            return False
    
    def speed_healing(self):
        """Accelerated healing."""
        if self.speed_force_energy >= 20:
            self.speed_force_energy -= 20
            health_gain = 40
            current_health = self.get_health()
            # Using a workaround since we can't directly modify private attributes
            self.rest()  # This adds 30 health
            self.rest()  # This adds another 30 health (but caps at 100)
            print(f"⚡ {self.name} uses speed healing! Energy: {self.speed_force_energy}")

class TechHero(Superhero):
    """Technology-based heroes with gadgets."""
    
    def __init__(self, name, real_name, power_level=55, tech_level=80):
        super().__init__(name, real_name, power_level, "Advanced Technology")
        self.tech_level = tech_level
        self.gadgets = ["Scanner", "Grappling Hook", "Energy Shield"]
        self.suit_power = 100
    
    def move(self):
        """Override: Tech-assisted movement."""
        print(f"🤖 {self.name} moves using advanced tech suit with {self.suit_power}% power!")
    
    def use_gadget(self, gadget_name=None):
        """Use a technological gadget."""
        if self.suit_power >= 15:
            if not gadget_name:
                gadget_name = random.choice(self.gadgets)
            
            self.suit_power -= 15
            print(f"🔧 {self.name} deploys {gadget_name}! Suit power: {self.suit_power}%")
            return self.use_power()
        else:
            print(f"🔋 {self.name}'s suit needs recharging!")
            return False
    
    def upgrade_tech(self):
        """Upgrade technology level."""
        self.tech_level = min(100, self.tech_level + 10)
        self.gadgets.append(f"Upgrade-{len(self.gadgets) + 1}")
        print(f"⬆️ {self.name} upgrades tech to level {self.tech_level}!")

# =============================================================================
# ASSIGNMENT 2: POLYMORPHISM CHALLENGE - VEHICLES 🚗✈️🚢
# =============================================================================

class Vehicle(ABC):
    """Abstract base class for all vehicles (Polymorphism example)."""
    
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.fuel = 100
    
    @abstractmethod
    def move(self):
        """Abstract method - each vehicle moves differently."""
        pass
    
    def refuel(self):
        """Common method for all vehicles."""
        self.fuel = 100
        print(f"⛽ {self.name} refueled to 100%!")

class Car(Vehicle):
    """Car vehicle class."""
    
    def __init__(self, name="Sports Car", max_speed=200):
        super().__init__(name, max_speed)
        self.wheels = 4
    
    def move(self):
        """Car-specific movement."""
        if self.fuel > 10:
            self.fuel -= 10
            print(f"🚗 {self.name} is driving on the road at {self.max_speed} mph! (Fuel: {self.fuel}%)")
        else:
            print(f"⛽ {self.name} is out of fuel!")

class Plane(Vehicle):
    """Airplane vehicle class."""
    
    def __init__(self, name="Fighter Jet", max_speed=1500):
        super().__init__(name, max_speed)
        self.altitude = 0
    
    def move(self):
        """Plane-specific movement."""
        if self.fuel > 20:
            self.fuel -= 20
            self.altitude = 30000
            print(f"✈️ {self.name} is flying through the sky at {self.max_speed} mph at {self.altitude} ft! (Fuel: {self.fuel}%)")
        else:
            print(f"⛽ {self.name} needs fuel to fly!")

class Boat(Vehicle):
    """Boat vehicle class."""
    
    def __init__(self, name="Speed Boat", max_speed=80):
        super().__init__(name, max_speed)
        self.in_water = True
    
    def move(self):
        """Boat-specific movement."""
        if self.fuel > 15:
            self.fuel -= 15
            print(f"🚢 {self.name} is sailing across the water at {self.max_speed} mph! (Fuel: {self.fuel}%)")
        else:
            print(f"⛽ {self.name} is stranded without fuel!")

class Motorcycle(Vehicle):
    """Motorcycle vehicle class."""
    
    def __init__(self, name="Racing Bike", max_speed=180):
        super().__init__(name, max_speed)
        self.wheels = 2
    
    def move(self):
        """Motorcycle-specific movement."""
        if self.fuel > 8:
            self.fuel -= 8
            print(f"🏍️ {self.name} roars down the highway at {self.max_speed} mph! (Fuel: {self.fuel}%)")
        else:
            print(f"⛽ {self.name} sputtered to a stop!")

# =============================================================================
# DEMONSTRATION PROGRAM 🎮
# =============================================================================

def demonstrate_polymorphism(entities):
    """Demonstrate polymorphism by calling move() on different objects."""
    print("\n🎭 === POLYMORPHISM DEMONSTRATION ===")
    print("Calling move() on different objects:")
    print("-" * 40)
    
    for entity in entities:
        entity.move()
        print()

def create_superhero_team():
    """Create a team of diverse superheroes."""
    print("\n🦸‍♂️ === CREATING SUPERHERO TEAM ===")
    
    heroes = [
        FlyingHero("Sky Guardian", "Sarah Johnson", 85, 250),
        SpeedsterHero("Lightning Bolt", "Barry Chen", 90, 400),
        TechHero("Iron Defender", "Tony Martinez", 80, 95),
        Superhero("Mystic Force", "Diana Prince", 75, "Magic")
    ]
    
    return heroes

def create_vehicle_fleet():
    """Create a fleet of different vehicles."""
    print("\n🚗 === CREATING VEHICLE FLEET ===")
    
    vehicles = [
        Car("Batmobile", 300),
        Plane("Invisible Jet", 2000),
        Boat("Aqua Cruiser", 120),
        Motorcycle("Thunder Bike", 250)
    ]
    
    return vehicles

def superhero_battle_simulation(heroes):
    """Simulate superhero activities."""
    print("\n⚔️ === SUPERHERO ACTIVITIES ===")
    
    for hero in heroes:
        print(f"\n--- {hero.name}'s Turn ---")
        hero.use_power()
        
        # Special abilities based on type
        if isinstance(hero, FlyingHero):
            hero.fly_up(2000)
            hero.dive_attack()
        elif isinstance(hero, SpeedsterHero):
            hero.time_travel()
        elif isinstance(hero, TechHero):
            hero.use_gadget()
        
        hero.rest()
        print()

def main():
    """Main program demonstrating OOP concepts."""
    print("🦸‍♂️✨ WELCOME TO THE SUPERHERO UNIVERSE ✨🦸‍♀️")
    print("=" * 60)
    print("Demonstrating OOP: Classes, Inheritance & Polymorphism")
    
    # Create superheroes (Assignment 1)
    heroes = create_superhero_team()
    
    # Create vehicles (Assignment 2)
    vehicles = create_vehicle_fleet()
    
    # Display initial stats
    print(f"\n📊 Total Heroes Created: {Superhero.get_hero_count()}")
    
    # Demonstrate polymorphism with heroes
    print("\n🦸‍♂️ HERO MOVEMENT DEMONSTRATION:")
    demonstrate_polymorphism(heroes)
    
    # Demonstrate polymorphism with vehicles  
    print("🚗 VEHICLE MOVEMENT DEMONSTRATION:")
    demonstrate_polymorphism(vehicles)
    
    # Interactive menu
    while True:
        print("\n" + "=" * 50)
        print("🎮 SUPERHERO UNIVERSE MENU")
        print("=" * 50)
        print("1. View Hero Stats")
        print("2. Superhero Activities")
        print("3. Vehicle Operations")
        print("4. Create New Hero")
        print("5. Demonstrate Polymorphism")
        print("6. Exit")
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                print("\n📊 === HERO STATISTICS ===")
                for hero in heroes:
                    hero.display_stats()
            
            elif choice == "2":
                superhero_battle_simulation(heroes)
            
            elif choice == "3":
                print("\n🚗 === VEHICLE OPERATIONS ===")
                for vehicle in vehicles:
                    vehicle.move()
                    if vehicle.fuel < 30:
                        vehicle.refuel()
                    print()
            
            elif choice == "4":
                name = input("Enter hero name: ").strip()
                real_name = input("Enter real name: ").strip()
                power = input("Enter primary power: ").strip()
                
                new_hero = Superhero(name, real_name, 60, power)
                heroes.append(new_hero)
                new_hero.display_stats()
            
            elif choice == "5":
                all_entities = heroes + vehicles
                demonstrate_polymorphism(all_entities)
            
            elif choice == "6":
                print("\n👋 Thank you for exploring the Superhero Universe!")
                print(f"Final hero count: {Superhero.get_hero_count()}")
                break
            
            else:
                print("❌ Invalid choice! Please enter 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
