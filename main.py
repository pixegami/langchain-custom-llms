import os
from langchain.llms.openai import OpenAI
from langchain.llms.bedrock import Bedrock
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain


PROMPT_TEMPLATE_TEXT = """
Generate a table in CSV format from the following bank statement data.

Add a column called "Category" and populate it with one of the following values: 
[Groceries, Transport, Entertainment, Shopping, Utilities, Eating Out, Unknown]

{statement}
"""

CODING_TEMPLATE_TEXT = """
First, hard-code this data as a Python variable called 'items', with the category name and value.
Then write a Python script to sum this data by 'Category' and print the results.

{categorized_transactions}
"""


# OpenAI (GPT-4) LLM
llm_open_ai = OpenAI(max_tokens=1024)

# AWS Bedrock LLM
BEDROCK_CLAUDE_MODEL = "anthropic.claude-v2"
BEDROCK_LLAMA_MODEL = "meta.llama2-70b-chat-v1"
llm_bedrock = Bedrock(
    credentials_profile_name="default",
    model_id=BEDROCK_CLAUDE_MODEL,
    model_kwargs={"max_tokens_to_sample": 1024},
)

# Google Gemini LLM
llm_gemini = GoogleGenerativeAI(
    model="gemini-pro",
    max_output_tokens=1024,
    google_api_key=os.environ["GOOGLE_AI_API_KEY"],
)

llm = llm_gemini  # Or llm_bedrock or llm_open_ai.

# Create the individual prompt templates.
categorization_template = PromptTemplate.from_template(PROMPT_TEMPLATE_TEXT)
coding_template = PromptTemplate.from_template(CODING_TEMPLATE_TEXT)

# Create the chains.
categorization_chain = LLMChain(llm=llm, prompt=categorization_template)
coding_chain = LLMChain(llm=llm, prompt=coding_template)

# Join them into a sequential chain.
overall_chain = SimpleSequentialChain(
    chains=[categorization_chain, coding_chain], verbose=True
)

# Load the bank statement data.
with open("bank_statement.csv", "r") as f:
    bank_statement_data = f.read()

# Run the chain using the bank statement data as input.
overall_chain.run(bank_statement_data)
