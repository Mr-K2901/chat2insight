from core.pipeline.pipeline import process_conversation


if __name__ == "__main__":
    print(process_conversation([{"sender": "demo", "text": "Hello"}]))
