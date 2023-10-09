# FastfoodMenuProject_WithRDS


Developed an engaging Fast Food Menu Application using HTML, CSS, Python, and Flask, with AWS Services (EC2, Amazon RDS, MariaDB) for hosting and data management, enhancing customer ordering experiences and restaurant management

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/53673123-e2e9-4795-9a04-2b994c3b3c7b)


Step 1: Create VPC, Subnets, and Internet Gateway

* Go to the AWS VPC console.
* Click on "Your VPCs" and then "Create VPC and more."
* Provide a name for your VPC and specify the IPv4 CIDR block.
* Number of Availability Zones (AZs) is one
* Create one public subnet and one private subnet within this VPC.
* Choose NAT gateway "None".
* Keep other details with default values.Then click on create VPC.
  
Step 2: Launch EC2 Instance

* Go to the AWS EC2 console.
* Launch a Linux EC2 instance( Amazon Linux 2023 AMI - Free tier eligible)
* Instance Type t2.micro
* Create a new Key Pair. 
* In the network settings , Choose the VPC you created in step 1.
* Select the public subnet, and choose Auto-assign public IP : "Enable".
* Create a security group and allow inbound traffic on port 22 (SSH) for "Anywhere" or specify your IP.
Add another security group rule on port 5000(custom TCP) for "Anywhere" for your Flask application.
* In the Advanced details -> User Data -> copy and paste the below script.
```
 #!/bin/bash
sudo yum update -y
sudo yum install python -y
sudo yum install python-pip -y
pip install flask
pip install mysql-connector-python
sudo dnf install mariadb105 -y
sudo yum install git -y
git clone https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS.git
```
* Then Launch the EC2 instance

Step 4: Set Up MariaDB (RDS)

* In the AWS Management Console, search for RDS.
* Click "Create Database."
* Choose "MariaDB" as the database engine.
* Select the "Templates: Free Tier" option.
* Give your database a name like "fastfoodDB."
* Specify a username and password for the database.
* Choose the DB instance class (e.g., db.t3.micro).
* For connectivity, select "Connect to EC2 instance" and choose the EC2 instance created earlier.
* Choose an automatic subnet group.
* Set "Public access" to "No."
* Create a new DB security group.
* Review and launch the RDS instance.


