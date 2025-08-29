# OOP Superhero Universe 🦸‍♂️🦸‍♀️

A comprehensive Python program demonstrating Object-Oriented Programming concepts through an interactive superhero-themed application. This program combines both assignments into an engaging learning experience!

## 🎯 Program Overview

This program demonstrates all major OOP concepts:
- **Classes and Objects** - Custom superhero and vehicle classes
- **Inheritance** - Specialized hero types extending base class
- **Polymorphism** - Same method names with different behaviors
- **Encapsulation** - Private attributes with getter/setter methods
- **Abstraction** - Abstract base classes for vehicle types

## 🏗️ Assignment 1: Custom Class Design

### Base Superhero Class Features
- **Constructor**: Initialize heroes with unique attributes
- **Encapsulation**: Private attributes (`__power_level`, `__health`, `__secret_identity`)
- **Methods**: Bring heroes to life with actions and abilities
- **Class Variables**: Track total hero count across all instances

### Core Attributes
```python
# Public Attributes
- name: Hero name
- real_name: Secret identity
- primary_power: Main superpower

# Private Attributes (Encapsulated)
- __power_level: Strength rating (1-100)
- __health: Current health status
- __secret_identity: Identity revelation status
- __experience_points: Gained through power usage
```

### Key Methods
- `use_power()` - Utilize superhero abilities
- `rest()` - Recover health and energy
- `reveal_identity()` - Expose secret identity
- `display_stats()` - Show complete hero information
- `move()` - Base movement (overridden by subclasses)

## 🌟 Inheritance Layer - Specialized Heroes

### FlyingHero Class
```python
class FlyingHero(Superhero):
    - flight_speed: Aerial velocity
    - altitude: Current height
    - fly_up(): Gain altitude
    - dive_attack(): Special aerial attack
    - move(): "Soars through the sky" ✈️
```

### SpeedsterHero Class
```python
class SpeedsterHero(Superhero):
    - top_speed: Maximum running speed
    - speed_force_energy: Special energy source
    - time_travel(): Manipulate time
    - speed_healing(): Accelerated recovery
    - move(): "Runs leaving lightning trails" 💨
```

### TechHero Class
```python
class TechHero(Superhero):
    - tech_level: Technology advancement
    - gadgets: Available equipment list
    - suit_power: Armor energy level
    - use_gadget(): Deploy technology
    - upgrade_tech(): Improve capabilities
    - move(): "Moves using advanced tech suit" 🤖
```

## 🎭 Assignment 2: Polymorphism Challenge

### Vehicle Base Class (Abstract)
```python
class Vehicle(ABC):
    @abstractmethod
    def move(self):  # Must be implemented by subclasses
        pass
```

### Vehicle Types with Unique Movement

| Vehicle Class | move() Behavior | Special Feature |
|---------------|----------------|-----------------|
| **Car** 🚗 | "Driving on the road" | 4 wheels, road travel |
| **Plane** ✈️ | "Flying through the sky" | Altitude tracking |
| **Boat** 🚢 | "Sailing across water" | Water navigation |
| **Motorcycle** 🏍️ | "Roars down highway" | 2 wheels, speed focused |

### Polymorphism Demonstration
```python
# Same method call, different behaviors
for entity in [car, plane, boat, motorcycle]:
    entity.move()  # Each prints different movement style!

# Output:
# 🚗 Sports Car is driving on the road at 200 mph!
# ✈️ Fighter Jet is flying through the sky at 1500 mph!
# 🚢 Speed Boat is sailing across the water at 80 mph!
# 🏍️ Racing Bike roars down the highway at 180 mph!
```

## 🚀 Program Features

### Interactive Menu System
1. **View Hero Stats** - Display detailed hero information
2. **Superhero Activities** - Simulate power usage and battles
3. **Vehicle Operations** - Demonstrate vehicle movement
4. **Create New Hero** - Add custom heroes to the roster
5. **Demonstrate Polymorphism** - Show same method, different behaviors
6. **Exit** - Close the program

### Advanced OOP Concepts Demonstrated

