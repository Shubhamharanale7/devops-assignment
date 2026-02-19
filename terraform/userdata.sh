#!/bin/bash

# Update packages
apt update -y

# Install Docker
apt install -y docker.io
systemctl start docker
systemctl enable docker

# Install wget
apt install -y wget

# Download CloudWatch Agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb

# Install CloudWatch Agent
dpkg -i amazon-cloudwatch-agent.deb

# Create CloudWatch config file
cat <<EOF > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/lib/docker/containers/*/*.log",
            "log_group_name": "devops-assignment-logs",
            "log_stream_name": "{instance_id}"
          }
        ]
      }
    }
  }
}
EOF

# Start CloudWatch Agent
systemctl restart amazon-cloudwatch-agent

