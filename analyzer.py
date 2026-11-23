class GitHubAnalyzer:

    def __init__(self, profile, repositories):
        self.profile = profile
        self.repositories = repositories

    def display_profile(self):
        print("\n========== GITHUB PROFILE ==========")

        print("Username:", self.profile.get("login"))
        print("Name:", self.profile.get("name") or "Not provided")
        print("Bio:", self.profile.get("bio") or "Not provided")
        print("Location:", self.profile.get("location") or "Not provided")
        print("Public Repositories:", self.profile.get("public_repos"))
        print("Followers:", self.profile.get("followers"))
        print("Following:", self.profile.get("following"))
        print("Profile URL:", self.profile.get("html_url"))

    def get_total_stars(self):
        return sum(
            repo.get("stargazers_count", 0)
            for repo in self.repositories
        )

    def get_top_repository(self):
        if not self.repositories:
            return None

        return max(
            self.repositories,
            key=lambda repo: repo.get("stargazers_count", 0)
        )

    def get_language_statistics(self):
        languages = {}

        for repo in self.repositories:
            language = repo.get("language")

            if language:
                languages[language] = languages.get(language, 0) + 1

        return languages

    def display_repositories(self):
        print("\n========== PUBLIC REPOSITORIES ==========")

        if not self.repositories:
            print("No public repositories found.")
            return

        sorted_repositories = sorted(
            self.repositories,
            key=lambda repo: repo.get("stargazers_count", 0),
            reverse=True
        )

        for repo in sorted_repositories:
            print(f"""
Repository: {repo.get('name')}
Description: {repo.get('description') or 'No description'}
Language: {repo.get('language') or 'Not specified'}
Stars: {repo.get('stargazers_count', 0)}
URL: {repo.get('html_url')}
-------------------------------
""")

    def display_statistics(self):
        print("\n========== REPOSITORY ANALYSIS ==========")

        print("Total repositories:", len(self.repositories))
        print("Total stars:", self.get_total_stars())

        top_repo = self.get_top_repository()

        if top_repo:
            print("\nMost Popular Repository:")
            print("Name:", top_repo.get("name"))
            print("Stars:", top_repo.get("stargazers_count", 0))

        print("\nProgramming Languages:")

        languages = self.get_language_statistics()

        if not languages:
            print("No language information available.")
        else:
            for language, count in sorted(
                languages.items(),
                key=lambda item: item[1],
                reverse=True
            ):
                print(f"{language}: {count} repositories")

    def run_analysis(self):
        self.display_profile()
        self.display_repositories()
        self.display_statistics()