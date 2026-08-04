import os


def take_screenshot(page, name):

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    page.screenshot(
        path=f"screenshots/{name}.png"
    )