from lambda_simulation.handler import lambda_handler

def simulate_s3_upload(file_path):
    print(f"🗂️ File uploaded: {file_path}")
    print("🚀 Triggering Lambda function...")
    event = {
        "file_path": file_path
    }
    lambda_handler(event)

if __name__ == "__main__":
    simulate_s3_upload("sample_files/urgent_report.txt")
