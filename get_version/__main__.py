import sys
from subprocess import getstatusoutput

import click

from .versions import version_dict


@click.command()
@click.argument('command')
def get_version(command):
    """Get the version of so many things.\n
    Supported tools:\n
      'python', 'python3', 'pip', 'node', 'npm', 'yarn', 'java', 'mvn', 'gradle', 'gcc', 'clang', 'go'
    """
    if command not in version_dict:
        click.echo('Not support for {}.'.format(command))
        sys.exit(0)

    status, output = getstatusoutput('{} {}'.format(command, version_dict[command]))

    if status:
        click.echo(output)
        sys.exit(status)
    else:
        click.echo('The version info of {} is:'.format(command))
        click.echo(output)
        click.echo('From command "{} {}"'.format(command, version_dict[command]))


def main():  # pragma: no cover
    get_version()


if __name__ == "__main__":  # pragma: no cover
    main()
