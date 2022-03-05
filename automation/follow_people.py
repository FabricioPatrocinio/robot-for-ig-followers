# External modules
from alive_progress import alive_bar
from playwright.async_api import async_playwright

# Internal modules
from utils.logging import info
from utils.settings import settings
from utils.progress import process_progress


async def follow_people(show_browser: bool = True):
    '''Follow suggested people.'''

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=show_browser)
        page = await browser.new_page()

        # await page.wait_for_timeout(3000)
        info('Loading page...')
        process_progress(milliseconds=3000)

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

        view_all = '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div'

        # Suggestions for you, see all
        await page.click(view_all)

        follow_range = range(1, settings.FALLOW_PEOPLE + 1)

        info('following people...')

        with alive_bar(settings.FALLOW_PEOPLE, bar='blocks') as bar:
            for number in follow_range:
                fallowers = f'//html/body/div[1]/section/main/div/div[2]/div/div/div[{number}]/div[3]/button'

                await page.click(fallowers)

                await page.wait_for_timeout(400)

                bar()

        print() # Space

        info(f'{settings.FALLOW_PEOPLE} PEOPLE FOLLOWED SUCCESSFULLY')

        await browser.close()
