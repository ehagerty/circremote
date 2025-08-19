# SPDX-FileCopyrightText: 2025 John Romkey
#
# SPDX-License-Identifier: CC0-1.0

import time
import board
import adafruit_bno055
import sys

# Initialize the BNO055 sensor
i2c = board.I2C({{ scl }}, {{ sda }})
sensor = adafruit_bno055.BNO055_I2C(i2c, address={{ address }})

print("BNO055 9-Axis Absolute Orientation Sensor")
print("=" * 50)

# Check if sensor is detected
if not sensor:
    print("Error: BNO055 sensor not found!")
    print("Please check your wiring and I2C address.")
    sys.exit(1)

print(f"✅ BNO055 sensor detected at address 0x{{ address:02X}}")
print()

def get_calibration_status():
    """Get and display calibration status for all sensors."""
    cal_status = sensor.calibration_status
    cal_sys = (cal_status >> 6) & 0x03
    cal_gyro = (cal_status >> 4) & 0x03
    cal_accel = (cal_status >> 2) & 0x03
    cal_mag = cal_status & 0x03
    
    print("Calibration Status:")
    print(f"  System: {cal_sys}/3")
    print(f"  Gyroscope: {cal_gyro}/3")
    print(f"  Accelerometer: {cal_accel}/3")
    print(f"  Magnetometer: {cal_mag}/3")
    print()

def get_operation_mode():
    """Get and display current operation mode."""
    mode = sensor.mode
    mode_names = {
        0x00: "CONFIG",
        0x01: "ACCONLY",
        0x02: "MAGONLY", 
        0x03: "GYRONLY",
        0x04: "ACCMAG",
        0x05: "ACCGYRO",
        0x06: "MAGGYRO",
        0x07: "AMG",
        0x08: "IMU",
        0x09: "COMPASS",
        0x0A: "M4G",
        0x0B: "NDOF_FMC_OFF",
        0x0C: "NDOF"
    }
    mode_name = mode_names.get(mode, f"UNKNOWN (0x{mode:02X})")
    print(f"Operation Mode: {mode_name}")
    print()

def classify_movement(accel):
    """Classify movement based on accelerometer data."""
    x, y, z = accel
    magnitude = (x**2 + y**2 + z**2)**0.5
    
    if magnitude < 8.0:
        return "Stationary"
    elif magnitude < 12.0:
        return "Gentle Movement"
    elif magnitude < 16.0:
        return "Active Movement"
    else:
        return "Rapid Movement"

def classify_orientation(euler):
    """Classify orientation based on Euler angles."""
    heading, roll, pitch = euler
    
    # Normalize heading to 0-360
    heading = heading % 360
    
    # Determine cardinal direction
    if 315 <= heading or heading < 45:
        direction = "North"
    elif 45 <= heading < 135:
        direction = "East"
    elif 135 <= heading < 225:
        direction = "South"
    else:
        direction = "West"
    
    # Determine tilt
    if abs(roll) < 10 and abs(pitch) < 10:
        tilt = "Level"
    elif abs(roll) > 45 or abs(pitch) > 45:
        tilt = "Steep Tilt"
    else:
        tilt = "Slight Tilt"
    
    return f"{direction}, {tilt}"

# Main sensor reading loop
print("Starting continuous sensor readings...")
print("Press Ctrl+C to stop")
print()

try:
    while True:
        print("\033[2J\033[H")  # Clear screen
        print("BNO055 Sensor Readings")
        print("=" * 30)
        
        # Get calibration status
        get_calibration_status()
        
        # Get operation mode
        get_operation_mode()
        
        # Read accelerometer data
        accel = sensor.acceleration
        if accel:
            print(f"Accelerometer (m/s²):")
            print(f"  X: {accel[0]:6.2f}")
            print(f"  Y: {accel[1]:6.2f}")
            print(f"  Z: {accel[2]:6.2f}")
            print(f"  Movement: {classify_movement(accel)}")
        else:
            print("Accelerometer: No data")
        print()
        
        # Read gyroscope data
        gyro = sensor.gyro
        if gyro:
            print(f"Gyroscope (rad/s):")
            print(f"  X: {gyro[0]:6.3f}")
            print(f"  Y: {gyro[1]:6.3f}")
            print(f"  Z: {gyro[2]:6.3f}")
        else:
            print("Gyroscope: No data")
        print()
        
        # Read magnetometer data
        mag = sensor.magnetic
        if mag:
            print(f"Magnetometer (μT):")
            print(f"  X: {mag[0]:6.2f}")
            print(f"  Y: {mag[1]:6.2f}")
            print(f"  Z: {mag[2]:6.2f}")
        else:
            print("Magnetometer: No data")
        print()
        
        # Read Euler angles (heading, roll, pitch)
        euler = sensor.euler
        if euler:
            print(f"Euler Angles:")
            print(f"  Heading: {euler[0]:6.1f}°")
            print(f"  Roll:    {euler[1]:6.1f}°")
            print(f"  Pitch:   {euler[2]:6.1f}°")
            print(f"  Orientation: {classify_orientation(euler)}")
        else:
            print("Euler Angles: No data")
        print()
        
        # Read quaternion
        quat = sensor.quaternion
        if quat:
            print(f"Quaternion:")
            print(f"  W: {quat[0]:6.3f}")
            print(f"  X: {quat[1]:6.3f}")
            print(f"  Y: {quat[2]:6.3f}")
            print(f"  Z: {quat[3]:6.3f}")
        else:
            print("Quaternion: No data")
        print()
        
        # Read linear acceleration (gravity removed)
        linear_accel = sensor.linear_acceleration
        if linear_accel:
            print(f"Linear Acceleration (m/s²):")
            print(f"  X: {linear_accel[0]:6.2f}")
            print(f"  Y: {linear_accel[1]:6.2f}")
            print(f"  Z: {linear_accel[2]:6.2f}")
        else:
            print("Linear Acceleration: No data")
        print()
        
        # Read gravity vector
        gravity = sensor.gravity
        if gravity:
            print(f"Gravity Vector (m/s²):")
            print(f"  X: {gravity[0]:6.2f}")
            print(f"  Y: {gravity[1]:6.2f}")
            print(f"  Z: {gravity[2]:6.2f}")
        else:
            print("Gravity Vector: No data")
        print()
        
        # Temperature
        temp = sensor.temperature
        if temp:
            print(f"Temperature: {temp:.1f}°C")
        else:
            print("Temperature: No data")
        print()
        
        print("Press Ctrl+C to stop")
        time.sleep({{ update_rate }})

except KeyboardInterrupt:
    print("\nStopping BNO055 sensor readings...")
    print("Sensor shutdown complete.")

