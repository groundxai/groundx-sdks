# GroundX On-Prem
<TODO video to film>

For up-to-date instructions and more configuration details, visit the [Github Repo](https://github.com/eyelevelai/eyelevel-iac)

## Introduction

In this tutorial we'll go over how to deploy GroundX On-Prem, a free and open-source version of GroundX that can be deployed in secure and air-gapped environments; allowing you to employ the power of GroundX in regulated industries.

GroundX On Prem is a next-generation platform for building Retrieval-Augmented Generation (RAG) applications that meet the demands of regulated enterprises. Designed for environments where accuracy, security, and scalability aren’t negotiable, GroundX deploys in just a few lines of code and runs entirely within your secure environment—including air-gapped setups.

**What Makes GroundX Unique**
GroundX delivers a unique approach to advanced RAG that’s built on Kubernetes, powered by fine-tuned open source models and consists of three interlocking systems:
- **GroundX Ingest:** A state-of-the-art vision model trained on over 1M pages of enterprise documents. It delivers unparalleled document understanding and can be fine-tuned for your unique document sets.
- **GroundX Store:** Secure, encrypted storage for source files, semantic objects, and vectors, ensuring your data is always protected.
- **GroundX Search:** Built on OpenSearch, it combines text and vector search with a fine-tuned re-ranker model for precise, enterprise-grade results.
Performance

In head-to-head testing, GroundX significantly outperformed first generation RAG tools (link), especially with complex documents at scale. GroundX is trusted by leading organizations like Air France, Dartmouth, and Samsung, with over 2 billion tokens ingested on our models.

**Who’s It For?**
GroundX On Prem is purpose-built for regulated industries that demand secure, scalable, and accurate AI solutions—financial services, healthcare, government, and beyond. But any org that demands secure, accurate, RAG can take advantage.

## Setting Up GroundX On-Prem

**⚠️ Warning ⚠️**

**The resources being created in this tutorial will incur cost via AWS. It is recommended to follow all instructions accurately and completely. Taredown instructions are provided which, when followed, will properly discard all created resources. Experience with AWS is recommended.**

The Default resource configurations are specified [here](https://github.com/eyelevelai/eyelevel-iac/blob/1f851fdd7dbfc959b5830ccf0f121692c1454eb2/environment/aws/variables.tf#L120), consisting of:
```
2x m6a.xlarge
3x t3a.medium
1x g4dn.xlarge
3x g4dn.2xlarge
2x g5.xlarge
~300 GB gp2
```

### Step 1) Installing Dependencies

Please ensure you have the following software tools installed before proceeding:

1. `bash` shell (version 4.0 or later recommended. AWS Cloud Shell has insufficient resources.)
2. `terraform` ([Setup Docs](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)) 
3. `AWS CLI` ([Setup Docs](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
4. `kubectl` ([Setup Docs](https://kubernetes.io/docs/tasks/tools/))

### Step 2) Setting Up Kubernetes in AWS

First, clone the repo
```bash
git clone https://github.com/eyelevelai/eyelevel-iac.git
```
Then run

```bash
cd eyelevel-iac/
cp environment/aws/env.tfvars.example environment/aws/env.tfvars
```

`env.tfvars` is the configuration file terraform will use when defining the resources. The content of `env.tfvars` can be modified to update this configuration as necessary. By copying `env.tfvars.example` to `env.tfvars` you will be using the default configuration.

once `env.tfvars` has been created, run

```bash
environment/aws/setup-eks
```

You will be prompted for an AWS region to set up your cluster, and will also be asked to double check that you're happy with the state of the configuration file.

Once this command has executed all infrastructural resources will have been created, and you can proceed to deploying GroundX.

### Step 3) Deploying GroundX On-Prem

```bash
cp operator/env.tfvars.example operator/env.tfvars
```

This copies an example config file for the GroundX application, similarly to what was done in step 1. Now, however, some configuration is required.

For security reasons, you **MUST** modify the following:

  - `admin.api_key`: Set this to a random UUID. You can generate one by running `bin/uuid`. This will be the API key associated with the admin account and will be used for inter-service communications.
  - `admin.username`: Set this to a random UUID. You can generate one by running `bin/uuid`. This will be the user ID associated with the admin account and will be used for inter-service communications.
  - `admin.email`: Set this to the email address you want associated with the admin account.

Once `env.tfvars` has been properly configured, run

```bash
operator/setup
```

This will deploy GroundX On-Prem onto the kubernetes cluster defined in Step 2.

## Using GroundX On-Prem
Once the setup is complete, run `kubectl -n eyelevel get svc` to get the API endpoint. It will be the external IP associated with the GroundX load balancer.

For instance, the "external IP" might resemble the following:
```    
EXTERNAL-IP
b941a120ecd91455fa7b8682be2a9e41-1427794132.us-east-2.elb.amazonaws.com
```

That endpoint, in conjuction with the `admin.api_key`, can be used to configure the GroundX SDK to communicate with your On-Prem instance of GroundX.

:::code
```python
from groundx import Groundx
from groundx.configuration import Configuration

external_ip = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxx.us-east-2.elb.amazonaws.com'

groundx = Groundx(
    configuration=Configuration(
        host=f"http://{external_ip}/api",
        api_key="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    )
)
```

```javascript

import { Groundx } from "groundx-typescript-sdk";

const external_ip = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxx.us-east-2.elb.amazonaws.com'

const groundx = new Groundx({
  apiKey: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  basePath: `http://${external_ip}/api`;,
});
```
:::

## Taredown
After all resources have been created, taredown can be done with the following commands.

```
bin/operator app -c
bin/operator services -c
bin/operator init -c
bin/environment eks -c
bin/environment aws-vpc -c
```

It is vital to run these commands in order, and it is recommended to run them one at a time manually. We have observed inconsistency and race conditions when these are run automatically.