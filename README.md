# FastfoodMenuProject_WithRDS


Developed an engaging Fast Food Menu Application using HTML, CSS, Python, and Flask, with AWS Services (EC2, Amazon RDS, MariaDB) for hosting and data management, enhancing customer ordering experiences and restaurant management

![image](https://github.com/sreedevi-langoju/FastfoodMenuProject_WithRDS/assets/135724041/53673123-e2e9-4795-9a04-2b994c3b3c7b)


Step 1: Create VPC, Subnets, and Internet Gateway

* Go to the AWS VPC console.
* Click on "Your VPCs" and then "Create VPC."
* Provide a name for your VPC and specify the IPv4 CIDR block.
* Create a public subnet and a private subnet within this VPC.
* Create an Internet Gateway and attach it to your VPC.
* Create a route table for the public subnet with the default route pointing to the Internet Gateway.
* Create a security group and allow inbound traffic on port 22 (SSH) for "Anywhere" or specify your IP. Add another allow inbound traffic on port 5000 for your Flask application in the same security group.
