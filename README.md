# 🚀 AWS Event-Driven ETL Pipeline

An event-driven ETL (Extract, Transform, Load) pipeline built using AWS services. The pipeline automatically processes CSV files uploaded to Amazon S3, triggers an AWS Lambda function, executes an AWS Glue ETL job to remove duplicate records, and stores the cleaned data back in Amazon S3.

This project demonstrates the use of serverless architecture to automate data processing workflows without managing any servers.

---

# 📌 Project Overview

This project implements an automated ETL pipeline where:

* A CSV file is uploaded to an Amazon S3 bucket.
* Amazon S3 triggers an AWS Lambda function.
* The Lambda function starts an AWS Glue ETL job using boto3.
* AWS Glue removes duplicate records from the dataset.
* The cleaned CSV file is stored in another S3 folder.

---

# 🏗️ Architecture

```text
CSV Upload
     │
     ▼
Amazon S3 (older-data/)
     │
ObjectCreated Event
     │
     ▼
AWS Lambda
     │
boto3.start_job_run()
     │
     ▼
AWS Glue ETL
     │
Drop Duplicates
     │
     ▼
Amazon S3 (new-data2/)
     │
     ▼
Cleaned CSV
```

---

# ⚙️ AWS Services Used

| Service         | Purpose                                           |
| --------------- | ------------------------------------------------- |
| Amazon S3       | Stores input and processed CSV files              |
| AWS Lambda      | Automatically triggers the Glue ETL job           |
| AWS Glue Studio | Performs visual ETL and removes duplicate records |
| IAM             | Manages permissions for AWS resources             |
| CloudWatch      | Stores Lambda execution logs                      |
| boto3           | Starts the Glue job programmatically from Lambda  |

---

# 📂 Project Structure

```text
ETL/
│
├── lambda/
│   └── trigger_glue_job.py
│
├── sample-data/
│   ├── employee_v3.csv
│   └── cleaned_output.csv
│
├── screenshots/
│   ├── 01-s3-input-folder.png
│   ├── 02-lambda-function-code.png
│   ├── 03-lambda-trigger-configuration.png
│   ├── 04-cloudwatch-lambda-logs.png
│   ├── 05-glue-visual-etl-workflow.png
│   ├── 06-glue-job-run-success.png
│   ├── 07-s3-output-folder.png
│   ├── 08-cleaned-output-csv.png
│   └── 09-project-architecture.png
│
├── architecture.png
├── README.md
└── .gitignore
```

---

# 🔄 Workflow

1. Upload a CSV file to the **older-data/** folder.
2. Amazon S3 generates an ObjectCreated event.
3. AWS Lambda is triggered automatically.
4. Lambda starts the AWS Glue ETL job.
5. AWS Glue reads the CSV file.
6. Duplicate records are removed.
7. The cleaned CSV file is written to the **new-data2/** folder.

---

# 📊 Dataset Used

Input:

* Employee CSV file containing duplicate records.

Transformation:

* Remove duplicate rows using AWS Glue Visual ETL.

Output:

* Clean CSV containing only unique employee records.

---

# 🧠 Key Features

* Event-driven architecture
* Fully serverless workflow
* Automatic ETL execution
* Duplicate record removal
* CloudWatch logging
* AWS Glue Visual ETL
* No manual intervention after file upload

---

# 📸 Project Screenshots

The repository contains screenshots covering the complete implementation.

* Amazon S3 Input Folder
* Lambda Function Code
* Lambda Trigger Configuration
* CloudWatch Logs
* AWS Glue Visual Workflow
* Successful Glue Job Execution
* Amazon S3 Output Folder
* Cleaned CSV Output
* Complete Architecture Diagram

---

# 🛠️ Technologies Used

* AWS Lambda
* Amazon S3
* AWS Glue Studio
* IAM
* CloudWatch
* Python
* boto3

---

# 📈 Future Enhancements

The following features are planned for future versions of this project:

* EventBridge integration
* Amazon SNS email notifications
* Interactive frontend dashboard
* Processing statistics dashboard
* Download processed files from the UI

---

# 👨‍💻 Author

**Sahil Sharma**

B.Tech Computer Science Engineering

Passionate about Cloud Computing, Machine Learning, AWS, and Data Engineering.

---

# ⭐ Learning Outcomes

Through this project, I learned:

* Building serverless workflows on AWS
* Configuring Amazon S3 event triggers
* Invoking AWS Glue from AWS Lambda using boto3
* Working with AWS IAM roles and permissions
* Designing ETL workflows using AWS Glue Studio
* Monitoring execution with Amazon CloudWatch
* Debugging real-world AWS pipelines

---

## Thank You

If you found this project useful, consider giving it a ⭐ on GitHub.
