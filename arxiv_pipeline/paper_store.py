import json

from arxiv_pipeline.paper import Paper

class PaperStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, papers):
        if papers is None:
            print("No papers matched the specified keywords.")
            return None

        data = [paper.to_dict() for paper in papers]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2)

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
            
        except FileNotFoundError:
            return []