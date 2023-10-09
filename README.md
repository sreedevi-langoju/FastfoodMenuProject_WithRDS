# FastfoodMenuProject_WithRDS


Developed an engaging Fast Food Menu Application using HTML, CSS, Python, and Flask, with AWS Services (EC2, Amazon RDS, MariaDB) for hosting and data management, enhancing customer ordering experiences and restaurant management

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/53673123-e2e9-4795-9a04-2b994c3b3c7b)


#### Step 1: Create VPC, Subnets, and Internet Gateway

* Go to the AWS VPC console.
* Click on "Your VPCs" and then "Create VPC and more."
* Provide a name for your VPC and specify the IPv4 CIDR block.
* Number of Availability Zones (AZs) is one
* Create one public subnet and one private subnet within this VPC.
* Choose NAT gateway "None".
* Keep other details with default values.Then click on create VPC.
  
#### Step 2: Launch EC2 Instance

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
* Once EC2 is up and running , notedown the EC2 public and private IP addresses.

#### Step 3: Set Up Amazon RDS (MariaDB)

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
* Create a new DB security group.And keep all other details with default values.
* Review and launch the RDS instance.
* Once RDs is up and running , notedown the RDS Endpoint

#### Step 4: SSH into EC2

Change the permissions on your key pair: chmod 400 <key-pair-filename>
SSH into your EC2 instance:
```
ssh -i <key-pair-filename> ec2-user@<your-ec2-public-ip>

```
#### Step 5: Connect to MariaDB (RDS) from EC2

* Use the database endpoint you copied: <rds-end-point>
* Run the following command to connect to the MariaDB database:
```
mysql -h <rds-end-point> -P 3306 -u <user-name> -p

```
* Enter your password when prompted.
* Execute your database-related queries, e.g., create tables, insert data, etc. Refer to the RDS_Queries.pdf file in this repository.
* Type exit; to exit the MariaDB command line.

#### Step 6: Update Flask Application Configuration

* Go back to your EC2 instance.
* Navigate to your project folder, e.g.,
  ``` cd FastfoodMenuProject_WithRDS ```
* Open the databaselogic.py file using your favorite editor.
``` vim databaselogic.py ```
* Press Enter to edit the file and  update the database host (RDS Endpoint) , username, and password with the values you used in the step 3 (RDS setup).
* Save and exit the file.

Your project is now set up with VPC, EC2 instance, RDS (MariaDB), and your Flask application ready to run.

#### Step 7: Start Your Flask Application

* Go to your project folder,
  e.g., ``` cd FastfoodMenuProject_WithRDS ```
* Set the Flask app environment variable: export FLASK_APP=app.
* Start your Flask application, e.g., flask run --host=0.0.0.0

Once it running, you can goto web browser and type  http://<ec2-public-ip>:5000/ and enter

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/f8eed6eb-3a88-4170-8112-543b2a87bb07)

Select items and add the quantity and place order , you will see the Order Receipt

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/aee5c9c3-055d-4e29-bca3-9cff0ad87ed9)

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/fdbd3cfe-e65e-403c-a6b9-e16bd7441c52)

--------End--------- 




