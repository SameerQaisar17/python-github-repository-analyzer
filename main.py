from github_api import GitHubAPI
from analyzer import GitHubAnalyzer
from database import create_table, add_search, view_history


def analyze_profile():
    username = input("\nEnter GitHub username: ").strip()

    if not username:
        print("\nUsername cannot be empty.")
        return

    api = GitHubAPI()

    try:
        print("\nFetching GitHub profile...")

        profile = api.get_profile(username)
        repositories = api.get_repositories(username)

        analyzer = GitHubAnalyzer(profile, repositories)
        analyzer.run_analysis()

        add_search(profile.get("login"))

    except Exception as error:
        print("\nError:", error)


def display_history():
    history = view_history()

    print("\n========== SEARCH HISTORY ==========")

    if not history:
        print("No search history found.")
        return

    for record in history:
        print(f"""
ID: {record[0]}
Username: {record[1]}
Search Date: {record[2]}
-------------------------
""")


def main():
    create_table()

    while True:
        print("""
========== GITHUB REPOSITORY ANALYZER ==========

1. Analyze GitHub Profile
2. View Search History
3. Exit

================================================
""")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            analyze_profile()

        elif choice == "2":
            display_history()

        elif choice == "3":
            print("\nThank you for using GitHub Repository Analyzer!")
            break

        else:
            print("\nInvalid option! Please choose 1-3.")


if __name__ == "__main__":
    main()