#### Encapsulation Examples
```python
# Private attributes protected from direct access
hero.__power_level = 999  # Won't work!
hero.set_power_level(85)  # Correct way with validation
```

#### Inheritance Examples
```python
# Base class method
superhero.move()  # "Moves with superhuman agility"

# Overridden in subclasses
flying_hero.move()    # "Soars through the sky"
speedster_hero.move() # "Runs leaving lightning trails"
```

#### Polymorphism Examples
```python
# Same interface, different implementations
heroes = [FlyingHero(), SpeedsterHero(), TechHero()]
for hero in heroes:
    hero.move()  # Each hero moves differently!
```

## 📊 Sample Program Output

### Hero Creation
```
🦸‍♂️ New hero created: Sky Guardian (ID: 1)
🦸‍♂️ New hero created: Lightning Bolt (ID: 2)
🦸‍♂️ New hero created: Iron Defender (ID: 3)
```

### Polymorphism Demonstration
```
🎭 === POLYMORPHISM DEMONSTRATION ===
Calling move() on different objects:
----------------------------------------
✈️ Sky Guardian soars through the sky at 250 mph!
💨 Lightning Bolt runs at 400 mph, leaving lightning trails!
🤖 Iron Defender moves using advanced tech suit with 100% power!
🚗 Batmobile is driving on the road at 300 mph! (Fuel: 90%)
```

### Hero Statistics
```
🦸‍♂️ === SKY GUARDIAN STATS ===
Hero ID: 1
Real Name: Sarah Johnson
Primary Power: Flight
Power Level: 85/100
Health: 100/100
Experience: 15 XP
Identity: Secret
Created: 2025-08-30 14:30:15
```

## 🎓 Learning Outcomes

By running this program, you'll master:

### Core OOP Principles
✅ **Class Design** - Creating meaningful class structures  
✅ **Object Creation** - Using constructors effectively  
✅ **Encapsulation** - Protecting data with private attributes  
✅ **Inheritance** - Extending base classes with specialization  
✅ **Polymorphism** - Same interface, different implementations  

### Advanced Concepts
✅ **Abstract Base Classes** - Defining interfaces  
✅ **Method Overriding** - Customizing inherited behavior  
✅ **Class vs Instance Variables** - Understanding scope  
✅ **Property Management** - Getter/setter methods  
✅ **Multiple Inheritance Patterns** - Complex class hierarchies  

### Programming Best Practices
✅ **Code Organization** - Logical class structure  
✅ **Documentation** - Clear method descriptions  
✅ **Error Handling** - Robust input validation  
✅ **User Interface Design** - Interactive menu systems  
✅ **Data Validation** - Input sanitization and bounds checking  

## 🛠️ Technical Requirements

- **Python Version**: 3.6 or higher
- **Modules Used**: `abc`, `random`, `datetime` (all built-in)
- **No external dependencies required**

## 🎮 How to Run

1. Save as `superhero_oop.py`
2. Run: `python superhero_oop.py`
3. Explore the interactive menu options
4. Create heroes, demonstrate polymorphism, and learn OOP!

## 🏆 Advanced Features

### Class Methods and Static Methods
```python
@classmethod
def get_hero_count(cls):
    return cls.total_heroes
```

### String Representation
```python
def __str__(self):
    return f"{self.name} (Power: {self.__power_level})"
```

### Type Checking with isinstance()
```python
if isinstance(hero, FlyingHero):
    hero.fly_up(2000)  # Only flying heroes can do this
```

## 🎉 Success Indicators

After completing this program, you'll have demonstrated:

🎯 **Custom Class Creation** with unique attributes and methods  
🎯 **Constructor Usage** for object initialization  
🎯 **Inheritance Implementation** with specialized subclasses  
🎯 **Polymorphism Mastery** through method overriding  
🎯 **Encapsulation Skills** with private attributes and validation  
🎯 **Interactive Program Design** with user-friendly interfaces  

This comprehensive program brings together all essential OOP concepts in an engaging, practical application that's both educational and entertaining! 🌟
