# ntbotPostIssue

AWS Lambda function to post issues to GitHub from a web form.

## Building

Ensure `src/secret.py` exists with `GH_TOKEN` specified. Run `./make.sh` to build the .zip file to upload to AWS.

## Uploading

Either with the web interface or via a correctly configured CLI: `aws lambda update-function-code --function-name ntbotPostIssue --zip-file fileb://ntbotPostIssue.zip`.
