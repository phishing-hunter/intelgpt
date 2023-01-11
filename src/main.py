# 参考
# https://note.com/npaka/n/nd9a4a26a8932
# https://note.com/npaka/n/n155e66a263a2

import os
import sys
import click

from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, SerpAPIWrapper, LLMChain, LLMMathChain, LLMBashChain
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor, load_tools, initialize_agent

def generate_prompt(identifier:str,input_value:str):
    if identifier in ["url", "domain"]:
        prompt = f"""
以下の手順を使ってURL({input_value})の調査を行い、悪意の有無について「日本語」で出力してください。
* digコマンドを使って入力されたドメイン名からIPアドレスを取得します。
* whoisコマンドを使ってWhois情報を取得します。
* shodanコマンドを使ってサーバの情報を取得します。(コマンドの使い方`shodan host 189.201.128.250`)
* IPアドレスをgoogleで検索する

判定基準
* IP Abuse Reports
"""

    if identifier == "ip":
        prompt = f"""
以下の手順を使ってIPアドレス({input_value})の調査を行い、悪意の有無について「日本語」で出力してください。
* whoisコマンドを使ってWhois情報を取得します。
* shodanコマンドを使ってサーバの情報を取得します。(コマンドの使い方`shodan host 189.201.128.250`)
* IPアドレスをgoogleで検索する

判定基準
* shodanのレポート内容
* 悪意のあるIPアドレスとして報告されている
* IP Abuse Reports
"""

    if identifier == "hash":
       prompt = f"""
以下の手順を使ってHash({input_value})の調査を行い、悪意の有無について「日本語」で出力してください。
* ハッシュ値をGoogle検索する

判定基準
* 悪意のあるファイルとして報告されている
"""
    return prompt

@click.command()
@click.option("--url", "identifier", flag_value="url", help="Investigate based on URL.")
@click.option("--hash", "identifier", flag_value="hash", help="Investigate based on file hash.")
@click.option("--domain", "identifier", flag_value="domain", help="Investigate based on domain name.")
@click.option("--ip", "identifier", flag_value="ip", help="Investigate based on IP address.")
@click.argument("input_value")
def main(identifier: str, input_value: str):
    # ツールの準備
    llm = OpenAI(temperature=0)
    tools = load_tools(["terminal", "google-search"], llm=llm)
    llm_math_chain = LLMMathChain(llm=llm, verbose=True)
    llm_bash_chain = LLMBashChain(llm=llm, verbose=True)
    tools.append(
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        )
    )

    memory = ConversationBufferMemory(memory_key="chat_history")
    prompt = generate_prompt(identifier, input_value)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    agent.run(prompt)

if __name__ == "__main__":
    main()

