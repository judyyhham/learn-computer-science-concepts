import random
"""
Extract all titles from <dt> tags in Glossary.html and print as a list.
"""

from html.parser import HTMLParser


class DTExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles = []
        self.in_dt = False
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "dt":
            self.in_dt = True
            self.current_text = []

    def handle_endtag(self, tag):
        if tag == "dt" and self.in_dt:
            # Join the text and clean it up
            title = "".join(self.current_text).strip()
            if title:
                self.titles.append(title)
            self.in_dt = False
            self.current_text = []

    def handle_data(self, data):
        if self.in_dt:
            # Capture text content inside <dt>
            self.current_text.append(data)


def main():
    # Read the glossary HTML file
    glossary_file = "Glossary.html"
    
    with open(glossary_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Parse the HTML and extract <dt> titles
    parser = DTExtractor()
    parser.feed(html_content)
    
    # Print the titles
    print(f"Total <dt> titles found: {len(parser.titles)}\n")
    
    # for i, title in enumerate(parser.titles, 1):
    #     print(f"{title}")
    return(parser.titles[random.randint(0, len(parser.titles)-1)])  # Print a random title 


if __name__ == "__main__":
    main()
