# Multi-Node K8s_cluster
we have automated the Kubernetes Multi-node cluster over AWS cloud using Ansible automation tool 

Requirements:
1. Python 
   - To install python:
            - refer this " https://www.python.org/downloads/ " and download python according to your Operating System.
                                                            or
            - Download Anaconda3 using " https://www.anaconda.com/products/individual#Downloads "
2. Ansible 
   - To Install ansible run "pip3 install ansible" in your terminal 
3. AWS CLI
   - To Install AWS CLI refer this " https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html " and download AWS CLI according to your Operating System.
   - run 'aws configure' command and provide access key and secret key of IAM user. REFER: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**First Step:**
To create a kubernetes multi-node cluster We have to create instances over AWS EC2 and for that run EC2.yml playbook:

$ ansible-playbook -v EC2.yml

Fill the reqired parameters according to your requirement. you can find below screenshot as a example:  

![Screenshot 2021-04-07 at 3 35 57 PM](https://user-images.githubusercontent.com/71692764/113849279-f4b0c680-97b6-11eb-8a31-eb83d486eb59.png)

Now, it will launch 3 AWS ec2 instances one master and 2 slave.

**NOTE:** If you want to lauch more the 2 slave instances then you have to manually change main.yml file inside vars directory of Launch_Instance role and change instance_count from 2 to {as per your reqirement} inside Slave tag_list which is mention below.

![Screenshot 2021-04-07 at 3 41 03 PM](https://user-images.githubusercontent.com/71692764/113850033-ab14ab80-97b7-11eb-80f6-ba1ab4634b13.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Second Step:**
To Configure Instances as master and Slave we have to run cluster.yml playbook:

$ ansible-playbook -v cluster.yml

First, it will do the basic configuration we reqiured in both master and slave node.

Second, it will configure flannel network over master node. to do so we have to provide required output:{Find sceernshot below for reference}

![Screenshot 2021-04-07 at 4 09 56 PM](https://user-images.githubusercontent.com/71692764/113853795-b4a01280-97bb-11eb-9f46-6b9c665b4595.png)

Third, it will connect slave node to the master node to bulid cluster.

Fourth, it will create deployment over master node and to do so we have to provide required output:{Find sceernshot below for reference}

![Screenshot 2021-04-07 at 4 15 01 PM](https://user-images.githubusercontent.com/71692764/113854362-6b03f780-97bc-11eb-8848-d60406b4232f.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Find Demo Video Of This architechture over aws from below link:


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Thank you for your time
# Hope it is helpful for you


