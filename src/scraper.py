thonimport requests
from extractors.tripadvisor_parser import parse_reviews
from outputs.json_exporter import export_to_json
import json

def main():
    url = 'https://www.tripadvisor.com/Hotel_Review-g60763-d15288822-Reviews-SpringHill_Suites_New_York_Manhattan_Times_Square_South-New_York_City_New_York.html'
    response = requests.get(url)
    if response.status_code == 200:
        reviews = parse_reviews(response.text)
        export_to_json(reviews, 'data/sample_output.json')
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()