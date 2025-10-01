from SalesChatWebDriver import SalesChatWebDriver as scwd
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    LINK = os.getenv("LINK")

    scwd = scwd(LINK)
    scwd.open_page()
    scwd.send_prompt()
    scwd.scrape_prompts()
    scwd.save_prompts()

    scwd.driver.close()