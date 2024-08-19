from utils import *


def main():
    book = load_data()
    print(bot_answer("Welcome to the assistant bot!"))
    try:
        while True:
            user_input = input('Enter command: ').strip()
            if user_input:
                command, *args = parse_input(user_input)

                match command:
                    # Finish
                    case 'exit' | 'close':
                        print(bot_answer('Goodbye!'))
                        save_data(book)
                        break

                    # Greeting
                    case 'hi' | 'hello':
                        print(bot_answer('Hello! How can I help you?'))

                    # Add contact
                    case 'add':
                        print(bot_answer(add_contact(args, book)))

                    # Change contact
                    case 'change':
                        print(bot_answer(change_contact(args, book)))

                    # Show contact
                    case 'contact':
                        print(bot_answer(show_contact(args, book)))

                    # Show all contact
                    case 'all':
                        print(bot_answer(show_all(book)))

                    # Add birthday
                    case 'add-birthday':
                        print(bot_answer(add_birthday(args, book)))

                    # Show birthday
                    case 'show-birthday':
                        print(bot_answer(show_birthday(args, book)))

                    # Show upcoming birthdays
                    case 'birthdays':
                        print(bot_answer(birthdays(book)))

                    # Show info
                    case 'info':
                        print(bot_answer(show_info()))

                    # Invalid command
                    case _:
                        print(bot_answer('I don\'t know how to handle this command.'))

    except KeyboardInterrupt:
        print(bot_answer('Oops.. Something went wrong..'))


if __name__ == '__main__':
    main()
