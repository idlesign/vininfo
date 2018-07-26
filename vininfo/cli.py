#!/usr/bin/env python
import sys

import click

from vininfo import VERSION_STR, Vin


@click.group()
@click.version_option(version=VERSION_STR)
def entry_point():
    """vininfo command line utilities."""


@entry_point.command()
@click.argument('vin')
def show(vin):
    """Show information for VIN"""
    num = Vin(vin)

    click.secho('Basic:')

    def out(annotatable):
        for k, v in annotatable.annotate().items():
            click.secho('%s: ' % k, fg='green', nl=False)
            click.secho(v)

    out(num)

    details = num.details

    if details:
        click.secho('')
        click.secho('Details:')
        out(details)


@entry_point.command()
@click.argument('vin')
def check(vin):
    """Perform VIN checksum validation"""

    if Vin(vin).verify_checksum():
        click.secho('Checksum is valid', fg='green')
    else:
        click.secho('Checksum is not valid', fg='red', err=True)
        sys.exit(1)


def main():
    entry_point(obj={})


if __name__ == '__main__':
    main()
