import os
import argparse
from llama_index import download_loader, GPTSimpleVectorIndex

INTEGRATION_TOKEN = os.getenv("NOTION_INTEGRATION_TOKEN")
DEFAULT_QUERY = "やりたいことを三つ挙げてください"

def notion_search(query: str) -> str:
    NotionPageReader = download_loader('NotionPageReader')
    reader = NotionPageReader(integration_token=INTEGRATION_TOKEN)
    page_ids = reader.search("")
    documents = reader.load_data(page_ids=page_ids)
    index = GPTSimpleVectorIndex.from_documents(documents)
    result = index.query(query)
    return result  # type: ignore

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Search from Notion',
        usage='python notion_index.py -q [query]',
    )
    parser.add_argument('-q', '--query')
    args = parser.parse_args()
    query = args.query or DEFAULT_QUERY
    result = notion_search(query)
    print(result)
