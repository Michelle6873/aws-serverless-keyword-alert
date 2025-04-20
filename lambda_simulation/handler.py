def lambda_handler(event):
    file_path = event["file_path"]
    keywords = ["breaking", "urgent", "alert"]

    try:
        with open(file_path, "r") as file:
            content = file.read()
            for keyword in keywords:
                if keyword.lower() in content.lower():
                    print(f"📢 Notification: Found keyword '{keyword}' in {file_path}")
                    return
        print("✅ No keywords found.")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
