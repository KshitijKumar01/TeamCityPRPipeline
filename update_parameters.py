from fetch_label import GitHubPRLabelsFetcher

GITHUB_TOKEN = "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"
GITHUB_REPO_NAME = "capestone2"
GITHUB_REPO_OWNER = "KshitijKumar01"

def update():
    fetcher = GitHubPRLabelsFetcher(GITHUB_REPO_OWNER, GITHUB_REPO_NAME, GITHUB_TOKEN)
    labels = fetcher.fetch_and_print_labels("1")

    # Check if the labels were returned as key-value pairs
    if labels:
        print("##teamcity[setParameter name='HAS_LABELS' value='true']")
        for key, value in labels.items():
            if key.lower() == "pmbd-prod":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='PMBD_Prod' value='{value}']")
            if key.lower() == "asw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='ASW' value='{value}']")
            if key.lower() == "bsw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='BSW' value='{value}']")
    else:
        print("##teamcity[setParameter name='HAS_LABELS' value='false']")
