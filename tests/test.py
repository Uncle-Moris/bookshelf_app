COMMANDS = {"ADD": "Add new categories",
                "LS": "To list categories",
                "Q": "to go out from categories managing"}
nl = '\n'
command = input(f'What you like do ?\n\n'
                            f'{str().join([f"{k} - {v}{nl}" for k, v in COMMANDS.items()])}\n'
                            f'Type command :').upper()