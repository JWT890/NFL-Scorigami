import requests
from bs4 import BeautifulSoup

def get_scorigami_scores():
    url = "https://www.pro-football-reference.com/boxscores/game-scores.htm"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrive scores. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    scores = set()

    for cell in soup.find_all("td", class_="right", attrs={"data-stat": "pts"}):
        scores.add(int(cell.text.strip))

    return scores

def is_scorigami(home_score, away_score, scorigami_scores):
    total_score = home_score + away_score
    return total_score not in scorigami_scores

def main():
    scorigami_scores = get_scorigami_scores()

    home_score = int(input("Enter home team's score: "))
    away_score = int(input("Enter away team's score: "))

    if is_scorigami(home_score, away_score, scorigami_scores):
        print("Scorigami")
    else:
        print("Not a Scorigami")

if __name__ == "__main__":
    main()