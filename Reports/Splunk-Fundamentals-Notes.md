# Splunk Fundamentals - Notes

## 1. What is Splunk?
Splunk is a powerful platform designed to search, monitor, and analyze machine-generated data. It is widely used for operational intelligence, log management, and as a Security Information and Event Management (SIEM) tool.

## 2. Core Architecture & Data Flow
The flow of data in Splunk involves three main components:
- **Forwarders:** Lightweight agents installed on source machines to collect and send data.
- **Indexers:** Process and store the data, making it searchable. Data is stored in repositories called **indexes**.
- **Search Head:** The web interface where users interact with the data through searches, reports, and dashboards.

## 3. Key Concepts and Terminology
- **Index:** A container for storing data (e.g., `main` is the default index).
- **Source:** The origin of the data, such as a file path (`/var/log/auth.log`).
- **Sourcetype:** The format of the data, which tells Splunk how to parse it (e.g., `linux_secure` for SSH logs).
- **Field:** A key-value pair extracted from the raw data during search time (e.g., `user="root"`, `ip_address="192.168.1.1"`). Fields are the primary way to search and filter data effectively.
