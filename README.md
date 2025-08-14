# circremote

A command-line tool for remotely executing CircuitPython code on devices over serial or Web Workflow connections.

It can run the commands included with it, your own commands from anywhere in the filesystem, and commands that it loads over HTTP/HTTPS. It can easily execute example programs from Github.

## Features

- **Cross-platform support**: Works on Windows, macOS, and Linux
- **Multiple connection types**: Serial ports and CircuitPython Web Workflow
- **Built-in commands**: 100+ sensor and utility commands included
- **Remote commands**: Execute commands from URLs and GitHub repositories
- **Dependency management**: Automatic installation of CircuitPython libraries via circup
- **Configuration**: Device aliases and search paths for easy management
- **Quiet mode**: Suppress output for scripting and automation

## Installation

```bash
pip install circremote
```

## Quick Start

### Serial Connection (macOS/Linux)
```bash
# List files on device
circremote /dev/ttyUSB0 ls /

# Run a sensor command
circremote /dev/ttyUSB0 BME280
```

### Serial Connection (Windows)
```bash
# List files on device
circremote COM3 ls /

# Run a sensor command
circremote COM3 BME280
```

### Web Workflow Connection
```bash
# Connect to device over network
circremote 192.168.1.100 BME280

# With password
circremote -p mypassword 192.168.1.100 BME280
```

### Remote Commands
```bash
# Run command from GitHub
circremote /dev/ttyUSB0 https://github.com/user/repo/tree/main/commands/BME280

# Run Python file from web
circremote /dev/ttyUSB0 https://example.com/my_sensor.py
```

## Configuration

Create `~/.circremote/config.json` (cross-platform):

```json
{
  "devices": [
    {
      "name": "my-device",
      "device": "/dev/ttyUSB0",
      "friendly_name": "My CircuitPython Board"
    }
  ],
  "command_aliases": [
    {
      "name": "temp",
      "command": "BME280"
    }
  ],
  "search_paths": [
    "/path/to/my/commands"
  ],
  "circup": "/usr/local/bin/circup"
}
```

Then use device aliases:
```bash
circremote my-device temp
```

## Options

- `-v, --verbose`: Verbose output
- `-q, --quiet`: Quiet mode (suppress output except device output)
- `-y, --yes`: Auto-confirm all prompts
- `-c, --skip-circup`: Skip dependency installation
- `-p, --password`: Web Workflow password
- `-C, --config`: Custom config file path
- `-u, --circup`: Custom circup path
- `-t, --timeout`: Connection timeout (seconds)

## Documentation

- [Usage Guide](doc/usage.md)
- [Command Reference](doc/commands.md)
- [FAQ](doc/faq.md)

## License

MIT License - see [LICENSE](LICENSE) file for details.
