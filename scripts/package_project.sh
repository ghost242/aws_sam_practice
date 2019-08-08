cd ..
sam package --template-file .aws-sam/build/template.yaml --s3-bucket sam-practice-lambda-src --output-template-file ./.aws-sam/build/packaged_template.yaml