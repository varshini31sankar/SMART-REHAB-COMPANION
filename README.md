Smart Rehabilitation Companion
 Overview

The Smart Rehabilitation Companion is an affordable, IoT-based wearable rehabilitation system designed to assist patients recovering from neurological and orthopedic conditions. It enables real-time monitoring, feedback, and remote supervision, improving therapy consistency and recovery outcomes.

This system integrates EMG, IMU, and force sensors to track muscle activity, motion, and grip strength, providing intelligent feedback to patients during rehabilitation exercises.

 Problem Statement

Patients undergoing rehabilitation often face:

Inconsistent therapy sessions
Lack of real-time feedback
Heavy dependence on physiotherapists

This leads to delayed recovery and improper exercise execution

 Proposed Solution

The system provides a wearable and interactive rehabilitation platform consisting of:

 Wearable Band → Tracks muscle activity (EMG) and motion (IMU)
 Interactive Smart Ball → Measures grip strength
 Master Control Board → Processes data and provides feedback
 Mobile App → Enables remote monitoring using IoT



⚙️ Key Features

✔ Real-time muscle activity monitoring
✔ Motion tracking using IMU
✔ Grip strength analysis
✔ Instant feedback via LCD, buzzer & LED
✔ Remote monitoring for physiotherapists
✔ Low-cost and scalable design

Working Principle
Sensors collect data:
EMG → Muscle activation
IMU → Movement tracking
Force sensor → Grip strength
Data is processed in microcontroller
System provides feedback:
LCD → “Doing Good” / “Try Again”
Buzzer → Incorrect movement alert
Data is sent to cloud for remote monitoring


📊 Results & Performance
 EMG accuracy: ~92% in detecting muscle activity
 IMU accuracy: ±3° motion tracking
Real-time feedback improves exercise correctness
⚠ Minor issues: noise, sensor drift, calibration sensitivity

Impact
Reduces hospital visits
Enables home-based rehabilitation
Helps physiotherapists monitor remotely
Improves patient engagement and recovery speed

Challenges
EMG signal noise
Sensor calibration issues
Data synchronization

Future Scope
AI-based adaptive therapy
Gamified rehabilitation system
Improved sensor accuracy
Better power optimization
Cloud-based analytics

 How to Run the Project
Connect all sensors to Raspberry Pi Pico W
Upload code using Arduino IDE
Power the system using Li-ion battery
Open serial monitor / LCD display for output
Connect to IoT platform for remote monitoring

🤝 Contributors
Varshini S (Biomedical Engineering, CIT Chennai)
Shankar M ( Electrical & Electronics Engineering ,CIT Chennai)
Hari Venketaesh( Electrical & Electronics Engineering, CIT Chennai)
Deepak Raj (Electronics & Communication Engineering, CIT Chennai)
