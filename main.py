import os
from typing import List
from dotenv import load_dotenv
from rich.console import Console
from langchain_core.tools import StructuredTool
from serpapi import GoogleSearch
import argparse
from textwrap import fill

load_dotenv()

console = Console()

class GoogleSearchClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, query: str, num_results: int = 10) -> List[dict]:
        search = GoogleSearch({
            "q": query,
            "api_key": self.api_key,
            "num": num_results
        })
        results = search.get_dict().get("organic_results", [])
        return results

class SearchResultsDisplayer:
    @staticmethod
    def render(results: List[dict]):
        print("\nTop Google search results:\n")
        for idx, result in enumerate(results, start=1):
            title = result.get("title", "No Title").strip()
            link = result.get("link", "No Link").strip()

            print(f"{idx}. {fill(title, width=150)}")
            print(f"   {link}\n")

class GoogleSearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("Missing SERPAPI_API_KEY in .env file.")
        self.client = GoogleSearchClient(api_key=self.api_key)

    def tool_function(self, query: str) -> str:
        results = self.client.search(query)
        SearchResultsDisplayer.render(results)
        return "Done"

    def as_langchain_tool(self) -> StructuredTool:
        return StructuredTool.from_function(
            name="google_search",
            description="Search Google for a given query and return the top 10 results",
            func=self.tool_function,
            args_schema={"query": str}
        )

def main():
    parser = argparse.ArgumentParser(description="Google Search CLI using SerpAPI + LangChain Tool")
    parser.add_argument("query", help="Search query to look up")
    args = parser.parse_args()
    tool = GoogleSearchTool()
    tool.tool_function(args.query)

if __name__ == "__main__":
    main()