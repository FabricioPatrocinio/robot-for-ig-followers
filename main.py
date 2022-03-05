# External modules
import typer
import asyncio

# Internal modules
from utils.logging import error
from automation.follow_people import follow_people
from automation.unfollow_people import unfollow_people
from automation.clear_message_direct import delete_message_direct


cli = typer.Typer(add_completion=False, help='Basic CLI manager for the API', name='Bot IG followers')


@cli.command(help='Run the automation follow people')
def follow(browser: str = typer.Option('off', help='View automation in browser set False')):
    '''Automation to follow suggested people.'''

    if browser in ['off', 'on']:
        pass

    else:
        error('Invalid browser option!')
        return

    try:
        asyncio.run(follow_people(show_browser=True if browser == 'off' else False))

    except Exception as e:
        error('Something went wrong!')
        error(e)


@cli.command(help='Run the automation unfollow people')
def unfollow(browser: str = typer.Option('off', help='View automation in browser set False')):
    '''Automation to unfollow suggested people.'''

    if browser in ['off', 'on']:
        pass

    else:
        error('Invalid browser option!')
        return

    try:
        asyncio.run(unfollow_people(show_browser=True if browser == 'off' else False))

    except Exception as e:
        error('Something went wrong!')
        error(e)


@cli.command(help='Run the automation clear message direct')
def cleardirect(browser: str = typer.Option('off', help='View automation in browser set False')):
    '''Automation to unfollow suggested people.'''

    if browser in ['off', 'on']:
        pass

    else:
        error('Invalid browser option!')
        return

    try:
        asyncio.run(delete_message_direct(show_browser=True if browser == 'off' else False))

    except Exception as e:
        error('Something went wrong!')
        error(e)


if __name__ == '__main__':
    cli()
