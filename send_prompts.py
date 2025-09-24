import pandas as pd
from SalesChatWebDriver import SalesChatWebDriver as scwd

if __name__ == "__main__":
    prompts = pd.read_csv(r'C:\Users\Zach_Schulz-Behrend\dev\Syncro\\output_prompts.csv', index_col=None, header=None, encoding="windows-1252")
    prompts = prompts[0] + " In one paragraph."
    count = 0

    scwd = scwd('https://dell.glean.com/chat/')

    while prompts.__len__() > 0:
        prompt_send = prompts.pop(count)
        scwd.open_page()
        scwd.send_prompt(prompt_send)
        
        count += 1
    
    scwd.driver.close()