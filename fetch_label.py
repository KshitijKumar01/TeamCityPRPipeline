import requests
import json
 
# from Initialization.pr_details.Authentication import BearerAuth
# GITHUB_TOKEN = "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"
# GITHUB_REPO_NAME = "capestone2"
# GITHUB_REPO_OWNER = "KshitijKumar01"
 
 
class GitHubPRLabelsFetcher:
    def __init__(self, organisation, repo_name, token):
        self.organisation = organisation
        self.repo_name = repo_name
        self.token = token
        self.url = f'https://api.github.com/repos/{self.organisation}/{self.repo_name}/issues/labels'
 
 
    def fetch_labels(self, pr_number):
        # Set headers for authentication
        headers = {
        "Authorization" : f"Bearer {self.token}",
        "Content_Type" : "application/json"
    }
        url = 'https://api.github.com/repos/' + self.organisation + '/' + \
              self.repo_name + '/' + 'issues' + '/' + pr_number + '/' + 'labels'
        response = requests.get(url, headers=headers)
        # print(response.json())
        return response
 
    def fetch_and_print_labels(self, pr_number):
        response = self.fetch_labels(pr_number)
 
        if response.status_code == 200:
            # Parse the JSON response containing labels
            labels = response.json()
            label_dict = {}
            if labels:
                print(f"Labels for Pull Request #{pr_number}:")
                for label in labels:
                    description = label.get('description', '')
                    if description:
                        # Split the description by comma to separate multiple labels
                        descriptions = description.split(',')
                        for desc in descriptions:
                            try:
                                key, value = desc.split(':', 1)
                                label_dict[key.strip()] = value.strip()
                                print(f"{key.strip()} : {value.strip()}")
                            except ValueError:
                                print(f"Invalid label description format: {desc}")
            else:
                print(f"No labels found for Pull Request #{pr_number}")
            return label_dict
        else:
            print(f"Failed to fetch labels. HTTP Status Code: {response.status_code}")
            print("Error:", response.json())
            return None
 
# if __name__ == "__main__":
#     a = GitHubPRLabelsFetcher(GITHUB_REPO_OWNER, GITHUB_REPO_NAME, GITHUB_TOKEN)
#     a.fetch_and_print_labels("1")
