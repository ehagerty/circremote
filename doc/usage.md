# Usage Guide

## Basic Usage

```bash
circremote <device> <command> [options]
```

## Device Connections

### Serial Connections

**macOS/Linux:**
```bash
# USB-to-serial adapter
circremote /dev/ttyUSB0 BME280

# Arduino-style device
circremote /dev/ttyACM0 scan-i2c

# Built-in serial port
circremote /dev/ttyS0 system-info
```

**Windows:**
```bash
# Standard COM ports
circremote COM3 BME280
circremote COM1 scan-i2c
circremote COM2 system-info
```

### Web Workflow Connections

```bash
# Default port (80)
circremote 192.168.1.100 BME280

# Custom port
circremote 192.168.1.100:8080 BME280

# With password
circremote -p mypassword 192.168.1.100 BME280
```

## Commands

### Built-in Commands

```bash
# List files on device
circremote /dev/ttyUSB0 ls /

# Remove files
circremote /dev/ttyUSB0 rm old_file.py

# Scan I2C bus
circremote /dev/ttyUSB0 scan-i2c

# System information
circremote /dev/ttyUSB0 system-info
```

### Remote Commands

```bash
# From GitHub repository
circremote /dev/ttyUSB0 https://github.com/user/repo/tree/main/commands/BME280

# From web server
circremote /dev/ttyUSB0 https://example.com/sensor_demo.py

# From local file
circremote /dev/ttyUSB0 /path/to/my/command.py
```

## Options

- `-v, --verbose`: Verbose debug output
- `-q, --quiet`: Quiet mode (suppress output except device output)
- `-y, --yes`: Auto-confirm all prompts
- `-c, --skip-circup`: Skip dependency installation
- `-p, --password`: Web Workflow password
- `-C, --config`: Custom config file path
- `-u, --circup`: Custom circup path
- `-t, --timeout`: Connection timeout (seconds)

## Examples

### Basic Sensor Reading
```bash
# Temperature and humidity
circremote /dev/ttyUSB0 BME280

# With verbose output
circremote -v /dev/ttyUSB0 BME280
```

### File Operations
```bash
# List all files
circremote /dev/ttyUSB0 ls /

# List specific directory
circremote /dev/ttyUSB0 ls /lib

# Remove file
circremote /dev/ttyUSB0 rm old_data.txt
```

### Web Workflow Setup
```bash
# Configure Web Workflow on ESP32 device
circremote /dev/ttyUSB0 enable-webworkflow "MyWiFiNetwork" "mypassword" 8080 "webpass"

# After configuration, use Web Workflow connection
circremote 192.168.1.100:8080 -p webpass BME280
```

### Remote Code Execution
```