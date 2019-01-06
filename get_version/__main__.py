import click
import sys
from subprocess import getstatusoutput
from .versions import version_dict


@click.command()
@click.argument('command')
def get_version(command):
    if command not in version_dict:
        click.echo('Not support for {}.'.format(command))
        sys.exit(0)

    click.echo('The version info of {} is:'.format(command))
    status, output = getstatusoutput('{} {}'.format(command, version_dict[command]))

    if status:
        click.echo(output)
        sys.exit(status)
    else:
        click.echo(output)
        click.echo('From command "{} {}"'.format(command, version_dict[command]))


def main():
    get_version()


if __name__ == "__main__":
    main()