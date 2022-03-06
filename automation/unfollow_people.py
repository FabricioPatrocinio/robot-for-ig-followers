# External modules
from alive_progress import alive_bar
from playwright.async_api import async_playwright

# Internal modules
from utils.logging import info
from utils.settings import settings
from utils.progress import process_progress


async def unfollow_people(show_browser: bool = True):
    '''Follow suggested people.'''

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
        process_progress(milliseconds=1200)

        await page.locator('text=Agora não').click()

        # Waiting for loader a little bit of the page
        # await page.wait_for_timeout(3000)
        info('Loading a little bit of the page...')
        process_progress(milliseconds=3000)

        profile_img = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img'
        profile = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div'

        await page.click(profile_img)

        info('Entering the profile...')
        process_progress(milliseconds=100)

        await page.click(profile)

        following = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div'

        await page.click(following)

        follow_range = range(1, settings.UNFALLOW_PEOPLE + 1)

        info('Unfollowing people...')

        # Number of followers that load in a time interval
        count = 1

        # progress bar
        with alive_bar(settings.UNFALLOW_PEOPLE, bar='blocks') as bar:
            for number in follow_range:
                await page.wait_for_timeout(250)

                unfallowers = f'//html/body/div[6]/div/div/div/div[3]/ul/div/li[{number}]/div/div[3]/button'

                await page.click(unfallowers)

                await page.wait_for_timeout(400)

                unfollow = '//html/body/div[7]/div/div/div/div[3]/button[1]'
                await page.click(unfollow)

                await page.wait_for_timeout(250)

                if count >= 12:
                    count = 0
                    await page.wait_for_timeout(5000)

                count += 1

                bar()

        print() # Space

        info(f'{settings.UNFALLOW_PEOPLE} PEOPLE UNFOLLOWED SUCCESSFULLY')

        await browser.close()
