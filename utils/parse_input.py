def parse_input(user_input: str) -> tuple[str, list[str]]:
    command, *args = user_input.split()
    return command.lower(), *args
