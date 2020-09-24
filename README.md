# aws_lambda_function
AWS lambda function to copy data from source S3 to another target S3 and triggering email notification


Lambda function: test_mm_S3_copy
Prerequisite: create S3 source and target buckets

1. Login to AWS console https://console.aws.amazon.com (If you dont have AWS account, follow AWS console signup options)
2. Click on Services link on main menu and choose Lambda option under compute section 
3. Under Lambda functions page, click on create function button 
4. Create lambda function from from scratch.
5. Fill the name of the lambda function and runtime (here we have used Python 2.7) 
6. Choose permissions to run/ execute the lambda function.
   For this demo below role is used ,
   Role name: test_mm_lambda_s3 
   Policy: AmazonS3FullAccess, AmazonSESFullAccess and CloudWatchFullAccess
7. Click on Create Function button
8. Click on Add Trigger button, since we want to execute the lambda function for specific triggers/ events. 
9. Choose a trigger type and its configuration as bucket, event type 
10. write a code for the lambda function.




Lambda function: test_email_notification
Prerequisite: Configure email addresses in AWS SES service

1. Login to AWS console https://console.aws.amazon.com (If you dont have AWS account, follow AWS console signup options)
2. Click on Services link on main menu and choose Lambda option under compute section 
3. Under Lambda functions page, click on create function button 
4. Create lambda function from from scratch.
5. Fill the name of the lambda function and runtime (here we have used Python 3.6) 
6. Choose permissions to run/ execute the lambda function.
   For this demo below role is used ,
   Role name: test_mm_lambda_s3 
   Policy: AmazonS3FullAccess, AmazonSESFullAccess and CloudWatchFullAccess
7. Click on Create Function button
8. Click on Add Trigger button, since we want to execute the lambda function for specific triggers/ events. 
9. Choose a trigger type and its configuration as bucket, event type 
10. write a code for the lambda function.
