from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.tools.google_search.tool import GoogleSearchRun, GoogleSearchAPIWrapper

agent = initialize_agent(
    llm=OpenAI(model_name="gpt-3.5-turbo", temperature=0),
    tools=[
        PythonREPLTool(
            description="A Python shell. Use this to execute python commands. "
                        "Input should be a valid python command. "
                        "If you want to see the output of a value, you should print it out "
                        "with `print(...)`."),
        GoogleSearchRun(
            description="A wrapper around Google Search. "
                        "Useful for when you need to answer questions about current events. "
                        "Input should be a search query.",
            api_wrapper=GoogleSearchAPIWrapper()),
    ],
    verbose=True
)
question = input()
answer = agent.run(question)
print("==>", answer)