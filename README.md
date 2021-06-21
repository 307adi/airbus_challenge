Airbus_Challenge_DevOps

We will mention the question and then follow up with questions along with them.

1.Deploy an EC2 Machine using CFT/TF
For this case we are using Terraform script to spin up EC2 instances with the basic configurations.

--> Kindly find the attached file main.tf file which we can use to spin up instances. I have mentioned the random access keys and secret keys. But we should mention the actual  ones to connect.

2.Install Java8 and Jenkins server using Ansible.
■ No passwords should be used while connecting to the
machine.(configure ansible.cfg according to not use the password in the
command line)
■ Jenkins UI configuration can be done manually. No need to automate
that part.

--> Kindly find the attached ansible playbook playbook.yml which can automatically install Java8 and Jenkins server .We can put the hostname/IP of the machine in inventory file ,where we want to run the ansible script.We can trigger the ansible script using this command below.
ansible-playbook -i inventoryfilename playbook.yml
For connection to the remote server we can configure the password less access from the host server using SSH keys.
Jenkins UI configuration has been done manually as requested.

3.Create a pipeline in the Jenkins you have deployed.
○ Retrieve Source code from VCS(Github or anything of your choice)

--> We have created jenkins pipeline and configured it manually and for VCS we are using Github as our source .

4.Case 1:
○ Write a lambda function (python) to Add, Subtract, Multiply, and Divide
two numbers.
--> Ask user to input two numbers and the operator (+, –, *, /). Based on
the input program should compute the result and display the output.
--> Write the test case to validate any operator's functionality and then
deploy the code in AWS (lambda) with Jenkins.

--> For this we have written a lambda function (python) which does Add, Subtract, Multiply and Divide two number based on user input and the operator input. Please find the code in cal.py .
Along with this we have written test cases to validate the functionality of the same. Please find the code in test.py
Also to deploy this used AWS Lambda plugin in Jenkins .Along with this we need to define IAM role in AWS with trust relationship with the Lambda function. Please find the screenshot below for the same.

5.Case 2:
○ Build a docker image (Any image which can run a web application service)
■ Example: A node:12/python:3.6(with flask application) image which
returns a message(“Hello Airbus”) when we curl it.
Note: You should write the flask application or node js application which
returns the data.
● Python Flask: Please write Class structured code while
implementing.
○ Test the docker image
■ Testing is basically Running the docker image, checking the status of the
service. Curl and check if it is returning information(message
body=”Hello Airbus”), and check the status code as well.
--> For this scenario we have build a simple python flask application app.py which basically just prints the message "Hello Airbus" .Also after curl on this we get a response "Hello Airbus".
--> We have then containerized this whole application for our use using docker for which we have specified the dockerfile as dockerfile.And for testing the same we have tested this by deploying it and doing curl and checking if we get the desired output . 
