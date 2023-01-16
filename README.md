# IntelGPT

IntelGPT is a command line tool that allows you to examine specific input such as URLs, file hashes, domain names, and IP addresses using GPT3.

GPT-3, or Generative Pre-trained Transformer 3, is a language generation model developed by OpenAI. One of the key features of GPT-3 is its ability to generate human-like text. This makes it suitable for a variety of natural language processing tasks.

[![asciicast](https://asciinema.org/a/550940.svg)](https://asciinema.org/a/550940)

## Usage
To build the IntelGPT tool, run the following command:
```bash
docker-compose build
```

To use the IntelGPT tools, you need to set up your API keys for OpenAI, Google Custom Search, and Shodan in a .env file. You can do this by following these steps:

1. Copy the env.template file to create a new .env file.
```bash
cp env.template .env
```

2. Open the .env file in a text editor and enter your API keys.
```bash
vim .env
```
3. Input your OpenAI API Key to OPENAI_API_KEY
```bash
OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxx
```

4. Input your Google Custom Search ID to GOOGLE_CSE_ID and Google Custom Search API Key to GOOGLE_API_KEY
```bash
GOOGLE_CSE_ID=xxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=xxxxxxxxxxxxxxxxxxx
```

5. Input your Shodan API Key to SHODAN_API_KEY
```bash
SHODAN_API_KEY=xxxxxxxxxxxxxxxxxxx
```

To run the tool, use the following command:
```
docker-compose run intelgpt [OPTIONS] INPUT_VALUE
```
Please make sure to keep your API keys private and never share them with anyone.

## Options
* `--url`: Investigate the given URL. Example: docker-compose run intelgpt --url http://example.com
* `--hash`: Investigate the given file hash. Example: docker-compose run intelgpt --hash fafe11f23567080fb14cfd3b51cb440b9c097804569402d720fd32dd66059830
* `--domain`: Investigate the given domain name. Example: docker-compose run intelgpt --domain example.com
* `--ip`: Investigate the given IP address. Example: docker-compose run intelgpt --ip 192.168.1.1
* `--lang`: Output the result in the specified language. Example: docker-compose run intelgpt --url http://example.com --lang english

You can also use the help option to see the usage instructions for the tool:
```bash
docker-compose run intelgpt --help
docker-compose run intelgpt --hash fafe11f23567080fb14cfd3b51cb440b9c097804569402d720fd32dd66059830 --lang english
```

## References
- [LangChain の Googleカスタム検索 連携を試す](https://note.com/npaka/n/nd9a4a26a8932)
- [LangChain の HOW-TO EXAMPLES (6) - メモリ](https://note.com/npaka/n/n155e66a263a2)
