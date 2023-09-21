import pytest
import unittest

from promptflow.connections import CustomConnection
from promptflow_clu.tools.conversational_language_understanding import analyze_conversation


@pytest.fixture
def my_custom_connection() -> CustomConnection:
    my_custom_connection = CustomConnection(
        {
            "LanguageResourceKey" : "435763f7fe5741609cb54d482b4d0cce"
        }
    )
    return my_custom_connection


class TestTool:
    def test_analyze_conversation(self, my_custom_connection):
        clu_endpoint = "https://absenSCUS.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview"
        project_name = "GM-Media-0808"
        deployment_name = "adv100-0"
        input_text = "Play Eric Clapton"
        result = analyze_conversation(my_custom_connection, input_text, clu_endpoint, project_name, deployment_name)
        clu_topintent = result["result"]["prediction"]["topIntent"]
        assert clu_topintent == "MediaPlayMedia"


# Run the unit tests
if __name__ == "__main__":
    unittest.main()