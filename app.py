import json
import requests
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LeetCodeAPI:
    def fetch_question(self, question_id):
        url = "https://leetcode.com/graphql"
        headers = {
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com/problemset/all/",
        }
        query = """
        query getQuestion($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                content
                difficulty
                categoryTitle
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                exampleTestcases
                similarQuestions
                topicTags {
                    name
                    slug
                }
            }
        }
        """
        variables = {
            "titleSlug": question_id,
        }

        response = requests.post(
            url, json={"query": query, "variables": variables}, headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            logger.error(
                f"Failed to fetch question data. Status code: {response.status_code}"
            )
            logger.error("Response content: %s", response.content)
            return None

    def create_python_file(self, question_data):
        title = question_data["data"]["question"]["title"]
        title_underscore = title.replace(" ", "_")
        content = question_data["data"]["question"]["content"]
        code_snippets = question_data["data"]["question"]["codeSnippets"]

        filename = f"{title_underscore}.py"
        os.makedirs(title_underscore, exist_ok=True)
        with open(os.path.join(title_underscore, filename), "w") as file:
            file.write("class Solution:\n")
            file.write(
                "    def twoSum(self, nums: List[int], target: int) -> List[int]:\n"
            )
            logger.info(f"Python file created: {filename}")

    def create_markdown_file(self, question_data):
        title = question_data["data"]["question"]["title"]
        title_underscore = title.replace(" ", "_")
        content = question_data["data"]["question"]["content"]

        filename = f"{title_underscore}.md"
        os.makedirs(title_underscore, exist_ok=True)
        with open(os.path.join(title_underscore, filename), "w") as file:
            file.write(content)
            logger.info(f"Markdown file created: {filename}")

    def create_test_file(self, question_data):
        title = question_data["data"]["question"]["title"]
        title_underscore = title.replace(" ", "_")
        example_testcases = question_data["data"]["question"]["exampleTestcases"]
        print(example_testcases)
        print(question_data["data"]["question"])

        # filename = f"{title_underscore}_test.py"
        # os.makedirs(title_underscore, exist_ok=True)
        # with open(os.path.join(title_underscore, filename), "w") as file:
        #     file.write("import unittest\n")
        #     file.write("from solution import Solution\n")
        #     for testcase in example_testcases:
        #         file.write(f"def test_{testcase}():\n")
        #         file.write(f"    self.assertEqual(Solution().twoSum({testcase}), [])\n")
        #     logger.info(f"Test file created: {filename}")


if __name__ == "__main__":
    api = LeetCodeAPI()
    question_id = "two-sum"
    question_data = api.fetch_question(question_id)
    if question_data is not None:
        api.create_python_file(question_data)
        api.create_markdown_file(question_data)
        api.create_test_file(question_data)
    else:
        logger.error("Failed to fetch or create Python file.")
