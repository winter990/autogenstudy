from autogen import AssistantAgent, UserProxyAgent

import openai
import autogen
import os
from autogen import ConversableAgent
#If proxy servers are applicable, add the following line
#os.environ["https_proxy"] = "http://127.0.0.1:23457"

#llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}

config_list = autogen.config_list_from_json(
    env_or_file="config_list.json",
)

llm_config = {"config_list": config_list}

User = ConversableAgent(
    name="User",
    system_message="please design the 4-bit binary adder by Verilog HDL",
    llm_config=llm_config,
)
Engineer = autogen.ConversableAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message="Engineer，Define the specifications for  the 4-bit binary adder by Verilog HDL, including input/output requirements . The engineer must specify any performance constraints like maximum propagation delay and desired power consumption levels.",
)
DesignAssistant = autogen.ConversableAgent(
    name="DesignAssistant",
    llm_config=llm_config,
    system_message="""DesignAssistant. Provide a conceptual . This involves suggesting the use of basic gates or a series of requirements. Sketch a basic logic diagram and propose a list of components (AND, OR, XOR gates).
""",
)
HDLDeveloper = autogen.ConversableAgent(
    name="HDLDeveloper",
    llm_config=llm_config,
    system_message="""HDLDeveloper. Translate the conceptual design into Verilog code. This code will implement the series of full adders, each handling one bit of the input numbers, and generating a corresponding bit of the output number and a carry-out. The Verilog code for this task would typically involve instantiating four 1-bit full adder modules and chaining them together.""",
)
VerificationEngineer = autogen.ConversableAgent(
    name="VerificationEngineer",
    system_message="""Verify the Verilog code by simulating the binary adder for all possible combinations of 4-bit inputs. Check if the sum and carry outputs are correct for each combination. Ensure the code adheres to any specified performance constraints such as propagation delay.
""",
    llm_config=llm_config,
)
OptimizationandTapeoutSpecialister = autogen.ConversableAgent(
    name="OptimizationandTapeoutSpecialister",
    system_message=""" Review the Verilog code for optimization opportunities, such as reducing gate delays or simplifying logic expressions for power efficiency. Finalize the design for inclusion in larger digital systems, ensuring that the design adheres to standard practices for easy integration.
""",
    llm_config=llm_config,
)

chat_results = User.initiate_chats(
    [
        {
            "recipient": Engineer,
            "message": "design the 4-bit binary adder by Verilog HDL",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": DesignAssistant,
            "message": "design the 4-bit binary adder by Verilog HDL",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": HDLDeveloper,
            "message": "design the 4-bit binary adder by Verilog HDL",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
        {
            "recipient": VerificationEngineer,
            "message": "design the 4-bit binary adder by Verilog HDL",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
{
            "recipient": OptimizationandTapeoutSpecialister,
            "message": "design the 4-bit binary adder by Verilog HDL",
            "max_turns": 2,
            "summary_method": "last_msg",
        },
    ]
)
print("First Chat Summary: ", chat_results[0].summary)
print("Second Chat Summary: ", chat_results[1].summary)
print("Third Chat Summary: ", chat_results[2].summary)
print("Fourth Chat Summary: ", chat_results[3].summary)
print("Fifth Chat Summary: ", chat_results[4].summary)
