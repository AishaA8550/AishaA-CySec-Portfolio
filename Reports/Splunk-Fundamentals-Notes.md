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
## 4. Introduction to SPL (Splunk Processing Language)
SPL is the search language used to interact with data in Splunk. Commands are chained together using a pipe character `|`, where the output of one command becomes the input for the next.

### Basic Search Patterns
- Keyword search: `error`
- Searching a specific index: `index="main"`
- Using fields in search: `status_code=404`

### Essential SPL Commands
- `| search`: Filters events further (e.g., `| search user="admin"`).
- `| fields`: Selects which fields to display (e.g., `| fields user, ip_address`).
- `| table`: Formats results into a table (e.g., `| table timestamp, user, action`).
- `| top`: Shows the most common values of a field (e.g., `| top limit=5 user`).
- `| stats`: Calculates statistics (e.g., `| stats count by status_code`).

### Practical SPL Examples

```splunk
# Example 1: Find failed login attempts and count them by user
index="main" "login failed" | stats count by user

# Example 2: Top 10 source IPs generating errors in the last 24 hours
error | top limit=10 src_ip

# Example 3: Search web server logs for client IPs and requested URLs
sourcetype="access_combined" | table clientip, uri_path, status
