
# 📟 Arduino LCD Voting System

An embedded voting system prototype developed using Arduino, push buttons, LEDs, and an I2C LCD display.  
The project simulates a digital voting machine capable of counting votes in real time and displaying results directly on the LCD interface.

## ⚙️ Features
- Real-time vote counting
- LCD result display
- Multiple candidate buttons
- Automatic winner detection
- Tie detection system
- Voting reset functionality
- LED feedback indicator
- Built-in debounce delay

## 🛠 Technologies
- Arduino C++
- Tinkercad
- I2C LCD Display
- Embedded Systems
- Digital Electronics

## 🔗 Online Simulation
<link>[https://www.tinkercad.com/things/3JEgzBsuaYO-trabalho-arthur-henrique-lcd?sharecode=Ul8mdHHD3B2uZ8mD3XpBoS6NvlNMdnEbQgAwsHI7-P0]

## 💽 Hardware Components
- Arduino Uno
- I2C LCD 16x2
- Push Buttons
- LED
- Resistors
- Breadboard
- Jumper Wires

## 🧠 System Logic
Each button represents a candidate (A, B, C, and D).  
When a button is pressed, the system:
1. Registers the vote
2. Updates the LCD display
3. Activates LED feedback

The reset button finalizes the election, checks the winner or tie condition, displays the result, and resets all votes.

## 📌 Purpose
This project was created to study embedded systems logic, digital input handling, LCD communication, and hardware interaction using Arduino.

## 📜 License
This project is licensed under the MIT License.
