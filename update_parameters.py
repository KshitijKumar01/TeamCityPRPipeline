from fetch_label import GitHubPRLabelsFetcher

GITHUB_TOKEN = "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"
GITHUB_REPO_NAME = "capestone2"
GITHUB_REPO_OWNER = "KshitijKumar01"

def update():
    fetcher = GitHubPRLabelsFetcher(GITHUB_REPO_OWNER, GITHUB_REPO_NAME, GITHUB_TOKEN)
    labels = fetcher.fetch_and_print_labels("1")

    if labels:
        for key, value in labels.items():
            if key.lower() == "":
                print(f"##teamcity[setParameter name='label1' value = '{value}']")