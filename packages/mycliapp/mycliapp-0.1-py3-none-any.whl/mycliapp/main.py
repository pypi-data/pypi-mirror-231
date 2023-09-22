import click


@click.command()
def hello():
   click.echo(f'Hello, !')
