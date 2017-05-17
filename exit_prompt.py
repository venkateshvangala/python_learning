def ask_ok(prompt = "Do you really want to quit?", entries = 4, reminder = "Please Try again"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        entries = entries - 1;
        if entries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Do you really want to quit..?", 2, "Please try again later")

