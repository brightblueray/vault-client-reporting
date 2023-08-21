# Dockerfile

# Use a base image with Python and Jupyter Notebook
FROM jupyter/scipy-notebook:latest

# Install additional Python packages
RUN pip install requests pandas matplotlib

# Set working directory
WORKDIR /app

# Copy your script and notebook into the container
COPY src/client-report.py .
COPY notebooks/Vault_Client_Audit.ipynb .

# Set environment variables (optional)
ENV VAULT_ADDR="http://host.docker.internal:8200"
ENV VAULT_TOKEN="hvs.CAESIPA6tTKqzn_UiXnRRmstt7nuhJYadG_ed7itSZbBo-pyGh4KHGh2cy54MTlhZmt0cGFnOHF0bjBCQVRVdVhFcHE"

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]