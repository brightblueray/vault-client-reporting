# vault-client-reporting
MVP for Showback / Chargeback of Vault Clients

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Image](#docker-image)
- [Contributing](#contributing)
- [License](#license)

## Overview
[Explain what your project does and its main features. Provide context and background information.]

## Installation
[Explain how users can install or set up your project. Include any prerequisites, dependencies, or environment setup steps.]

## Usage
[Provide detailed instructions on how to use your project. Include examples and explanations of different functionalities.]

### Running the Jupyter Notebook
[If applicable, provide instructions for running the Jupyter Notebook. Explain how users can interact with it.]

### Running the Python Script
Requires the following environment variables:
- VAULT_TOKEN: A token with access to the following 
```hcl
path "sys/auth" {
  capabilities = ["read"]
}

path "identity" {
  capabilities = ["read"]
}

path "sys/internal/counters/activity/export" {
  capabilities = ["read"]
}
```

VAULT_ADDR: Address of Vault Cluster


## Docker Image
### Build
While in the root directory of the repo
```zsh
docker build -t vault-client-reporter . --file docker/Dockerfile
```

### Run
```zsh
docker run -p 8888:8888 vault-client-reporter    
```

## Contributing
[Explain how others can contribute to your project. Include guidelines for submitting issues and pull requests.]

## License
[Include information about the license under which your project is released. Choose a license that aligns with your goals.]

## Acknowledgements
[Optional: Give credit to any resources, libraries, or individuals who contributed to your project.]

## Contact
[Provide your contact information or ways for users to reach out if they have questions or feedback.]