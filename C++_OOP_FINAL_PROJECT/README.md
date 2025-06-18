# Traffic Light Simulation - C++ Project

## Project Description
This project simulates a set of traffic lights using C++ object-oriented programming concepts, particularly:
- Structs and dynamic memory
- Inheritance and polymorphism
- Abstract classes
- Pointer arithmetic

The simulation features two types of traffic lights:
- `SimpleTrafficLight` with three states (Red, Yellow, Green)
- `PedestrianTrafficLight` with four states (Red, Yellow, Green, Walk)

Each light cycles through its states for a specific number of seconds. The system dynamically manages multiple traffic light controllers.

---

## Project Structure

- `exam.cpp` — The main C++ program
- `README.md` — This documentation file

---

##  How It Works

1. **Struct Definition**
```cpp
struct LightState {
    char color[10];
    int durationSec;
};
```
Holds the color name and its display duration.

2. **Abstract Base Class**
```cpp
class TrafficLight {
    virtual void runCycle() = 0;
};
```
Defines the interface for any traffic light.

3. **Derived Classes**
- `SimpleTrafficLight`: Three states (Red, Yellow, Green)
- `PedestrianTrafficLight`: Four states (Red, Yellow, Green, Walk)

Each uses a dynamically allocated `LightState*` array.

4. **TrafficSystem Class**
Handles adding, removing, and running all traffic light controllers using dynamic arrays.

5. **Main Function**
- Adds one simple and one pedestrian traffic light
- Runs all cycles
- Removes one controller and runs again

---

## Console Output Example

```bash
Running Simple Traffic Light Cycle:
Color: Red | Duration: 3 seconds
Color: Yellow | Duration: 1 seconds
Color: Green | Duration: 2 seconds

Running Pedestrian Traffic Light Cycle:
Color: Red | Duration: 3 seconds
Color: Yellow | Duration: 1 seconds
Color: Green | Duration: 2 seconds
Color: Walk | Duration: 4 seconds
```

---

## ▶️ How to Compile and Run

### Requirements:
- C++11 or later

### Compile:
```bash
g++ exam.cpp -o traffic_sim
```


##  Notes
- All memory is dynamically allocated and safely deleted.
- You can extend the system by creating more light types derived from `TrafficLight`.
---

## 👨‍🎓 Created By
IHIMBAZWE Genevieve, 223014976
