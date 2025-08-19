from arxiv_pipeline.paper import Paper

class PaperFilter:
    def __init__(self, preferences):
        self.preferences = preferences

    def filter(self, papers):

        filtered = []

        if papers is None:
            print("No papers found with the specified preferences")
            return []

        for paper in papers:
            for category in paper.categories:
                
                field = category.lower().split(".")
                
                keywords = []

                if len(field) == 2:
                    subfield = field[1]
                    field = field[0]
                    if self.preferences[field]["subfields"][subfield]["active"]:
                        keywords = self.preferences[field]["subfields"][subfield]["keywords"]                   

                else:
                    field = field[0]
                    if self.preferences[field]["active"]:
                        keywords = self.preferences[field]["keywords"]

                if paper.matches_keywords(keywords):
                    filtered.append(paper)
                    break
        
        return filtered