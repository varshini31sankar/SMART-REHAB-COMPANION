from machine import ADC, Pin, I2C
import time
import utime
from imu import MPU6050
import network
import BlynkLib

# WiFi Setup (Optional, but not using Blynk)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Redmi 10 Prime", "123456789")

led = Pin(15, Pin.OUT)

# Connect to WiFi
BLYNK_AUTH = "TMPL3bg2GBqqV"
blynk = BlynkLib.Blynk(BLYNK_AUTH)

wait = 30
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    led.value(0)  # Turn the LED off
else:
    print('Connected')
    ip = wlan.ifconfig()[0]
    print('IP: ', ip)

# Force Sensor Setup (GP28/ADC2)
FORCE_SENSOR_PIN = 28
force_sensor = ADC(Pin(FORCE_SENSOR_PIN))

# EMG Sensor Setup (GP26/ADC0)
EMG_SENSOR_PIN = 26
emg = ADC(Pin(EMG_SENSOR_PIN))

# I2C for IMU (I2C0: GP0=SDA, GP1=SCL)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

led.value(0)

while True:
    # Read IMU Data
    ax = round(imu.accel.x, 2)
    ay = round(imu.accel.y, 2)
    az = round(imu.accel.z, 2)
    gx = round(imu.gyro.x)
    gy = round(imu.gyro.y)
    gz = round(imu.gyro.z)

    print(f"ax: {ax}, ay: {ay}, az: {az}, gx: {gx}, gy: {gy}, gz: {gz}")

    # Read Force Sensor Data
    analog_reading = force_sensor.read_u16() // 64
    print("Force sensor reading =", analog_reading)

    if analog_reading < 10:
        print(" -> no pressure")
    elif analog_reading < 150:
        print(" -> light grip")
    elif analog_reading < 350:
        print(" -> medium grip")
    elif analog_reading < 650:
        print(" -> strong grip-RELAX")

    if analog_reading > 700:
        led.value(1)
    else:
        led.value(0)

    # Read EMG Sensor Data
    EMG_value = emg.read_u16()

    # Determine feedback message
    if EMG_value <= 16295:
        feedback = "NO MOVEMENT"
    elif EMG_value <= 32590:
        feedback = "GOING GOOD!"
    elif EMG_value <= 48885:
        feedback = "VERY PERFECT"
    elif EMG_value <= 65180:
        feedback = "STRESS - RELAX"
    else:
        feedback = "STOP DOING"

    print(f"EMG: {EMG_value} -> {feedback}")

    # Send data to Blynk
    blynk.virtual_write(0, EMG_value)
    blynk.virtual_write(1, analog_reading)
    blynk.virtual_write(2, gx)
    blynk.virtual_write(3, gy)
    blynk.virtual_write(4, gz)
    blynk.virtual_write(5, ax)

    time.sleep(0.5)