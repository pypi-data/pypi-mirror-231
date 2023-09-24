import subprocess
import time
import curses
import sys
import yaml


colorCounter = 0


def scale_color(r, g, b):
    f = (curses.COLORS - 1) / 255
    rgb = (min(round(r * f), curses.COLORS - 1),
           min(round(g * f), curses.COLORS - 1),
           min(round(b * f),  curses.COLORS - 1))
    return rgb


def get_color(r, g, b):
    global colorCounter
    colorCounter += 1
    r, g, b = scale_color(r, g, b)
    curses.init_color(colorCounter, *scale_color(r, g, b))
    curses.init_pair(colorCounter, colorCounter, -1)
    return curses.color_pair(colorCounter)


def create_session(target, localPortNumber, remotePortNumber, profile):
    command = ["aws", "ssm", "start-session",
               "--target", target,
               "--document-name", "AWS-StartPortForwardingSession",
               "--parameters", f"localPortNumber={localPortNumber},portNumber={remotePortNumber}",
               "--region", "eu-west-2",
               "--profile", profile]

    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                               )
    return process


def open_app(command, commandParams):
    commandParams = commandParams.split(' ')
    process = subprocess.Popen([command] + commandParams,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                               )
    return process


def render(stdscr):

    if len(sys.argv) < 2:
        print('config file parameter required')
        exit()
    with open(sys.argv[1]) as f:
        config = yaml.safe_load(f)
        config = config['connections']

    curses.use_default_colors()
    curses.curs_set(0)  # hide the cursor

    c_gray = get_color(192, 192, 192)
    c_green = get_color(0, 255, 0)
    c_red = get_color(255, 32, 0)
    c_lightgray = get_color(240, 240, 240)
    c_orange = get_color(255, 165, 0)
    c_light = get_color(240, 240, 240)

    stdscr.clear()

    width = curses.COLS

    stdscr.addstr(1, 3, 'AWS Session Manager', c_gray)
    stdscr.refresh()

    def refresh_screen(config):
        for session in config:
            refresh_session(session, updateScreen=False)
        curses.doupdate()

    def refresh_session(session, updateScreen=True):
        printer = session['win']
        printer.clear()
        key = session['key']

        selected_gray = c_light if session['selected'] else c_lightgray if  session['connected'] else c_gray

        printer.addstr((f'{key}) ' + session['name']).ljust(20), selected_gray)
        printer.addstr((session['protocol']).ljust(10), selected_gray)

        txt, color = ('Connected', c_green) if session['connected'] else ('Connecting...', c_orange) if session['connecting'] else ('Disconnected', c_red)
        printer.addstr(txt, color)

        if session['connected']:
            localPortNumber = session['localPortNumber']
            printer.addstr(f' ({localPortNumber})', color)

        printer.noutrefresh()
        if updateScreen:
            curses.doupdate()

    for i, session in enumerate(config):
        win = curses.newwin(1, width - 1 - 3, i + 3, 3)
        session['win'] = win
        session['key'] = i + 1
        session['connected'] = False
        session['connecting'] = False
        session['selected'] = i == 0

    refresh_screen(config)
    stdscr.refresh()

    buffer = []
    while True:
        key = stdscr.getkey()
        buffer.append(key)
        if ''.join(buffer[-4:]).lower() == 'quit':
            break
        elif key == 'c' and (i := buffer[-2]).isnumeric():
            i = int(i) - 1
            if command := config[i].get('command'):
                p = open_app(command, config[i].get('commandParams', ''))
                config[i]['app'] = p
        else:
            refresh_screen(config)
            stdscr.refresh()  # do not remove me because

        try:
            session = list(filter(lambda s: str(s['key']) == str(key), config))[0]
        except IndexError:
            continue

        session['connected'] = not session['connected']

        if session['connected']:
            session['connected'] = False
            session['connecting'] = True
            refresh_session(session)
            process = create_session(session['target'], session['localPortNumber'], session['remotePortNumber'], session.get('profile', 'default'))

            process.stdout.readline()
            session['connected'] = 'Starting session with SessionId' in process.stdout.readline().decode() 

            session['process'] = process
            session['connecting'] = False
        else:
            if process := session.get('process'):
                process.send_signal(1)

        refresh_session(session)

    for session in config:
        if session['connected']:
            if process := session.get('process'):
                process.send_signal(1)
                session['connected'] = False
            if process := session.get('app'):
                process.send_signal(1)
            time.sleep(0.1)
            refresh_session(session)
    time.sleep(0.1)


def main():
    curses.wrapper(render)


if __name__ == '__main__':
    main()
