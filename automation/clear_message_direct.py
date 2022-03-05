# External modules
from alive_progress import alive_bar
from playwright.async_api import async_playwright

# Internal modules
from utils.logging import info
from utils.settings import settings
from utils.progress import process_progress


async def delete_message_direct(show_browser: bool = True):
    '''Clear messages in direct.'''

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=show_browser)
        page = await browser.new_page()

        # await page.wait_for_timeout(3000)
        info('Loading page...')
        process_progress(milliseconds=4000)

        await page.goto(settings.SITE)

        button_login = '//*[@id="loginForm"]/div/div[3]'
        input_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        input_password = '//*[@id="loginForm"]/div/div[2]/div/label/input'

        await page.fill(input_login, settings.EMAIL)
        await page.fill(input_password, settings.PASSWORD)
        await page.click(button_login)

        info('Login successfully!')

        save_password = '//*[@id="react-root"]/section/main/div/div/div/div/button'

        await page.click(save_password)

        # await page.wait_for_timeout(1000)
        info('Loading page...')
        process_progress(milliseconds=1000)

        await page.locator('text=Agora não').click()

        # Waiting for loader a little bit of the page
        # await page.wait_for_timeout(3000)
        info('Loading a little bit of the page...')
        process_progress(milliseconds=3000)

        direct = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'
        await page.click(direct)

        process_progress(milliseconds=100)

        info('Deleting direct messages...')

        msg_del_range = range(2, settings.DELETE_MESSAGE + 2)

        # progress bar
        with alive_bar(settings.DELETE_MESSAGE, bar='blocks') as bar:
            for number in msg_del_range:
                profile_msg = '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a'
                await page.click(profile_msg)

                await page.wait_for_timeout(200)

                # See notifications, to clear
                # Somehow the notifications were getting in the way to interact with the messages button
                button_options = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]'

                await page.click(button_options)

                await page.wait_for_timeout(200)

                delete_msg = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button'
                await page.click(delete_msg)

                await page.wait_for_timeout(600)

                bar()

        print() # Space

        info(f'{settings.DELETE_MESSAGE} MESSAGE DIRECT DELETED SUCCESSFULLY')

        await browser.close()
