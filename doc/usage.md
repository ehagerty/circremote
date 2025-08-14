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

### Remote Code Execution
```bash
# Run GitHub example
circremote /dev/ttyUSB0 https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/I2C_Scanners/circuitpython/code.py

# Run local command
circremote /dev/ttyUSB0 ~/my_commands/temp_sensor.py
```

### Web Workflow
```bash
# Connect to network device
circremote 192.168.1.100 BME280

# With password and timeout
circremote -p mypassword -t 30 192.168.1.100:8080 BME280
```

### Quiet Mode
```bash
# Quiet mode - suppresses all circremote output
circremote -q 192.168.1.100 BME280

# Quiet mode with auto-confirm
circremote -q -y 192.168.1.100 BME280

# Quiet mode with skip-circup (if dependencies need to be installed)
circremote -q -c 192.168.1.100 BME280
```

### Skip dependency installation
```bash
# Skip circup dependency installation
circremote -c /dev/ttyUSB0 BME280
```

## Configuration

### Device Aliases

Create `~/.circremote/config.json`:

```json
{
  "devices": [
    {
      "name": "feather",
      "device": "/dev/ttyUSB0",
      "friendly_name": "Adafruit Feather"
    },
    {
      "name": "pico",
      "device": "COM3",
      "friendly_name": "Raspberry Pi Pico"
    }
  ]
}
```

Then use aliases:
```bash
circremote feather BME280
circremote pico scan-i2c
```

### Command Aliases

```json
{
  "command_aliases": [
    {
      "name": "temp",
      "command": "BME280"
    },
    {
      "name": "scan",
      "command": "scan-i2c"
    }
  ]
}
```

Use aliases:
```bash
circremote /dev/ttyUSB0 temp
circremote /dev/ttyUSB0 scan
```

### Search Paths

```json
{
  "search_paths": [
    "/home/user/my_commands",
    "C:\\Users\\user\\my_commands"
  ]
}
```

### Quiet Mode
Use the `-q` flag to suppress all circremote output except device output:

- **Suppresses**: All circremote messages, warnings, progress info, module descriptions
- **Shows**: Only output from the CircuitPython device
- **Exits with error**: If any confirmation is needed (untested commands, offline warnings, dependencies)
- **Use with `-y`**: Combine with `-y` to auto-confirm all prompts in quiet mode
- **Use with `-c`**: Combine with `-c` to skip dependency installation in quiet mode
- **Mutually exclusive**: Cannot be used with `-v` (verbose) option

Perfect for scripting and automation where you only want the device output.
