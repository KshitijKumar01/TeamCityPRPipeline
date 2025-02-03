import os
from fetch_label import GitHubPRLabelsFetcher
 
def main():
    # GitHub repository details
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN environment variable is not set")
    owner = 'KshitijKumar01'  # Replace with the repository owner's GitHub username
    repo = 'TeamCityPRPipeline'  # Replace with the repository name
    pr_number = 1  # Replace with the pull request number
 
    # Create an instance of the GitHubPRLabelsFetcher class
    fetcher = GitHubPRLabelsFetcher(owner, repo, GITHUB_TOKEN)
 
    # Fetch and print label descriptions
    labels = fetcher.fetch_and_print_labels(pr_number)
 
    # Check if the labels were returned as key-value pairs
    if labels:
        print("##teamcity[setParameter name='HAS_LABELS' value='true']")
        for key, value in labels.items():
            if key.lower() == "pmbd-prod":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='PMBD_PROD' value='{value}']")
            if key.lower() == "asw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='ASW' value='{value}']")
            if key.lower() == "bsw":
            # Set the TeamCity parameters for each value
                print(f"##teamcity[setParameter name='BSW' value='{value}']")
    else:
        print("##teamcity[setParameter name='HAS_LABELS' value='false']")
 
if __name__ == "__main__":
    main()
