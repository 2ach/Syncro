from SalesChatWebDriver import SalesChatWebDriver as scwd

LINK = 'https://dell.glean.com/chat/'

if __name__ == "__main__":
    scwd = scwd(LINK)
    scwd.open_page()
    scwd.send_prompt()
    scwd.scrape_prompts()
    scwd.save_prompts()

    scwd.driver.close()