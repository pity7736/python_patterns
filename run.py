import argparse

from command import ClientCommand
from singleton import ClientSingleton


patterns = {
    'command': ClientCommand,
    'singleton': ClientSingleton
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Design patterns examples')
    parser.add_argument(
        'pattern',
        metavar='pattern',
        choices=patterns.keys(),
        help='Pattern to run. choices: %(choices)s'
    )
    parser.add_argument(
        '-t',
        metavar='type',
        help='Run concept o example. Choices: %(choices)s. Default: %(default)s',
        choices=('concept', 'example'),
        default='concept'
    )
    args = parser.parse_args()
    client_pattern = patterns[args.pattern](args.t)
    client_pattern.run()
