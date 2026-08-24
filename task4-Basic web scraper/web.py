import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
    
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  

        
        soup = BeautifulSoup(response.text, "html.parser")

        
        
        headlines = soup.find_all(["h1", "h2", "h3"])

        print(f"\n--- Scraped Headlines from {url} ---\n")

        count = 1
        for headline in headlines:
            text = headline.get_text(strip=True)

            
            if text and len(text) > 15:
                
                parent_link = headline.find_parent("a") or headline.find("a")
                link = parent_link["href"] if parent_link else "N/A"

               
                if link.startswith("/"):
                    link = url.rstrip("/") + link

                
                print(f"{count}. {text}")
                if link != "N/A":
                    print(f"   URL: {link}")
                print("-" * 50)
                count += 1

                if count > 10:  # Limit output to top 10 headlines
                    break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")


if __name__ == "__main__":
    
    target_url = "https://www.bbc.com/news"
    scrape_news(target_url)