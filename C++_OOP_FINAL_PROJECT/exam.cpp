// traffic_light_simulation.cpp
#include <iostream>
#include <cstring>
#include <thread>
#include <chrono>
using namespace std;

// Structure to define the state of the light
struct LightState {
    char color[10];
    int durationSec;
};

// Abstract class for polymorphism
class TrafficLight {
public:
    LightState* states;   // dynamic array of states
    int numStates;

    virtual void runCycle() = 0; // pure virtual function

    virtual ~TrafficLight() {
        delete[] states; // Free memory when object is destroyed
    }
};

// SimpleTrafficLight with 3 states: Red, Yellow, Green
class SimpleTrafficLight : public TrafficLight {
public:
    SimpleTrafficLight() {
        numStates = 3;
        states = new LightState[numStates];
        strcpy(states[0].color, "Red");
        states[0].durationSec = 3;
        strcpy(states[1].color, "Yellow");
        states[1].durationSec = 1;
        strcpy(states[2].color, "Green");
        states[2].durationSec = 2;
    }

    void runCycle() override {
        cout << "Running Simple Traffic Light Cycle:\n";
        for (int i = 0; i < numStates; i++) {
            cout << "Color: " << states[i].color << " | Duration: " << states[i].durationSec << " seconds" << endl;
            this_thread::sleep_for(chrono::seconds(states[i].durationSec));
        }
        cout << endl;
    }
};

// PedestrianTrafficLight with 4 states: Red, Yellow, Green, Walk
class PedestrianTrafficLight : public TrafficLight {
public:
    PedestrianTrafficLight() {
        numStates = 4;
        states = new LightState[numStates];
        strcpy(states[0].color, "Red");
        states[0].durationSec = 3;
        strcpy(states[1].color, "Yellow");
        states[1].durationSec = 1;
        strcpy(states[2].color, "Green");
        states[2].durationSec = 2;
        strcpy(states[3].color, "Walk");
        states[3].durationSec = 4;
    }

    void runCycle() override {
        cout << "Running Pedestrian Traffic Light Cycle:\n";
        for (int i = 0; i < numStates; i++) {
            cout << "Color: " << states[i].color << " | Duration: " << states[i].durationSec << " seconds" << endl;
            this_thread::sleep_for(chrono::seconds(states[i].durationSec));
        }
        cout << endl;
    }
};

// Controller list
class TrafficSystem {
public:
    TrafficLight** controllers;
    int count;

    TrafficSystem() {
        controllers = nullptr;
        count = 0;
    }

    // Add new controller
    void addController(TrafficLight* controller) {
        TrafficLight** newList = new TrafficLight*[count + 1];
        for (int i = 0; i < count; i++) {
            newList[i] = controllers[i];
        }
        newList[count] = controller;
        delete[] controllers;
        controllers = newList;
        count++;
    }

    // Remove controller by index
    void removeController(int index) {
        if (index < 0 || index >= count) return;
        TrafficLight** newList = new TrafficLight*[count - 1];
        for (int i = 0, j = 0; i < count; i++) {
            if (i != index) {
                newList[j++] = controllers[i];
            } else {
                delete controllers[i];
            }
        }
        delete[] controllers;
        controllers = newList;
        count--;
    }

    void runAllCycles() {
        for (int i = 0; i < count; i++) {
            controllers[i]->runCycle();
        }
    }

    ~TrafficSystem() {
        for (int i = 0; i < count; i++) {
            delete controllers[i];
        }
        delete[] controllers;
    }
};

int main() {
    TrafficSystem system;

    // Add 1 simple and 1 pedestrian traffic light
    system.addController(new SimpleTrafficLight());
    system.addController(new PedestrianTrafficLight());

    // Run cycles
    system.runAllCycles();

    // Remove the first traffic light
    system.removeController(0);

    // Run remaining cycle
    system.runAllCycles();

    return 0;
}
