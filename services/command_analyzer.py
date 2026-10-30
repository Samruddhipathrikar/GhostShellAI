def analyze_command(command):
    command = command.strip().lower()

    dangerous_commands = [
        "rm ",
        "del ",
        "format ",
        "shutdown",
        "rmdir",
        "rd ",
    ]

    developer_commands = [
        "git",
        "npm",
        "python",
        "pip",
        "docker",
        "node",
    ]

    system_commands = [
        "dir",
        "cd",
        "whoami",
        "ipconfig",
        "tasklist",
        "systeminfo",
    ]

    if any(cmd in command for cmd in dangerous_commands):
        return {
            "type": "Dangerous",
            "haunting_level": "💀💀💀💀💀",
            "warning": "This command could modify or delete system data."
        }

    if any(command.startswith(cmd) for cmd in developer_commands):
        return {
            "type": "Developer",
            "haunting_level": "👻👻👻",
            "warning": None
        }

    if any(command.startswith(cmd) for cmd in system_commands):
        return {
            "type": "System",
            "haunting_level": "👻👻",
            "warning": None
        }

    return {
        "type": "Unknown",
        "haunting_level": "👻",
        "warning": None
    }