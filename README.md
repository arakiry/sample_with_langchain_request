# sample_with_langchain_request
## Get start
### Setup
このレポジトリでは、.env に以下の環境変数を設定する必要があります。
- OPENAI_API_KEY: OpenAI の API key
- NOTION_INTEGRATION_TOKEN: Notion の Integration token

#### Notion Integration
Notionからデータを取ってくるには、Notion Integration を作る必要があります。
以下のURLからIntegrationを作成してください。
（ Integration type は Internal を想定しています。）
https://www.notion.so/my-integrations

Integrationが作成できたら、Internal Integration Token を .env の NOTION_INTEGRATION_TOKEN に設定してください。

### Run
```sh
docker compose up -d --build
docker compose exec python3 bash

# on Docker container
python3 scripts/notion_index.py -q {適当なクエリ}
```
