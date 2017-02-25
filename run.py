import argparse
import sys


if sys.version_info.major < 3:
    sys.stderr.write('Python version error.\nMinimun Python version 3.0.\n')
    sys.exit()


if __name__ == '__main__':
    from patterns import ClientCommand, ClientSingleton, ClientTemplateMethod

    patterns = {
        'command': ClientCommand,
        'singleton': ClientSingleton,
        'template_method': ClientTemplateMethod
    }
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
