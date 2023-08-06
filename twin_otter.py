from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
from datetime import datetime

# List of 20 different user-agents to choose from
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.31 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
]

msn_list = []
registration_list = []
status_list = []

for i in range(1, 844):
    url = f'https://twinotterworld.com/msn-{i}'

    # Choose a random user-agent from the list
    user_agent = random.choice(user_agents)

    headers = {
        'User-Agent': user_agent
    }

    try:
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, 'lxml')
        msn = soup.find('h2', style='white-space:pre-wrap;').text
        registration = soup.find('h2', style='text-align:right;white-space:pre-wrap;').text.split()[0]
        status_tags = soup.find_all('a', class_='sqs-block-button-element--medium sqs-button-element--primary sqs-block-button-element')
        status = status_tags[-1].text.strip()

        msn_list.append(msn)
        registration_list.append(registration)
        status_list.append(status)

        time.sleep(random.uniform(1, 2))

        print(f"MSN: {msn}\n")
        print(f"Registration: {registration}\n")
        print(f"Status: {status}\n")

    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")
        continue

for i in range(845, 995):
    url = f'https://twinotterworldseries400.com/msn-{i}'

    # Choose a random user-agent from the list
    user_agent = random.choice(user_agents)

    headers = {
        'User-Agent': user_agent
    }

    try:
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, 'lxml')
        msn = soup.find('h2', style='white-space:pre-wrap;').text
        registration = soup.find('h2', style='text-align:right;white-space:pre-wrap;').text.split()[0]
        status = soup.find('a', class_='sqs-block-button-element--large sqs-button-element--secondary sqs-block-button-element').text.strip()

        msn_list.append(msn)
        registration_list.append(registration)
        status_list.append(status)

        time.sleep(random.uniform(1, 2))

        print(f"MSN: {msn}\n")
        print(f"Registration: {registration}\n")
        print(f"Status: {status}\n")

    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")
        continue

data = {
    'MSN': msn_list,
    'Registration': registration_list,
    'Status': status_list
}

df = pd.DataFrame(data)

# Process the 'Registration' column to remove leading spaces
df['Registration'] = df['Registration'].str.lstrip()

# Get today's date in 'yyyy-mm-dd' format
today_date = datetime.now().strftime('%Y-%m-%d')

# Generate the filename with today's date
filename = f'twin_otter_scraped_{today_date}.xlsx'

# Export the updated DataFrame to an Excel file with the generated filename
df.to_excel(filename, index=False)