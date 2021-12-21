resource "aws_lambda_function" "main" {
  function_name = var.lambda_function_name

  s3_bucket = var.lambda_deploy_bucket
  s3_key    = "main.zip"
  source_code_hash = filebase64sha256("main.zip")

  handler = "main.handler"
  runtime = "python3.9"

  timeout = 60

  role = aws_iam_role.lambda_role.arn

  depends_on = [
    aws_iam_role_policy_attachment.lambda_logs,
    aws_cloudwatch_log_group.example,
  ]
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.main.function_name
  principal     = "apigateway.amazonaws.com"

  # The "/*/*" portion grants access from any method on any resource
  # within the API Gateway REST API.
  source_arn = "${aws_api_gateway_rest_api.main.execution_arn}/*/*"
}
