FROM debian:bullseye-slim

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ansible \
    openssh-client \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create user "ansible"
RUN useradd -m -s /bin/bash ansible

# Set working directory and copy repository
WORKDIR /home/ansible/ansible-template
COPY . /home/ansible/ansible-template

# Copy SSH keys (assuming your SSH keys are located in the .ssh directory)
COPY .ssh /home/ansible/.ssh
RUN chown -R ansible:ansible /home/ansible && \
    chmod 700 /home/ansible/.ssh && \
    chmod 600 /home/ansible/.ssh/*

# Switch to user "ansible"
USER ansible

# On container start, execute the playbook and then exit
CMD ["ansible-playbook", "playbooks/deploy.yaml"]
